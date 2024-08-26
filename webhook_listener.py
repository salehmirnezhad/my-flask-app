def trigger_pipeline():
    # Define the parameters for the request
    data = {
        'ref': 'main',  # نام شاخه‌ای که می‌خواهید برای آن Pipeline را Trigger کنید
        'token': glpat-E4fgvLn_yLfh577m8zkx  # توکن احراز هویت
    }
    
    # Send a request to trigger the pipeline
    response = requests.post(GITLAB_URL, headers={'PRIVATE-TOKEN': GITLAB_TOKEN}, data=data)
    
    if response.status_code == 201:
        print("Pipeline triggered successfully.")
    else:
        print("Failed to trigger pipeline:", response.content)
