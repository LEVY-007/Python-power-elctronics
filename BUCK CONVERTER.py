import numpy as np
import matplotlib.pyplot as plt
#Buck converter: Vout vs Duty Cycle
Vin = 24 
D=np.linspace(0,1,100)
Vout = D*Vin
plt.plot(D,Vout)
plt.title('Buck Converter: Vout vs Duty Cycle')
plt.xlabel('Duty Cycle (D)')
plt.ylabel('Output Voltage (Vout)')
plt.grid(True)
plt.show()