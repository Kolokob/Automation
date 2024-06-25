
import sys
import time


def step_impl():
    end_time = time.time() + 5
    while time.time() < end_time:
        for dots in range(4):
            sys.stdout.write(f"\r{'Enjoying my work'}{'.' * dots}   ")
            sys.stdout.flush()
            time.sleep(0.3)

step_impl()
