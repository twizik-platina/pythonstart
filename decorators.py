def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Выполняется действие: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper