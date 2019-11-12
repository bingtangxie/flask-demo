from apps import create_app
from flask_script import Manager
from flask_script import Command


class Hello(Command):
    """hello world"""
    def run(self):
        print("Hello world !!!")


develop_mode = "dev"
app = create_app(develop_mode)
manager = Manager(app)
manager.add_command('hello', Hello())


@manager.command
def hello2():
    """hello world 2 !!!"""
    print("Hello World 2 !!!")


@manager.option('-n', '--name', dest='name', help='Your name', default='world')
@manager.option('-u', '--url', dest='url', default='www.csdn.com')
def hello3(name, url):
    """hello world or hello <setting name>"""
    print('hello', name)
    print(url)


if __name__ == '__main__':
    manager.run()
