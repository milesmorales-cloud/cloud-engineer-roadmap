
import time
import urllib.error
import urllib.request


def check_service(name, url, timeout=10):
    """Check a service's availability and response time."""
    start_time = time.perf_counter()

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "ServiceStatusMonitor/1.0"},
        )

        with urllib.request.urlopen(request, timeout=timeout) as response:
            status_code = response.status

        response_time = round(
            (time.perf_counter() - start_time) * 1000, 2
        )

        return {
            "name": name,
            "url": url,
            "online": 200 <= status_code < 400,
            "status_code": status_code,
            "response_time_ms": response_time,
            "error": None,
        }

    except urllib.error.HTTPError as error:
        response_time = round(
            (time.perf_counter() - start_time) * 1000, 2
        )

        return {
            "name": name,
            "url": url,
            "online": False,
            "status_code": error.code,
            "response_time_ms": response_time,
            "error": str(error),
        }

    except (urllib.error.URLError, TimeoutError, OSError) as error:
        response_time = round(
            (time.perf_counter() - start_time) * 1000, 2
        )

        return {
            "name": name,
            "url": url,
            "online": False,
            "status_code": None,
            "response_time_ms": response_time,
            "error": str(error),
        }


def main():
    """Check multiple services and display their statuses."""

    services = [
        (
            "QuizLive",
            "https://quizlive-jmpp.onrender.com/api/health",
        ),
        (
            "Google",
            "https://www.google.com",
        ),
    ]

    print("\n====== SERVICE STATUS MONITOR ======\n")

    for name, url in services:
        result = check_service(name, url)

        print(f"Service:       {result['name']}")
        print(f"URL:           {result['url']}")
        print(
            f"Status:        "
            f"{'ONLINE' if result['online'] else 'OFFLINE'}"
        )
        print(f"HTTP Code:     {result['status_code']}")
        print(f"Response Time: {result['response_time_ms']} ms")

        if result["error"]:
            print(f"Error:         {result['error']}")

        print("------------------------------------")

    print("\n====================================")


if __name__ == "__main__":
    main()
