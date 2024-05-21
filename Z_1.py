def calculate_item_size(length, width) :
    return length * width

    # Функция для проверки возможности уравновешивания веревки
    def can_balance(rope_length, items, index = 0, left_sum = 0, right_sum = 0) :
    if left_sum == right_sum or left_sum + right_sum == 2 * rope_length :
        return True

        if index == len(items) :
            return False

            if can_balance(rope_length, items, index + 1, left_sum + calculate_item_size(items[index][0], items[index][1]), right_sum) :
                return True

                if can_balance(rope_length, items, index + 1, left_sum, right_sum + calculate_item_size(items[index][0], items[index][1])) :
                    return True

                    return can_balance(rope_length, items, index + 1, left_sum, right_sum)

                    # Длина веревки
                    rope_length = 10
                    # Список предметов с их размерами
                    items = [(1, 1), (9, 9), (5, 5)]

                    # Сортировка предметов по убыванию площади
                    items.sort(key = lambda x : calculate_item_size(x[0], x[1]), reverse = True)

                    # Предмет, который был украден
                    stolen_item = (3, 2)
                    # Добавление украденного предмета в список и удаление его из списка
                    items.append(stolen_item)
                    items.remove(stolen_item)

                    # Проверка возможности уравновешивания веревки с учетом украденного предмета
                    if can_balance(rope_length, items) :
                        print("Да, веревку можно уравновесить.")
                    else:
print("Нет, веревку нельзя уравновесить.")

