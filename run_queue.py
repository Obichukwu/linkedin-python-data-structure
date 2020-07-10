import random
from queue import Queue

class Printer:
    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except ValueError:  # Queue is empty
            return "No more jobs to print."

    def print_current_job(self):
        if self.current_job != None:
            self.print_job(self.current_job)

    def get_job_from_queue_and_print(self, print_queue):
        self.get_job(print_queue)
        if self.current_job != None:
            self.print_current_job()        

    def print_job(self, job):
        while job.pages > 0:
            job.print_page()

        if job.check_complete():
            return "Printing complete."
        else:
            return "An error occurred."


class PrintQueue(Queue):
    def method1(self):
        print ("myClass method1")


class Job:
    def __init__(self, job_name):
        self.name = job_name
        self.pages = random.randint(1, 11)

    def print_page(self):
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self):
        if self.pages == 0:
            return True
        return False
    
    def __repr__(self):
        return self.name


def test_print_queue():
    print_queue = PrintQueue()
    printer = Printer()

    for i in range(1,3):
        job = Job(f'Job {i}')
        print_queue.enqueue(job)

    print(print_queue.items)
    printer.get_job_from_queue_and_print(print_queue)
    print(print_queue.items)
    printer.get_job_from_queue_and_print(print_queue)
    print(print_queue.items)
    printer.get_job_from_queue_and_print(print_queue)
    print(print_queue.items)

if __name__ == "__main__":
    test_print_queue()