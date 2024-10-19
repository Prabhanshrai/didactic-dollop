from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return '''
    <h1>Welcome to the server!</h1>
    <p>Visit <a href="/htop">/htop</a> for system information.</p>
    '''

# /htop route
@app.route('/htop')
def htop():
    # Get system information
    full_name = "Your Full Name"
    system_username = os.getenv('USER', 'unknown')
    server_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    # Get the `top` command output
    top_output = subprocess.getoutput('top -bn1')

    # Format the data to return it as a webpage
    return f'''
    <h1>Server Information</h1>
    <p><strong>Name</strong>: {full_name}</p>
    <p><strong>Username</strong>: {system_username}</p>
    <p><strong>Server Time (IST)</strong>: {server_time} IST</p>
    <pre>{top_output}</pre>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)