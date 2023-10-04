import requests
import sys
import csv


def get_employee_info(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee details
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    user_id = employee_data.get("id")
    username = employee_data.get("username")

    # Get employee's TODO list
    todo_url = f"{base_url}/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    todo_list = todo_response.json()

    # Create a CSV file with the user_id as the filename
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the CSV header
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write the tasks to the CSV file
        for task in todo_list:
            task_completed_status = str(task["completed"])
            task_title = task["title"]
            csv_writer.writerow(
                [user_id, username, task_completed_status, task_title])

    print(f"Data exported to {'USER_ID.csv'}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
