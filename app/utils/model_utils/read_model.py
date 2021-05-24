from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import (asc, desc)

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


def read_all(*args, **kwargs):
    """
    Return Model class instances. Performs READ ALL action with dynamic filtering
    @param args[0] Model class
    @param args[1] OPTIONAL tuple filters
    @param kwargs OPTIONAL order by i.e. order=asc. If no given order kwarg, default is ascending
    """
    try:
        if len(args) < 2:
            query = args[0].query
        else:
            query = args[0].query.filter(args[1])
        
        if len(kwargs) > 0:
            if kwargs['order'] == "desc":
                return query.order_by(desc(args[0].timestamp)).all() or None
            elif kwargs['order'] == "asc":
                return query.order_by(asc(args[0].timestamp)).all() or None

        
        return query.all() or None
    except SQLAlchemyError:
        return False


