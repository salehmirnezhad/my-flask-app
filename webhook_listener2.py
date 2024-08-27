import os
import time
import requests

# GitLab settings
GITLAB_URL = 'http://192.168.200.54:8929/api/v4/projects/1/trigger/pipeline'
GITLAB_TOKEN = 'glpat-dZx5211DG12zwLg13RF4'
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

if __name__ == '__main__':
    print("Monitoring changes in inventory_file...")
    while True:
        time.sleep(10)  # Check for changes every 10 seconds
        current_modified_time = os.path.getmtime(INVENTORY_FILE_PATH)

        if current_modified_time != last_modified_time:
            print("Changes detected in inventory_file. Triggering pipeline...")
            last_modified_time = current_modified_time
            trigger_pipeline()  # Call the API to trigger the pipeline
