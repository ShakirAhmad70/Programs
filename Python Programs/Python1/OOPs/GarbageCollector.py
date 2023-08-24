import gc

# print(dir(gc))

print(gc.isenabled()) #By default enabled

gc.disable()
print(gc.isenabled())

gc.enable()
print(gc.isenabled())