import os
from config_parser import ConfigParser


def run_tests():
    # Пример 1: Конфигурация для веб-сервера
    config1_content = """
    |# Конфигурация веб-сервера #|
    port = 8080
    routes = ({ "/home", "/about", "/contact" })
    """
    with open("test_config1.txt", "w") as file:
        file.write(config1_content)

    parser = ConfigParser("test_config1.txt")
    result = parser.parse()
    assert result == {
        "port": 8080,
        "routes": ["/home", "/about", "/contact"]
    }
    print("Тест 1 пройден: конфигурация веб-сервера")

    # Пример 2: Конфигурация базы данных
    config2_content = """
    |# Конфигурация базы данных #|
    host = "localhost"
    port = 5432
    retries = ({ 1, 2, 3, 4, 5 })
    """
    with open("test_config2.txt", "w") as file:
        file.write(config2_content)

    parser = ConfigParser("test_config2.txt")
    result = parser.parse()
    assert result == {
        "host": "localhost",
        "port": 5432,
        "retries": [1, 2, 3, 4, 5]
    }
    print("Тест 2 пройден: конфигурация базы данных")


if __name__ == "__main__":
    run_tests()
    print("Все тесты пройдены успешно!")
