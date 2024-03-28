import requests

# You have to provide the link 
response = requests.get("https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls")


details = response.json()
names_of_users={''}

# Initialize an empty dictionary to store the counts
login_counts = {}

# Assuming 'details' is a list of dictionaries
for detail in details:
    bc = detail["user"]["login"]

    login_counts[bc] = login_counts.get(bc,0) + 1

# Print the login counts
for login, count in login_counts.items():
    print(f"{login} -> {count}")


# # repeatative users : Show the unique users .
# for x in names_of_users:
#     print(x)