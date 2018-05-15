from config import DbOperations
from initialScript import Initiate


class Job:
    def __init__(self):
        self.db = DbOperations()
        self.server = Initiate().server

    def start_jobs(self):
        print(self.server.get_jobs())


if __name__ == '__main__':
       job = Job()
       job.start_jobs()