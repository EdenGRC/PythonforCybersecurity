# List of API's and what they do 

# CheckPhish API
# Checks if a URL is a phishing attempt

# VirusTotal API
# lets you analyze files, URL's and IP's for malicious activity.

# Shodan API
# Acts like a search engine for internet-connected devices.


# I'm choosing to write a script to use the CheckPhish API to scan URL's

import requests
import json
import time

# Define your API key
api_key = 'gr65azt4bpmkuzciycce2agcvcghznaxvua3wcbz8sxaf0bd1zettz62nxgr4ocv'  # Replace with your API key

# Define the base API URL
base_url = 'https://developers.checkphish.ai/api/neo/scan'

# Function to submit URL for a scan
def submit_url_for_scan(url, scan_type='quick'):
    # Data payload for the scan request
    data = {
        "apiKey": api_key,
        "urlInfo": {"url": url},
        "scanType": scan_type
    }
    
    # Send the POST request to start the scan
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f"{base_url}", json=data, headers=headers)
    
    if response.status_code == 200:
        # Parse the response to get the job ID
        response_data = response.json()
        job_id = response_data.get('jobID', None)
        timestamp = response_data.get('timestamp', None)
        print(f"Scan submitted successfully. Job ID: {job_id}, Timestamp: {timestamp}")
        return job_id
    else:
        print(f"Failed to submit scan. Status Code: {response.status_code}, Response: {response.text}")
        return None

# Function to check the status of the scan
def get_scan_status(job_id):
    # Data payload for checking scan status
    data = {
        "apiKey": api_key,
        "jobID": job_id,
        "insights": True  # Set to True to get insights and screenshot info
    }
    
    # Send the POST request to check scan status
    response = requests.post(f"{base_url}/status", json=data)
    
    if response.status_code == 200:
        # Parse and return the scan result
        result = response.json()
        # Get the disposition and provide a message
        disposition = result.get('disposition', 'unknown')
        
        # Return a message based on the disposition
        if disposition == 'clean':
            print(f"The URL is CLEAN and not malicious: {result['url']}")
        else:
            print(f"The URL is considered malicious or suspicious: {result['url']} (Disposition: {disposition})")
        
        return result
    else:
        print(f"Failed to get scan status. Status Code: {response.status_code}, Response: {response.text}")
        return None

# Example Usage
if __name__ == '__main__':
    # Step 1: Get URL from the user
    url_to_scan = input("Enter the URL to scan: ").strip()
    
    if url_to_scan:
        # Step 2: Submit URL for scan
        job_id = submit_url_for_scan(url_to_scan, scan_type='quick')  # You can choose 'full' or 'quick'
        
        if job_id:
            # Step 3: Wait for the scan to complete (this can take some time)
            print("Waiting for scan to complete...")
            time.sleep(10)  # Adjust the sleep time as needed based on your scan duration
            
            # Step 4: Get the scan result
            get_scan_status(job_id)
