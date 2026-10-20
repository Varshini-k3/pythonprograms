# Initialize a sample dictionary
user_profile = {
    "username": "coder123",
    "email": "coder@example.com",
    "location": "New York",
    "status": "Active"
}

# The keyword (key) we want to delete
keyword_to_delete = input("Enter the keyword which should be deleted:")

# Safely check if the key exists before deleting to avoid a KeyError
if keyword_to_delete in user_profile:
    del user_profile[keyword_to_delete]
    print(f"Successfully deleted '{keyword_to_delete}'.")
else:
    print(f"The key '{keyword_to_delete}' does not exist.")

# Output the updated dictionary
print("Updated Dictionary:", user_profile)
