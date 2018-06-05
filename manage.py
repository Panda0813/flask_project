from flask_migrate import MigrateCommand
from flask_script import Manager
from mainapp import create_app

app = create_app()
manager = Manager(app)

manager.add_command('db',MigrateCommand)

manager.run()