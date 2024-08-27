import requests

# بررسی دسترسی به URL
response = requests.get('http://192.168.200.54:8929/api/v4/projects/1', headers={'PRIVATE-TOKEN': 'glpat-E4fgvLn_yLfh577m8zkx'}, verify=False)

if response.status_code == 200:
    print("Project found:", response.json())
else:
    print("Failed to find project:", response.content)
