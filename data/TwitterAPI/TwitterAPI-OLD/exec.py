import database as db
from models import tweets

def run():
    pass
# Create all the tables in Models
if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()