import requests
import csv


def get_employee_todo_progress(employee_id):
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct the URLs for employee details and TODO items
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

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
                task_completed_status = "Completed" if task['completed'] else "Not Completed"
                csv_writer.writerow(
                    [employee_id, employee_data['username'], task_completed_status, task['title']])

        # Print a message to indicate that the CSV file has been created
        print(f"CSV file '{filename}' created successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
