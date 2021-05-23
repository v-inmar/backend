from sqlalchemy.exc import SQLAlchemyError
from app.index import db


def create(*args, **kwargs):
    """
    Return model instance that had been created
    @param args[0] Model class
    @param kwargs Named arguments i.e. something=value
    """
    try:

        # Checks model class arguments
        if not kwargs:
            new_obj = args[0]()
        else:
            new_obj = args[0](**kwargs)
        

        if type(new_obj) is not args[0]:
            raise TypeError("new_obj is not of type {}".format(args[0]))
        db.session.add(new_obj)
        db.session.flush()
        return new_obj
    except (SQLAlchemyError, TypeError):
        db.session.rollback()
        return False