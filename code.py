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
                ft.Text("To open the terminal on most Linux distributions, you can use the keyboard shortcut Ctrl + Alt + T or search for 'Terminal' in your application menu. Once the terminal is open, you'll see a command prompt where you can start typing commands.", color="white")
            ]
            article_content.extend([
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
                ft.Text("• cat: Displays the contents of a file. Use cat file.txt to view the contents of file.txt.", color="white")
            ])
            article_content.extend([
                ft.Text("Advanced Techniques", size=24, weight="bold", color="white"),
                ft.Text("Once you're comfortable with the basics, you can explore more advanced techniques:", color="white"),
                ft.Text("• grep: Searches for text within files. For example, grep 'search_term' file.txt will search for search_term in file.txt.", color="white"),
                ft.Text("• awk: A powerful text-processing language. Use awk '{print $1}' file.txt to print the first column of file.txt.", color="white"),
                ft.Text("• sed: A stream editor for filtering and transforming text. For example, sed 's/old/new/g' file.txt will replace all instances of old with new in file.txt.", color="white"),
                ft.Text("• Bash Scripting: Automate tasks with shell scripts. Create a script with nano script.sh, add your commands, save the file, and make it executable with chmod +x script.sh.", color="white"),
                ft.Text("Tips and Tricks", size=24, weight="bold", color="white"),
                ft.Text("• Tab Completion: Use the Tab key to auto-complete commands and file names.", color="white"),
                ft.Text("• Command History: Use the Up and Down arrow keys to navigate through your command history.", color="white"),
                ft.Text("• Aliases: Create shortcuts for frequently used commands by adding aliases to your .bashrc or .zshrc file.", color="white")
            ])
            article_content.append(ft.Text("Conclusion", size=24, weight="bold", color="white"))
            article_content.append(ft.Text("The Linux Terminal is an indispensable tool for any Linux user. By mastering the commands and techniques outlined in this article, you'll be well on your way to becoming a more efficient and effective user. Keep practicing and exploring new commands to unlock the full potential of the terminal.", color="white"))
        
        elif category == "File Management":
            article_content = [
                ft.Text("File Management", size=30, weight="bold", color="white"),
                ft.Text("Introduction", size=24, weight="bold", color="white"),
                ft.Text("File management is the process of organizing and maintaining files on your computer. It involves various tasks such as copying, moving, and deleting files. Effective file management helps you keep your data organized and easily accessible.", color="white"),
                ft.Text("Getting Started with File Management", size=24, weight="bold", color="white"),
                ft.Text("To manage files efficiently, you need to understand the basic commands for file manipulation. The terminal provides several commands that allow you to perform these tasks quickly and efficiently.", color="white")
            ]
            article_content.extend([
                ft.Text("Basic File Operations", size=24, weight="bold", color="white"),
                ft.Text("• cp: Copies files or directories. For example, cp file.txt /home/user/Backup/ will copy file.txt to the Backup directory.", color="white"),
                ft.Text("• mv: Moves or renames files or directories. For example, mv oldname.txt newname.txt will rename oldname.txt to newname.txt.", color="white"),
                ft.Text("• rm: Removes files or directories. Use rm file.txt to delete a file and rm -r folder to delete a directory and its contents.", color="white")
            ])
            article_content.extend([
                ft.Text("Organizing Files", size=24, weight="bold", color="white"),
                ft.Text("• Creating Directories: Use the mkdir command to create new directories. For example, mkdir Projects will create a directory named Projects.", color="white"),
                ft.Text("• Navigating Directories: Use the cd command to change the current directory. For example, cd Projects will navigate to the Projects directory.", color="white"),
                ft.Text("• Listing Contents: Use the ls command to list the contents of a directory. For example, ls Projects will list the contents of the Projects directory.", color="white"),
                ft.Text("Advanced File Management", size=24, weight="bold", color="white"),
                ft.Text("• rsync: Synchronizes files and directories between two locations. For example, rsync -av source/ destination/ will synchronize the contents of the source directory with the destination directory.", color="white"),
                ft.Text("• find: Searches for files and directories based on various criteria. For example, find . -name '*.txt' will find all .txt files in the current directory and its subdirectories.", color="white"),
                ft.Text("• tar: Creates and extracts compressed archives. For example, tar -czvf archive.tar.gz folder/ will create a compressed archive of the folder directory.", color="white")
            ])
            article_content.extend([
                ft.Text("Tips and Tricks", size=24, weight="bold", color="white"),
                ft.Text("• Use Aliases: Create shortcuts for frequently used commands by adding aliases to your .bashrc or .zshrc file.", color="white"),
                ft.Text("• Organize by Type: Keep your files organized by creating directories for different file types, such as documents, images, and scripts.", color="white"),
                ft.Text("• Regular Backups: Regularly back up your important files to avoid data loss.", color="white"),
                ft.Text("Conclusion", size=24, weight="bold", color="white"),
                ft.Text("Effective file management is crucial for keeping your data organized and easily accessible. By mastering the commands and techniques outlined in this article, you'll be able to manage your files efficiently and avoid clutter. Keep practicing and exploring new commands to improve your file management skills.", color="white")
            ])
        
        page.views.append(ft.View(
            route=f"/{category.lower().replace(' ', '_')}",
            bgcolor="#2C2C2C",
            controls=            [
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
ft.app(target=main)
