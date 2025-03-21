import unittest
from unittest.mock import patch, MagicMock
import json
import tkinter as tk
from src.gui import fetch_json_data, send_json_data, populate_table

class TestGuiFunctions(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_json_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"key": "value"}
        result = fetch_json_data("http://testurl.com")
        self.assertEqual(result, {"key": "value"})

    @patch('requests.get')
    def test_fetch_json_data_failure(self, mock_get):
        mock_get.side_effect = Exception("Network error")
        result = fetch_json_data("http://testurl.com")
        self.assertIsNone(result)

    @patch('requests.post')
    def test_send_json_data_success(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"response": "success"}
        data = {"A": 80.0}
        result = send_json_data("http://testurl.com", data)
        self.assertEqual(result, {"response": "success"})

    @patch('requests.post')
    def test_send_json_data_failure(self, mock_post):
        mock_post.side_effect = Exception("Network error")
        data = {"A": 80.0}
        result = send_json_data("http://testurl.com", data)
        self.assertIsNone(result)

    def test_populate_table_with_dict(self):
        root = tk.Tk()
        tree = tk.ttk.Treeview(root)
        tree.pack()
        data = {"key1": "value1", "key2": "value2"}
        populate_table(tree, data)
        self.assertEqual(tree.get_children(), ['I001', 'I002'])  # Check if two items are added

    def test_populate_table_with_list(self):
        root = tk.Tk()
        tree = tk.ttk.Treeview(root)
        tree.pack()
        data = [{"key1": "value1", "key2": "value2"}, {"key1": "value3", "key2": "value4"}]
        populate_table(tree, data)
        self.assertEqual(tree.get_children(), ['I001', 'I002'])  # Check if two items are added

    def test_populate_table_with_invalid_data(self):
        root = tk.Tk()
        tree = tk.ttk.Treeview(root)
        tree.pack()
        populate_table(tree, None)
        self.assertEqual(tree.get_children(), [])  # Check if no items are added

if __name__ == '__main__':
    unittest.main()