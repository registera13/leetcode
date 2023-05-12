import unittest

def solution(A):
    """
    unction that takes a positive integer A and returns the number formed by taking one digit from the front and one from the back,
    then the second digit from the front and second from the back, and so on...
    @param A: [int]
    @return: [int]
    """
    str_A = str(A)
    length = len(str_A)
    result = []

    for i in range(length // 2):
        result.append(str_A[i])  # Front digit
        result.append(str_A[length - 1 - i])  # Back digit

    # If A has an odd number of digits
    if length % 2 != 0:
        result.append(str_A[length // 2])

    return int("".join(result))


class TestBinaryGap(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution(123456),162534)
        self.assertEqual(solution(130),103)

    def test_case_1(self):
        self.assertEqual(solution(0),0)
        self.assertEqual(solution(1),1)


if __name__ == "__main__":
    unittest.main()
