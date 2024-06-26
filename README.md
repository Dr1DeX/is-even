# is-even
![workflow](https://github.com/Dr1DeX/is-even/actions/workflows/main.yml/badge.svg)

## Объяснение двух реализаций алгоритма по определению четности чисел

### У нас имеются две реализации алгоритма:

    def is_even(value):
        return value % 2 == 0

    def is_even_bitwise(value):
        return not value & 1

-------

### В первой реализации мы ``сравниваем`` остаток от деления по модулю равным нулю.

-------

### Во второй реализации ``побитовое`` сравнение младших битов(у четных это 1, нечетных 0)

-------

### Преимущества второй реализаций:

#### Теоретически побитовые операции работают быстрее, чем деление по модулю, однако в реальности они будут работать +- одинаково за счет оптимизации компилятора

### Бенчмарк:

    Func is_even start the execution:
    Func is_even completes execution:
    0.04389549998450093

    Func is_even_bitwise start the execution: 
    Func is_even_bitwise completes execution: 
    0.037116499996045604 

-----

### Преимущества первой реализации:

#### По сравнению со второй реализацией простой и понятный код.

_____

### Недостатки:

#### 1) Если стоит задача написать мега-эффективный код то, первая реализация нам не подойдет, так как будет работать медленнее, а значит вторая реализация в данном контексте побеждает.
#### 2) Если стоит задача написать 'хороший' код, то второй вариант нам не подойдет, так как побитовые операции ухудшают читабельность кода. 

_____

## Developer: Dr1DeX
