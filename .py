import requests
import xmltodict
import splunklib.client as client
import splunklib.results as results
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define Palo Alto API endpoint and API key
palo_alto_api_endpoint = 'https://your-palo-alto-device.com/api/'
palo_alto_api_key = 'YOUR_API_KEY_HERE'

# Define Splunk connection details
splunk_host = 'your-splunk-server.com'
splunk_port = 8089
splunk_username = 'your-splunk-username'
splunk_password = 'your-splunk-password'

# Define Splunk index and sourcetype
splunk_index = 'your-splunk-index'
splunk_sourcetype = 'your-splunk-sourcetype'

# Create a Splunk service object
try:
    service = client.connect(
        host=splunk_host,
        port=splunk_port,
        username=splunk_username,
        password=splunk_password
    )
    logging.info("Connected to Splunk successfully.")
except Exception as e:
    logging.error(f"Failed to connect to Splunk: {e}")
    raise

# Define the Palo Alto log types to retrieve
log_types = ['traffic', 'threat', 'system']

# Loop through each log type and retrieve logs
for log_type in log_types:
    try:
        # Construct the API request
        url = f"{palo_alto_api_endpoint}?type=log&log-type={log_type}&key={palo_alto_api_key}"
        headers = {'X-PAN-KEY': palo_alto_api_key}

        # Send the API request
        logging.info(f"Fetching {log_type} logs from Palo Alto API...")
        response = requests.get(url, headers=headers)

        # Check if the response is successful
        if response.status_code == 200:
            # Parse the XML response
            response_dict = xmltodict.parse(response.content)

            # Extract the log entries
            log_entries = response_dict.get('response', {}).get('result', {}).get('log', {}).get('logs', {}).get('entry', [])

            if log_entries:
                logging.info(f"Processing {len(log_entries)} {log_type} log entries...")
                # Loop through each log entry and index in Splunk
                for log_entry in log_entries:
                    # Prepare the event data as a string
                    event_data = str(log_entry)

                    # Submit event to Splunk
                    try:
                        service.indexes[splunk_index].submit(event_data, sourcetype=splunk_sourcetype)
                        logging.info(f"Successfully indexed {log_type} log event in Splunk.")
                    except Exception as e:
                        logging.error(f"Failed to index log entry in Splunk: {e}")
            else:
                logging.info(f"No {log_type} log entries found in the response.")
        else:
            logging.error(f"Failed to fetch {log_type} logs. Status Code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        logging.error(f"Error occurred while processing {log_type} logs: {e}")
