from random import randint

class Insertion_sort():

    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)

    def sort(self):

        for i in range(self.length):
            if not self.sorted_until(i):
                self.push_down(i)

    def sorted_until(self, i):

        if i > 0:
            if self.arr[i-1] > self.arr[i]:
                return False
        return True

    def push_down(self, i):

        while self.arr[i-1] > self.arr[i]:
            self.arr[i-1], self.arr[i] = self.arr[i], self.arr[i-1]
            i -= 1
            if i == 0: break
            
arr = [randint(0, 100) for i in range(10)]
print(arr)
demo = Insertion_sort(arr)
demo.sort()
print(demo.arr)


    
            
    
