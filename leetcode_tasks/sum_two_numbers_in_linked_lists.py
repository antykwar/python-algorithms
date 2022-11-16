# https://leetcode.com/problems/add-two-numbers/

from data_structures.singly_linked_list import *


class SumTwoNumbersInLinkedLists:
    def __init__(self, first_number, second_number):
        self.first_number = self._prepare_number_for_list(first_number)
        self.second_number = self._prepare_number_for_list(second_number)
        self.first_list = SinglyLinkedList()
        self.second_list = SinglyLinkedList()
        self._init_linked_lists()

    @staticmethod
    def _prepare_number_for_list(number):
        return [int(digit) for digit in str(number)[::-1]]

    def _init_linked_lists(self):
        for digit in self.first_number:
            self.first_list.append(digit)
        for digit in self.second_number:
            self.second_list.append(digit)

    def calculate_sum_to_list(self):
        result_list = SinglyLinkedList()
        first_list_iterator = SinglyLinkedListIterator(self.first_list)
        second_list_iterator = SinglyLinkedListIterator(self.second_list)

        remaining = 0

        while True:
            first_digit = first_list_iterator.next()
            second_digit = second_list_iterator.next()

            if first_digit is None and second_digit is None:
                if remaining == 0:
                    break
                else:
                    result_list.append(remaining)
                    break
            elif first_digit is None:
                first_digit = 0
                second_digit = second_digit.value
            elif second_digit is None:
                first_digit = first_digit.value
                second_digit = 0
            else:
                first_digit = first_digit.value
                second_digit = second_digit.value

            sum_digit = first_digit + second_digit + remaining
            result_list.append(sum_digit % 10)
            remaining = sum_digit // 10

        return result_list
