import sys
import os
import time
import subprocess
import multiprocessing
import multiprocessing.pool

def run(cmd):
    print("Running: " + cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print("Output: " + out)
    print("Error: " + err)
    return p.returncode

def run_cmd(cmd):
    print("Running: " + cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print("Output: " + out)
    print("Error: " + err)
    return p.returncode

def run_cmd_and_wait(cmd):
    print("Running: " + cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess