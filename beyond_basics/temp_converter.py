temperatures = [10, -20, -289, 100]

def c_to_f(c):
    if c < -273.15:
        print("No sense!")
    else:
        f = c * 9/5 + 32
        with open("c_to_f.txt", "a") as myFile:
            myFile.write(str(f) + "\n")
for t in temperatures:
    print(c_to_f(t))