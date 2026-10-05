# *args- variable argument length positional argument(0 to n number of argument)
def add(*args):
    #print(args, type(args))
    fun = sum(args)
    print(fun)
add(12,4,3,6,45,0,65)  


# def student_info(name,id,*marks):
#     fun =(sum(marks) / len(marks))
#     #print(sum(marks),len(marks))
#     print(f"{name} with {id} secured total marks {fun}%. out of 100%")
# student_info("Bittu",100,78,93,85,90,69,77)


def student_info(name,id,*marks):
    #print(sum(marks),len(marks))
    if len(marks) == 0:
        print(f"{name} with {id} absent all the Exam.")
    else:
        fun =(sum(marks) / len(marks))
        print(f"{name} with {id} secured total marks {fun}%. out of 100%")


student_info("Bittu",101,78,93,85,90,69,77)
student_info("Shivam",102,34,58,73,57,94)
student_info("Piyush",103)