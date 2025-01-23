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




# import threading
# import time

# def print_numbers():
#     for i in range(1, 6):
#         print(f"Number: {i}")
#         time.sleep(1)  # Simulates a delay

# def print_letters():
#     for letter in 'ABCDE':
#         print(f"Letter: {letter}")
#         time.sleep(1)  # Simulates a delay


# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)


# thread1.start()
# thread2.start()


# thread1.join()              #this will help us to wait for the thread to finish
# thread2.join()

# print("Both tasks are done!")



# from multiprocessing import Process

# def print_square(numbers):
#     for n in numbers:
#         print(f"Square of {n}: {n**2}")

# def print_cube(numbers):
#     for n in numbers:
#         print(f"Cube of {n}: {n**3}")

# numbers = [1, 2, 3, 4, 5]

# # Creating processes
# process1 = Process(target=print_square, args=(numbers,))
# process2 = Process(target=print_cube, args=(numbers,))

# # Starting processes
# process1.start()
# process2.start()

# # Waiting for processes to finish
# # process1.join()
# # process2.join()

# print("Both calculations are done!")



# import asyncio

# async def jump_long():
#     print("Jumping long")
#     await asyncio.sleep(5)
#     print("Long jump done")

# async def jump_short():
#     print("Jumping short")
#     await asyncio.sleep(2)      #here we can download the file which may take some time
#     print("Short jump done")

# async def main():
#     await asyncio.gather( jump_long(),jump_short())

# asyncio.run(main())

