import threading

class FibonacciThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.result = []
    
    def run(self):
        p, q = 0, 1
        count = 0
        while count < 10000:
            self.result.append(p)
            p, q = q, p + q
            count += 1

class SquareThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.result = []
    
    def run(self):
        count = 1
        while count <= 10000:
            self.result.append(count * count)
            count += 1

class CubeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.result = []
    
    def run(self):
        count = 1
        while count <= 10000:
            self.result.append(count * count * count)
            count += 1

def main():
    # Create and start the Fibonacci thread
    fibonacci_thread = FibonacciThread()
    fibonacci_thread.start()
    
    # Create and start the Square thread
    square_thread = SquareThread()
    square_thread.start()
    
    # Create and start the Cube thread
    cube_thread = CubeThread()
    cube_thread.start()
    
    # Wait for all threads to finish
    fibonacci_thread.join()
    square_thread.join()
    cube_thread.join()

    # Retrieve the results
    fibonacci_result = fibonacci_thread.result
    square_result = square_thread.result
    cube_result = cube_thread.result
    
    # Print the first and last elements of each result
    print("Fibonacci Result: First={}, Last={}".format(fibonacci_result[0], fibonacci_result[-1]))
    print("Square Result: First={}, Last={}".format(square_result[0], square_result[-1]))
    print("Cube Result: First={}, Last={}".format(cube_result[0], cube_result[-1]))

if __name__ == '__main__':
    main()
