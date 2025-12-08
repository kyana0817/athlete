from time import time


class TestCaseExecutor:
    def __init__(self, solution: callable):
        self.solution = solution
        self.cases: list[tuple[tuple, any]] = []

    def add_case(self, *args, expected):
        self.cases.append((args, expected))
        return self
    
    def run(self):
        for (idx, (args, expected)) in enumerate(self.cases):
            start_time = time()
            result = self.solution(*args)
            end_time = time()
            assert result == expected, f"Test failed for args {args}: expected {expected}, got {result}"
            print(f"Test case {idx} passed in {end_time - start_time:.6f} seconds")
        print('All tests passed!')
