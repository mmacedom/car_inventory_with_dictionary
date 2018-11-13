          
# LOAD DATA FUNCTION
def load_data(file, inventory, records):
    '''(file open for reading, dict of {str: list of str}, list) -> None
    
    This function loads all data from the input file into the inventory and the records. 
    
    >>>load_data(file, inventory, records)
    None
    '''
    
    # Read every line on file  
    for line in file: 
        # For lines without a hash, strip white space and split the data by commas
        if not line.startswith('#'): 
            accessory, model_number, year, colour, make, model, body_type, quantity = line.strip().split(',')
            
            # If accessory is not in inventory 
            if accessory not in inventory:
                #create an empty list in inventory for the accessory and add the model number to the inventory 
                inventory[accessory] = []
            inventory[accessory].append(model_number)
            
            #Add the split and stripped data to records 
            records.append([model_number, int(year), colour, make, model, body_type, int(quantity)])                
        
          
        
# MENU FUNCTION
def menu(inventory_size):
    ''' (int) -> str
    
    Return the menu selection from the user based on the inventory size. 
    
    >>> menu(0)
    Car Inventory Menu
    ==================

    1- Add a Car
    Q- Quit

    Enter your selection:
    
    >>> menu(1)
    Car Inventory Menu
    ==================

    1- Add a Car
    2- Remove a Car
    3- Find a Car
    4- Show Complete Inventory
    5- Output Inventory to File
    Q- Quit

    Enter your selection: 
    
    >>> menu(5)
    Car Inventory Menu
    ==================

    1- Add a Car
    2- Remove a Car
    3- Find a Car
    4- Show Complete Inventory
    5- Output Inventory to File
    Q- Quit

    Enter your selection: 
    '''
    # Always print this statement when function is called 
    print('\nCar Inventory Menu\n================== \n\n1- Add a Car')
    
    # Get and return user input when the lenght of the inventory is greater than 0        
    if inventory_size > 0:  
        print('2- Remove a Car\n3- Find a Car\n4- Show Complete Inventory\n5- Output Inventory to File')
        
    # Always print this statment when the function is called
    print('Q- Quit')
    
    # Get selection input from user
    selection = input('\nEnter your selection: ')
    print()
    
    return selection
        
          

# FIND INDEX FUNCTION    
def find_index(records, model_number):
    '''(list, str) -> int
    
    Return the index of the car with a matching model number after searching through records.
    
    >>>find_index(records, NDAD7)
    0
    >>>find_index(records, ZN3EU)
    2
    >>>find_index(records, ABCDE)
    -1
    '''
    # start result at -1 
    result = -1    
    
    # if the model number is a match in inventory, assign tbe model number index to result 
    for item in range(len(records)): 
        if model_number == records[item][0]:
            result = item
            
    return result    


# ADD CAR FUNCTION
def add_car(inventory, records):
    '''(dict of {str: list of str}, list) -> None
    
    This function adds the accessory and model number to the inventory and the car to the records if and only if the car is not already part of the inventory. 
    
    >>> add_car(inventory, records)
    None
    '''
    
    # Get model number input from user
    model_number = input('Enter the model number: ')
    
    index = find_index(records, model_number)
    
    # If the car model number cannot be found in records.
    if index == -1:
        accessory = input('Enter the accessory: ')
        
        # if the accessory is not found in inventory
        if accessory not in inventory:
            
            #create an empty list and append the model number to the accessory in inventory 
            inventory[accessory] = []
        inventory[accessory].append(model_number)
            
        year = int(input('Enter the year: '))
        colour = input('Enter the colour: ')          
        make = input('Enter the make: ')
        model = input('Enter the model: ')
        body_type = input('Enter the body type: ')
        quantity = int(input('Enter the quantity: '))
        
        # Add data to records
        records.append([model_number, year, colour, make, model, body_type, quantity])       
        print('\nNew car successfully added.\n')     
    
    # If the car model number is found in records
    else:
        print('\nCar already exist in inventory.\n')
        quantity = int(input('Enter the quantity to be added: '))
        records[index][6] += quantity
        
        print('Increased quantity by' , quantity, '. New quantity is:', records[index][6], '\n')  
         
          
      
# REMOVE CAR FUNCTION
def remove_car(inventory, records):
    '''(dict of {str: list of str}, list) -> None
    
    This function removes a model number of a car from the inventory and from the list of records if and only if the car quantity is one. If the quantity is greater than one, it decreases the quantity of the car by one. 
    
    >>> remove_car(inventory, records)
    None
    '''
  
    # get accessory input from user
    accessory = input('Enter the accessory: ')
    
    # Search accessory in inventory and if accessory if found in inventory
    if accessory in inventory:
        model_number = input('Enter the model number: ')
        
        # Search for model number in the accessory list in inventory
        if model_number in inventory[accessory]:
            index = find_index(records, model_number)
            
            # If the model number is found in records
            if index != -1:
                # If the car quantity is 1
                if records[index][6] == 1:
                    records.pop(index) 
                    print('\nCar removed from inventory.\n')
                    inventory[accessory].remove(model_number)
                    
                    # if the accessory list is empty, remove accessory from inventory
                    if len(inventory[accessory]) == 0:
                        inventory.pop(accessory)                           
                # If the car quantity is different than 1   
                else:
                    records[index][6] = records[index][6] - 1
                    print("Car quantity is greater than one.\n Decreased quantity by 1. New quantity is: " + str(records[index][6]) + '\n')  
        # If the model number is not found in record           
        else:
            print('No cars with model number ' + model_number + ' for accessory ' + accessory + '. Cannot remove car!')  
            
    # if accessory is found in inventory      
    else: 
        print('No cars for accessory ' + accessory + '. Cannot remove car!\n')  
        
          
           
# FIND CAR FUNCTION   
def find_car(inventory, records):
    '''(dict of {str: list of str}, list) -> None
    
    This function searches for a car model model number to determine if a car record already exists or not. If the model number is found in the inventory accessories, the function prints the car data.  
    
    >>> find_car(inventory, records)
    None
    '''
    # Get accessory from user
    accessory = input('Enter the accessory: ')
    
    # Search inventory for accessory and if the accessory is found in inventory
    if accessory in inventory: 
        model_number = input('Enter the model number: ')
        
        # Search for model number in the accessory list in inventory
        if model_number in inventory[accessory]:
            index = find_index(records, model_number)
            print()
            
            # If the model number is found in records
            if index != -1: 
                for item in range(len(records[index])): 
                    print(records[index][item], end = '\t')
                print('\nAccessory:', accessory)

        else:  
            print('No cars with model number ' + model_number + ' for accessory ' + accessory + '.')
            
    # if the accessory is not found in inventory   
    else: 
        print('No cars for accessory ' + accessory + '.')  
        
          
            
# SHOW INVENTORY FUNCTION
def show_inventory(inventory, records):
    '''(dict of {str: list of str}, list) -> None
    
    This function prints all of the cars for every accessory, tab-delimited, one car per line. 
    
    >>> show_inventory(inventory, records)
    None
    '''
    
    print('Complete Inventory:\n==================')
    
    
    for accessory in inventory:
        print('\n' + accessory + '\n-------------')
        
        for car in range(len(records)):
            
            # If the model number iis found in the inventory accessory
            if records[car][0] in inventory[accessory]: 
                for item in range(len(records[car])):
                    print(records[car][item], end = '\t')
                print()
        
          
              
# OUTPUT INVENTORY FUNCTION
def output_inventory(f, inventory, records):
    '''(file open for writing, dict of {str: list of str}, list) -> None
    
    This function outputs all of the cars for every accessory, one car per line on a text file. 
    
    >>> output_inventory(f, inventory, records)
    None
    '''    
    
    # On file, write
    f.write('Complete Inventory:\n==================\n')
    
    # Loop through inventory 
    for accessory in inventory:
        
        # Write the accessory 
        f.write('\n' + accessory + '\n-------------\n')
        
        for car in range(len(records)):
            
            # If the model number iis found in the inventory accessory 
            if records[car][0] in inventory[accessory]: 
                for item in range(len(records[car])):
                    f.write(str(records[car][item]))
                    f.write('\t')
                f.write('\n')
        
          

# MAIN FUNCTION   
def main():
    
    inventory = {}
    records = []
    
    #Open file
    with open ("a3.csv", "r") as file: 
        load_data(file, inventory, records)
    
    
    selection = menu(len(inventory))
    
    # Call different functions based on user input
    while selection != 'q' and selection != 'Q':
        if selection == '1':       
            add_car(inventory, records)
            
        elif len(inventory) == '0' or selection < '0' or selection > '5':
            print('Wrong Selection, try again!') 
            
        elif selection == '2':        
            remove_car(inventory, records)
            
        elif selection == '3':        
            find_car(inventory, records)
            
        elif selection == '4':
            show_inventory(inventory, records)
            
        elif selection == '5':
                with open('output.txt', 'w') as f:
                    output_inventory(f, inventory, records)
                  
        selection = menu(len(inventory))
            
    print('Goodbye!')
        
        
if __name__ =="__main__":
    main()