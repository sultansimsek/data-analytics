#define a dictionary named contact_info that includes the following keys and the sample values of your choice: name, address, city, state, zip
contact_info = {
    "name": "Sultana Bahar",
    "address": "123 N Sheridan Rd",
    "city": "Chicago",
    "state": "IL",
    "zip": "60600"
}
#Print the address as properly formatted for mailing. Avoid using multiple print statements. Experiment with using a multi-line f-string (triple quotes), or use "\n" (new line) to break the address into multiple lines.\n
print(f"{contact_info['name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")
del contact_info["name"]
full_name = {
    "first name": "Sultana",
    "last name": "Bahar"
}
full_name.update({"honorific": "Ms."})
#Use the .update() method to add full_name to contact_info
contact_info.update(full_name)
print(contact_info)
#Print the formatted address again, updating as needed to include the new dictionary items.
print(f"{contact_info['honorific']} {contact_info['first name']} {contact_info['last name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")