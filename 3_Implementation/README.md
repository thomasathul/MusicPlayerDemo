# Getting Started with Music Stream App

## Folder Structure

| Folder   | Description                                   |
| -------- | --------------------------------------------- |
| database      | Contains the database folder for storing data (server)       |
| music      | Contains all the audio files for playing                |


## Installing the dependencies

To run the program, you would require to download any of the [Python 3.6+ releases](https://www.python.org/downloads)

You would require to download additional dependecies:-

1. For Windows:
   - Open the terminal and navigate to the 3_Implementation project directory. 
   - Run `pip install -r windows_requirements.txt` command to install all the additional dependencies.
   
2. For Linux:
   - Open the terminal and run the following commands:-
   
      ```console
         sudo pip install openpyxl
         sudo pip install pygame
         sudo pip install pygame 
         sudo pip install pylint
     ```

## Running the program

1. Once you have downloaded the dependencies required, clone this github repository.

2. Next, Open up the terminal console and navigate to the 3_Implementation project directory.

3. You can run the program by running the command `python3 main.py`.

4. ***Enjoy streaming!*** :tada:

## Need More Help?

1. After you run the program, you will be directed to User Authentication page.

   - If you are new to the program and wish to Signup, enter your credentials to create an account.
   
   - If you are an existing user, go to the login page and enter the credentials.
   
   - If you wish to login as a Guest, Login with ( username - test123@gmail.com ) and ( password - hello@123 ).

2. After successful login, you will be directed to the Music player menu where you can search or browse the songs.

3. Enter the song name you want to play and enjoy listening!

## Advanced Guide

### Pytest:
- Run `python test_streaming.py` in the Implementation folder to test the project.
     
### Pylint:
- Go to the root project directory (i.e Genesis_OOPS_Using_Python)
- Run `pylint 3_Implementation` to run code quality score check.

