import flet as ft

def main(page: ft.Page):
    page.title = "User Manual"
    page.bgcolor = "#2C2C2C"  # Dark Grey Background
    def navigate_to_category(e, category):
        article_content = []
        if category == "Linux Terminal":
            article_content = [
                ft.Text("Linux Terminal", size=30, weight="bold", color="white"),
                ft.Text("Introduction", size=24, weight="bold", color="white"),
                ft.Text("The Linux Terminal is a command-line interface that enables you to interact with your operating system using text-based commands. It is a powerful tool that can greatly enhance your productivity by allowing you to perform various tasks quickly and efficiently. Whether you're managing files, installing software, or configuring system settings, the terminal can help you accomplish these tasks with ease.", color="white"),
                ft.Text("Getting Started with the Terminal", size=24, weight="bold", color="white"),
                ft.Text("To open the terminal on most Linux distributions, you can use the keyboard shortcut Ctrl + Alt + T or search for 'Terminal' in your application menu. Once the terminal is open, you'll see a command prompt where you can start typing commands.", color="white"),
                ft.Text("Basic Commands", size=24, weight="bold", color="white"),
                ft.Text("Here are some essential commands to get you started:", color="white"),
                ft.Text("• ls: Lists the contents of a directory. For example, ls /home will list the contents of the /home directory.", color="white"),
                ft.Text("• cd: Changes the current directory. For example, cd /home/user/Documents will navigate to the /home/user/Documents directory.", color="white"),
                ft.Text("• pwd: Prints the current working directory.", color="white"),
                ft.Text("• mkdir: Creates a new directory. For example, mkdir new_folder will create a directory named new_folder.", color="white"),
                ft.Text("• rm: Removes files or directories. Use rm file.txt to delete a file and rm -r folder to delete a directory and its contents.", color="white"),
                ft.Text("File Manipulation", size=24, weight="bold", color="white"),
                ft.Text("Managing files is a crucial aspect of using the terminal. Here are some commands to help you manipulate files:", color="white"),
                ft.Text("• cp: Copies files or directories. For example, cp file.txt /home/user/Backup/ will copy file.txt to the Backup directory.", color="white"),
                ft.Text("• mv: Moves or renames files or directories. For example, mv oldname.txt newname.txt will rename oldname.txt to newname.txt.", color="white"),
                ft.Text("• touch: Creates an empty file. For example, touch newfile.txt will create an empty file named newfile.txt.", color="white"),
                ft.Text("• cat: Displays the contents of a file. Use cat file.txt to view the contents of file.txt.", color="white"),
                ft.Text("Advanced Techniques", size=24, weight="bold", color="white"),
                ft.Text("Once you're comfortable with the basics, you can explore more advanced techniques:", color="white"),
                ft.Text("• grep: Searches for text within files. For example, grep 'search_term' file.txt will search for search_term in file.txt.", color="white"),
                ft.Text("• awk: A powerful text-processing language. Use awk '{print $1}' file.txt to print the first column of file.txt.", color="white"),
                ft.Text("• sed: A stream editor for filtering and transforming text. For example, sed 's/old/new/g' file.txt will replace all instances of old with new in file.txt.", color="white"),
                ft.Text("• Bash Scripting: Automate tasks with shell scripts. Create a script with nano script.sh, add your commands, save the file, and make it executable with chmod +x script.sh.", color="white"),
                ft.Text("Tips and Tricks", size=24, weight="bold", color="white"),
                ft.Text("• Tab Completion: Use the Tab key to auto-complete commands and file names.", color="white"),
                ft.Text("• Command History: Use the Up and Down arrow keys to navigate through your command history.", color="white"),
                ft.Text("• Aliases: Create shortcuts for frequently used commands by adding aliases to your .bashrc or .zshrc file.", color="white"),
                ft.Text("Conclusion", size=24, weight="bold", color="white"),
                ft.Text("The Linux Terminal is an indispensable tool for any Linux user. By mastering the commands and techniques outlined in this article, you'll be well on your way to becoming a more efficient and effective user. Keep practicing and exploring new commands to unlock the full potential of the terminal.", color="white")
            ]
        elif category == "File Management":
            article_content = [
                ft.Text("File Management", size=30, weight="bold", color="white"),
                ft.Text("Introduction", size=24, weight="bold", color="white"),
                ft.Text("File management is the process of organizing and maintaining files on your computer. It involves various tasks such as copying, moving, and deleting files. Effective file management helps you keep your data organized and easily accessible.", color="white"),
                ft.Text("Getting Started with File Management", size=24, weight="bold", color="white"),
                ft.Text("To manage files efficiently, you need to understand the basic commands for file manipulation. The terminal provides several commands that allow you to perform these tasks quickly and efficiently.", color="white"),
                ft.Text("Basic File Operations", size=24, weight="bold", color="white"),
                ft.Text("• cp: Copies files or directories. For example, cp file.txt /home/user/Backup/ will copy file.txt to the Backup directory.", color="white"),
                ft.Text("• mv: Moves or renames files or directories. For example, mv oldname.txt newname.txt will rename oldname.txt to newname.txt.", color="white"),
                ft.Text("• rm: Removes files or directories. Use rm file.txt to delete a file and rm -r folder to delete a directory and its contents.", color="white"),
                ft.Text("Organizing Files", size=24, weight="bold", color="white"),
                ft.Text("• Creating Directories: Use the mkdir command to create new directories. For example, mkdir Projects will create a directory named Projects.", color="white"),
                ft.Text("• Navigating Directories: Use the cd command to change the current directory. For example, cd Projects will navigate to the Projects directory.", color="white"),
                ft.Text("• Listing Contents: Use the ls command to list the contents of a directory. For example, ls Projects will list the contents of the Projects directory.", color="white"),
                ft.Text("Advanced File Management", size=24, weight="bold", color="white"),
                ft.Text("• rsync: Synchronizes files and directories between two locations. For example, rsync -av source/ destination/ will synchronize the contents of the source directory with the destination directory.", color="white"),
                ft.Text("• find: Searches for files and directories based on various criteria. For example, find . -name '*.txt' will find all .txt files in the current directory and its subdirectories.", color="white"),
                ft.Text("• tar: Creates and extracts compressed archives. For example, tar -czvf archive.tar.gz folder/ will create a compressed archive of the folder directory.", color="white"),
                ft.Text("Tips and Tricks", size=24, weight="bold", color="white"),
                ft.Text("• Use Aliases: Create shortcuts for frequently used commands by adding aliases to your .bashrc or .zshrc file.", color="white"),
                ft.Text("• Organize by Type: Keep your files organized by creating directories for different file types, such as documents, images, and scripts.", color="white"),
                ft.Text("• Regular Backups: Regularly back up your important files to avoid data loss.", color="white"),
                ft.Text("Conclusion", size=24, weight="bold", color="white"),
                ft.Text("Effective file management is crucial for keeping your data organized and easily accessible. By mastering the commands and techniques outlined in this article, you'll be able to manage your files efficiently and avoid clutter. Keep practicing and exploring new commands to improve your file management skills.", color="white")
            ]
        elif category == "Software Installation":
            article_content = [
                ft.Text("Software Installation", size=30, weight="bold", color="white"),
                ft.Text("Introduction", size=24, weight="bold", color="white"),
                ft.Text("Software installation involves adding new applications and programs to your computer. This can be done using package managers or by downloading and installing software manually.", color="white"),
                ft.Text("Getting Started with Software Installation", size=24, weight="bold", color="white"),
                ft.Text("To install software, you need to understand the different methods available, including using package managers and manual installation.", color="white"),
                ft.Text("Using Package Managers", size=24, weight="bold", color="white"),
                ft.Text("Package managers are tools that automate the process of installing, updating, and removing software. Here are some popular package managers:", color="white"),
                ft.Text("• apt: A package manager for Debian-based systems like Ubuntu. Use sudo apt update to update the package list and sudo apt install package-name to install a package.", color="white"),
                ft.Text("• yum: A package manager for Red Hat-based systems like CentOS. Use sudo yum update to update the package list and sudo yum install package-name to install a package.", color="white"),
                ft.Text("• pacman: A package manager for Arch Linux. Use sudo pacman -Syu to update the package list and sudo pacman -S package-name to install a package.", color="white"),
                ft.Text("Manual Installation", size=24, weight="bold", color="white"),
                ft.Text("Some software is not available through package managers and needs to be installed manually. Here's how to do it:", color="white"),
                ft.Text("1. Download the Software: Visit the software's official website and download the appropriate version for your system.", color="white"),
                ft.Text("2. Extract the Files: Use the tar command to extract the downloaded archive. For example, tar -xvzf software.tar.gz will extract the contents of software.tar.gz.", color="white"),
                ft.Text("3. Install the Software: Follow the instructions provided by the software's documentation. This usually involves running ./configure, make, and sudo make install.", color="white"),
                ft.Text("Managing Installed Software", size=24, weight="bold", color="white"),
                ft.Text("Updating Software: Regularly update your software to ensure you have the latest features and security patches. Use your package manager's update command, such as sudo apt update && sudo apt upgrade.", color="white"),
                ft.Text("Removing Software: Use your package manager to remove software you no longer need. For example, sudo apt remove package-name will remove a package.", color="white"),
                ft.Text("Tips and Tricks", size=24, weight="bold", color="white"),
                ft.Text("Check Dependencies: Before installing new software, check for any dependencies required by the software to ensure a smooth installation.", color="white"),
                ft.Text("Use Repositories: Add official repositories to your package manager to access a wider range of software.", color="white"),
                ft.Text("Conclusion", size=24, weight="bold", color="white"),
                ft.Text("Software installation is a fundamental skill for managing your system and adding new functionality. By mastering the methods and techniques outlined in this article, you'll be able to install, update, and manage software effectively. Keep exploring new software to enhance your system's capabilities.", color="white")
            ]
        elif category == "System Settings":
            article_content = [
                ft.Text("System Settings", size=30, weight="bold", color="white"),
                ft.Text("Introduction", size=24, weight="bold", color="white"),
                ft.Text("System settings allow you to configure and customize your computer's behavior and appearance. This includes settings for display, sound, network, and more.", color="white"),
                ft.Text("Getting Started with System Settings", size=24, weight="bold", color="white"),
                ft.Text("Understanding how to navigate and modify system settings can help you tailor your computer to your preferences and improve its performance.", color="white"),
                ft.Text("Display Settings", size=24, weight="bold", color="white"),
                ft.Text("Adjusting Resolution: Use the xrandr command to adjust your screen resolution. For example, xrandr --output HDMI-1 --mode 1920x1080 will set the resolution to 1920x1080.", color="white"),
                ft.Text("Setting Brightness: Use the xbacklight command to adjust screen brightness. For example, xbacklight -set 50 will set the brightness to 50%.", color="white"),
                ft.Text("Sound Settings", size=24, weight="bold", color="white"),
                ft.Text("Adjusting Volume: Use the amixer command to adjust the system volume. For example, amixer set Master 50% will set the volume to 50%.", color="white"),
                ft.Text("Selecting Audio Output: Use the pavucontrol command to open the PulseAudio Volume Control application and select your audio output device.", color="white"),
                ft.Text("Network Settings", size=24, weight="bold", color="white"),
                ft.Text("Connecting to Wi-Fi: Use the nmcli command to connect to a Wi-Fi network. For example, nmcli device wifi connect 'SSID' password 'PASSWORD' will connect to the specified network.", color="white"),
                ft.Text("Configuring Ethernet: Use the ifconfig command to configure Ethernet settings. For example, ifconfig eth0 192.168.1.100 will set the IP address of eth0 to 192.168.1.100.", color="white"),
                ft.Text("Power Management", size=24, weight="bold", color="white"),
                ft.Text("Setting Power Saving Options: Use the tlp command to configure power-saving options. For example, sudo tlp start will start the TLP power management tool.", color="white"),
                ft.Text("Suspending and Hibernating: Use the systemctl command to suspend or hibernate your system. For example, systemctl suspend will suspend the system.", color="white"),
                ft.Text("Tips and Tricks", size=24, weight="bold", color="white"),
                ft.Text("Customization Tools: Use tools like gsettings and dconf-editor to customize desktop settings and preferences.", color="white"),
                ft.Text("Backup Configurations: Regularly back up your configuration files to avoid losing your custom settings.", color="white"),
                ft.Text("Conclusion", size=24, weight="bold", color="white"),
                ft.Text("System settings allow you to customize your computer to meet your needs and preferences. By mastering the commands and tools outlined in this article, you'll be able to configure and optimize your system settings effectively. Keep experimenting with different settings to create a personalized computing experience.", color="white")
            ]
        elif category == "Networking":
            article_content = [
                ft.Text("Networking", size=30, weight="bold", color="white"),
                ft.Text("Introduction", size=24, weight="bold", color="white"),
                ft.Text("Networking involves connecting your computer to other devices and networks. This includes setting up internet connections, configuring network interfaces, and troubleshooting network issues.", color="white"),
                ft.Text("Getting Started with Networking", size=24, weight="bold", color="white"),
                ft.Text("Understanding basic networking concepts and commands can help you manage network connections and troubleshoot issues.", color="white"),
                ft.Text("Setting Up Internet Connections", size=24, weight="bold", color="white"),
                ft.Text("Connecting to Wi-Fi: Use the nmcli command to connect to a Wi-Fi network. For example, nmcli device wifi connect 'SSID' password 'PASSWORD' will connect to the specified network.", color="white"),
                ft.Text("Configuring Ethernet: Use the ifconfig command to configure Ethernet settings. For example, ifconfig eth0 192.168.1.100 will set the IP address of eth0 to 192.168.1.100.", color="white"),
                ft.Text("Network Configuration", size=24, weight="bold", color="white"),
                ft.Text("Viewing Network Interfaces: Use the ip a command to view all network interfaces and their statuses.", color="white"),
                ft.Text("Assigning IP Addresses: Use the ip addr add command to assign an IP address to a network interface. For example, ip addr add 192.168.1.100/24 dev eth0 will assign the IP address 192.168.1.100 to eth0.", color="white"),
                ft.Text("Troubleshooting Network Issues", size=24, weight="bold", color="white"),
                ft.Text("Ping Command: Use the ping command to test connectivity to another device. For example, ping google.com will test connectivity to Google.", color="white"),
                ft.Text("Traceroute Command: Use the traceroute command to trace the path to a remote host. For example, traceroute google.com will show the path taken to reach Google.", color="white"),
                ft.Text("Tips and Tricks", size=24, weight="bold", color="white"),
                ft.Text("• Use the netstat command to display network connections, routing tables, and interface statistics.", color="white"),
                ft.Text("• Use the nslookup command to query DNS servers and obtain domain name information.", color="white"),
                ft.Text("• Regularly update your network drivers to ensure compatibility and performance.", color="white"),
                ft.Text("Conclusion", size=24, weight="bold", color="white"),
                ft.Text("Networking is a fundamental skill for connecting and managing your computer within various networks. By mastering the commands and techniques outlined in this article, you'll be able to set up, configure, and troubleshoot network connections effectively. Keep exploring new networking tools and concepts to enhance your network management skills.", color="white")
            ]
        elif category == "Security & Permissions":
            article_content = [
                ft.Text("Security & Permissions", size=30, weight="bold", color="white"),
                ft.Text("Introduction", size=24, weight="bold", color="white"),
                ft.Text("Security and permissions involve protecting your computer and data from unauthorized access. This includes setting file permissions, configuring firewalls, and using encryption.", color="white"),
                ft.Text("Getting Started with Security & Permissions", size=24, weight="bold", color="white"),
                ft.Text("Understanding the basics of security and permissions can help you safeguard your computer and data.", color="white"),
                ft.Text("File Permissions", size=24, weight="bold", color="white"),
                ft.Text("Changing File Permissions: Use the chmod command to change file permissions. For example, chmod 755 file.txt will set the file permissions to allow the owner to read, write, and execute, and others to read and execute.", color="white"),
                ft.Text("Viewing File Permissions: Use the ls -l command to view the permissions of files in a directory.", color="white"),
                ft.Text("Firewalls", size=24, weight="bold", color="white"),
                ft.Text("Configuring Firewalls: Use the ufw command to configure the Uncomplicated Firewall. For example, sudo ufw allow 22 will allow SSH connections through the firewall.", color="white"),
                ft.Text("Checking Firewall Status: Use the sudo ufw status command to check the status of the firewall.", color="white"),
                ft.Text("Encryption", size=24, weight="bold", color="white"),
                ft.Text("Encrypting Files: Use the gpg command to encrypt files. For example, gpg -c file.txt will encrypt file.txt using a password.", color="white"),
                ft.Text("Decrypting Files: Use the gpg command to decrypt files. For example, gpg file.txt.gpg will decrypt the encrypted file.txt.gpg.", color="white"),
                ft.Text("Tips and Tricks", size=24, weight="bold", color="white"),
                ft.Text("• Use strong passwords and change them regularly.", color="white"),
                ft.Text("• Keep your system and software up to date with security patches.", color="white"),
                ft.Text("• Regularly back up your important data to protect against data loss.", color="white"),
                ft.Text("Conclusion", size=24, weight="bold", color="white"),
                ft.Text("Security and permissions are crucial for protecting your computer and data. By mastering the commands and techniques outlined in this article, you'll be able to configure file permissions, firewalls, and encryption effectively. Keep practicing and exploring new security tools to enhance your system's security.", color="white")
            ]
        elif category == "User Management":
            article_content = [
                ft.Text("User Management", size=30, weight="bold", color="white"),
                ft.Text("Introduction", size=24, weight="bold", color="white"),
                ft.Text("User management involves creating and managing user accounts on your computer. This includes adding new users, setting passwords, and configuring user permissions.", color="white"),
                ft.Text("Getting Started with User Management", size=24, weight="bold", color="white"),
                ft.Text("Understanding the basics of user management can help you effectively manage user accounts and permissions.", color="white"),
                ft.Text("Creating and Managing Users", size=24, weight="bold", color="white"),
                ft.Text("Adding a New User: Use the sudo adduser command to add a new user. For example, sudo adduser newuser will add a user named newuser.", color="white"),
                ft.Text("Deleting a User: Use the sudo deluser command to delete a user. For example, sudo deluser olduser will delete the user olduser.", color="white"),
                ft.Text("Setting User Permissions", size=24, weight="bold", color="white"),
                ft.Text("Changing User Groups: Use the sudo usermod -aG groupname username command to add a user to a group. For example, sudo usermod -aG sudo newuser will add newuser to the sudo group.", color="white"),
                ft.Text("Viewing User Groups: Use the groups command to view the groups a user belongs to. For example, groups newuser will display the groups for newuser.", color="white"),
                ft.Text("Changing User Passwords", size=24, weight="bold", color="white"),
                ft.Text("Setting a User Password: Use the sudo passwd username command to set or change a user's password. For example, sudo passwd newuser will set the password for newuser.", color="white"),
                ft.Text("Tips and Tricks", size=24, weight="bold", color="white"),
                ft.Text("• Regularly review and update user permissions to ensure security.", color="white"),
                ft.Text("• Use strong passwords for all user accounts.", color="white"),
                ft.Text("• Keep a record of user accounts and their permissions for reference.", color="white"),
                ft.Text("Conclusion", size=24, weight="bold", color="white"),
                ft.Text("User management is essential for maintaining control over who can access your computer and what they can do. By mastering the commands and techniques outlined in this article, you'll be able to create, manage, and secure user accounts effectively. Keep practicing and exploring new user management tools to enhance your skills.", color="white")
            ]
        elif category == "Disk Management":
            article_content = [
                ft.Text("Disk Management", size=30, weight="bold", color="white"),
                ft.Text("Introduction", size=24, weight="bold", color="white"),
                ft.Text("Disk management involves organizing and maintaining your computer's storage devices. This includes tasks such as partitioning disks, formatting drives, and managing file systems.", color="white"),
                ft.Text("Getting Started with Disk Management", size=24, weight="bold", color="white"),
                ft.Text("Understanding the basics of disk management can help you optimize your storage and ensure data integrity.", color="white"),
                ft.Text("Partitioning Disks", size=24, weight="bold", color="white"),
                ft.Text("Creating Partitions: Use the fdisk command to create and manage disk partitions. For example, sudo fdisk /dev/sda will open the disk partitioning tool for the /dev/sda disk.", color="white"),
                ft.Text("Viewing Partitions: Use the lsblk command to view all partitions and their sizes.", color="white"),
                ft.Text("Formatting Drives", size=24, weight="bold", color="white"),
                ft.Text("Formatting a Partition: Use the mkfs command to format a partition. For example, sudo mkfs.ext4 /dev/sda1 will format the /dev/sda1 partition with the ext4 file system.", color="white"),
                ft.Text("Checking Disk Space", size=24, weight="bold", color="white"),
                ft.Text("Checking Free Space: Use the df command to check the available disk space. For example, df -h will display disk space usage in a human-readable format.", color="white"),
                ft.Text("Checking Disk Usage: Use the du command to check the disk usage of files and directories. For example, du -sh /home/user/Documents will display the disk usage of the Documents directory.", color="white"),
                ft.Text("Managing File Systems", size=24, weight="bold", color="white"),
                ft.Text("Mounting File Systems: Use the mount command to mount file systems. For example, sudo mount /dev/sda1 /mnt will mount the /dev/sda1 partition to the /mnt directory.", color="white"),
                ft.Text("Unmounting File Systems: Use the umount command to unmount file systems. For example, sudo umount /mnt will unmount the /mnt directory.", color="white"),
                ft.Text("Tips and Tricks", size=24, weight="bold", color="white"),
                ft.Text("• Regularly back up your data to prevent data loss.", color="white"),
                ft.Text("• Use disk monitoring tools to keep track of disk health and performance.", color="white"),
                ft.Text("• Keep your file systems organized to make data management easier.", color="white"),
                ft.Text("Conclusion", size=24, weight="bold", color="white"),
                ft.Text("Effective disk management is crucial for maintaining your computer's storage devices and ensuring data integrity. By mastering the commands and techniques outlined in this article, you'll be able to manage your disks efficiently and prevent data loss. Keep practicing and exploring new disk management tools to enhance your skills.", color="white")
            ]
        elif category == "Troubleshooting":
            article_content = [
                ft.Text("Troubleshooting", size=30, weight="bold", color="white"),
                ft.Text("Introduction", size=24, weight="bold", color="white"),
                ft.Text("Troubleshooting involves diagnosing and fixing issues with your computer. This includes checking system logs, running diagnostic tools, and resolving common problems.", color="white"),
                ft.Text("Getting Started with Troubleshooting", size=24, weight="bold", color="white"),
                ft.Text("Understanding the basics of troubleshooting can help you quickly identify and fix issues with your computer.", color="white"),
                ft.Text("Checking System Logs", size=24, weight="bold", color="white"),
                ft.Text("Viewing System Logs: Use the journalctl command to view system logs. For example, sudo journalctl -xe will display detailed logs of recent system events.", color="white"),
                ft.Text("Viewing Log Files: Use the cat command to view log files. For example, sudo cat /var/log/syslog will display the contents of the syslog file.", color="white"),
                ft.Text("Running Diagnostic Tools", size=24, weight="bold", color="white"),
                ft.Text("Running System Diagnostics: Use the dmesg command to display system diagnostic messages. For example, sudo dmesg | less will display diagnostic messages in a readable format.", color="white"),
                ft.Text("Checking Disk Health: Use the smartctl command to check the health of your disks. For example, sudo smartctl -a /dev/sda will display detailed health information for the /dev/sda disk.", color="white"),
                ft.Text("Resolving Common Problems", size=24, weight="bold", color="white"),
                ft.Text("Fixing Network Issues: Use the ping command to check network connectivity. For example, ping google.com will test connectivity to Google.", color="white"),
                ft.Text("Fixing Disk Space Issues: Use the df command to check disk space usage. For example, df -h will display disk space usage in a human-readable format.", color="white"),
                ft.Text("Tips and Tricks", size=24, weight="bold", color="white"),
                ft.Text("• Keep your system and software up to date with the latest updates and patches.", color="white"),
                ft.Text("• Regularly back up your data to prevent data loss.", color="white"),
                ft.Text("• Use system monitoring tools to keep track of system performance and health.", color="white"),
                ft.Text("Conclusion", size=24, weight="bold", color="white"),
                ft.Text("Troubleshooting is a crucial skill for maintaining the health and performance of your computer. By mastering the commands and techniques outlined in this article, you'll be able to diagnose and fix issues effectively. Keep practicing and exploring new troubleshooting tools to enhance your skills.", color="white")
            ]
        
        page.views.append(ft.View(
            route=f"/{category.lower().replace(' ', '_')}",
            bgcolor="#2C2C2C",
            controls=[
                ft.Row(
                    [ft.Container(
                        content=ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    on_click=lambda e: go_back(page),
                                    icon_color="white"
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            expand=True
                        ),
                        bgcolor="#1F1F1F",
                        padding=10,
                        border_radius=20,
                        width=page.window_width * 0.85,
                        height=60
                    )],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Container(
                    content=ft.Column(
                        controls=article_content,
                        scroll=ft.ScrollMode.AUTO
                    ),
                    padding=40,
                    alignment=ft.alignment.center,
                    expand=True  # Enable scrolling
                )
            ]
        ))
        page.update()
    def go_back(page):
        if len(page.views) > 1:
            page.views.pop()
        else:
            page.views.clear()
            page.go("/")
        page.update()
    # Top Bar for Home Page
    top_bar = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.SETTINGS,
                    icon_color="white"
                ),
                ft.Text("User Manual", size=22, weight="bold", color="white"),
                ft.IconButton(
                    icon=ft.icons.SEARCH,
                    on_click=lambda e: page.go("/search"),
                    icon_color="white"
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        bgcolor="#1F1F1F",
        padding=10,
        border_radius=20,
        width=page.window_width * 0.85,
        height=60
    )
    # Main Heading
    heading = ft.Container(
        content=ft.Text("How to use AdaOS", size=36, weight="bold", color="white"),
        padding=40,
        alignment=ft.alignment.center
    )
    # Category Buttons
    categories = [
        "Linux Terminal",
        "File Management",
        "Software Installation",
        "System Settings",
        "Networking",
        "Security & Permissions",
        "User Management",
        "Disk Management",
        "Troubleshooting"
    ]
    category_buttons = ft.Column(
        controls=[
            ft.Row([
                ft.Container(
                    ft.ElevatedButton(
                        text=categories[i],
                        bgcolor="white",
                        color="black",
                        width=250,
                        height=60,
                        on_click=lambda e, c=categories[i]: navigate_to_category(e, c)
                    ),
                    padding=10
                ) for i in range(j, min(j + 3, len(categories)))
            ], alignment=ft.MainAxisAlignment.CENTER) for j in range(0, len(categories), 3)
        ]
    )
    # Page Layout
    page.add(
        ft.Row([top_bar], alignment=ft.MainAxisAlignment.CENTER),
        heading,
        category_buttons
    )
    def go_back(page):
        if len(page.views) > 1:
            page.views.pop()
        else:
            page.views.clear()
            page.go("/")
        page.update()
        
ft.app(target=main)
