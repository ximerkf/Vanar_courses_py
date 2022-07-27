## 3 SOLUTION to:

# start, end from input
# program outputs increasing or decreasing values between start .. end

# 1. if/else + seperate whiles

# start = int(input("start: "))
# end = int(input("end: "))

# if start < end:
#     while start <= end:
#         print(start)
#         start +=1
# else:
#     while start >= end:
#         print(start)
#         start -=1

# 2. seperate whiles

# start = int(input("start: "))
# end = int(input("end: "))

# while start < end:
#     print(start)
#     start +=1
    
# while start >= end:
#     print(start)
#     start -=1

#3. one while < if/else inside

start = int(input("start: "))
end = int(input("end: "))

while True:
    print(start)

    if start == end:
        break
    
    if start < end:
        start += 1
    else:
        start -= 1