import time
import sys

test_string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, " \
    "it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of " \
    "Darkness, it was the spring of hope, it was the winter of despair".split()

def SameLinePrint(list = ('No', 'input', 'list'), timer=0.5):
    """
    SameLinePrint takes a list or tuple and prints it on the same line. Visually similar to a timer or a loading bar.
	"""
    try:
        for i in list:
            sys.stdout.write(i+"\r")
            time.sleep(timer)
            sys.stdout.write(" " * len(i)+"\r")
    except TypeError:
        print("Error: First argument must be a list or tuple, and second argument must be an integer.")


if __name__ == "__main__":
    while True:
        SameLinePrint(test_string, 0.3)
