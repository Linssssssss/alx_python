import requests
import csv
import sys

def get_employee_info(employee_id):
    # Define the API URLs for employee details and TODO list
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch employee details
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print("Employee not found.")
        return

    employee_data = employee_response.json()
    user_id = employee_data["id"]
    username = employee_data["username"]

    # Fetch TODO list
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print("Failed to fetch TODO list.")
        return

    todo_list = todo_response.json()

    # Write data to CSV file with uppercase USER_ID
    filename = f"{user_id}.csv"
    with open(filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_list:
            task_completed_status = "True" if task["completed"] else "False"
            task_title = task["title"]
            csv_writer.writerow([user_id, username, task_completed_status, task_title])

    print(f"Data exported to {filename}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
