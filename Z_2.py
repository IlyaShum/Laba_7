def get_kth_permutation(n, k, numbers): //Объявление функции getKthPermutation с параметрами n, k и numbers
    if n == 1:
        return str(numbers[0]) //Возвращаем строковое представление первого элемента вектора numbers

    fact = 1
    for i in range(1, n): //Цикл для вычисления факториала.
        fact *= i  //Умножение fact на i 

    index = (k - 1)  // fact
    number = numbers[index]
    numbers.pop(index)

    return str(number) + get_kth_permutation(n - 1, k - index * fact, numbers) // Рекурсивный вызов функции с новыми параметрами.

if __name__ == "__main__":
    n = int(input("Введите n: "))
    k = int(input("Введите k: "))

    numbers = [i + 1 for i in range(n)]

    print("Выход:", get_kth_permutation(n, k, numbers))

