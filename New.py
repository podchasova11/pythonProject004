# def find_missing_number(arr):
#     n = len(arr) + 1  # Длина должна быть на 1 больше из-за потерянного числа
#     total_sum = n * (n - 1) // 2  # Сумма чисел от 0 до n-1
#     actual_sum = sum(arr)  # Сумма элементов в массиве
#     return total_sum - actual_sum  # Потерянное число
#
# # Пример
# array = [0, 3, 6, 1, 4, 2, 5, 7, 8, 10, 11]
# missing_number = find_missing_number(array)
# print(f"Потерянное число: {missing_number}")


# def find_missing_number(arr):
#     n = len(arr) + 1  # Длина массива плюс 1, чтобы учесть потерянное число
#     total_sum = n * (n + 1) // 2  # Сумма чисел от 1 до n
#     actual_sum = sum(arr)  # Сумма элементов в массиве
#     return total_sum - actual_sum  # Потерянное число
#
# # Пример
# array = [3, 6, 1, 4, 2, 5, 7, 8, 10, 11]
# missing_number = find_missing_number(array)
# print(f"Потерянное число: {missing_number}")

# class Calculator:
#     @staticmethod
#     def add(a: float, b: float) -> float:
#         Calculator._validate_numbers(a, b)
#         return a + b
#
#     @staticmethod
#     def subtract(a: float, b: float) -> float:
#         Calculator._validate_numbers(a, b)
#         return a - b
#
#     @staticmethod
#     def multiply(a: float, b: float) -> float:
#         Calculator._validate_numbers(a, b)
#         return a * b
#
#     @staticmethod
#     def divide(a: float, b: float) -> float:
#         Calculator._validate_numbers(a, b)
#         if b == 0:
#             raise ValueError("Деление на ноль запрещено!")
#         return a / b
#
#     @staticmethod
#     def _validate_numbers(a, b):
#         if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#             raise TypeError("Операции поддерживают только числовые значения!")
#
# import unittest
#
#
# class TestCalculator(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(Calculator.add(2, 3), 5)
#         self.assertEqual(Calculator.add(-2, 3), 1)
#         self.assertEqual(Calculator.add(0, 0), 0)
#         self.assertEqual(Calculator.add(2.5, 3.5), 6.0)
#
#     def test_subtract(self):
#         self.assertEqual(Calculator.subtract(5, 3), 2)
#         self.assertEqual(Calculator.subtract(2, 3), -1)
#         self.assertEqual(Calculator.subtract(0, 0), 0)
#         self.assertEqual(Calculator.subtract(5.5, 1.5), 4.0)
#
#     def test_multiply(self):
#         self.assertEqual(Calculator.multiply(5, 3), 15)
#         self.assertEqual(Calculator.multiply(-5, 3), -15)
#         self.assertEqual(Calculator.multiply(0, 5), 0)
#         self.assertEqual(Calculator.multiply(2.5, 4), 10.0)
#
#     def test_divide(self):
#         self.assertEqual(Calculator.divide(6, 3), 2)
#         self.assertEqual(Calculator.divide(5, 2), 2.5)
#         self.assertEqual(Calculator.divide(-6, 3), -2)
#         self.assertRaises(ValueError, Calculator.divide, 5, 0)
#
#     def test_invalid_arguments(self):
#         self.assertRaises(TypeError, Calculator.add, "2", 3)
#         self.assertRaises(TypeError, Calculator.subtract, 2, "3")
#         self.assertRaises(TypeError, Calculator.multiply, "a", "b")
#         self.assertRaises(TypeError, Calculator.divide, 5, "0")
#
# if __name__ == '__main__':
#     unittest.main()
# suma = [100, 200, 300]
# total = sum(suma)
# print(total)

# seqNum = int(input('Введите количество чисел: '))
# max_m = 0
# max_sum =0
# summ = 0
# for i in range(seqNum):
#     print('Введите число: ', end = ' ')
#     number = int(input())
#     this_num = number
# while number > 0:
#     summ += number %10
#     number //= 10
# if summ > max_sum:
#     max_sum = summ
#     max_num = this_num
#     summ = 0
# print('Число',max_num,'имеет максимальную сумму цифр:', max_sum)

# n = int(input('Введите количество чисел: '))
# big = 0
# summ = 0
#
# for i in range (n):
#   numbers = int(input('Ввелите число: '))
#   while numbers > big:
#     big = numbers
#     summ = (big // 10) + (big)
# print('Самое большое число:', big, ', а сумма цифр:', summ)


# def sum_of_digits(n):
#   return sum(int(digit) for digit in str(n))
#
#
# def find_number_with_max_digit_sum(arr):
#   max_sum = 0
#   number_with_max_sum = None
#
#   for num in arr:
#     digit_sum = sum_of_digits(num)
#     if digit_sum > max_sum:
#       max_sum = digit_sum
#       number_with_max_sum = num
#
#   return number_with_max_sum, max_sum
#
#
# # Пример:
# arr = [91, 22, 89]
# number, digit_sum = find_number_with_max_digit_sum(arr)
#
# print(f"Число с наибольшей суммой цифр: {number}")
# print(f"Сумма цифр: {digit_sum}")


# def sortedSquares(nums):
#   n = len(nums)
#   result = [0] * n  # Создаем массив для результатов
#   left, right = 0, n - 1  # Указатели на начало и конец массива
#
#   for i in range(n - 1, -1, -1):  # Заполняем результат с конца
#     if abs(nums[left]) > abs(nums[right]):
#       result[i] = nums[left] ** 2
#       left += 1
#     else:
#       result[i] = nums[right] ** 2
#       right -= 1
#
#   return result
#
#
# # Пример использования
# nums = [-4, -1, 0, 3, 10]
# result = sortedSquares(nums)
# print(result)  # Вывод: [0, 1, 9, 16, 100]


# def sortedSquares(nums):
#   n = len(nums)
#   result = [0] * n  # Создаем массив для результатов
#   left, right = 0, n - 1  # Указатели на начало и конец массива
#
#   for i in range(n - 1, -1, -1):  # Заполняем результат с конца
#     if abs(nums[left]) > abs(nums[right]):
#       result[i] = nums[left] ** 2
#       left += 1
#     else:
#       result[i] = nums[right] ** 2
#       right -= 1
#
#   return result
#
#
# # Пример использования
# nums = [-4, -1, 0, 3, 10]
# result = sortedSquares(nums)
# print(result)  # Вывод: [0, 1, 9, 16, 100]

# g = 80 % 8
# print(g)
# print(type(g))


# greeting = ['Hello']
# greeting *= 5
# print(greeting)

# greeting = 5
# greeting *= 5
# print(greeting)

# _spam = 'Hello'
# print(_spam)
#
# a = 1
# print('Hello world!', a)
#
# #  Аргумент с ключевым словом endможно использовать, чтобы избежать новой строки после вывода
# phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
# for word in phrase:
#     print(word, end=' ')
#
#
# a = [1, 2]
# if len(a):
#     print('Its OK')
#     print(a)




def sortedsquares(nums):
  n = len(nums)
  squares = [0]*n
  left, right = 0, n - 1

  for i in range(n - 1, -1, -1):  # n - 1 второй с конца элемент списка, -1 первый с конца элемент списка
      left_square = nums[left] ** 2
      right_square = nums[right] ** 2

      if left_square > right_square:
        squares[i] = left_square
          left += 1
      else

  print(n)
nums = [1, 2, 3, 5]
