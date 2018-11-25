#!/usr/bin/env python3

heap_size = 0 # dummy

def parent(i):
    return (i+1) //2  -1

def left(i):
    return (i+1)*2 -1

def right(i):
    return (i+1)*2

def heapify(h, i):
    global heap_size

    l = left(i)
    r = right(i)
    if (l < heap_size) and h[l] > h[i]:
        largest = l
    else:
        largest = i
    if (r < heap_size) and h[r] > h[largest]:
        largest = r
    if largest != i:
        # exchange
        h[i], h[largest] = h[largest], h[i]
        heapify(h, largest)


def build_heap(a):
    global heap_size

    heap_size = len(a)
    for i in range(len(a)//2, -1, -1):
        heapify(a, i)


def heapsort(a):
    global heap_size

    build_heap(a)
    for i in range(len(a)-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heap_size -= 1
        heapify(a, 0)


def main():
    a = [0, 1, 4, 11, 3, 2, 5]
    heapsort(a)
    print(a)


if __name__ == '__main__':
    main()
