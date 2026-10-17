
import unittest
from unittest.mock import patch

import main


class TestSystemHealthChecker(unittest.TestCase):

    @patch("main.psutil.cpu_percent", return_value=25.0)
    def test_cpu_usage(self, mock_cpu):
        self.assertEqual(main.get_cpu_usage(), 25.0)
        mock_cpu.assert_called_once_with(interval=1)

    @patch("main.psutil.virtual_memory")
    def test_memory_usage(self, mock_memory):
        mock_memory.return_value.percent = 60.0
        self.assertEqual(main.get_memory_usage(), 60.0)

    @patch("main.psutil.disk_usage")
    def test_disk_usage(self, mock_disk):
        mock_disk.return_value.percent = 40.0
        self.assertEqual(main.get_disk_usage(), 40.0)
        mock_disk.assert_called_once_with("/")

    @patch("main.psutil.boot_time", return_value=1000.0)
    @patch("main.time.time", return_value=4600.0)
    def test_system_uptime(self, mock_time, mock_boot):
        self.assertEqual(main.get_system_uptime(), 3600)

    def test_format_uptime(self):
        result = main.format_uptime(90061)
        self.assertEqual(result, "1 days, 1 hours, 1 minutes, 1 seconds")


if __name__ == "__main__":
    unittest.main()
