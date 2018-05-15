from initialScript import Initiate


class DbOperations:
    def __init__(self):
        db = Initiate()
        self.conn = db.conn
        self.jobs = db.jobs
        self.c = db.c

    def save(self, data):
        self.c.execute("INSERT INTO {tn} (name, status, time) VALUES ('{n}', '{s}', {t})". \
                  format(tn=self.jobs, n=data['name'], s=str(data['status']), t=data['time']))

        self.conn.commit()
