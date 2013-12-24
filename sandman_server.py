from sandman import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///db.sqlite3'

from sandman.model import activate

activate()

app.run()
