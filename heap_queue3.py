#!/usr/bin/env python3

class Heapq():
    def __init__(self):
        self.hq = list()

    def __parent(self, i):
        return (i+1) //2  -1

    def __left(self, i):
        return (i+1)*2 -1

    def __right(self, i):
        return (i+1)*2

    def __heapify(self, i, i_v):
        _cmp =  self.__right(i) - len(self.hq)
        if _cmp > 0:
            self.hq[i] = i_v
            return

        if _cmp == 0:
            l = self.__left(i)
            if self.hq[l] < i_v:
                self.hq[i], self.hq[l] = self.hq[l], i_v
            else:
                self.hq[i] = i_v
            return

        # case of _cmp < 0
        idx = [self.__left(i), self.__right(i)]
        s_v, s = min([ (self.hq[x], x) for x in idx ] + [(i_v, i)])
        if s == i:
            self.hq[i] = i_v
            return
        self.hq[i] = s_v
        self.__heapify(s, i_v)


    def pop(self):
        if len(self.hq) < 1:
            return None
        if len(self.hq) == 1:
            return self.hq.pop()

        result = self.hq[0]
        v = self.hq.pop()

        self.__heapify(0, v)
        return result

    def push(self, v):
        i = len(self.hq)
        self.hq.append(v)

        while i > 0:
            p = self.__parent(i)
            if self.hq[p] <= v: break
            self.hq[i] = self.hq[p]
            i = p

        self.hq[i] = v
        return


def main():
    b = [0, 1, 4, 4, 11, 3, 2, 5]
    heap_q = Heapq()
    for x in b:
        heap_q.push(x)

    print(heap_q.hq)
    while True:
        v = heap_q.pop()
        if v == None: break
        print (v)

if __name__ == '__main__':
    main()
