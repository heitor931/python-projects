from get_headers import generate_requests
# The goal of this script is to get the HTTP headers from a request to a list of url's

# Get input from the user

url_list_from_user = []
user_input = input("Type the url you want to request: ")
while True:
    url_list_from_user.append(user_input)
    more_url = input("Are you done? [Y/N]:")
    if more_url.lower() == "y":
        user_input = input("Type the url you want to request: ")
    else:
        print("Ok, We are Working...")
        generate_requests(url)















