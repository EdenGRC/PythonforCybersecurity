#In class assignment
#I added a function to the code to count restricted access attempts.

import re 

from collections import defaultdict

from urllib.parse import urlparse 

log_file_path = r'C:\Users\piegu\OneDrive\Documents\GitHub\PythonforCybersecurity\start\CH07\access.log'

with open(log_file_path, 'r') as file: 
    log_lines = file.readlines()

status_code_count = defaultdict(int)

for line in log_lines:
    match = re.search(r'\" \d{3} ', line)
    if match:
        status_code = match.group().strip().split()[1]
        status_code_count[status_code] += 1

print("Status Code Distribution: ")
for code, count in status_code_count.items():
    print(f"{code}: {count}")

ip_counts = defaultdict(int)
total_requests = len(log_lines)

for line in log_lines:
    ip_address = line.split()[0]
    ip_counts[ip_address] += 1

most_frequent_ip = max(ip_counts, key=ip_counts.get)
percentage = (ip_counts[most_frequent_ip] / total_requests) * 100

print(f"Most frequent IP: {most_frequent_ip} - {percentage:.2f}% of total")

#added functions that count the times restricted pages are attempted to be accessed.

restricted_pages = ['/admin', '/login']
restricted_page_counts = defaultdict(int)
for line in log_lines:
    for page in restricted_pages:
        if page in line:
            restricted_page_counts[page] += 1

for page, count in restricted_page_counts.items():
    print(f"{page}: {count} attempts")
