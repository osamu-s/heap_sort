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

    _cmp =  right(i) - heap_size
    if _cmp > 0:
        return

    if _cmp == 0:
        l = left(i)
        if h[l] < h[i]:
            h[i], h[l] = h[l], h[i]
        return

    idx = [i, left(i), right(i)]
    _, s = min([ (h[x], x) for x in idx ])

    if s != i:
        # exchange
        h[i], h[s] = h[s], h[i]
        heapify(h, s)


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


def pop_heap(h):
    global heap_size

    if len(h) < 1:
        return None
    if len(h) == 1:
        return h.pop()

    result = h[0]
    v = h.pop()
    h[0] = v

    heap_size = len(h)
    heapify(h, 0)
    return result

def push_heap(h, v):

    i = len(h)
    h.append(v)

    while i > 0:
        p = parent(i)
        if h[p] <= v: break
        h[i] = h[p]
        i = p

    h[i] = v


def main():
    a = [0, 1, 4, 11, 3, 2, 5]
    heapsort(a)
    print(a)

    b = [0, 1, 4, 4, 11, 3, 2, 5]
    heap = list()
    for x in b:
        push_heap(heap, x)

    print(heap)
    while True:
        v = pop_heap(heap)
        print (v)
        if v == None: break

if __name__ == '__main__':
    main()
