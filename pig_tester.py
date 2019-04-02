import pig_refactored as pr
import os
import subprocess


def main():
    hello = subprocess.Popen(["python", "pig_refactored.py"],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE)
    each = subprocess.Popen(["python", "pig_refactored.py"],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE)
    pc = subprocess.Popen(["python", "pig_refactored.py"],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE)
    print(hello.communicate("hello".encode("UTF-8")))
    hello.wait()
    print(each.communicate("Each".encode("UTF-8")))
    each.wait()
    print(pc.communicate("PC".encode("UTF-8")))
    pc.wait()
    # print(pr.pig_latinize("hello"))
    # print("First test passes: ", (pr.pig_latinize("hello") == "ellohay"))
    # print(pr.pig_latinize("each"))
    # print("Second test passes: ", (pr.pig_latinize("Each") == "Eachway"))
    # print(pr.pig_latinize("PC"))
    # print("Third test passes: ", (pr.pig_latinize("PC") == "PCAY"))

if __name__ == "__main__":
    main()
