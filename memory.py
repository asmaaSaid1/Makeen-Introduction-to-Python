
#write a program to detemine if the memory enought or not to save files

memory=int(input("Enter size of memory:"))
n_files=int(input("Enter number of files:"))
file_size=int(input("Enter file size:"))

#caclate total size of multiple files
total_size=n_files*file_size

# if condition to compare total size with size of memory
if total_size<=memory:
    print("yes")
else:
    print("no")