contact = {
    "Alice": "555-1234",
    "bob": "555-5678",
    "charlie": "555-9999"
}
print(f"Alice's number: {contact["Alice"]}")
contact["Diana"] = "555-4321"
print(f"contact after adding Diana:{contact}")
contact["bob"] = "555-0000"
print(f"contact after update bob:{contact}")
del contact["charlie"]
print(f"contact after deleting charlie:{contact}")
print(f"All names: {contact.keys()}")
print(f"All numbers: {contact.values()}")
print(f"total contacts:{len(contact)}")