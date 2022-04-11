
import numpy as np
import matplotlib.pyplot as plt

bits=[]
print("enter the bits")
for i in range(8):
    bits.append(int(input()))

print("enter the frequency")
fc=int(input())
t=np.arange(0,8,0.01)
c_00=np.sin(2*np.pi*fc*t)
c_01=np.cos(2*np.pi*fc*t)
c_10=-np.sin(2*np.pi*fc*t)
c_11=-np.cos(2*np.pi*fc*t)

#creating binary stream:
interpolated_bits=[]

for i in range(8):
    for j in range(100):
        interpolated_bits.append(bits[i])

#generating qpsk wave

qpsk=[]

for i in np.arange(0,8,2):
    for j in range(200):
        if(interpolated_bits[i*100]==0):
            if(interpolated_bits[i*100+100]==0):
                qpsk.append(c_00[100*i+j])
            else:
                qpsk.append(c_01[100*i+j])

        else:
            if(interpolated_bits[i*100+100]==0):
                qpsk.append(c_10[100*i+j])
            else:
                qpsk.append(c_11[100*i+j])

demodulated_bits=[]

for i in range(4):
    if  (qpsk[i*100+1]==c_00[i*100+1]):
        for j in range(200):
            demodulated_bits.append(0)
    elif(qpsk[i*100+1]==c_01[i*100+1]):
        for j in range(200):
            if(j<=99):
                demodulated_bits.append(0)
            else:
                demodulated_bits.append(1)
    elif(qpsk[i*100+1]==c_10[i*100+1]):
        for j in range(200):
            if(j<=99):
                demodulated_bits.append(1)
            else:
                demodulated_bits.append(0)
    elif(qpsk[i*100+1]==c_11[i*100+1]):
        for j in range(200):
            if(j<=99):
                demodulated_bits.append(1)
            else:
                demodulated_bits.append(1)


fig,axs=plt.subplots(6)
axs[0].plot(t,interpolated_bits)
axs[0].set_xlabel("time")
axs[0].set_ylabel("bits")

axs[1].plot(t,c_00)
axs[1].set_xlabel("time")
axs[1].set_ylabel("c_00")

axs[2].plot(t,c_01)
axs[2].set_xlabel("time")
axs[2].set_ylabel("c_01")

axs[3].plot(t,c_10)
axs[3].set_xlabel("time")
axs[3].set_ylabel("c_10")

axs[4].plot(t,c_11)
axs[4].set_xlabel("time")
axs[4].set_ylabel("c_11")

axs[5].plot(t,qpsk)
axs[5].set_xlabel("time")
axs[5].set_ylabel("qpsk wave")


plt.show()



