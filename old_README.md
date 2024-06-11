
### Name

Circular trainer - небольшая консольная утилита, помогающая выполнять интервальные тренировки

### Synopsis

Использование: 
    
    ./cirner.py -i

    ./cirner.py -f [файлы тренировок]


### Description

Спортивный ассистент, на данный момент, использует файлы с тренировками.

Возможен запуск в интерактивном режиме, когда предлагается выбрать существующую программу из директории 'basics', или запуск с передачей файлов напрямую.

### File format

Файлы тренировок для спортивного ассистента должны быть созданы вручную с соблюдением определенного синтаксиса. Рекомендуется сохранять файлы с раширением '\*.tss' в директории 'basics'.

Пример синтаксиса файла тренировки:

    # Название тренировки
    name='Warm-up'
    # Продолжительность пауз
    pause=5s
    # Отдых между повторами
    relax=0s
    # Количество повторов
    repiats=1
    # Пауза между тренировками
    on_end=10s

    # Символ '|' может быть использован для указания алтернативных упражнений
    ex1|ex2:30s
    # Разделителем между названия упражнения и его продолжительностью может быть как символ ':' так и '->'
    ex2|ex5->0.5m
    # Продолжительность упражнения указывается в виде числа, тогда оно будет измеряться в секундах, или чиса с модификатором времени
    ex3->40s
    ex5:1m
