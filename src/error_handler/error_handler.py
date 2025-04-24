import time


def retry_on_error(max_retries=3, delay=1, exceptions=(Exception,)):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    print(f"Error: {e} — Retying ({attempts}/{max_retries})...")
                    time.sleep(delay)
            print(f"Error: Failed after {max_retries} attempts.")
            raise Exception(
                f"Error: Failed to search for image {kwargs['img_path'] if 'img_path' in kwargs.keys() else None}"
                )
        return wrapper
    return decorator
