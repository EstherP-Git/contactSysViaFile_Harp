# Create contact dictionary
my_dict = {
    "name": {"last":"","first":"","mi":""},
    "phone": "", 
    "email": ""
}

import json
data = ""

# load the contact.txt file in the beginning
def load_contacts_from_file(file):
  with open(file, 'r') as data_file:
    json_data = data_file.read()
    global data
    data = json.loads(json_data)
  
# call the load contact.txt file with the correct filename
load_contacts_from_file('contacts.txt')

# after we are finished working with the entire list on exit it will save the final version of the lsit
def save_contacts_to_file(contacts, filename):
  with open(filename, 'w') as outfile:
    json.dump(contacts, outfile)
    print(f'file {outfile.name} saved ')

# Get user information and append it to the dictionary list use global variables data to make sure we are on a main list
def add_contact():
  fname = input("Enter First Name: ")
  lname = input("Enter Last Name: ")
  mi = input("Enter middle Initial: ")
  phone = input("Enther Phone Number: ")
  email = input("Enther email: ")
      
  my_dict["name"]["first"] = fname
  my_dict["name"]["last"] = lname
  my_dict["name"]["mi"] = mi
  my_dict["phone"] = phone
  my_dict["email"] = email
  global data
  data.append(my_dict)
  return lname
  
  # loop through the array and list each item in a readable format
def view_contact():
  for item in data:
      print(f'Name: {item['name']['first']} {item['name']['mi']} {item['name']['last']}  phone: {item['phone']} email:  {item['email']} ')
    
    
  # find the contact based on the last name and update the phone and email
def update_contact(last_name):
    
    input_phone = input('Enter the new phone: ')
    input_email = input('Enter the new email: ')
    
    global data
    for i in data:
      if i['name']['last'] == last_name:
        i['phone'] = input_phone
        i['email'] = input_email
       
    # remove contact via last name
def remove_contact(last_name):
    
    global data
    for i in data:
      if i['name']['last'] == last_name:
        data.remove(i)
        
  # create a while loop that will continue until you press e for exit and it will end the program
exit = False
print("What would you like to do today? ")
# This loop will continue until the user presses e for exit
while True: 
  # ask the use what they want to do and use if else statements to make it happen
  user_choice = input("Press a to add a contact: v to view: u to update: r to remove: e to exit: ")
  
  if (user_choice == "a"):
    # add contact and return the last name and print message
    last_name = add_contact()
    print(f'Create an entry for {last_name}')
    # call the view function
  elif (user_choice == "v"):
    
    view_contact()
    #  call the upate function send in last name
  elif (user_choice == "u"):
    last_name = input("identify the last name of the person you would you like to update? ")
    update_contact(last_name)
    print(f'last Name: {last_name} updated')
    # call the remove function based on the last name
  elif (user_choice == "r"):  
    last_name = input("identify the last name of the person you would you like to remove? ")
    remove_contact(last_name)
    print(f'last Name: {last_name} removed')
    #this choice saves the dictioinary array to the file and prints a thank you messag and exits the program
  elif (user_choice == "e"):
    save_contacts_to_file(data, 'contacts.txt')
    print("Thank you for using our contact system!")
    break  
  # this message prints if the use enteres an different choice that what is available
  else:
    print("invald choice please press a to add a contact: v to view: u to update: r to remove: e to exit")
  