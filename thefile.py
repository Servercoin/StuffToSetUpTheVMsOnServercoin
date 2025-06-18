#!/usr/bin/env python3
import subprocess
import os
from datetime import datetime

def get_virtualbox_vm_name():
    try:
        output = subprocess.check_output(
            ['VBoxControl', 'guestproperty', 'get', 'VM_NAME'],
            stderr=subprocess.STDOUT
        ).decode()
        if "Value:" in output:
            return output.strip().split("Value:")[1].strip()
        return "Not set"
    except Exception as e:
        return f"Error: {e}"

vm_name = get_virtualbox_vm_name()
log_file = "/var/log/vm_name_log.txt"

# Log to a file (make sure the script has permission)
with open(log_file, "a") as f:
    f.write(f"[{datetime.now()}] VM Name: {vm_name}\n")
