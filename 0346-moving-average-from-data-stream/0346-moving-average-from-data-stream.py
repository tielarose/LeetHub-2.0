from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.curr_total = 0
        

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.curr_total -= self.queue[0]
            self.queue.popleft()
        
        self.queue.append(val)
        self.curr_total += val

        return self.curr_total / len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)