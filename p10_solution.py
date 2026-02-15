import time
attempts = 0
max_attempts = 5
wait_time = 1
while (attempts<max_attempts):
    print("attempt - ", attempts + 1, "- wait time", wait_time)
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2