from argparse import ArgumentParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os
import re


def setup_driver():
    """Seleniumドライバーの設定"""
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')  # 新しいヘッドレスモード
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36')
    
    # 自動化検出を回避するための設定
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    chrome_options.binary_location = '/usr/bin/chromium'
    
    # chromedriverのパスを指定
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # WebDriverの痕跡を隠す
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
    })
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver


def scrape_leetcode_problem(url: str):
    """
    LeetCodeの問題ページをスクレイピングしてタイトルとExampleを取得
    
    Args:
        url: LeetCodeの問題URL
        
    Returns:
        dict: タイトルとExampleを含む辞書
    """
    driver = setup_driver()
    
    try:
        print(f"Accessing: {url}")
        driver.get(url)
        
        # ページの読み込みを十分に待機（Cloudflareチャレンジ対応）
        print("Waiting for page to load (this may take a while)...")
        time.sleep(15)  # Cloudflareチャレンジの完了を待つ
        
        # タイトルを取得
        title = "Title not found"
        
        # LeetCodeの問題タイトルを探す様々な方法
        title_selectors = [
            # クラス名を使用（最も信頼性が高い）
            ("CSS", "div.text-title-large"),
            ("CSS", "a.text-title-large"),
            # data-cy属性を使用
            ("CSS", "a[data-cy='question-title']"),
            ("CSS", "div[data-cy='question-title']"),
            # その他のセレクタ
            ("CSS", "a[class*='text-title']"),
            ("CSS", "div[class*='question-title']"),
        ]
        
        for method, selector in title_selectors:
            try:
                if method == "CSS":
                    title_element = driver.find_element(By.CSS_SELECTOR, selector)
                else:  # XPATH
                    title_element = driver.find_element(By.XPATH, selector)
                
                if title_element and title_element.text.strip():
                    title = title_element.text.strip()
                    break
            except:
                continue
        
        print(f"\nTitle: {title}")
        
        # Exampleを取得
        examples = []
        
        try:
            # Method 1: XPathで"Example"を含むテキストの後の<pre>を探す
            example_elements = driver.find_elements(By.XPATH, "//p[contains(text(), 'Example')]/following-sibling::pre")
            
            if example_elements:
                for elem in example_elements[:5]:  # 最初の5つのExampleまで
                    text = elem.text.strip()
                    if text:
                        examples.append(text)
            
            # Method 2: "Example"を含む要素の近くの<pre>
            if not examples:
                example_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Example')]/ancestor::div[1]//pre")
                if example_elements:
                    for elem in example_elements[:5]:
                        text = elem.text.strip()
                        if text:
                            examples.append(text)
            
            # Method 3: すべての<pre>タグを取得
            if not examples:
                all_pre_elements = driver.find_elements(By.TAG_NAME, "pre")
                for pre in all_pre_elements[:10]:  # 最初の10個まで確認
                    text = pre.text.strip()
                    if text and len(text) > 10:  # 空でない、ある程度の長さがあるもの
                        examples.append(text)
            
            if examples:
                print(f"\nExamples: {len(examples)} found")
                for i, example in enumerate(examples, 1):
                    print(f"\n--- Example {i} ---")
                    print(example)
            else:
                print("\nExamples: Not found")
                
        except Exception as e:
            print(f"\nError while searching for examples: {e}")
        
        return {
            "title": title,
            "examples": examples
        }
        
    finally:
        driver.quit()


def generate_python_file(title: str, examples: list[str], output_dir: str = "/app/src/leetcode"):
    """
    スクレイピングした情報からPythonファイルを生成
    
    Args:
        title: 問題のタイトル (例: "1. Two Sum")
        examples: Example文字列のリスト
        output_dir: 出力ディレクトリ
    """
    # タイトルから問題番号と名前を抽出
    match = re.match(r'(\d+)\.\s+(.+)', title)
    if not match:
        print(f"Error: Could not parse title '{title}'")
        return None
    
    problem_number = match.group(1)
    problem_name = match.group(2)
    
    # ファイル名を生成 (例: "1_two_sum.py")
    filename = f"{problem_number}_{problem_name.lower().replace(' ', '_').replace('-', '_')}.py"
    filepath = os.path.join(output_dir, filename)
    
    # クラス名を生成 (一般的にSolutionを使用)
    class_name = "Solution"
    
    # メソッド名を生成（キャメルケース）
    method_name = re.sub(r'[^a-zA-Z0-9]+', ' ', problem_name).strip()
    method_name = ''.join(word.capitalize() if i > 0 else word.lower() 
                          for i, word in enumerate(method_name.split()))
    
    # Exampleからテストケースを生成
    test_cases = []
    for example in examples:
        # Input行を探す
        input_match = re.search(r'Input:\s*(.+?)(?:\n|$)', example, re.MULTILINE)
        output_match = re.search(r'Output:\s*(.+?)(?:\n|$)', example, re.MULTILINE)
        
        if input_match and output_match:
            input_text = input_match.group(1).strip()
            output_text = output_match.group(1).strip()
            
            # 複数のパラメータを抽出（配列の中のカンマを考慮）
            inputs = []
            current = []
            bracket_depth = 0
            
            for char in input_text + ',':
                if char == '[':
                    bracket_depth += 1
                    current.append(char)
                elif char == ']':
                    bracket_depth -= 1
                    current.append(char)
                elif char == ',' and bracket_depth == 0:
                    part = ''.join(current).strip()
                    if part and '=' in part:
                        key, value = part.split('=', 1)
                        inputs.append((key.strip(), value.strip()))
                    current = []
                else:
                    current.append(char)
            
            test_cases.append({
                'inputs': inputs,
                'output': output_text,
                'raw_input': input_text
            })
    
    # メソッドのパラメータを推測
    method_params = []
    if test_cases and test_cases[0]['inputs']:
        for key, value in test_cases[0]['inputs']:
            # 型ヒントを推測（簡易版）
            param_type = "list[int]" if "[" in value else "int" if value.replace('-', '').isdigit() else "str"
            method_params.append(f"{key}: {param_type}")
    
    params_str = ", ".join(["self"] + method_params) if method_params else "self"
    return_type = "list[int]"  # デフォルト（改善の余地あり）
    
    # Pythonファイルのコンテンツを生成
    content = f'''class {class_name}(object):
    def {method_name}({params_str}) -> {return_type}:
        """
        {title}
        
        TODO: Implement this method
        """
        pass

if __name__ == "__main__":
    solution = {class_name}()
'''
    
    # テストケースを追加
    if test_cases:
        for i, test_case in enumerate(test_cases, 1):
            # 入力パラメータを取得
            params = ', '.join(value for _, value in test_case['inputs'])
            expected = test_case['output']
            
            content += f'    assert solution.{method_name}({params}) == {expected}\n'
        
        content += "    print('All tests passed!')\n"
    
    # ディレクトリが存在しない場合は作成
    os.makedirs(output_dir, exist_ok=True)
    
    # ファイルに書き込み
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n{'='*50}")
    print(f"Generated file: {filepath}")
    print(f"{'='*50}")
    
    return filepath


def main():
    """メイン関数"""
    parser = ArgumentParser(description='Scrape LeetCode problem page and generate Python file')
    parser.add_argument('url', type=str, help='LeetCode problem URL')
    parser.add_argument('-o', '--output', type=str, default='/app/src/leetcode',
                        help='Output directory for generated file (default: /app/src/leetcode)')
    parser.add_argument('--no-generate', action='store_true',
                        help='Only scrape, do not generate Python file')
    
    args = parser.parse_args()
    
    # スクレイピング実行
    result = scrape_leetcode_problem(args.url)
    
    print("\n" + "="*50)
    print("Scraping completed!")
    print("="*50)
    
    # Pythonファイル生成
    if not args.no_generate and result['title'] != "Title not found":
        generate_python_file(
            title=result['title'],
            examples=result['examples'],
            output_dir=args.output
        )


if __name__ == "__main__":
    main()
