Домашнее задание №4 - Парсер конфигураций

Запуск парсинга первой конфигурации:
```bash
python parser.py --input config1.txt --output config1.json
```

Запуск парсинга второй конфигурации:
```bash
python parser.py --input config2.txt --output config2.json
```

Запуск тестов с покрытием:
```bash
coverage run --source=parser,test -m test
```