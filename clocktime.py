import time
def second_1():
    start_time = time.time()
    running = True
    while running:
        elapsed_time = time.time() - start_time
        if int(elapsed_time)>1:
            running = False
