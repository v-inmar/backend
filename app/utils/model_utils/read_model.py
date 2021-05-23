from sqlalchemy.exc import SQLAlchemyError

def read_single(*args):
    """
    Returna single Model class instance. Performs READ action with dynamic filtering
    @param args[0] Model class
    @param args[1] tuple filters
    """
    try:
        return args[0].query.filter(args[1]).first() or None
    except SQLAlchemyError:
        return False


def read_all(*args):
    """
    Return Model class instances. Performs READ ALL action with dynamic filtering
    @param args[0] Model class
    @param args[1] tuple filters
    """
    try:
        return args[0].query.filter(args[1]).all() or None
    except SQLAlchemyError:
        return False


