def log_action(func):

    def wrapper(*args, **kwargs):
        print("[LOG] Running:", func.__name__)
        result = func(*args, **kwargs)
        print("[LOG] Finished:", func.__name__)
        return result

    return wrapper