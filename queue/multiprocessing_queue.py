from multiprocessing import Queue

custom_queue = Queue(maxsize=5)
custom_queue.put(1)
print(custom_queue.get())