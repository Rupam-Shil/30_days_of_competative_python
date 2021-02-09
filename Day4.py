# Jack bought a 400 hot dogs for the school picnic.
# If they were contained in packages of 8 hot dogs,
# hot many total packages did he buy?
# Create a python program without using / or % operator

hotdogs = 400
packages = 0
z = 1
for i in range(1,hotdogs+1):
  if z == 8:
    packages += 1
    z = 1
  else:
    z += 1
print(packages)
