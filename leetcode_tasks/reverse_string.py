# https://leetcode.com/problems/reverse-string/

from typing import List


class ReverseString:
    @staticmethod
    def reverse_string(s: List[str]) -> None:
        s.reverse()


if __name__ == '__main__':
    test = ReverseString()
    test_string = ["h", "e", "l", "l", "o"]
    test.reverse_string(test_string)
    print(test_string)
