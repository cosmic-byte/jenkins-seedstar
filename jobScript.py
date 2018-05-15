import jenkins
from config import Config


def start():
    db = Config()
    db.start()
    server = jenkins.Jenkins('http://localhost:8080', username='admin', password='e60fae9cf43e45cba8faa33c3ff746c9')
    user = server.get_whoami()
    version = server.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))

if __name__ == '__main__':
       start()