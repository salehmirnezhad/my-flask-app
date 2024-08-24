from flask import Flask, request
import requests
import os

app = Flask(__name__)

# GitLab configuration settings
GITLAB_URL = 'http://192.168.200.54:8929/api/v4/projects/1/trigger/pipeline'
GITLAB_TOKEN = 'glpat-E4fgvLn_yLfh577m8zkx'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    # Check for changes in the my_playbook.yml file
    if data and 'commits' in data:
        for commit in data['commits']:
            for modified_file in commit['modified']:
                if modified_file == 'inventory_file':
                    # If the file has changed, trigger the pipeline
                    trigger_pipeline()
                    return 'Pipeline triggered', 200

    return 'No relevant changes', 200

def trigger_pipeline():
    # Send a request to trigger the pipeline
    response = requests.post(GITLAB_URL, headers={'PRIVATE-TOKEN': GITLAB_TOKEN})
    if response.status_code == 201:
        print("Pipeline triggered successfully.")
    else:
        print("Failed to trigger pipeline:", response.content)

if __name__ == '__main__':
    app.run(port=5000)
