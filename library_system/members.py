library_members = []


def register_member(name):
    library_members.append(name)


def find_member(name):
    if name in library_members:
        print("Registered")
    else:
        print("Not Register")


'''name_ex = input("Enter name: ")
print(register_member(name_ex))
print(library_members)
print(find_member(name_ex))

'''


