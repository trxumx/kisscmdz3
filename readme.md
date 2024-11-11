Домашнее задание №3

Парсер конфигурационных файлов

Для запуска:

python config_parser.py --input test_config1.txt --output output.json

или

python config_parser.py --input test_config2.txt --output output.json

Для проверки покрытия ввести в консоль:

coverage run --source=config_parser,tests -m tests

coverage report
