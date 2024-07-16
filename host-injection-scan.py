import requests


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m' 
    FAIL = '\033[91m'  
    ENDC = '\033[0m' 
    UNDERLINE = '\033[4m'


banner = (
    colors.HEADER  + "| |_| |/ _ \\/ __| __| | |_| |/ _ \\/ _` |/ _` |/ _ \\ '__|\n" +
    "|  _  | (_) \\__ \\ |_  |  _  |  __/ (_| | (_| |  __/ |\n" +
    "|_| |_|\\___/|___/\\__| |_| |_|\\___|\\__,_|\\__,_|\\___|_|   \n" +
    "\n" +
    " ___        _           _   _               ____\n" +
    "|_ _|_ __  (_) ___  ___| |_(_) ___  _ __   / ___|  ___ __ _ _ __\n" +
    " | || '_ \\ | |/ _ \\/ __| __| |/ _ \\| '_ \\  \\___ \\ / __/ _` | '_ \\\n" +
    " | || | | || |  __/ (__| |_| | (_) | | | |  ___) | (_| (_| | | | |\n" +
    "|___|_| |_|/ |\\___|\\___|\\__|_|\\___/|_| |_| |____/ \\___\\__,_|_| |_|\n" +
    "         |__/\n\n" +
    colors.UNDERLINE + colors.FAIL +
    "\nCreated by " + colors.UNDERLINE + "computer_boy5" + 
    " also known as huntinghackers\n" +
    "\nInstagram: " + colors.UNDERLINE + "computer_boy5\n" +
    colors.ENDC
)

print(banner + colors.ENDC)
Url = input("Enter the site: ") 
print(colors.OKGREEN + "\nThe entered url for testing was:", Url)

if Url:
    try:
        headers = {'X-Forwarded-Host': 'evil.com'}
        response = requests.get(Url, headers=headers)

        print("\n\nThe status code is:", response.status_code)
        print("\nResponse headers are:\n", response.headers)
        if 'Host header value' in response.text:
            print(colors.FAIL + "\nVulnerable to host header injection\n" + colors.ENDC)

        else:
            print(colors.OKGREEN + "\nNot vunlearble \n")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

else:
    print("No URL provided")

print(colors.OKBLUE + "\nThank you for using this tool just made for fun :)" )
