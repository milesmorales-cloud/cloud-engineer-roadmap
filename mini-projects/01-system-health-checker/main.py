
import time
import psutil


def get_cpu_usage():
    """Return the current CPU usage as a percentage."""
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    """Return the current memory usage as a percentage."""
    return psutil.virtual_memory().percent


def get_disk_usage(path="/"):
    """Return disk usage as a percentage for the given path."""
    return psutil.disk_usage(path).percent


def get_system_uptime():
    """Return system uptime in seconds."""
    return int(time.time() - psutil.boot_time())


def format_uptime(seconds):
    """Convert uptime seconds into days, hours, minutes and seconds."""
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    return (
        f"{days} days, {hours} hours, "
        f"{minutes} minutes, {seconds} seconds"
    )


def main():
    """Display a summary of the system's health."""
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    uptime = format_uptime(get_system_uptime())

    print("\n=== SYSTEM HEALTH REPORT ===")
    print(f"CPU Usage:    {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage:   {disk}%")
    print(f"System Uptime: {uptime}")
    print("============================\n")


if __name__ == "__main__":
    main()
