import pyshark
from collections import defaultdict
import time
import random


# Function to log incoming requests with the source IP
def log_request(ip):
    with open("traffic_log.txt", "a") as log_file:
        log_file.write(f"{ip}\n")
    print(f"Logged IP: {ip}")


# Function to capture real IP addresses using pyshark
def capture_traffic(interface="eth0", packet_count=100):
    capture = pyshark.LiveCapture(interface=interface)
    captured_ips = []
    print(f"Starting packet capture on {interface}...")

    for packet in capture.sniff_continuously(packet_count=packet_count):
        try:
            if "IP" in packet:
                ip_src = packet.ip.src
                captured_ips.append(ip_src)
                log_request(ip_src)
        except AttributeError:
            continue  # Ignore packets without an IP layer
    print("Capture complete.")
    return captured_ips


# Function to simulate traffic and detect potential DDoS
def detect_ddos(captured_ips, threshold=100):
    ip_count = defaultdict(int)
    potential_ddos_ips = []

    for ip in captured_ips:
        ip_count[ip] += 1
        if ip_count[ip] > threshold and ip not in potential_ddos_ips:
            potential_ddos_ips.append(ip)

    for ip in potential_ddos_ips:
        print(f"Potential DDoS attack detected from IP: {ip}")


# Main function to capture and analyze traffic
def main():
    interface = "br-8bc10c89f5be"  # Set to your network interface
    packet_count = 1000  # Adjust as needed
    threshold = 50  # Adjust as needed for DDoS detection

    # Capture real IP addresses from traffic
    captured_ips = capture_traffic(interface=interface, packet_count=packet_count)

    # Detect potential DDoS based on the captured traffic
    detect_ddos(captured_ips, threshold=threshold)


if __name__ == "__main__":
    main()
