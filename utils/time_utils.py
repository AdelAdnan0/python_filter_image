from datetime import datetime

def unique_id():
    """Generate a unique ID using the current timestamp."""
    return datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
