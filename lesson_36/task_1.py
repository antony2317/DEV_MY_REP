import threading
import time
import random
from queue import Queue


MAX_WORKERS = 3
worker_semaphore = threading.Semaphore(MAX_WORKERS)

orders_queue = Queue()

order_lock = threading.Lock()


class Order:
    def __init__(self, order_id, process_time):
        self.order_id = order_id
        self.process_time = process_time
        self.status = "pending"

    def __str__(self):
        return f"Order {self.order_id}: {self.status}"


class Worker(threading.Thread):
    def __init__(self, worker_id):
        super().__init__()
        self.worker_id = worker_id

    def run(self):
        while not orders_queue.empty():

            with worker_semaphore:
                order_lock.acquire()
                if orders_queue.empty():
                    order_lock.release()
                    break

                order = orders_queue.get()
                order.status = "В процессе"
                print(f"[Worker {self.worker_id}] взял {order}")
                order_lock.release()

                time.sleep(order.process_time)

                with order_lock:
                    order.status = "Выполнено"
                    print(f"[Worker {self.worker_id}] завершил {order}")


for i in range(10):
    processing_time = random.uniform(1, 3)
    orders_queue.put(Order(order_id=i + 1, process_time=processing_time))


workers = [Worker(worker_id=i + 1) for i in range(5)]

for w in workers:
    w.start()

for w in workers:
    w.join()

print("\nВсе заказы обработаны.")
