import time
import random
import collections

# Parameters for traffic monitoring
TIME_WINDOW = 60  # seconds
REQUEST_THRESHOLD = 1000  # maximum requests allowed per IP in the time window

# A dictionary to keep track of request counts per IP address
request_counts = collections.defaultdict(list)


def log_request(ip_address):
    current_time = time.time()
    # Clean up old requests
    request_counts[ip_address] = [
        timestamp
        for timestamp in request_counts[ip_address]
        if current_time - timestamp < TIME_WINDOW
    ]

    # Log the new request
    request_counts[ip_address].append(current_time)

    # Check if the IP has exceeded the request threshold
    if len(request_counts[ip_address]) > REQUEST_THRESHOLD:
        print(
            f"Potential DDoS attack detected from IP: {ip_address} at {time.ctime(current_time)}"
        )
    else:
        print(f"Request logged for IP: {ip_address} at {time.ctime(current_time)}")


# Simulating traffic
for _ in range(5000):  # Adjust the range to simulate more traffic
    ip = f"192.168.1.{random.randint(1, 255)}"  # Randomly generating an IP address
    log_request(ip)
    time.sleep(
        random.uniform(0.01, 0.1)
    )  # Random sleep to simulate incoming traffic at irregular intervals
