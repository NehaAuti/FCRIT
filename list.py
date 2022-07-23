myList = ["apple", "banana", "cherry"]
print("\nList of: ")
print(myList)
print(len(myList))
print(type(myList))
myList.insert(5, 6)
print(myList)
print(myList[::-1])  # does not modify the original list
myList.reverse()     # modifies the original list
print(myList)
print(min([1, 2, 3]))
print(max([1, 2, 3]))
