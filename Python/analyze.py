from scapy.all import rdpcap
from collections import Counter

# Load the pcap file
packets = rdpcap("network_logs.pcap")

# Count the IP addresses
ip_counter = Counter()
for packet in packets:
    if packet.haslayer("IP"):
        ip_counter[packet["IP"].src] += 1

# Print the top 10 IPs by packet count
for ip, count in ip_counter.most_common(10):
    print(f"IP: {ip} - Packets: {count}")
