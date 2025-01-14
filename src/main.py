import time
from case_generator import generate_case_task_observable, get_observable  # Updated import
from cortex_job_generator import generate_cortex_jobs, get_cortex_job

def main():
    # Step 1: Generate Case, Task, and Observables
    file_path = "vulnerable_ip.txt"
    case_id, task_id, observableIds = generate_case_task_observable(file_path)

    # Step 2: Generate Cortex Jobs
    cortexJobIDs = generate_cortex_jobs(observableIds)

    # Step 3: Wait for Cortex Jobs to Complete
    time.sleep(1 * len(cortexJobIDs))

    # Step 4: Print Results
    for cortex_job_id, observable_id in cortexJobIDs.items():
        cortex_job_response = get_cortex_job(cortex_job_id).json()
        if "report" in cortex_job_response:
            if "full" in cortex_job_response["report"]:
                if "node" in cortex_job_response["report"]["full"]:
                    observable_response = get_observable(observable_id).json()

                    with open("log.txt", "a") as file:
                        file.write(f"Ip Result : {observable_response['data']} {cortex_job_response['report']['full']['node']}\n")
                    print(f"Tor Node : {observable_response['data']} {cortex_job_response['report']['full']['node']}")

if __name__ == "__main__":
    main()