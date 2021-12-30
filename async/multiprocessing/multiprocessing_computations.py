import datetime
import math
import multiprocessing


def main():
    do_math(1)

    t0 = datetime.datetime.now()

    print("Doing math on {:,} processors.".format(multiprocessing.cpu_count()))

    pool = multiprocessing.Pool() # by default uses the system's cpu count
    processor_count = multiprocessing.cpu_count()
    tasks = []
    for n in range(1, processor_count + 1):

        # pool.apply_async(function, args)
        #   - the function that will get its own process
        #   - the arguements for that function 
        task = pool.apply_async(do_math, (30_000_000 * (n - 1) / processor_count,
                                          30_000_000 * n / processor_count))
        tasks.append(task)

    pool.close() # lets the pool know that no more work is coming. 
    pool.join() # brings the processes together again 

    dt = datetime.datetime.now() - t0
    print("Done in {:,.2f} sec.".format(dt.total_seconds()))
    print("Our results: ")
    for t in tasks:
        print(t.get())


def do_math(start=0, num=10):
    pos = start
    k_sq = 1000 * 1000
    ave = 0
    while pos < num:
        pos += 1
        val = math.sqrt((pos - k_sq) * (pos - k_sq))
        ave += val / num

    return int(ave)


if __name__ == '__main__':
    main()