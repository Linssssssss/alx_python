import requests
import csv
import sys


def export_employee_todo_to_csv(employee_id):
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct the URLs for employee details and TODO items
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch employee details
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()

        # Fetch TODO items for the employee
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Create a CSV file for the employee
        filename = f"{employee_id}.csv"
        with open(filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write the CSV header
            csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write each task to the CSV file
            for task in todo_data:
                task_completed_status = "True" if task['completed'] else "False"
                csv_writer.writerow(
                    [employee_id, employee_data['username'], task_completed_status, task['title']])

        print(f"CSV file '{filename}' created successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_employee_todo_to_csv(employee_id)
