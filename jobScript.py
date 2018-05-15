from config import DbOperations
from initialScript import Initiate
import time


class Job:
    def __init__(self):
        self.db = DbOperations()
        self.server = Initiate().server

    def start_jobs(self):
        for job in self.server.get_jobs():
            print(job)
            self.db.save(data={'name': job['name'], 'status': job['color'],'time': str(time.time())})


if __name__ == '__main__':
       job = Job()
       job.start_jobs()

