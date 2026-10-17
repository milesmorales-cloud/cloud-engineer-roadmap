
import unittest
from unittest.mock import patch, MagicMock
import urllib.error

import main


class TestServiceStatusMonitor(unittest.TestCase):

    @patch("main.urllib.request.urlopen")
    def test_successful_response(self, mock_urlopen):
        response = MagicMock()
        response.status = 200
        mock_urlopen.return_value.__enter__.return_value = response

        result = main.check_service(
            "QuizLive",
            "https://example.com/health",
        )

        self.assertTrue(result["online"])
        self.assertEqual(result["status_code"], 200)
        self.assertIsNone(result["error"])
        self.assertGreaterEqual(result["response_time_ms"], 0)

    @patch("main.urllib.request.urlopen")
    def test_http_error(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.HTTPError(
            "https://example.com/health",
            503,
            "Service Unavailable",
            {},
            None,
        )

        result = main.check_service(
            "QuizLive",
            "https://example.com/health",
        )

        self.assertFalse(result["online"])
        self.assertEqual(result["status_code"], 503)
        self.assertIsNotNone(result["error"])

    @patch("main.urllib.request.urlopen")
    def test_connection_failure(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError(
            "Connection failed"
        )

        result = main.check_service(
            "QuizLive",
            "https://example.com/health",
        )

        self.assertFalse(result["online"])
        self.assertIsNone(result["status_code"])
        self.assertIsNotNone(result["error"])


if __name__ == "__main__":
    unittest.main()
