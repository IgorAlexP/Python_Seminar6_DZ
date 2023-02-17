"""
   Задача 32: Определить индексы элементов массива (списка),
   значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше
   заданного максимума) 
    
    """
  
  
    
def find_indices(arr, min_val, max_val):
    indices = []  # создаем пустой список для хранения индексов

    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:  # проверяем, удовлетворяет ли элемент условию
            indices.append(i)  # добавляем индекс элемента в список

    return indices  # возвращаем список индексов

arr = [2, 5, 3, 8, 7, 9, 1, 4]
min_val = 3
max_val = 7
result = find_indices(arr, min_val, max_val)
print(result)  
