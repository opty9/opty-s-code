def f1(*args) : 
    result = args[0]
    #첫번쨰 원소를 출력
    #첫번째 원소와 두번째 원소의 값을 비교하여 큰 값을 result에 대입
    #if args[0] > args[1] : 
    #   result = args[0]
    #else: 
    #   result = args[1]
    # if result < args[1] :
    #     result = args[1]
    
    # result 와 세번째 원소를 비교 
    #if result > args[2] : 
    #   result = result 
    #else:
    #    result = args[2]
    # if result < args[2]
    #     result = args[2]
#     for i in range(1,len(args)):
#         if result < args[i]:
#             result = args[i]
#     return result
# print(f1(1,3,56,7,8,)) 



    for i in args : 
         if result < i : 
          result = i
    return result
print(f1(1,3,54,3,))


def f2(*args) : 
    result = args[0]
    for i in args :
        print(i)
    result = 0
    for i in args : 
        result += i
    avg = result / len(args)
    return avg

print(f2(1,2,3,4,5))

