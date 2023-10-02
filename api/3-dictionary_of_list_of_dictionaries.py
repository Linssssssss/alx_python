import requests
import json


def get_all_employees_todo():
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        # Fetch a list of all employees
        employees_url = f"{base_url}/users"
        employees_response = requests.get(employees_url)
        employees_data = employees_response.json()

        # Create a dictionary to store tasks for all employees
        all_tasks = {}

        # Iterate over each employee
        for employee in employees_data:
            employee_id = employee['id']
            employee_username = employee['username']

            # Fetch TODO items for the employee
            todo_url = f"{base_url}/users/{employee_id}/todos"
            todo_response = requests.get(todo_url)
            todo_data = todo_response.json()

            # Create a list of tasks for the employee
            employee_tasks = [
                {
                    "username": employee_username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                for task in todo_data
            ]

            # Store the employee tasks in the dictionary
            all_tasks[employee_id] = employee_tasks

        # Create a JSON file for all employees' tasks
        filename = "todo_all_employees.json"
        with open(filename, 'w') as json_file:
            json.dump(all_tasks, json_file, indent=4)

        # Print a message to indicate that the JSON file has been created
        print(f"JSON file '{filename}' created successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_all_employees_todo()
