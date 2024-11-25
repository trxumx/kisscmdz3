import argparse
import json
import re


class ConfigParser:
    def __init__(self):
        self.constants = {}

    def parse(self, content):
        print("Оригинальный контент:\n", content)
        # Удаляем многострочные комментарии
        content = re.sub(r"\|\#.*?\#\|", "", content, flags=re.DOTALL)
        print("После удаления комментариев:\n", content)
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        print("Строки для обработки:", lines)

        result = {}
        for line in lines:
            try:
                print(f"Обработка ключ-значения: {line}")
                key, value = self._parse_key_value(line)
                result[key] = value
            except ValueError as e:
                print(f"Ошибка при обработке строки '{line}': {e}")
        print("Результат парсинга:", result)
        return result

    def _parse_constant(self, line):
        key, value = map(str.strip, line.split("=", 1))
        parsed_value = self._parse_value(value)
        self.constants[key] = parsed_value
        return key, parsed_value

    def _parse_key_value(self, line):
        key, value = map(str.strip, line.split("=", 1))
        return key, self._parse_value(value)

    def _parse_value(self, value):
        if re.match(r"^\d+$", value):  # Числа
            return int(value)
        elif re.match(r"^\(\{.*\}\)$", value):  # Массивы
            return self._parse_array(value)
        elif re.match(r'^".*"$', value):  # Строки
            return value.strip('"')
        elif value in self.constants:  # Константы
            return self.constants[value]
        else:
            raise ValueError(f"Unsupported value: {value}")

    def _parse_array(self, value):
        value = value[2:-2]  # Убираем скобки ({ })
        return [self._parse_value(item.strip()) for item in value.split(",")]


def main():
    parser = argparse.ArgumentParser(description="Учебный конфигурационный язык")
    parser.add_argument("--input", required=True, help="Путь к входному файлу")
    parser.add_argument("--output", required=True, help="Путь к выходному файлу")

    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        content = f.read()

    parser = ConfigParser()
    try:
        parsed_data = parser.parse(content)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(parsed_data, f, indent=4)


if __name__ == "__main__":
    main()
