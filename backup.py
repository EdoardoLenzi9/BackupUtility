import platform
import category_manager as category

# can assume: "Windows", "Ubuntu", "Debian", "Arch" 
current_os = platform.system()

def printMessage(message):
    print("\n\n-----------------------------------------")
    print("\n\t {0} \n".format(message))
    print("-----------------------------------------\n\n")

def menu():
    printMessage("BackUp folder: App")
    category.scan_app()

def check_os():
    current_os = platform.system()
    if current_os == 'Linux':
        current_os = platform.dist()[0]
    printMessage("Current OS: {0}\n".format(current_os))

def main():
    printMessage("Welcome to BackUp-Utility by dodo")
    check_os()
    menu()

main()