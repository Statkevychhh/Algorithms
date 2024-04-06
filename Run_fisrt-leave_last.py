class MyStack:

    def __init__(self):
        self.steck = []

    def push(self, x: int) -> None:
        self.steck.append(x)

    def pop(self) -> int:
        s = self.steck[len(self.steck)-1]
        self.steck.pop()
        return s

    def top(self) -> int:
        return self.steck[len(self.steck)-1]

    def empty(self) -> bool:
        return not self.steck
    

st = MyStack()
st.push(1)
print(st.top())
st.push(2)
print(st.top())
st.push(3)
print(st.top())
st.push(4)
print(st.top())
st.push(2)
print(st.top())
print(st.pop())
print(st.top())