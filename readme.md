Домашнее задание №3

Парсер конфигурационных файлов

Для запуска:

python parser.py --input config1.txt --output config1.json

или

python parser.py --input config2.txt --output config2.json

Для проверки покрытия ввести в консоль:

coverage run --source=parser,test -m test

coverage report
