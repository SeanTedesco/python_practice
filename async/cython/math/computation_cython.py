import datetime
import computation_lib
import multiprocessing
from threading import Thread


def main():
    computation_lib.do_math(1)

    print("Doing math on {:,} processors.".format(multiprocessing.cpu_count()))

    processor_count = multiprocessing.cpu_count()
    threads = []
    for n in range(1, processor_count + 1):
        threads.append(Thread(target=computation_lib.do_math,
                              args=(3_000_000 * (n - 1) / processor_count,
                                    3_000_000 * n / processor_count),
                              daemon=True)
                       )
    [t.start() for t in threads]

    t0 = datetime.datetime.now()

    [t.join() for t in threads]

    dt = datetime.datetime.now() - t0
    print("Done in {:,.2f} sec.".format(dt.total_seconds()))
    print("factor of {}x faster".format(1.19/dt.total_seconds()))


if __name__ == '__main__':
    main()