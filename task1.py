import random
import time
from queue import Queue

queue = Queue()


def generate_request():
    """ Generate a random request and add it to the queue. """
    request_id = random.randint(1, 1000)
    print(f"New request with ID {request_id} was created.")
    queue.put(request_id)


def process_request():
    """ Process a request and remove it from the queue. """
    if not queue.empty():
        request_id = queue.get()
        print(f"Request with ID {request_id} is being processed.")
    else:
        print("Requests queue is empty.")


def run():
    """ Main application workflow """
    try:
        while True:
            generate_request()
            time.sleep(1)
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("App was interrupted by user.")


if __name__ == "__main__":
    run()
