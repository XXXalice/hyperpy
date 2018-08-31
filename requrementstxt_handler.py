fname = "./my_super_lib_collection.txt"
import sys
try:
    with open(fname, mode="r") as re:
        lines = [ re.readlines()]
        for line in lines:
            lib_names = [line.split('==')[0] for line in lines]
            with open(fname, mode="w") as wr:
                wr.write('')
                wr.write("\n".join(lib_names))
except Exception as e:
    sys.stderr.write(str(e)+"\n")
    exit()
print("good job!!")
