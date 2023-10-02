import requests
import sys
import csv

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 1-export_to_CSV.py <employee_id>")
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

# Extract employee name and username
employee_name = employee_data['name']
employee_username = employee_data['username']

# Create a CSV file with the user ID as the filename
csv_filename = f"{employee_id}.csv"

# Open the CSV file for writing
with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Write the CSV header
    csv_writer.writerow(
        ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

    # Write TODO list data to the CSV file
    for task in todo_data:
        task_completed_status = str(task['completed'])
        task_title = task['title']
        csv_writer.writerow([employee_id, employee_username,
                            task_completed_status, task_title])

# Print a message indicating the CSV file has been created
print(f"Data exported to {csv_filename}")
