import jenkins
from config import Config


# server = jenkins.Jenkins('http://localhost:3000', username='greg', password='mypassword')
# user = server.get_whoami()
# version = server.get_version()
# print('Hello %s from Jenkins %s' % (user['fullName'], version))

if __name__ == '__main__':
       db = Config()
       db.start()