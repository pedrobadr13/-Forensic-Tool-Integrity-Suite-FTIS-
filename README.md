# Forensic Tool Integrity Suite (FTIS) 🚀

## Overview 🔍
The **Forensic Tool Integrity Suite (FTIS)** is a comprehensive forensic analysis and diagnostic tool tailored for Windows systems. It enables users to evaluate system integrity, identify vulnerabilities, and detect potential compromises effectively. Designed for IT professionals, cybersecurity analysts, and system administrators, FTIS simplifies complex forensic tasks with an easy-to-use command-line interface.

---

## Features ✨
1. 📝 **Monitor Running Processes**: View and assess the system's task list (`tasklist`).
2. 💽 **Check Disk Health**: Detect and repair hard disk errors (`chkdsk C: /f /r`).
3. 📜 **Review System Logs**: Display detailed logs for anomaly detection (`wevtutil qe System /f:text`).
4. 🌐 **Analyze Network Activity**: Track active connections and open ports (`Get-NetTCPConnection` and `netstat -an`).
5. 👥 **Audit User Accounts**: Inspect accounts and password policies (`net user`, `net accounts`).
6. 🔧 **Inspect DNS/Network Settings**: Detect unauthorized changes (`ipconfig /displaydns`).
7. 🔥 **Evaluate Firewall Rules**: Review active configurations (`netsh advfirewall firewall show rule name=all`).
8. 🕒 **Check Scheduled Tasks**: Identify potentially harmful automation (`Get-ScheduledTask`).
9. 🗂️ **List Installed Programs**: View installed programs (`Get-WmiObject -Class Win32_Product`).
10. 📜 **Review ARP Cache**: Inspect ARP cache for anomalies (`arp -a`).

---

## Installation 🛠️
1. Clone the repository:
    ```bash
    git clone https://github.com/pedrobadr13/forensic-tool-integrity-suite.git
    ```
2. Navigate to the project directory:
    ```bash
    cd forensic-tool-integrity-suite
    ```
3. Run the script:
    ```bash
    python ftis.py
    ```

---

## Usage 💻
1. Run the script using Python.
2. Follow the on-screen menu to choose a diagnostic or forensic task.
3. Results will be displayed in the terminal.
4. Exit the program by selecting option `0`.

---

## Menu Options 📋
```text
1. View the Task List (tasklist)
2. Check Hard Disk for Errors (chkdsk C: /f /r)
3. Display System Logs (wevtutil qe System /f:text)
4. Check Network Activities (Get-NetTCPConnection)
5. View Recent System Log Events (wevtutil qe System /f:text /c:10)
6. View User Accounts on the System (net user)
7. Review Password Policy (net accounts)
8. Check for Modifications in DNS or Network Settings (ipconfig /displaydns)
9. Check User’s Autostart Folders
10. List Installed Programs (Get-WmiObject -Class Win32_Product)
11. Check Active Firewall Rules (netsh advfirewall firewall show rule name=all)
12. Review Scheduled Tasks (Get-ScheduledTask)
13. View Open Ports (netstat -an)
14. Review ARP Cache (arp -a)
0. Exit Program
```

---

## Requirements 📦
- Python 3.x
- Windows PowerShell or Command Prompt

---

## Contributing 🤝
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License 📄
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact 📧
For questions or suggestions, feel free to reach out:
- **GitHub**: [pedrobadr13](https://github.com/pedrobadr13)
- **Email**: badraitbella403@gmail.com

---

Enjoy using **Forensic Tool Integrity Suite (FTIS)**! 🎉
