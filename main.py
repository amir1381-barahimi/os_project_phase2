import multiprocessing
import threading
from multiprocessing import Process, Value, Array, Queue
from time import sleep


def add(num, value, l):
    tmp = 0
    while True:
        l.acquire()
        print('add')
        num.value += value
        tmp = num.value
        sleep(1)

        if tmp != num.value:
            print("Process conflict1")
        l.release()


def sub(num, value, l):
    tmp = 0
    while True:
        l.acquire()
        print('sub')
        num.value += value
        tmp = num.value
        sleep(1.5)
        if tmp != num.value:
            print("Process conflict2")
        l.release()


def mul(num, value, l):
    tmp = 0
    while True:
        l.acquire()
        print('mul')
        num.value *= value
        tmp = num.value
        sleep(2)
        if tmp != num.value:
            print("Process conflict3")
        l.release()


def div(num, value, l):
    tmp = 0

    while True:
        l.acquire()
        print('div')

        num.value /= value
        tmp = num.value
        sleep(3)

        if tmp != num.value:
            print("Process conflict4")

        l.release()


def Show(num, l):
    while True:
        l.acquire()
        sleep(0.5)
        print(num.value)
        l.release()


if __name__ == '__main__':
    num = Value('d', 0.0)
    l = multiprocessing.Lock()

    arr = Array('i', range(2))
    q = Queue()
    p1 = Process(target=add, args=(num, 10, l))
    p2 = Process(target=sub, args=(num, 5, l))
    p3 = Process(target=add, args=(num, 2, l))
    p4 = Process(target=sub, args=(num, 4, l))

    show = Process(target=Show, args=(num,l))
    show.start()
    sleep(1)
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
