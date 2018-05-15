from initialScript import Initiate


class DbOperations:
    def __init__(self):
        db = Initiate()
        self.conn = db.conn
        self.jobs = db.jobs
        self.c = db.c

    def save(self, data):
        self.c.execute("INSERT OR IGNORE INTO {tn} (name, status, time) VALUES ({n}, {s}, {t})". \
                  format(tn=self.jobs, n=data.name, s=data.status, t=data.time))

        self.conn.commit()
        self.conn.close()