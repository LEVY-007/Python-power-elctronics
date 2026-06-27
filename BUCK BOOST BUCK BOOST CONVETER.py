import numpy as np
import matplotlib.pyplot as plt
#Buck, Boost , Buck-Boost converter: Vout vs Duty Cycle
Vin = 24 
D=np.linspace(0.01,0.99,100)
Vout_Buck = D*Vin
Vout_Boost = Vin/(1-D)
Vout_BuckBoost = -(Vin*D/(1-D))
plt.plot(D,Vout_Buck, label='Buck',color='blue')
plt.plot(D,Vout_Boost, label='Boost', color='red')
plt.plot(D,Vout_BuckBoost, label='Buck-Boost', color='green')
plt.title('DC-DC Converter: Vout vs Duty Cycle')
plt.xlabel('Duty Cycle (D)')
plt.ylabel('Output Voltage (Vout)')
plt.legend()    
plt.ylim(-200, 200)
plt.axhline(y=0, color='black', linewidth=0.5)
plt.grid(True)
plt.show()
for d in [0.25, 0.5, 0.75]:
    print(f"D={d}: Buck={d*Vin:.1f}V, Boost={Vin/(1-d):.1f}V, Buck-Boost={-(d/(1-d))*Vin:.1f}V")