import requests
import re
from datetime import datetime

def generate_requests(url_list):
    if url_list:
        print(url_list)
    else:
        with open("urls.txt") as files:
            content = files.read()
            lines = content.splitlines()
            # files.write(f"{'='*50} \n")

        with open("url_response", "w") as response:
            time_of_request = f"{datetime.now()}"
            for line in lines:
                regex_match = re.match(r"https?://\S+", line)
                if not regex_match:
                    continue
                head = requests.get(line)
                response.write(f"{line} - {time_of_request}\n")
                response.write(f"{'-' * 50}\n")
                response.write(f"Headers: {head.headers}\nStatus-Code: {head.status_code}\n")
                response.write(f"\n")


