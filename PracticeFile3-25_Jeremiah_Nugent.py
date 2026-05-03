#In this practice file, I learned how to implement a GUI tracker.
# In[1]:
#First attempt without GUI tracker
contacts = {
    'jsmith@mymail.com': '801-555-1223',
    'jdoe@mymail.com': '810-555-9887'
}


def lookup_phone(email):
    """Return the phone number for the given email, or '** not found **' if not present."""
    if email in contacts:        
        return contacts[email]
    else:
        return '** not found **'


print('Enter an email address to lookup phone, or <return> when done')

while True:
    email = input('> ').strip()
    if email == '':
        break
    phone = lookup_phone(email)
    print(phone)


# In[2]:
#First attempt with GUI tracker
import tkinter as tk
from tkinter import ttk

# Contacts dictionary (same as console version)
contacts = {
    'jsmith@mymail.com': '801-555-1223',
    'jdoe@mymail.com': '810-555-9887'
}


def lookup_phone(email):
    """Return phone or not-found message."""
    if email in contacts:
        return contacts[email]
    else:
        return '** not found **'


def perform_lookup():
    """Get email from entry, lookup, and display result."""
    email = email_entry.get().strip()
    if not email:
        result_label.config(text="Please enter an email address", foreground="red")
        return
    
    phone = lookup_phone(email)
    result_label.config(text=phone, foreground="black")


def clear_fields():
    """Clear both input and result."""
    email_entry.delete(0, tk.END)
    result_label.config(text="", foreground="black")


#Using GUI setup
root = tk.Tk()
root.title("Contacts Phone Lookup")
root.geometry("420x220")
root.resizable(False, False)

# Main frame for padding
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

# Prompt label
prompt_label = ttk.Label(main_frame, text="Enter an email address to lookup the phone number:")
prompt_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

# Email entry box
email_entry = ttk.Entry(main_frame, width=40, font=("Arial", 11))
email_entry.grid(row=1, column=0, columnspan=2, pady=(0, 15))
email_entry.focus()  

# Lookup button
lookup_btn = ttk.Button(main_frame, text="Lookup Phone", command=perform_lookup)
lookup_btn.grid(row=2, column=0, pady=5, padx=(0, 5), sticky="e")

# Clear button
clear_btn = ttk.Button(main_frame, text="Clear", command=clear_fields)
clear_btn.grid(row=2, column=1, pady=5, padx=(5, 0), sticky="w")

# Result display area
result_frame = ttk.LabelFrame(main_frame, text="Phone Number", padding="10")
result_frame.grid(row=3, column=0, columnspan=2, pady=15, sticky="ew")

result_label = ttk.Label(result_frame, text="", font=("Arial", 12, "bold"))
result_label.pack()


email_entry.bind("<Return>", lambda event: perform_lookup())

# Start the GUI
root.mainloop()

# In[3]:
#Second attempt for GUI with anaconda assistant help
# Define the contacts dictionary first
contacts = {
    'jsmith@mymail.com': '801-555-1223',
    'jdoe@mymail.com': '810-555-9887'
}


def lookup_phone(email):
    """Return phone or not-found message."""
    if email in contacts:
        return contacts[email]
    else:
        return '** not found **'

# Simple command-line interface that works in any environment
def main():
    print("Phone Lookup System")
    print("------------------")
    
    while True:
        print("\nOptions:")
        print("1. Look up a phone number")
        print("2. Exit")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == '1':
            email = input("Enter email address: ").strip()
            if not email:
                print("Please enter an email address")
                continue
                
            phone = lookup_phone(email)
            print(f"Phone number: {phone}")
            
        elif choice == '2':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

# Run the text-based interface
if __name__ == "__main__":
    main()


# In[4]:
