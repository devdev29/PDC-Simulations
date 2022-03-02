import numpy as np
import matplotlib.pyplot as plot

bits=[]
print("enter 5 bits")

for i in range (5):
    
    bits.append(int(input()))

print("Enter the frequencies of the carrier waves")     
fc1=int(input())
fc2=int(input())
t=np.arange(0,5,0.01)

#generating carrier waves
c1=np.sin(2*np.pi*fc1*t)
c2=np.sin(2*np.pi*fc2*t)

interpolated_bits=[]
modulated_wave=[]
for i in range (5):
    for j in (np.arange(i,i+1,0.01)):
        interpolated_bits.append(bits[i])
        
        
    
for i in range (len(t)):
    if (interpolated_bits[i]==0):
            modulated_wave.append(c1[i])
    else:
            modulated_wave.append(c2[i])



fig, axs = plot.subplots(4)
s="carrier 1 with frequency="+str(fc1)
axs[0].plot(t, c1)
axs[0].set_xlabel("time")
axs[0].set_ylabel(s)

s="carrier 2 with frequency"+str(fc2)
axs[1].plot(t, c2)
axs[1].set_xlabel("time")
axs[1].set_ylabel(s)

axs[2].plot(t, interpolated_bits)
axs[2].set_xlabel("time")
axs[2].set_ylabel("bitstream")

axs[3].plot(t, modulated_wave)
axs[3].set_xlabel("time")
axs[3].set_ylabel("modulated wave")

plot.grid(True)
plot.show()