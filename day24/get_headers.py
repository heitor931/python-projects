import requests
import re
from datetime import datetime

def generate_requests(url_list):
    if url_list:
        try:
            write_to_file(url_list)
            print("Requests completed successfully.")
        except Exception as e:
            print(f"Something went wrong", e)
            exit(1)
    else:
        try:
            lines = open_file("urls.txt")
            write_to_file(lines)
            print(f" All requests completed successfully")
        except Exception as e:
            print(f"Something went wrong", e)
            exit(1)




# File functions
def open_file(file_path):
    with open(file_path) as files:
        content = files.read()
        lines = content.splitlines()
        return lines
        # files.write(f"{'='*50} \n")

def write_to_file(lines_from_text):
    with open("url_response", "w") as response:
        time_of_request = f"{datetime.now()}"
        for line in lines_from_text:
            regex_match = re.match(r"https?://\S+", line)
            if not regex_match:
                continue
            head = requests.get(line)
            response.write(f"{line} - {time_of_request}\n")
            response.write(f"{'-' * 50}\n")
            response.write(f"Headers: {head.headers}\nStatus-Code: {head.status_code}\n")
            response.write(f"\n")