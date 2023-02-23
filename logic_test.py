starttime = "starttime".upper()
times = "times".upper()

star = "STAR"

time = "Time".upper()

print("star in starttime   ")
print(star in starttime)

print("time in starttime   ")
print(time in starttime)

print("star or time in starttime    ")
print((star or time) in starttime)
print((star or time) in times)
print(star in times or time in times)





