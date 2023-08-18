import requests
from bs4 import BeautifulSoup

# Replace this with the URL of the site you want to gather information from
site_url = input("Enter the URL of the site: ")

try:
    response = requests.get(site_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract and print the website code
    site_code = soup.prettify()

    # Replace this with the specific element where admin plans are located
    admin_plans_element = soup.find('div', class_='admin-plans')

    # Extract and print the admin plans
    admin_plans = admin_plans_element.get_text() if admin_plans_element else "Admin plans not found."

    # Write the gathered information to a file
    with open('information.txt', 'w', encoding='utf-8') as file:
        file.write(f"Site Code:\n{site_code}\n\n")
        file.write(f"Admin Plans:\n{admin_plans}\n")

    print("Information has been saved to information.txt")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
