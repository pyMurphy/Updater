import subprocess
import time
import pull

run = True

pull.clone()

while run:
    result = subprocess.run(['git', 'pull'],capture_output=True)

    if result.stdout != "Already up to date.\n":
        print("No need to run")
    else:
        pull.pull()
    time.sleep(5)