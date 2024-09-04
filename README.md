# Palo Alto Splunk Integration

Integration of Palo Alto API logs with Splunk for real-time log analysis and monitoring.

Requirements

Before running the code, make sure you have the following Python packages installed:

pip install requests xmltodict splunk-sdk

----------------------------------------------------------------------------------------------------------------

Setup
Clone the repository:
git clone https://github.com/aperire-ctrl/palo-alto-splunk-integration.git
cd palo-alto-splunk-integration

Install dependencies:
pip install -r requirements.txt

----------------------------------------------------------------------------------------------------------------

Configuration
You'll need to configure the Palo Alto and Splunk details before running the script. Create a configuration file or modify the script with your own credentials.

Example configuration in the script:
palo_alto_api_endpoint = 'https://your-palo-alto-device.com/api/'
palo_alto_api_key = 'YOUR_API_KEY_HERE'

splunk_host = 'your-splunk-server.com'
splunk_port = 8089
splunk_username = 'your-splunk-username'
splunk_password = 'your-splunk-password'

splunk_index = 'your-splunk-index'
splunk_sourcetype = 'your-splunk-sourcetype'

----------------------------------------------------------------------------------------------------------------

Usage
To run the script and integrate logs into Splunk:
Ensure that Palo Alto API credentials and Splunk credentials are configured.
Execute the script:
python your_script.py

----------------------------------------------------------------------------------------------------------------

License
This project is licensed under the MIT License. See the LICENSE file for details.
