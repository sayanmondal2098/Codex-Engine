
# minion to connect with master and execute the command given by master in python

import paramiko

# Define the username, password, and command to be executed
username = "your_username"
password = "your_password"
command = "ls -l"

# Define the list of IP addresses or hostnames for the clients
clients = ["192.168.1.100", "192.168.1.101", "192.168.1.102"]

# Create an SSH client object
ssh = paramiko.SSHClient()

# Automatically add the host key for each client
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Iterate through the list of clients and execute the command
for client in clients:
    try:
        # Connect to the client using SSH
        ssh.connect(client, username=username, password=password)

        # Execute the command on the client
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()

        # Print the output of the command
        print(f"Output from {client}:")
        print(output)

    finally:
        # Close the SSH connection
        ssh.close()

