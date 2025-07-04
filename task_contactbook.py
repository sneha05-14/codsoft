contacts={}
def add_contact():
  name=input("Enter store name")
  pno=int(input("Enter contact number"))
  email=input("Enter email")
  address=input("Enter address")
  contacts[name]={"Phone":pno,"Email":email,"Address":address}
  print("Contact Added Successfully!\n")

def view_contact():
  if contacts:
    print("\nContact List:")
    for name, details in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
  else:
    print("No Contacts Found!\n")

def search_contact():
  search=input("Enter name to be searched")
  if search in contacts:
    print("Contact Found!\n")
  else:
    print("Contact Not Found!\n")

def update_contact():
  name=input("Enter contact name whose details to be updated")
  if name in contacts:
    pno=int(input("Enter contact number"))
    email=input("Enter email")
    address=input("Enter address")
    contacts[name]={"Phone":pno,"Email":email,"Address":address}
    print("Contact Updated Successfully!\n")
  else:
    print("Contact Not Found!\n")

def delete_contact():
  name=input("Enter contact name whose details to be deleted")
  if name in contacts:
    del contacts[name]
    print("Contact Deleted Successfully!\n")
  else:
    print("Contact Not Found!\n")

def menu():
  while True:
    print("\n****CONTACT BOOK MENU****")
    print("1.Add Contact")
    print("2.View Contact")
    print("3.Search Contact")
    print("4.Update Contact")
    print("5.Delete Contact")
    print("6.Exit")
    
    choice=input("Enter a choice{1-6}")

    if choice=='1':
      add_contact()
    elif choice=='2':
      view_contact()
    elif choice=='3':
      search_contact()
    elif choice=='4':
      update_contact()
    elif choice=='5':
      delete_contact()
    elif choice=='6':
      print("Exiting Contact Book....")
      break
    else:
      print("Invalid Choice Made!")
      print("Try Again..")

menu()
