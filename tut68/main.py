class A:
    def Parent_Method(self):
        print("Parent Method 1")


class B(A):
    def Parent_Method(self):
        print("Vishal")
        super().Parent_Method()

    def Child_Method(self):
        print("Parent Method 2")
        super().Parent_Method()

obj = B()
obj.Child_Method()

print("---------------")
obj.Parent_Method()