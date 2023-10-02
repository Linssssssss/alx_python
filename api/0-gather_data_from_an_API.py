import requests


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

        # Calculate the number of completed tasks
        completed_tasks = [task for task in todo_data if task['completed']]
        num_completed_tasks = len(completed_tasks)

        # Calculate the total number of tasks
        total_num_tasks = len(todo_data)

        # Print employee TODO list progress
        print(
            f"Employee {employee_data['name']} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")

        # Print the titles of completed tasks
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
