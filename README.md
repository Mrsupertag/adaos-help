# adaos-help
An app that acts as a guide to new AdaOS users. It uses Flet to run the application and deliver a smooth application for the users.
It contains categories depending on what the user needs help with based on our AdaOS. 

# Repo Navigation

[main.py](main.py) - This is the main source code for the entire code for the apps UI , its small but its the most important as it connects all the other files together

[ui.py](ui.py) - Thats the code for the apps UI for all of the pages included in the application

[navigation.py](navigation.py) - The code that helps the app to switch to different pages , functions the back button etc.

[categories.py](categories.py) - All of the articles and the categories are in this file 

[code.py](code.py) - This is the entire apps code in one single file , made for users who want to test the app on their normal desktop envirenments.


# How to run it?

This app will be installed on our AdaOS by default after installing it in your desktop , but if anyone is willing to test this code for themselves
they have to go through a few steps first. 

For Windows (Recommended): 

1. Install Flet

     Open ur windows powershell and type this:

       $pip install flet

2. Create a new python file in your desktop and edit that file with our [code.py](code.py) code.
3. Now run tht code

     Open the terminal and type:

       $flet run (your file name)

4. Make sure the file that edited ur python file in ends with ".py" , as it is a python code.
