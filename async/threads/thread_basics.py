import time
import threading

def greeter(name: str, n_times: int):
    for _ in range(0, n_times):
        print(f'Hello {name}!')
        time.sleep(0.5)

def leaver(name: str, n_times: int):
    for _ in range(0, n_times):
        print(f'Bye {name}!')
        time.sleep(0.5)

def main():

    """
    thread1 = threading.Thread(target=greeter, args=("sean", 5), daemon=True)
    thread2 = threading.Thread(target=leaver, args=("sean", 5), daemon=True)

    print("before start")
    thread1.start()
    print("between start")
    thread2.start()
    print("after start")

    thread1.join()
    thread2.join()
    """

    threads = [
        threading.Thread(target=greeter, args=("sean", 5), daemon=True),
        threading.Thread(target=leaver, args=("sean", 5), daemon=True),
    ]

    [t.start() for t in threads]
    [t.join() for t in threads]
    print("done")

if __name__ == '__main__':
    main()