#!/usr/bin/env python3

class Heapq(object):
    def __init__(self):
        self.hq = list()

    def __parent(self, i):
        return (i+1) //2  -1

    def __left(self, i):
        return (i+1)*2 -1

    def __right(self, i):
        return (i+1)*2

    def __heapify(self, i, i_v):
        qlen = len(self.hq)
        _cmp =  self.__right(i) - qlen
        while _cmp <= 0:
            if _cmp == 0:
                l = self.__left(i)
                l_v = self.hq[l]
                if l_v < i_v:
                    self.hq[i] = l_v
                    i = l
                break

            # case of _cmp < 0
            idx = [self.__left(i), self.__right(i)]
            s_v, s = min([ (self.hq[x], x) for x in idx ] + [(i_v, i)])
            if s == i:
                break

            self.hq[i] = s_v
            i = s
            _cmp =  self.__right(i) - qlen

        self.hq[i] = i_v
        return


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
