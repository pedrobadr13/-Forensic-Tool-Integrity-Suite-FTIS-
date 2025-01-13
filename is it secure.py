import ctypes
import subprocess

# Function to run a command with admin privileges in PowerShell
def run_as_admin(command):
    try:
        # Using ctypes to trigger UAC and run the command in PowerShell as an administrator
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "powershell.exe", f"-NoExit -Command {command}", None, 1)
    except Exception as e:
        print(f"Error executing command: {e}")

# Define a simple menu to choose commands
def menu():
    while True:  # Infinite loop to keep the menu running
        try:
            print("_______________________________________________________________________________________")
            print("===== Forensic Tool Integrity: Assessing Vulnerabilities and Potential Compromise ====")
            print("_______________________________________________________________________________________")
            print("1. View the Task List (tasklist)")
            print("2. Check Hard Disk for Errors (chkdsk C: /f /r)")
            print("3. Display System Logs (wevtutil qe System /f:text)")
            print("4. Check Network Activities (Get-NetTCPConnection)")
            print("5. View Recent System Log Events (wevtutil qe System /f:text /c:10)")
            print("6. View User Accounts on the System (net user)")
            print("7. Review Password Policy (net accounts)")
            print("8. Check for Modifications in DNS or Network Settings (ipconfig /displaydns)")
            print('9. Check User’s Autostart Folders()')
            print("10. List Installed Programs (Get-WmiObject -Class Win32_Product)")
            print("11. Check Active Firewall Rules (netsh advfirewall firewall show rule name=all)")  # Option 11 fixed here
            print("12. Review Scheduled Tasks (Get-ScheduledTask)")
            print("13. View Open Ports (netstat -an)--")
            print("14. Review ARP Cache (arp -a)---")
            print("0. Exit Program")  # Added option to exit
            print("___________________________________________________________________________________________")
            print("To ensure proper documentation, it is recommended to open a text editor, such as Notepad or any preferred note-taking application, before executing the commands. This will allow you to record any suspicious findings or observations during the process.")

            choice = input("\nEnter the number of the command you want to execute: ")

            # Execute the corresponding command in PowerShell
            if choice == '1':
                print("\nExecuting Task List (Get-Process)...\n")
                run_as_admin("Get-Process")
            elif choice == '2':
                print("\nChecking Hard Disk for Errors (chkdsk C: /f /r)...\n")
                run_as_admin("C:\\Windows\\System32\\chkdsk.exe C: /f /r")
            elif choice == '3':
                print("\nDisplaying System Logs (wevtutil qe System /f:text)...\n")
                run_as_admin("wevtutil qe Get-WinEvent -LogName System | Where-Object {$_.TimeCreated -gt (Get-Date).AddHours(-24)} | Format-List TimeCreated, Message")
            elif choice == '4':
                print("\nChecking Network Activities (Get-NetTCPConnection)...\n")
                run_as_admin("Get-NetTCPConnection")
            elif choice == '5':
                print("\nViewing Recent System Log Events (wevtutil qe System /f:text /c:10)...\n")
                run_as_admin("C:\\Windows\\System32\\wevtutil qe System /f:text /c:10")
            elif choice == '6':
                print("\nViewing User Accounts on the System (net user)...\n")
                run_as_admin("C:\\Windows\\System32\\net.exe user")
            elif choice == '7':
                print("\nReviewing Password Policy (net accounts)...\n")
                run_as_admin("C:\\Windows\\System32\\net.exe accounts")
            elif choice == '8':
                print("\nChecking for Modifications in DNS or Network Settings (ipconfig /displaydns)...\n")
                run_as_admin("Get-DnsClientServerAddress")
            elif choice == '9':
                print("\nCheck User’s Autostart Folders(run;dir)...\n")
                run_as_admin('Get-ChildItem -Path "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp"')
            elif choice == "10":
                print("\nList Installed Programs (Get-WmiObject -Class Win32_Product)...\n")
                run_as_admin("Get-ItemProperty -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\*' | Select-Object DisplayName, DisplayVersion, Publisher")
            elif choice == "11":
                print("\nCheck Active Firewall Rules (netsh advfirewall firewall show rule name=all)...\n")
                # Adjusted PowerShell command formatting to avoid escape issues
                run_as_admin('powershell.exe -Command "netsh advfirewall firewall show rule name=all"')
            elif choice == "12":
                print("\nReviewing Scheduled Tasks (Get-ScheduledTask)...\n")
                run_as_admin("Get-ScheduledTask")
            elif choice =="13":
                print("\nView Open Ports (netstat -an)--\n ")
                run_as_admin("Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State")
            elif choice == "14" :
                print("\nReview ARP Cache (arp -a)\n")   
                run_as_admin("Get-NetNeighbor")
            elif choice == '0':
                print("\nExiting the program...")
                break  # Exit the loop and terminate the program
            else:
                print("\nInvalid choice. Please select a number between 0 and 14.")
                continue  # Continue the loop without recursion

        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting gracefully...")
            break  # Exit the program gracefully on Ctrl + C
        except EOFError:
            print("\nEOFError encountered. Exiting gracefully...")
            break  # Exit the program gracefully on Ctrl + D or end-of-file input

# Run the menu
menu()

# share the script 