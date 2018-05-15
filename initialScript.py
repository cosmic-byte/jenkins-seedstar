import sqlite3
import jenkins


class Initiate:
    def __init__(self):
        DATABASE_NAME = 'job_script.sqlite'

        self.conn = sqlite3.connect(DATABASE_NAME)
        self.jobs = 'jobs'
        self.c = self.conn.cursor()

        self.server = jenkins.Jenkins('http://localhost:8080', username='admin',
                                      password='e60fae9cf43e45cba8faa33c3ff746c9')

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

        self.server.create_job('first-job', jenkins.EMPTY_CONFIG_XML)
        self.server.create_job('second-job', jenkins.EMPTY_CONFIG_XML)
        self.server.create_job('third-job', jenkins.EMPTY_CONFIG_XML)

if __name__ == '__main__':
    init = Initiate()
    init.start()