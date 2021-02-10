#!/usr/local/bin/python3.9

import time
import paramiko
import re
import os

ip = "192.168.1.5"


def connectPi():
    sshClient = paramiko.SSHClient()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient.connect(ip, "3232", "root", "Pie!23*")

    # terminate vnc process
    stdin, stdout, stderr = sshClient.exec_command("pkill vnc; vncserver")
    output = stdout.readlines()

    sshClient.close()

    return output


def getCurrentDirectory():
    return os.path.dirname(os.path.realpath(__file__))


def openVNCApp():
    os.system("open /Applications/VNC\ Viewer.app")
    print(getCurrentDirectory())


vncOutput = connectPi()

if len(vncOutput) > 0:
    statusStr = vncOutput[len(vncOutput) - 1]
    if re.findall(ip+":\d+", statusStr):
        print(statusStr)
        openVNCApp()
    else:
        print("Failed to create vnc server")
else:
    print("failed to connect pi")
