import requests
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Auth
API_KEY = "VTjUoDxcCXqUsjWYy9NOI9ivva+rJFy6"
headers = {"Authorization": f"Bearer {API_KEY}", 'X-Organisation': 'bob'}
HIVE_URL = "https://localhost/thehive"

def read_lines_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def create_case(data):
    response = requests.post(f"{HIVE_URL}/api/v1/case", json=data, headers=headers, verify=False)
    return response

def create_task(caseId, data):
    response = requests.post(f"{HIVE_URL}/api/v1/case/{caseId}/task", json=data, headers=headers, verify=False)
    return response

def create_observable(caseId, data):
    response = requests.post(f"{HIVE_URL}/api/v1/case/{caseId}/observable", json=data, headers=headers, verify=False)
    return response

def get_observable(observableId):
    response = requests.get(f"{HIVE_URL}/api/v1/observable/{observableId}", headers=headers, verify=False)
    return response

def generate_case_task_observable(file_path):
    # 1. Create Case
    case_data = {
        "title": "CheckSuspicious IP address",
        "description": "Test IP address",
    }
    case_response = create_case(case_data)
    case_id = case_response.json()["_id"]

    # 2. Create Task
    task_data = {
        "title": "Validate IP using IOC"
    }
    task_response = create_task(case_id, task_data)
    task_id = task_response.json()["_id"]

    # 3. Add Observable
    ip_addresses = read_lines_from_file(file_path)
    observableIds = []

    for ip_address in ip_addresses:
        observable_data = {"dataType": "ip", "data": ip_address}
        observable_response = create_observable(case_id, observable_data)
        observable_id = observable_response.json()[0]["_id"]
        observableIds.append(observable_id)

    return case_id, task_id, observableIds