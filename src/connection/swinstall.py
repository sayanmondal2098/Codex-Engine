from fabric import Connection

# Define the username, password, and package name
username = "your_username"
password = "your_password"
package_name = "numpy"

# Define the list of IP addresses or hostnames for the minions
minions = ["192.168.1.100", "192.168.1.101", "192.168.1.102"]

# Iterate through the list of minions and install the package
for minion in minions:
    # Create an SSH connection to the minion
    c = Connection(host=minion, user=username, connect_kwargs={"password": password})

    # Install the package using the package manager
    c.sudo(f"apt-get install {package_name} -y")

    # Close the SSH connection
    c.close()
