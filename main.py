from get_running_processes import get_running_processes
import json

def get_names_of_processes():
    processes = get_running_processes()
    process_names = []
    for proc in processes:
        process_names.append(proc['name'])
    return process_names

with open('processes.txt', 'w') as file:
    processes = get_names_of_processes()
    json_data = json.dumps(processes, indent=2)
    file.write(json_data)
    