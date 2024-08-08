'''Blur types'''

# сумма всех элементов должа быть равна 1
# размер матрицы оставляем 3 на 3, так как в функции Blur при вычислении используется поле 3 на 3
# баг возможно связан с округлением в меньшую сторону (если выходит <0 получается -1 и берется последний цвет в градиенте вместо первого)

standart = [
        [0.0625, 0.125, 0.0625],
        [0.125, 0.25, 0.125],
        [0.0625, 0.125, 0.0625]
    ]

outside = [
        [0.125, 0.125, 0.125],
        [0.125, 0.0, 0.125],
        [0.125, 0.125, 0.125]
    ]
 
# square = [ 1/9 
#         [0.125, 0.125, 0.125],
#         [0.125, 0.0, 0.125],
#         [0.125, 0.125, 0.125]
#     ]

cross = [
        [0.15, 0.0, 0.15],
        [0.0, 0.4, 0.0],
        [0.15, 0.0, 0.15]
    ]

plus = [
        [0.0, 0.15, 0.0],
        [0.15, 0.4, 0.15],
        [0.0, 0.15, 0.0]
    ]



outside_standart = [ # bug Рыба клоун в градиенте black_orange_yellow_white || в сумме дает меньше единицы
        [0.083333, 0.166666, 0.083333],
        [0.166666, 0.0, 0.166666],
        [0.083333, 0.166666, 0.083333]
    ]

outside_cross = [
        [0.25, 0.0, 0.25],
        [0.0, 0.0, 0.0],
        [0.25, 0.0, 0.25]
    ]

outside_plus = [
        [0.0, 0.25, 0.0],
        [0.25, 0.0, 0.25],
        [0.0, 0.25, 0.0]
    ]

horizontal = [
        [0.0, 0.0, 0.0],
        [0.25, 0.5, 0.25],
        [0.0, 0.0, 0.0]
    ]

vertical = [
        [0.0, 0.25, 0.0],
        [0.0, 0.5, 0.0],
        [0.0, 0.25, 0.0]
    ]

horizontal_cross = [ # bug with black -> white (1 -> 10) || в сумме дает ровно единицу 
        [0.1, 0.0, 0.1],
        [0.15, 0.3, 0.15],
        [0.1, 0.0, 0.1]
    ]

vertical_cross = [ # bug with black -> white (1 -> 10) || в сумме дает ровно единицу 
        [0.1, 0.15, 0.1],
        [0.0, 0.3, 0.0],
        [0.1, 0.15, 0.1]
    ]
