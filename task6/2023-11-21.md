# Упражнения на работу с pandas

## Упражнение № 1

Создайте Series из каждого из элементов: списка, ndarray и словаря.

Пример входных данных:

```python
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
```

## Упражнение № 2

Преобразуйте `ser` в датафрейм с его индексом в качестве еще одного столбца датафрейма.

Пример входных данных:

```python
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)
```

## Упражнение № 3

Объедините `ser1` и `ser2`, чтобы сформировать датафрейм.

Пример входных данных:

```python
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
```

## Упражнение № 4

Добавьте имя ряда  `ser`, назвав его `latin_letters`.

Пример входных данных:

```python
ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
```

## Упражнение № 5

Из `ser1` удалите элементы, присутствующие в `ser2`.

```python
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
```

## Упражнение № 6

Получить все элементы `ser1` и `ser2`, которые не являются общими для обоих рядов.

Пример входных данных:

```python
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
```

## Упражнение № 7

Вычислите минимальное значение, 25-й процентиль, медиану, 75-й процентиль и максимальное значение `ser`.

Пример входных данных:

```python
ser = pd.Series(np.random.normal(10, 5, 25))
```

## Упражнение № 8

Вычислите частоту встречаемости каждого уникального значения `ser`.

Пример входных данных:

```python
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
```

## Упражнение № 9

Из `ser` оставить 2 наиболее часто встречающихся элемента без изменений, а все остальные заменить на `Прочее`.

Пример входных данных:

```python
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
```

## Упражнение № 10

Разбейте ряд `ser` на 10 равных децилей и замените значения на название дециля.

Пример входных данных:

```python
ser = pd.Series(np.random.random(20))
```

Пример выходных данных:

```python
# First 5 items
0    7th
1    9th
2    7th
3    3rd
4    8th
dtype: category
Categories (10, object): [1st < 2nd < 3rd < 4th ... 7th < 8th < 9th < 10th]
```

## Упражнение № 11

Переформируйте ряд `ser` в датафрейм с 7 строками и 5 столбцами

Пример входных данных:

```python
ser = pd.Series(np.random.randint(1, 10, 35))
```

## Упражнение № 12

Найти позиции чисел, кратных 3, из ряда `ser`.

Пример входных данных:

```python
ser = pd.Series(np.random.randint(1, 10, 7))
```

## Упражнение № 13

Из `ser` извлечь элементы, находящиеся на позициях в списке `pos`.

Пример входных данных:

```python
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
```

## Упражнение № 14

Объедините `ser1` и `ser2` по вертикали и горизонтали (чтобы сформировать датафрейм).

Пример входных данных:

```python
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
```

## Упражнение № 15

Получите позиции элементов `ser2` в `ser1` в виде списка.

Пример входных данных:

```python
ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])
```

## Упражнение № 16

Вычислить среднеквадратическую ошибку рядов `truth` и `pred`.

Пример входных данных:

```python
truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)
```

## Упражнение № 17

В каждом слове `ser` поставьте первый символ каждого слова в верхний регистр.

```python
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
```

## Упражнение № 18

В каждом слове `ser` посчитайте число символов.

Пример входных данных:

```python
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
```

## Упражнение № 19

Вычислите разность разностей между последовательно идущими числами в `ser`.

Пример входных данных:

```python
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
```

Пример выходных данных:

```
[nan, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 8.0]
[nan, nan, 1.0, 1.0, 1.0, 1.0, 0.0, 2.0]
```

## Упражнение № 20

Преобразуйте строковое представление дат в `datetime64`.

Пример входных данных:

```python
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
```

Пример выходных данных:

```
0   2010-01-01 00:00:00
1   2011-02-02 00:00:00
2   2012-03-03 00:00:00
3   2013-04-04 00:00:00
4   2014-05-05 00:00:00
5   2015-06-06 12:20:00
dtype: datetime64[ns]
```

## Упражнение № 21

Получите из `ser` день месяца, номер недели, день года и день недели.

Пример входных данных:

```python
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
```

Пример выходных данных:

```
Date:  [1, 2, 3, 4, 5, 6]
Week number:  [53, 5, 9, 14, 19, 23]
Day num of year:  [1, 33, 63, 94, 125, 157]
Day of week:  ['Friday', 'Wednesday', 'Saturday', 'Thursday', 'Monday', 'Saturday']
```

## Упражнение № 22

Замените элементы `ser` на даты, начинающиеся с 4-го числа соответствующего месяца.

Пример входных данных:

```python
ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])
```

Пример выходных данных:

```
0   2010-01-04
1   2011-02-04
2   2012-03-04
dtype: datetime64[ns]
```

## Упражнение № 23

Из `ser` извлеките слова, содержащие не менее 2 гласных букв.

Пример входных данных:

```python
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
```

Пример выходных данных:

```
0     Apple
1    Orange
4     Money
dtype: object
```

## Упражнение № 24

Извлеките корректные адреса электронной почты из ряда `emails`. Шаблон регулярного выражения для корректных адресов электронной почты приведен в качестве образца.

Пример входных данных:

```python
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
```

Пример выходных данных:

```
1    rameses@egypt.com
2            matt@t.co
3    narendra@modi.com
dtype: object
```

## Упражнение № 25

Вычислить среднее значение веса в `weights` для каждого фрукта из `fruit`.

Пример входных данных:

```python
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))
print(weight.tolist())
print(fruit.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']
```

Пример выходных данных:

```python
# values can change due to randomness
apple     6.0
banana    4.0
carrot    5.8
dtype: float64
```

## Упражнение № 26

Вычислить [евклидово расстояние](https://en.wikipedia.org/wiki/Euclidean_distance) между векторами $p$ и $q$, не используя встроенную формулу.

Пример входных данных:

```python
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
```

Пример выходных данных:

```
18.165
```

## Упражнение № 27

Получите позиции пиков (значений, окруженных с двух сторон меньшими значениями) в `ser`.

Пример входных данных:

```python
ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])
```

Пример выходных данных:

```
array([1, 5, 7])
```

## Упражнение № 28

Замените пробелы в `my_str` на наименее часто встречающийся символ.

Пример входных данных:

```python
my_str = 'dbc deb abed gade'
```

Пример выходных данных:

```
'dbccdebcabedcgade'  # least frequent is 'c'
```

## Упражнение № 29

Создайте временной ряд, начинающийся с `2000-01-01`, содержащий 10 субботних дней после этого и имеющий в качестве значений случайные числа

Пример выходных данных:

```
# values can be random
2000-01-01    4
2000-01-08    1
2000-01-15    8
2000-01-22    4
2000-01-29    4
2000-02-05    2
2000-02-12    4
2000-02-19    9
2000-02-26    6
2000-03-04    6
```

## Упражнение № 30

В `ser` отсутствуют некоторые даты и значения. Сделайте так, чтобы все отсутствующие даты появились и заполнились значением из предыдущей даты.

Пример входных данных:

```python
ser = pd.Series([1,10,3,np.nan], index=pd.to_datetime(['2000-01-01', '2000-01-03', '2000-01-06', '2000-01-08']))
print(ser)
#> 2000-01-01     1.0
#> 2000-01-03    10.0
#> 2000-01-06     3.0
#> 2000-01-08     NaN
#> dtype: float64
```

Пример выходных данных:

```
2000-01-01     1.0
2000-01-02     1.0
2000-01-03    10.0
2000-01-04    10.0
2000-01-05    10.0
2000-01-06     3.0
2000-01-07     3.0
2000-01-08     NaN
```

## Упражнение № 31

Вычислите автокорреляции для первых 10 лагов `ser`. Определите, какой из лагов имеет наибольшую корреляцию. (см. также [Модель авторегрессии и распределённого лага — Википедия](https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C_%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%B8_%D0%B8_%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D1%91%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BB%D0%B0%D0%B3%D0%B0))

Пример входных данных:

```python
ser = pd.Series(np.arange(20) + np.random.normal(1, 10, 20))
```

Пример выходных данных:

```
# values will change due to randomness
[0.29999999999999999, -0.11, -0.17000000000000001, 0.46000000000000002, 0.28000000000000003, -0.040000000000000001, -0.37, 0.41999999999999998, 0.47999999999999998, 0.17999999999999999]
Lag having highest correlation:  9
```

## Упражнение № 32

Импортируйте каждую 50-ю строку набора данных [BostonHousing dataset](https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv) в виде датафрейма.

## Упражнение № 33

Импортируйте набор данных [boston housing dataset](https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv), но при импорте измените столбец `'medv'` (*median house value*) так, чтобы значения < 25 стали `Low`, а > 25 - `High`.

## Упражнение № 34

Создайте датафрейм со строками в виде шагов (интервалов) заданного ряда

Пример входных данных:

```python
L = pd.Series(range(15))
```

Пример выходных данных:

```
array([[ 0,  1,  2,  3],
       [ 2,  3,  4,  5],
       [ 4,  5,  6,  7],
       [ 6,  7,  8,  9],
       [ 8,  9, 10, 11],
       [10, 11, 12, 13]])
```

## Упражнение № 35

Импортируйте столбцы 'crim' и 'medv' из набора данных [BostonHousing dataset](https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv) в виде датафрейма.

## Упражнение № 36

Получите количество строк, столбцов, тип данных и суммарную статистику каждого столбца набора данных [Cars93](https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv). Также получите эквивалент датафрейма в виде numpy-массива и списка.

## Упражнение № 37

Извлеките номер строки и столбца конкретной ячейки по заданному критерию.

Пример входных данных:

```python
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
```

*Какой производитель, модель и тип имеет наибольшую цену в `Price`? Каков номер строки и столбца ячейки с наибольшим значением `Price`?*

## Упражнение № 38

Переименуйте в `df` столбец `Type` в `CarType` и замените `.` в именах столбцов на `_`.

Пример входных данных:

```python
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
print(df.columns)
#> Index(['Manufacturer', 'Model', 'Type', 'Min.Price', 'Price', 'Max.Price',
#>        'MPG.city', 'MPG.highway', 'AirBags', 'DriveTrain', 'Cylinders',
#>        'EngineSize', 'Horsepower', 'RPM', 'Rev.per.mile', 'Man.trans.avail',
#>        'Fuel.tank.capacity', 'Passengers', 'Length', 'Wheelbase', 'Width',
#>        'Turn.circle', 'Rear.seat.room', 'Luggage.room', 'Weight', 'Origin',
#>        'Make'],
#>       dtype='object')
```

Пример выходных данных:

```python
print(df.columns)
#> Index(['Manufacturer', 'Model', 'CarType', 'Min_Price', 'Price', 'Max_Price',
#>        'MPG_city', 'MPG_highway', 'AirBags', 'DriveTrain', 'Cylinders',
#>        'EngineSize', 'Horsepower', 'RPM', 'Rev_per_mile', 'Man_trans_avail',
#>        'Fuel_tank_capacity', 'Passengers', 'Length', 'Wheelbase', 'Width',
#>        'Turn_circle', 'Rear_seat_room', 'Luggage_room', 'Weight', 'Origin',
#>        'Make'],
#>       dtype='object')
```

## Упражнение № 39

Проверьте, нет ли в `df` отсутствующих значений.

Пример входных данных:

```python
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
```

## Упражнение № 40

Подсчитайте количество пропущенных значений в каждом столбце `df`. Какой столбец имеет наибольшее число пропущенных значений?

Пример входных данных:

```python
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
```

## Упражнение № 41

Замените отсутствующие значения в столбцах `Min.Price` и `Max.Price` на соответствующие им средние значения.

Пример входных данных:

```python
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
```

## Упражнение № 42

В `df` с помощью метода `apply` замените недостающие значения в `Min.Price` на среднее значение столбца, а в `Max.Price` — на медиану столбца.

Пример входных данных:

```python
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
```

[Подсказка на StackOverflow](https://stackoverflow.com/questions/32437435/passing-additional-arguments-to-python-pandas-dataframe-apply)

## Упражнение № 43

Получите первый столбец (`a`) в `df` в виде датафрейма (а не в виде ряда).

Пример входных данных:

```python
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
```

## Упражнение № 44

1. В `df` поменяйте местами столбцы `'a'` и `'c'`.
2. Создайте обобщенную функцию для обмена данными между двумя столбцами без фиксированного задания имен столбцов.
3. Отсортируйте столбцы в обратном алфавитном порядке, т.е. от столбца `'e'` до столбца `'a'`.

Пример входных данных:

```python
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
```

## Упражнение № 45

Измените настройки отображения `pandas` при выводе на печать датафрейма `df`, чтобы он показывал максимум 10 строк и 10 столбцов.

Пример входных данных:

```python
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
```

## Упражнение № 46

Исключите вывод научной нотации типа 'e-03' в `df` и выведите до 4 чисел после запятой.

Пример входных данных:

```python
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
df
#>          random
#> 0  3.474280e-03
#> 1  3.951517e-05
#> 2  7.469702e-02
#> 3  5.541282e-28
```

Пример выходных данных:

```python
#>    random
#> 0  0.0035
#> 1  0.0000
#> 2  0.0747
#> 3  0.0000
```

## Упражнение № 47

Отформатируйте значения в столбце `'random'` из `df` в виде процентов.

Пример входных данных:

```python
df = pd.DataFrame(np.random.random(4), columns=['random'])
df
#>      random
#> 0    .689723
#> 1    .957224
#> 2    .159157
#> 3    .21082
```

Пример выходных данных:

```python
#>      random
#> 0    68.97%
#> 1    95.72%
#> 2    15.91%
#> 3    2.10%
```

## Упражнение № 48

Из `df` отфильтруйте значения `Manufacturer`, `Model` и `Type` для каждой 20-й строки, начиная с 1-й (строка 0).

Пример входных данных:

```python
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
```

## Упражнение № 49

В `df` замените `NaN` на `missing` в столбцах `Manufacturer`, `Model` и `Type` , создайте индекс как комбинацию этих трех столбцов и проверьте, является ли этот индекс первичным ключом.

Пример входных данных:

```python
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv', usecols=[0,1,2,3,5])
```

Пример выходных данных:

```
                       Manufacturer    Model     Type  Min.Price  Max.Price
Acura_Integra_Small           Acura  Integra    Small       12.9       18.8
missing_Legend_Midsize      missing   Legend  Midsize       29.2       38.7
Audi_90_Compact                Audi       90  Compact       25.9       32.3
Audi_100_Midsize               Audi      100  Midsize        NaN       44.6
BMW_535i_Midsize                BMW     535i  Midsize        NaN        NaN
```

## Упражнение № 50

Найти положение строки с 5-м наибольшим значением столбца `'a'` в `df`.

Пример входных данных:

```python
df = pd.DataFrame(np.random.randint(1, 30, 30).reshape(10,-1), columns=list('abc'))
```

## Упражнение № 51

В `ser` найдите положение 2-го наибольшего значения, превышающего среднее.

Пример входных данных:

```python
ser = pd.Series(np.random.randint(1, 100, 15))
```

## Упражнение № 52

Получите две последние строки `df`, сумма строк которых больше 100.

```python
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
```

## Упражнение № 53

Замените все значения `ser`, находящиеся ниже 5%-ного и выше 95%-ного перцентиля, на соответствующие значения 5-го и 95-го перцентиля.

Пример входных данных:

```python
ser = pd.Series(np.logspace(-2, 2, 30))
```

## Упражнение № 54

Перестройте `df` в максимально возможный квадрат с удалением отрицательных значений. При необходимости отбросьте наименьшие значения. Порядок положительных чисел в результате должен остаться тем же, что и в исходном варианте.

Пример входных данных:

```python
df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))
```

## Упражнение № 55

Поменяйте местами строки 1 и 2 в `df`.

Пример входных данных:

```python
df = pd.DataFrame(np.arange(25).reshape(5, -1))
```

## Упражнение № 56

Переверните строки датафрейма `df` (первая строка становится последней).

Пример входных данных:

```python
df = pd.DataFrame(np.arange(25).reshape(5, -1))
```

## Упражнение № 57

Получите бинарный код для столбца `'a'` в датафрейме `df` и добавьте его в виде столбцов.

Пример входных данных:

```python
df = pd.DataFrame(np.arange(25).reshape(5,-1), columns=list('abcde'))
    a   b   c   d   e
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19
4  20  21  22  23  24
```

Пример выходных данных:

```python
   0  5  10  15  20   b   c   d   e
0  1  0   0   0   0   1   2   3   4
1  0  1   0   0   0   6   7   8   9
2  0  0   1   0   0  11  12  13  14
3  0  0   0   1   0  16  17  18  19
4  0  0   0   0   1  21  22  23  24
```

## Упражнение № 58

Получите название столбца с наибольшим количеством строчных максимумов в `df`.

```python
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1))
```

## Упражнение № 59

Создать новый столбец, в каждой строке которого будет указан номер строки, ближайшей по евклидову расстоянию к данной строке.

Пример входных данных:

```python
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
df
#     p   q   r   s
# a  57  77  13  62
# b  68   5  92  24
# c  74  40  18  37
# d  80  17  39  60
# e  93  48  85  33
# f  69  55   8  11
# g  39  23  88  53
# h  63  28  25  61
# i  18   4  73   7
# j  79  12  45  34
```

Пример выходных данных:

```python
df
#    p   q   r   s nearest_row   dist
# a  57  77  13  62           i  116.0
# b  68   5  92  24           a  114.0
# c  74  40  18  37           i   91.0
# d  80  17  39  60           i   89.0
# e  93  48  85  33           i   92.0
# f  69  55   8  11           g  100.0
# g  39  23  88  53           f  100.0
# h  63  28  25  61           i   88.0
# i  18   4  73   7           a  116.0
# j  79  12  45  34           a   81.0
```

## Упражнение № 60

Вычислите максимально возможное абсолютное значение корреляции каждого столбца с другими столбцами в `df`.

Пример входных данных:

```python
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1), columns=list('pqrstuvwxy'), index=list('abcdefgh'))
```

## Упражнение № 61

Вычислите минимум-максимум для каждой строки `df`.

```python
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))
```

## Упражнение № 62

Создайте новый столбец `penultimate`, который содержит второе по величине значение каждой строки `df`.

Пример входных данных:

```python
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))
```

## Упражнение № 63

1. Нормализуйте все столбцы `df`, вычитая среднее значение столбца и деля его на стандартное отклонение.
2. Произведите ранжирование всех столбцов `df` таким образом, чтобы минимальное значение в каждом столбце было равно 0, а максимальное — 1.

Не используйте внешние пакеты типа `sklearn`.

Пример входных данных:

```python
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))
```

## Упражнение № 64

Вычислите корреляцию каждой строки `df` с последующей строкой.

Пример входных данных:

```python
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))
```

## Упражнение № 65

Замените все значения в обеих диагоналях `df` на 0.

Пример входных данных:

```python
df = pd.DataFrame(np.random.randint(1,100, 100).reshape(10, -1))
df
#     0   1   2   3   4   5   6   7   8   9
# 0  11  46  26  44  11  62  18  70  68  26
# 1  87  71  52  50  81  43  83  39   3  59
# 2  47  76  93  77  73   2   2  16  14  26
# 3  64  18  74  22  16  37  60   8  66  39
# 4  10  18  39  98  25   8  32   6   3  29
# 5  29  91  27  86  23  84  28  31  97  10
# 6  37  71  70  65   4  72  82  89  12  97
# 7  65  22  97  75  17  10  43  78  12  77
# 8  47  57  96  55  17  83  61  85  26  86
# 9  76  80  28  45  77  12  67  80   7  63
```

Пример выходных данных:

```python
#     0   1   2   3   4   5   6   7   8   9
# 0   0  46  26  44  11  62  18  70  68   0
# 1  87   0  52  50  81  43  83  39   0  59
# 2  47  76   0  77  73   2   2   0  14  26
# 3  64  18  74   0  16  37   0   8  66  39
# 4  10  18  39  98   0   0  32   6   3  29
# 5  29  91  27  86   0   0  28  31  97  10
# 6  37  71  70   0   4  72   0  89  12  97
# 7  65  22   0  75  17  10  43   0  12  77
# 8  47   0  96  55  17  83  61  85   0  86
# 9   0  80  28  45  77  12  67  80   7   0
```

## Упражнение № 66

Из `df_grouped` получите в виде датафрейма группу, относящуюся к `apple`.

Пример входных данных:

```python
df = pd.DataFrame({'col1': ['apple', 'banana', 'orange'] * 3,
                   'col2': np.random.rand(9),
                   'col3': np.random.randint(0, 15, 9)})

df_grouped = df.groupby(['col1'])
```

Пример выходных данных

```
    col1      col2  col3
0  apple  0.673434     7
3  apple  0.182348    14
6  apple  0.050457     3
```

## Упражнение № 67

В `df` найдите второе по величине значение `taste` для `banana`.

Пример входных данных:

```python
df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'rating': np.random.rand(9),
                   'price': np.random.randint(0, 15, 9)})
```

## Упражнение № 68

В `df` вычислите среднюю цену `Price` каждого фрукта `Fruit`, сохраняя фрукт как еще один столбец вместо индекса.

Пример входных данных:

```python
df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'rating': np.random.rand(9),
                   'price': np.random.randint(0, 15, 9)})
```

## Упражнение № 69

Объединить датафреймы `df1` и `df2` по признакам `fruit-pazham` и `weight-kilo`.

Пример входных данных:

```python
df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})
```

## Упражнение № 70

Создайте в `df` два новых столбца, один из них — `lag1` (сдвиг столбца `a` вниз на 1 строку) столбца 'a', а другой — `lead1` (сдвиг столбца `b` вверх на 1 строку).

Пример входных данных:

```python
df = pd.DataFrame(np.random.randint(1, 100, 20).reshape(-1, 4), columns = list('abcd'))

    a   b   c   d
0  66  34  76  47
1  20  86  10  81
2  75  73  51  28
3   1   1   9  83
4  30  47  67   4
```

Пример выходных данных:

```python
    a   b   c   d  a_lag1  b_lead1
0  66  34  76  47     NaN     86.0
1  20  86  10  81    66.0     73.0
2  75  73  51  28    20.0      1.0
3   1   1   9  83    75.0     47.0
4  30  47  67   4     1.0      NaN
```

## Упражнение № 71

Получите частоты уникальных значений по всему датафрейму `df`.

Пример входных данных:

```python
df = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns = list('abcd'))
```

## Упражнение № 72

Разделите столбец `row` в `df` так, чтобы сформировать датафрейм с 3 столбцами, как показано в примере выходных данных. 

Пример входных данных:

```python
df = pd.DataFrame(["STD, City    State",
"33, Kolkata    West Bengal",
"44, Chennai    Tamil Nadu",
"40, Hyderabad    Telengana",
"80, Bangalore    Karnataka"], columns=['row'])

print(df)
#>                         row
#> 0          STD, City\tState
#> 1  33, Kolkata\tWest Bengal
#> 2   44, Chennai\tTamil Nadu
#> 3  40, Hyderabad\tTelengana
#> 4  80, Bangalore\tKarnataka
```

Пример выходных данных:

```
0 STD        City        State
1  33     Kolkata  West Bengal
2  44     Chennai   Tamil Nadu
3  40   Hyderabad    Telengana
4  80   Bangalore    Karnataka
```
