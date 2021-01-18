in_file=open("inA.txt")
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

out_file = open("outA.txt","w")

for line in lines:
    nums = line.split()
    if len(nums) != 3:
        pass
    else:
        try:
            for i,num in enumerate(nums):
                nums[i] = int(num)
            progress_each_day = nums[0]-nums[1]
            hill_height = nums[2]
            days = hill_height//progress_each_day
            out_file.write(str(days) + "\n")
        except ValueError:
            pass

out_file.close()
