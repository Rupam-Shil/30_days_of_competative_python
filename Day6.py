'''A floppy disk shows f bytes of free and u bytes of used.
If you delete a file of size o bytes and create a new file of size n bytes,
how many free bytes will the floppy disk have?
f,u,o,n are the user-entered value'''



bytesFree = int(input("Enter the free bytes:"))
bytesUsed = int(input("Enter the bytes used:"))
bytesDelete = int(input("Enter the bytes you want to delete:"))

if bytesDelete <= bytesUsed:
  bytesFree += bytesDelete
  bytesUsed -= bytesDelete

else:
  print("File size exceed!")


bytesCreate = int(input("Enter the bytes you want to create:"))

if bytesFree >= bytesCreate :
  bytesFree -= bytesCreate
  bytesUsed += bytesCreate

print("The Free space is {}".format(bytesFree))
