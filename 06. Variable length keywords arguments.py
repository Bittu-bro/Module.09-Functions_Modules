# # ** kwargs- variable length keyword arguments


# def student_info(name,id,**sub_marks):
#     #print(type(sub_marks),sum(sub_marks.values()))
    
#     if len(sub_marks) == 0:
#         print(f"{name} with {id} absent all the exam.")
    
#     elif sum(sub_marks.values()) == 0:
#         print(f"{name} with {id} got {sub_marks}") 
#     else:
#         percentage = sum(sub_marks.values())/len(sub_marks)
#         print(f"{name} with {id} secured total marks {percentage}%. out of 100%")
        

# student_info("Bittu",101)
# student_info("Shivam",102,Physic=0,chemistry=0,math = 0)
# student_info("Piyush",103,Physic=79,chemistry=82,math = 91)


def student_info(name,id,*habbit,**sub_marks):
    #print(type(sub_marks),sum(sub_marks.values()))
    
    if len(sub_marks) == 0:
        print(f"{name} with {id} absent all the exam.")
        print(f"\t They like {habbit} and may maore.")
    elif sum(sub_marks.values()) == 0:
        print(f"{name} with {id} got {sub_marks}") 
        print(f"\t They like {habbit} and may maore.")
    else:
        percentage = sum(sub_marks.values())/len(sub_marks)
        print(f"{name} with {id} secured total marks {percentage}%. out of 100%")
        print(f"\t They like {habbit} and may maore.")
        


student_info("Shivam",102,"Writing code",Physic=0,chemistry=0,math = 0)
student_info("Piyush",103,"Singing",Physic=79,chemistry=82,math = 91)
student_info("Bittu",101,"Watching Movie")