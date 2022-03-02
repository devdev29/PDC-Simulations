import numpy as np
import matplotlib.pyplot as plot

bits=[]
print("enter 5 bits")

for i in range (5):
    
    bits.append(int(input()))

print("Enter the frequency of the carrier wave")     
fc=float(input())

t=np.arange(0,5,0.01)

#generating carrier wave
c1=np.cos(2*np.pi*fc*t)
c2=-1*np.cos(2*np.pi*fc*t)


interpolated_bits=[]
modulated_wave=[]

#generating bitstream
for i in range (5):
    for j in (np.arange(i,i+1,0.01)):
        interpolated_bits.append(bits[i])
        
        
    
for i in range (len(t)):
    if (interpolated_bits[i]==0):
            modulated_wave.append(c1[i])
    else:
            modulated_wave.append(c2[i])

demodulated_wave=[]

for i in range (len(t)):
    if (modulated_wave[i]==c1[i]):
        demodulated_wave.append(0)
    else:
        demodulated_wave.append(1)

#plotting
fig, axs = plot.subplots(5)
s="carrier 1 with frequency="+str(fc)
axs[0].plot(t, c1)
axs[0].set_xlabel("time")
axs[0].set_ylabel(s)

s="carrier 2 with frequency"+str(fc)
axs[1].plot(t, c2)
axs[1].set_xlabel("time")
axs[1].set_ylabel(s)

axs[2].plot(t, interpolated_bits)
axs[2].set_xlabel("time")
axs[2].set_ylabel("bitstream")

axs[3].plot(t, modulated_wave)
axs[3].set_xlabel("time")
axs[3].set_ylabel("modulated wave")

axs[4].plot(t, demodulated_wave)
axs[4].set_xlabel("time")
axs[4].set_ylabel("demodulated wave")

plot.grid(True)
plot.show()