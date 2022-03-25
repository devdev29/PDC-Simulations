import numpy as np
import matplotlib.pyplot as plot

bits=[]
print("enter 5 bits")

for i in range (5):
    
    bits.append(int(input()))

t=np.arange(0,500,1)

interpolated_bits=[]
#Unipolar NRZ + RZ, Polar NRZ + RZ, Bipolar NRZ
unipolar_NRZ=[]  
unipolar_RZ=[]
polar_NRZ=[]
polar_RZ=[]
bipolar_NRZ=[]
bipolar_RZ=[]
manchester=[]
modulated_wave=[]

#generating bitstream
for i in range (5):
    for j in (np.arange(i,i+1,0.01)):
        interpolated_bits.append(bits[i])
        

k=1
l=0
for i in range (len(t)):

    if (interpolated_bits[i]==1):
            unipolar_NRZ.append(1)
            polar_NRZ.append(1)
            bipolar_NRZ.append((-1)**(k+1))

            if(i%100<50):
                unipolar_RZ.append(1)
                polar_RZ.append(1)
                bipolar_RZ.append((-1)**(k+1))
                manchester.append(1)

            elif(i%100>=50&i%100<100):
                
                unipolar_RZ.append(0)
                polar_RZ.append(0)
                bipolar_RZ.append(0)
                manchester.append(-1)
                if(i%100==99):
                    k+=1
                
    else:
        unipolar_NRZ.append(0)
        polar_NRZ.append(-1)
        bipolar_NRZ.append(0)
        unipolar_RZ.append(0)
        bipolar_RZ.append(0)

        if(i%100<50):
            polar_RZ.append(-1)
            manchester.append(-1)
            

        elif(i%100>=50&i%100<100):
            
            polar_RZ.append(0)
            manchester.append(1)
            # if(i%100==99):
            #         k+=1
            
            
            

#plotting

fig, axs = plot.subplots(5)

axs[0].plot(t, interpolated_bits)
axs[0].set_xlabel("time")
axs[0].set_ylabel("bitstream")

s="unipolar NRZ"
axs[1].plot(t, unipolar_NRZ)
axs[1].set_xlabel("time")
axs[1].set_ylabel(s)

s="unipolar RZ"
axs[2].plot(t, unipolar_RZ)
axs[2].set_xlabel("time")
axs[2].set_ylabel(s)

s="polar NRZ"
axs[3].plot(t, polar_NRZ)
axs[3].set_xlabel("time")
axs[3].set_ylabel(s)

s="polar RZ"
axs[4].plot(t, polar_RZ)
axs[4].set_xlabel("time")
axs[4].set_ylabel(s)

plot.grid(True)
plot.show()

fig1, axs1 = plot.subplots(4)

axs1[0].plot(t, interpolated_bits)
axs1[0].set_xlabel("time")
axs1[0].set_ylabel("bitstream")

s="bipolar NRZ"
axs1[1].plot(t, bipolar_NRZ)
axs1[1].set_xlabel("time")
axs1[1].set_ylabel(s)

s="bipolar RZ"
axs1[2].plot(t, bipolar_RZ)
axs1[2].set_xlabel("time")
axs1[2].set_ylabel(s)

s="manchester"
axs1[3].plot(t, manchester)
axs1[3].set_xlabel("time")
axs1[3].set_ylabel(s)


plot.grid(True)
plot.show()