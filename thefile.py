import subprocess

def get_vm_name():
    output = subprocess.check_output([
        'sudo', '/usr/bin/VBoxControl', 'guestproperty', 'get', 'VM_NAME'
    ]).decode()
    return output.split('Value:')[1].strip()

print(get_vm_name())
