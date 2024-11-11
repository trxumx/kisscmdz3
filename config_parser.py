import argparse
import re
import json


class ConfigParser:
    def __init__(self, filename):
        self.filename = filename
        self.variables = {}

    def parse(self):
        with open(self.filename, 'r') as file:
            content = file.read()

        # Удаление многострочных комментариев
        content = re.sub(r'\|#.*?#\|', '', content, flags=re.DOTALL)

        # Парсинг констант и массивов
        lines = content.splitlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if '=' in line:
                name, value = line.split('=', 1)
                name = name.strip()
                value = value.strip()
                if not re.match(r'^[a-z]+$', name):
                    raise ValueError(f"Invalid name: {name}")
                parsed_value = self.evaluate(value)
                self.variables[name] = parsed_value
            else:
                raise ValueError(f"Syntax error in line: {line}")

        return self.variables

    def evaluate(self, value):
        if value.startswith('$(') and value.endswith(')'):
            var_name = value[2:-1].strip()
            if var_name not in self.variables:
                raise ValueError(f"Undefined variable: {var_name}")
            return self.variables[var_name]
        elif value.startswith('({') and value.endswith('})'):
            items = value[2:-2].split(',')
            return [self.evaluate(item.strip()) for item in items]
        elif value.startswith('"') and value.endswith('"'):
            # Обработка строковых значений
            return value[1:-1]
        else:
            try:
                return int(value)
            except ValueError:
                raise ValueError(f"Invalid value: {value}")


def main():
    parser = argparse.ArgumentParser(description="Парсер учебного конфигурационного языка")
    parser.add_argument('--input', required=True, help="Путь к входному файлу")
    parser.add_argument('--output', required=True, help="Путь к выходному файлу")
    args = parser.parse_args()

    try:
        config_parser = ConfigParser(args.input)
        result = config_parser.parse()
        with open(args.output, 'w') as outfile:
            json.dump(result, outfile, indent=4)
        print(f"Parsing completed. JSON written to {args.output}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
