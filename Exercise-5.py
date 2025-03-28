from queue import Queue
from time import sleep


class ReservationQueue:
    def __init__(self):
        self.queue = Queue()

    def add_reservation(self, reservation):
        self.queue.put(reservation)

    def get_reservation(self):
        return self.queue.get()

    def is_empty(self):
        return self.queue.empty()

    def queue_size(self):
        return self.queue.qsize()

class ReservationAgent:
    def __init__(self, reservation_queue: ReservationQueue):
        self.reservation_queue = reservation_queue

    def process_reservation(self):
        if not self.reservation_queue.is_empty():
            reservation = self.reservation_queue.get_reservation()
            sleep(1)
            return reservation
        else:
            raise IndexError

#Entrypoint
if __name__ == '__main__':
    rq = ReservationQueue()
    agent1 = ReservationAgent(rq)
    agent2 = ReservationAgent(rq)

    i = 0
    while rq.queue_size() < 10:
        i += 1
        rq.add_reservation(f"reservation {i}")
        print(f"Added reservation {i}")

    while not rq.is_empty():
        print(f"Agent1 processed {agent1.process_reservation()}")
        print(f"Agent2 processed {agent2.process_reservation()}")