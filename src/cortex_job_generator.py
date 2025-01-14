import requests

# Auth
API_KEY = "VTjUoDxcCXqUsjWYy9NOI9ivva+rJFy6"
headers = {"Authorization": f"Bearer {API_KEY}", 'X-Organisation': 'bob'}
HIVE_URL = "https://localhost/thehive"
cortexId = "test"

def create_cortex_job(data):
    response = requests.post(f"{HIVE_URL}/api/connector/cortex/job", json=data, headers=headers, verify=False)
    return response

def get_cortex_job(jobId):
    response = requests.get(f"{HIVE_URL}/api/connector/cortex/job/{jobId}", headers=headers, verify=False)
    return response

def generate_cortex_jobs(observableIds):
    analyzerIds = {}

    for res in requests.get(f"{HIVE_URL}/api/connector/cortex/analyzer", headers=headers, verify=False).json():
        if res["name"] == "ThreatMiner_1_0":
            analyzerIds["ThreatMiner_1_0"] = res["id"]
        elif res["name"] == "TorProject_1_0":
            analyzerIds["TorProject_1_0"] = res["id"]
        elif res["name"] == "Urlscan_io_Search_0_1_1":
            analyzerIds["Urlscan_io_Search_0_1_1"] = res["id"]
        elif res["name"] == "VirusTotal_GetReport_3_1":
            analyzerIds["VirusTotal_GetReport_3_1"] = res["id"]
        elif res["name"] == "AbuseIPDB_1_0":
            analyzerIds["AbuseIPDB_1_0"] = res["id"]

    cortexJobIDs = {}

    for observable_id in observableIds:
        for analyzer_id in analyzerIds:
            cortex_job_data = {
                "analyzerId": analyzer_id,
                "cortexId": cortexId,
                "artifactId": observable_id
            }
            cortex_job_response = create_cortex_job(cortex_job_data)
            cortexJobIDs[cortex_job_response.json()["_id"]] = observable_id

    return cortexJobIDs