import requests
import json


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

        # Create a JSON data structure
        json_data = {
            "USER_ID": [
                {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": employee_data['username']
                }
                for task in todo_data
            ]
        }

        # Create a JSON file for the employee
        filename = f"{employee_id}.json"
        with open(filename, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        # Print a message to indicate that the JSON file has been created
        print(f"JSON file '{filename}' created successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
