#In class assnmt

import re 

from collections import defaultdict

from urllib.parse import urlparse 

log_file_path = r'C:\Users\piegu\OneDrive\Documents\GitHub\PythonforCybersecurity\start\CH07\access.log'

with open(log_file_path, 'r') as file: 
    log_lines = file.readlines()

statuscode_count = defaultdict(int)

for line in log_lines:
    match = re.search(r'\" \d{3} ', line)
    if match:
        status_code = match.group().strip().split()[1]
        statuscode_count[status_code] +- 1

print("Status Code Distbtn: ")
for code, count in statuscode_count.items():
    print(f"{code}: {count}")

ip_counts = defaultdict(int)
total_requests = len(log_lines)

for line in log_lines:
    ip_address = line.split()[0]
    ip_counts[ip_address] +- 1

most_frequent_ip = max(ip_counts, key=ip_counts.get)
percentage = (ip_counts[most_frequent_ip] / total_requests) * 100

print(f"Most frequent IP: {most_frequent_ip} - {percentage:.2f}% of total")
