# class A:
#     pass
# class B:
#     pass
# class c:
#     pass
# class x(A,B,c):
#     pass
# class Y(B,c):
#     pass
# class P(x,Y):
#     pass

# print(P.mro())      

# #[<class '__main__.P'>, <class '__main__.x'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.c'>, <class 'object'>]



# class MyContextManager:
#         def __enter__(self):
#             print("Entering the context")
#             return self  # Optionally return a value to the `as` variable

#         def __exit__(self, exc_type, exc_value, traceback):
#             print("Exiting the context")
#             if exc_type:
#                 print(f"An error occurred: {exc_value}")
#             return True  # Suppresses exceptions (if any)

# with MyContextManager() as cm:
#     print("Inside the context")
#     raise ValueError("Something went wrong")


import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)  # Simulates a delay

def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")
        time.sleep(1)  # Simulates a delay

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to finish
thread1.join()
thread2.join()

print("Both tasks are done!")
