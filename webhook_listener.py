from flask import Flask, request, jsonify
import requests
import os
import time
import threading

app = Flask(__name__)

# GitLab settings
GITLAB_URL = os.getenv('GITLAB_URL', 'http://192.168.200.54:8929/api/v4/projects/1/trigger/pipeline')
GITLAB_TOKEN = os.getenv('GITLAB_TOKEN', 'glpat-fDKxQ9JFzUfCE48AJwHa')
INVENTORY_FILE_PATH = '/root/my-flask-app/inventory_file'  # Path to the inventory_file

# Variable to store the last modified time
last_modified_time = os.path.getmtime(INVENTORY_FILE_PATH)

def trigger_pipeline(branch='main'):
    """
    This function triggers a pipeline in GitLab.

    Args:
        branch (str): The name of the branch for which you want to trigger the pipeline. Default is 'main'.
    """
    # Define request parameters
    data = {
        'ref': branch,
        'token': GITLAB_TOKEN,
        'variables[DEPLOY_ONLY]': 'true'  # Variable to execute the specific deployment stage
    }

    # Send request to trigger the pipeline
    response = requests.post(GITLAB_URL, data=data)

    if response.status_code == 201:
        print("Pipeline triggered successfully.")
    else:
        print("Failed to trigger pipeline:", response.content)

def monitor_inventory_file():
    """
    Monitors the inventory file for changes and triggers the pipeline if changes are detected.
    """
    global last_modified_time
    while True:
        time.sleep(10)  # Check for changes every 10 seconds
        current_modified_time = os.path.getmtime(INVENTORY_FILE_PATH)

        if current_modified_time != last_modified_time:
            print("Changes detected in inventory_file. Triggering pipeline...")
            last_modified_time = current_modified_time
            trigger_pipeline()  # Call the API to trigger the pipeline

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Webhook endpoint to trigger pipeline based on GitLab webhook events.
    """
    data = request.json
    print("Received data:", data)  # برای دیباگ

    # بررسی اینکه آیا نوع شیء 'pipeline' است
    if data and data.get('object_kind') == 'pipeline':
        # بررسی وضعیت پایپلاین
        if data.get('object_attributes', {}).get('status') == 'success':
            # Trigger deploy_to_servers stage
            response = requests.post(
                GITLAB_URL,
                headers={'PRIVATE-TOKEN': GITLAB_TOKEN},
                data={'ref': 'main'},
                verify=False
            )
            if response.status_code == 201:
                return jsonify({"message": "Pipeline triggered successfully"}), 200
            else:
                return jsonify({"message": "Failed to trigger pipeline"}), 500
        else:
            print("Pipeline status is not 'success'. Current status:", data.get('object_attributes', {}).get('status'))
            return jsonify({"message": "Pipeline not successful, no action taken."}), 200

    return jsonify({"message": "No relevant data to process"}), 400

if __name__ == '__main__':
    # Start the inventory file monitor in a separate thread
    monitoring_thread = threading.Thread(target=monitor_inventory_file)
    monitoring_thread.daemon = True
    monitoring_thread.start()

    # Start the Flask web server
    app.run(host='0.0.0.0', port=5000)
