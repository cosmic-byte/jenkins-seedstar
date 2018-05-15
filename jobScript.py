from config import DbOperations
from initialScript import Initiate
import time


class Job:
    def __init__(self):
        self.db = DbOperations()
        self.init = Initiate()
        self.server = self.init.server

    def start_jobs(self):
        for job in self.server.get_jobs():
            self.db.save(data={'name': job['name'], 'status': job['color'],'time': str(time.time())})


if __name__ == '__main__':
       job = Job()
       job.start_jobs()
       job.init.conn.close()

