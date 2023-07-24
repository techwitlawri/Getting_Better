if __name__=="__main__":
    name_file=open('trying,txt','w')
    first_name=input('Enter First Nmae: ')
    last_name=input('Eneter last Name: ')
    age=input('Enter Age: ')
    name_file.write(first_name)
    name_file.write(last_name)
    name_file.write(age)
    print(f"First name: {first_name} Lastname: {last_name} age:{age}")

