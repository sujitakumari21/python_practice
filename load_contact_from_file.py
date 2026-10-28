#LOAD_CONTACT_FROM_FILE

import json 
import os
FILE_NAME = "contacts.json"

#Dictionary
contacts = {}

#----------------------
#Load Contacts from file
#----------------------

def load_contacts():
    global contacts 
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                contacts = json.load(file)
        except:
            contacts = {}
    else:
        contacts = {}

#------------------------------
#Save Contacts
#-------------------------------

def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

#-------------------------
#Add contacts
#-------------------------

def add_contacts():
    name = input("Enter Name: ").strip().title()
    if name in contacts:
        print("Contact already exists.") 
        return
    phone = input("Enter phone number: ")
    email = input("Enter Email: ")
    
    contacts[name] = {
        "Phone" : phone,
        "Email" : email
    }       
    save_contacts()
    print("Contact added successfully.")
    
#------------------------
#Search Contact
#-----------------------
    
def search_contact():
    name = input("Enter Name to Search: ").strip().title()
    if name in contacts:
        print("\nContact Found")
        print("---------------------------------")
    else:
        print("Contact not found.")

#--------------------------
#Updated Contact
#---------------------------
def update_contact():
    name = input("Enter Name to Update : ").strip().title()
    if name in contacts:
        phone = input("Enter New Phone : ")
        email = input("Enter New Email : ")
        
        contacts[name]["Phone"] = phone
        contacts[name]["Email"] = email
        save_contacts()
        print("Contact updated successfully.")
    else:
        print("Contact Not Found.")

#--------------------------
#Delete Contact
#--------------------------

def delete_contacts():
    name = input("Enter Name to Delete : ").strip().title()
    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")
        
#--------------------------
#Display Contacts
#--------------------------
def display_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
        return
    print("\n=========== CONTACT LIST ===========\n")
    
    for name, details in contacts.items():
        print("Name :", name)
        print("Phone :", details["Phone"])
        print("Email :", details["Email"])
        print("-----------------------------------------------")

#----------------------
#Main program
#---------------------------
load_contacts()
while True:
    print("\n=====================================")
    print("        CONTACT BOOK SYSTEM       ")
    print("=======================================")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contacts()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contacts()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Thank you for using Contact Book.")
        break
    else:
        print("Invalid Choice. Please try again.")