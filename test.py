import unittest
import json
import os
from parser import ConfigParser, main


class TestConfigParser(unittest.TestCase):
    def setUp(self):
        self.parser = ConfigParser()

    def test_parse_constants(self):
        content = """
        timeout = 30
        retries = 5
        """
        expected = {"timeout": 30, "retries": 5}
        result = self.parser.parse(content)
        self.assertEqual(result, expected)

    def test_parse_array(self):
        content = """
        api_keys = ({ "key1", "key2", "key3" })
        """
        expected = {"api_keys": ["key1", "key2", "key3"]}
        result = self.parser.parse(content)
        self.assertEqual(result, expected)

    def test_multiline_comment_removal(self):
        content = """
        |#
        This is a multiline comment
        #|
        timeout = 30
        retries = 5
        """
        expected = {"timeout": 30, "retries": 5}
        result = self.parser.parse(content)
        self.assertEqual(result, expected)


class TestCommandLine(unittest.TestCase):
    def setUp(self):
        self.input_file = "test_input.txt"
        self.output_file = "test_output.json"

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_main(self):
        content = """
        timeout = 30
        retries = 5
        api_keys = ({ "key1", "key2" })
        """
        with open(self.input_file, "w", encoding="utf-8") as f:
            f.write(content)

        os.system(f"python parser.py --input {self.input_file} --output {self.output_file}")

        with open(self.output_file, "r", encoding="utf-8") as f:
            output = json.load(f)

        expected = {
            "timeout": 30,
            "retries": 5,
            "api_keys": ["key1", "key2"]
        }
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
