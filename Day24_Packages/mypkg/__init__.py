from time import ctime
from . import a
from . import common
from . import subpkg


__all__ = [ 'a', 'common', 'ctime' ] 

# if some writes from mypkg import * than __all__ list wil be imported