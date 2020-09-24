def print_lol (the_list):
    count=0
    for each_item in the_list:
        if(isinstance(each_item,list)):
            print("\t", end="")
            print_lol(each_item)
        else:
            if(count>0):
                print("\t", end=" ")
            count=1
            print(each_item, end=" ")
        print("")

cars = [['mercedes','Benz','S class'],'corvette',['Rolls Royce',['Wrath','Black Badge'],['Dawn','Aero Cowling']]]
print_lol(cars)