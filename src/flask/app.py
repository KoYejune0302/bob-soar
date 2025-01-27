from flask import Flask, request, render_template
import requests
import socket
import subprocess
import os

app = Flask(__name__)

def resolve_ip(domain):
    try:
        # Resolve the domain to an IP address
        ip = socket.gethostbyname(domain)
        return ip
    except socket.error as e:
        return f"Error resolving IP: {e}"

def write_ip_to_file(ip):
    try:
        # Overwrite the file with the resolved IP
        with open("check_ip.txt", "w") as file:
            file.write(f"{ip}\n")
    except IOError as e:
        return f"Error writing to file: {e}"

def run_main_script():
    try:
        # Get the parent directory path
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        # Path to main.py in the parent directory
        main_script_path = os.path.join(parent_dir, "main.py")
        # Run the main.py script
        print(f"Running main.py: {main_script_path}")
        subprocess.run(["python3", main_script_path], check=True)
    except subprocess.CalledProcessError as e:
        return f"Error running main.py: {e}"
    except FileNotFoundError:
        return "Error: main.py not found in the parent directory."

@app.route('/', methods=['GET', 'POST'])
def index():
    url = ""
    content = ""
    if request.method == 'POST':
        url = request.form['url']
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url

        # Extract the domain name from the URL
        domain = url.replace('http://', '').replace('https://', '').split('/')[0]

        # Resolve the IP address of the domain
        ip = resolve_ip(domain)

        # Write the resolved IP to the file (overwrite)
        if not ip.startswith("Error"):
            write_ip_to_file(ip)
            # Run main.py after writing the IP
            run_main_script()

        try:
            # Fetch the webpage content
            response = requests.get(url)
            if response.status_code == 200:
                content = response.text
            else:
                content = f"Error: Unable to fetch the webpage. Status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            content = f"Error: {e}"
    return render_template('index.html', url=url, content=content)

if __name__ == '__main__':
    app.run(debug=True)