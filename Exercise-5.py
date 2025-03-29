# Imports sleep and queue
from dataclasses import dataclass
from queue import Queue
from time import sleep

# Simple reservation dataclass for testing
@dataclass
class Reservation:
    id:int
    name:str

class ReservationQueue:
    def __init__(self):
        # Constructs a queue to store reservations
        self.queue = Queue()

    def add_reservation(self, reservation):
        # Adds a reservation to the end of the queue
        self.queue.put(reservation)

    def get_reservation(self):
        # returns reservation from the front of the queue
        return self.queue.get()

    def queue_size(self) -> int:
        # Returns size of queue as an int
        return self.queue.qsize()

    def is_empty(self) -> bool:
        # bool if queue is empty
        return self.queue.empty()


# Used to process reservations
class ReservationAgent:
    def __init__(self, reservation_queue: ReservationQueue):
        # ties the agent to a given reservation_queue
        self.reservation_queue = reservation_queue

    def process_reservation(self):
        if not self.reservation_queue.is_empty():
            reservation = self.reservation_queue.get_reservation()
            sleep(3)
            return reservation
        else:
            raise Exception("Reservation queue is empty")

#Entrypoint
if __name__ == '__main__':
    # creates a rq and two agents
    rq = ReservationQueue()
    a1 = ReservationAgent(rq)
    a2 = ReservationAgent(rq)

    # Loops until rq has 5 reservations
    i = 0
    while rq.queue_size() < 5:
        i += 1
        # creates reservation
        r = Reservation(i, "test name")
        # adds reservation to rq
        rq.add_reservation(r)
        print(f"Added reservation {r}")

    # prints/processes reservations until the queue has 1 left
    while rq.queue_size() > 1:
        print(f"Reservation agent 1 processed: {a1.process_reservation()}")
        print(f"Reservation agent 2 processed: {a2.process_reservation()}")

    # cleans up last reservation (with two agents, it will hang with an odd number of reservations otherwise)
    print(f"Reservation agent 1 processed: {a1.process_reservation()}")
