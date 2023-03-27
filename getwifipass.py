import subprocess

wifi_name = input("Name of your WiFi network: ")
command = f"/usr/bin/security find-generic-password -a {wifi_name} -g 2>&1 | awk -F '\"' '/^password:/ {{print $2}}'"
output = subprocess.check_output(command, shell=True)
password = output.decode().strip()

print(f"Your WiFi password for {wifi_name} is: {password}")
