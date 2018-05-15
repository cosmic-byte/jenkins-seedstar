import sqlite3


class Config:
    def __init__(self):
        DATABASE_NAME = 'job_script.sqlite'

        self.conn = sqlite3.connect(DATABASE_NAME)
        self.jobs = 'jobs'
        self.c = self.conn.cursor()

    def start(self):
        self.c.execute('CREATE TABLE {tn} ({nf} {ft})' \
                  .format(tn=self.jobs, nf='id', ft='INTEGER PRIMARY KEY'))

        self.c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}" \
                  .format(tn=self.jobs, cn='name', ct='TEXT'))

        self.c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}" \
                  .format(tn=self.jobs, cn='status', ct='TEXT'))

        self.c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}" \
                  .format(tn=self.jobs, cn='time', ct='TEXT'))

        self.conn.commit()
        self.conn.close()

    def save(self, data):
        self.c.execute("INSERT OR IGNORE INTO {tn} (name, status, time) VALUES ({n}, {s}, {t})". \
                  format(tn=self.jobs, n=data.name, s=data.status, t=data.time))

        self.conn.commit()
        self.conn.close()