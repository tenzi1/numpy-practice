# import time

# start = time.time()
# print(time.ctime())
# print(start)

# print(time.gmtime())
# print(time.thread_time())

# print(time.localtime())

# time.

# import time

# start = time.time()

# print(23*2.3)

# end = time.time()
# print('----',end - start)


from timeit import default_timer as timer

start = timer()
print(23*2.4)
end = timer()

print('----',end-start)
total = end - start

# from timeit import default_timer as timer

def get_timer(func, *args):
    
    start = timer()
    result = func(*args)
    stop = timer()
    print(f"Time taken ---{stop - start }")
    # return result
    return stop - start

# def add(a, b):
#     return a + b

# a = 1
# b= 2
# result = get_timer(add, a, b)

# print(result)

# def mul():
#     return 23*2.4

# result = get_timer(mul)
# print(result)

# print( total - result)
# if total > result:
#     print('true....')
# else:
#     print('false.........')