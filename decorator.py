from functools import wraps
from datetime import datetime
from pathlib import Path
import os


def logger(path='/', log_name='logger.log'):

    def decorator(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            ret = old_function(*args, **kwargs)
            log = f'''
    run-date => {datetime.now()}
    function-name =>  {old_function.__name__}
    args =>  {args}
    kwargs =>  {kwargs}
    returned :
    {ret}
    {'******'*20}'''
            Path(path).mkdir(parents=True, exist_ok=True)
            with open(os.path.join(path, log_name), 'a+', encoding="utf8") as f:
                f.write(log)
            return ret
        return new_function
    return decorator



