# https://leetcode.com/problems/zigzag-conversion/

class ZigzagConversion:
    @staticmethod
    def convert(s: str, num_rows: int, visualize: bool = False) -> str:
        if num_rows <= 1:
            return s

        # Хранилище строк, которые формируют зигзаг
        strings = {index: '' for index in range(1, num_rows + 1)}
        # Количество символов в одном элементе зигзага (вертикаль + диагональ)
        link_length = num_rows + num_rows - 2
        # Общая ширина проставки между вертикалями
        total_space_width = (num_rows - 2) * 2 + 1

        # Счётчик для перемещения по строке
        counter = 0

        # Цикл для заполнения строк, формирующих зигзаг
        while counter is not None:
            substring = s[counter * link_length : counter * link_length + link_length]

            # Если добрались до конца строки - выходим из цикла после его завершения
            counter = counter + 1 if len(substring) == link_length else None
            is_vertical_unfinished = False

            # Записываем вертикали
            for i in range(0, num_rows):
                if i >= len(substring):
                    is_vertical_unfinished = True
                    break
                strings[i + 1] += substring[i]
                if i == num_rows - 1 or i == 0:
                    strings[i + 1] += ' ' * total_space_width

            # Если не заполнили вертикаль - фрагмент не полный и можно выходить
            if is_vertical_unfinished is True:
                continue

            substring = substring[num_rows:]
            # Записываем диагонали
            diagonal_counter = 0
            for i in range(num_rows - 1, 1, -1):
                letter_index = diagonal_counter
                if letter_index >= len(substring):
                    break
                diagonal_counter += 1
                letter_with_spacer = ' ' * (2 * letter_index + 1) \
                                     + substring[letter_index] \
                                     + ' ' * (total_space_width - (2 * letter_index + 1) - 1)
                strings[i] += letter_with_spacer

        strings = {i: line.strip() for i, line in strings.items()}
        if visualize:
            return "\n".join(strings.values())
        return "".join(strings.values()).replace(' ', '')


if __name__ == '__main__':
    converter = ZigzagConversion()
    print(converter.convert('PAYPALISHIRING', 3))
    print(converter.convert('PAYPALISHIRING', 3, visualize=True))
