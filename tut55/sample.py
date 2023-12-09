def Greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Have a good one")
    return mfx


@Greet
def work(arr):
    print("Average : ", sum(arr)//len(arr))


def gym(arr):
    print("Average : ", sum(arr)//len(arr))


work([25, 8, 9, 5])

Greet(gym)([25, 8, 9, 5])
