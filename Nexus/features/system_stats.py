import psutil
from datetime import datetime


def get_system_stats():
    # Get the current time and date
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # Get memory usage
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    # Format the stats
    stats = (
        f"Current time and date is {current_time}. "
        f"CPU usage is at {cpu_usage} percent. "
        f"Memory usage is at {memory_usage} percent."
    )

    return stats
print(get_system_stats())