class Logger:
    def __init__(self):
        print("object is created ")
    def __del__(self):
        print("object is destroy ")
logger = Logger()