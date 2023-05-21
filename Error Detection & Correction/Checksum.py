def BinToDec(value):
    try:
        return int(value,2)
    except ValueError:
        return "Invalid binary value"


frame_count=int(input("Enter number of frames: "))
frame_size=int(input("Enter size of each frame: "))
frame=[]

sum_frames=0 #stores decimal sum of all frames

for i in range(frame_count):
    temp=str(input("Enter frame: "))
    frame.append(temp)
    #converting frame to Decimal and then adding
    sum_frames=sum_frames+BinToDec(frame[i]) 
    
#converting sum_frames to sum_frames_binary   
sum_frames_binary = str(bin(sum_frames))

#removing the intial 0b which indicates it's a binary
sum_frames_binary = sum_frames_binary[2:]  

#counting the the number of bits of binary of sum of frames exceeds the original frames size by how much
extra_bits_count = len(sum_frames_binary) - frame_size

#if extra bits are not zero then we do the following adjustments
if extra_bits_count!=0:
    #spliting binary of sum into 2 parts. 1st part the new extra bits (a.k.a carry bits) and the orginial frame size 
    split1 = sum_frames_binary[:extra_bits_count]
    split2 = sum_frames_binary[extra_bits_count:]
    
    #Now implementing: taking of the split 1 bits and adding to split 2 -->
    #converting split 1 and split 2 to Decimal
    split1_dec = BinToDec(split1)
    split2_dec = BinToDec(split2)
    #adding decimals of split 1 and split 2 and storing them
    temp_sum = split1_dec + split2_dec
    
    #removing the intial 0b which indicates it's a binary
    temp_sum = str(bin(temp_sum))
    temp_sum = temp_sum[2:]
    
    #to keep frame size constant we add 0 in the start
    missing = frame_size - len(temp_sum)
    temp_sum = "0"*missing + temp_sum
    ittr=temp_sum

#if extra bits count is 0 then we dont have to adjust the bits
else:
    missing = frame_size - len(sum_frames_binary)
    sum_frames_binary = "0"*missing + sum_frames_binary
    ittr=sum_frames_binary
    
#ittr the total sum in either of the cases (for uniformity of code)

#we can get our "Checksum" by taking 1's inverse of temp_sum
checksum=""
for i in range(frame_size):
    if(ittr[i]=="0"):
        checksum += "1"
    elif(ittr[i]=="1"):
        checksum += "0"

print("\nTotal Sum:",ittr)
print("Checksum:",checksum)

print("\nSent Message:")
print(checksum)
for i in range(frame_count):
    print(frame[i])
