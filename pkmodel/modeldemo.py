from model import Model

sys_model = Model([5.5, 6.1], [[1,2],[0.001, 2]], [])

print(sys_model.central)
print(sys_model.peripherals)
print(sys_model.dosage)