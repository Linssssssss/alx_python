import requests
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

# Get the employee ID from the command-line argument
employee_id = int(sys.argv[1])

# Define the base URL for the JSONPlaceholder API
base_url = "https://jsonplaceholder.typicode.com"

# Create URLs for getting employee details and TODO list
employee_url = f"{base_url}/users/{employee_id}"
todo_url = f"{base_url}/users/{employee_id}/todos"

# Send GET requests to the API
employee_response = requests.get(employee_url)
todo_response = requests.get(todo_url)

# Check if the responses are successful
if employee_response.status_code != 200:
    print(
        f"Error: Unable to retrieve employee details (Status Code: {employee_response.status_code})")
    sys.exit(1)

if todo_response.status_code != 200:
    print(
        f"Error: Unable to retrieve TODO list (Status Code: {todo_response.status_code})")
    sys.exit(1)

# Parse JSON responses
employee_data = employee_response.json()
todo_data = todo_response.json()

# Extract employee name
employee_name = employee_data['name']

# Calculate the number of completed and total tasks
total_tasks = len(todo_data)
completed_tasks = sum(1 for task in todo_data if task['completed'])

# Display employee TODO list progress
print(
    f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

# Display titles of completed tasks
for task in todo_data:
    if task['completed']:
        print(f"    {task['title']}")
