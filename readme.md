3-е домашнее задание по конфигурационному управлению
Парсер учебного языка (принимает .txt, выдает .json)

Запуск проекта: 

C первой конфигурацией:
```bash
python parser.py --input config1.txt --output config1.json
```
Со второй конфигурацией:
```bash
python parser.py --input config2.txt --output config2.json
```
Запуск тестов и проверка покрытия:
```bash
coverage run --source=parser,test -m unittest test.py
```

```bash     
coverage report
```
