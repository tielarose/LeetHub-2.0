class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.maxNumbers = maxNumbers
        self.directory = [[]] * maxNumbers

    def get(self) -> int:
        for i in range(self.maxNumbers):
            if not self.directory[i]:
                self.directory[i] = 'taken'
                return i
        return -1

    def check(self, number: int) -> bool:
        return self.directory[number] == []
        
    def release(self, number: int) -> None:
        self.directory[number] = []
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)