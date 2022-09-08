from . import main
from flask_script import Manager
from flask_migrate import MigrateCommand


manager = Manager(main.app_flask_app)
manager.add_command('db_mysql', MigrateCommand)

if __name__ == '__main__':
    manager.run()