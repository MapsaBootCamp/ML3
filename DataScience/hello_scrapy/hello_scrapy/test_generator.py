# import random
# with open("test.txt", "w") as f:
#     for i in range(10000):
#         f.write(str(random.random() * 10 ** 8) + " avekhglkehgikehglehgleq\n")

# exit(0)


def generator_read_file(filename: str, chunk_size=100):
    with open(filename, "r+") as f:
        f.seek(0)
        while True:
            try:
                chunk_data = f.read(chunk_size)
                if len(chunk_data):
                    yield chunk_data
                else:
                    break
            except:
                break


for elm in generator_read_file("test.txt"):
    print(elm)
    print("++++++++++++++++++++++++++++++++++++++++++++++++")


def f():
    print("start f")
    for i in range(10):
        print("aval loop")
        yield i
        print("akhar loop")
        yield "salam"
    print("end f")


a = f()
print(next(a))
print(next(a))

b = f()

print(list(b))
