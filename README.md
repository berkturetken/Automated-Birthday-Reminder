# Automated-Birthday-Reminder

## How to use Automated Birthday Reminder ***(ABR)***?

1. Pull the current project to a desired folder
2. Create a file called ***birthdays.csv***. Recall that csv stands for **C**omma **S**eperated **V**alues. Therefore, do not forget to seperate the values with commas :)
    1. The structure of the csv file should be as follows:
    
        name  | month | day
        ----- | ----- | ----
        jake  |   1   |  15
        amy   |   11  |  8
    2. Place the file inside ***docs*** folder in the project
3. Before running the code in the cloud for automation, you can try in your local machine
    1. Open the project in your favorite IDE or code editor
    2. [Suggestion] Create a new Gmail or Hotmail account for security reasons that are explained later in the document
    3. Replace the constants' values with your own credentials (i.e., ***MY_EMAIL***, ***PWD***, ***RECEIVER_EMAIL***)
    4. If your email provider is different than Gmail, then find its SMPT information from the internet and change ***line#32*** in the code accordingly. Some of the common email providers are listed here:
    
        Gmail           | Hotmail        | Yahoo
        --------------- | -------------- | --------------------
        smtp.gmail.com  | smtp.live.com  | smtp.mail.yahoo.com
    5. [Suggestion] Edit the email message in ***line#38*** if you would like to change the content of the email. In other words, do as you please!
    6. Run the project: ***python3 main.py***
4. If you do not encounter an error, that's perfect :) Otherwise, check the bullet points below if you are trying to send an email from Gmail:
    1.  Double check the global variables, especially ***PWD***, whether there are any typos or not
    2.  Double check the other hard-coded areas
    3.  Make sure you enter the correct email provider
    4.  Make sure you enabled ***Less Secure Apps*** from Gmail settings. Go to Gmail → Click on top-right corner → Manage Your Google Account → Security → Scroll down → Turn on Less Secure App Access. Enabling ***Less Secure App Access*** makes your account more vulnerable. Therefore, I highly recommend you to create a new (dummy) account!
    5.  Go to the following website: https://accounts.google.com/DisplayUnlockCaptcha. Click ***Continue*** and then you should see ***Account access enabled*** message
    6.  Change the port number in ***line#32***. Normally, no need for a port number but that didn't work in my case...
    7.  If you come to this step, sorry but ran out of solution :(
 5. [Suggestion] If you do not encounter an error but also cannot see the email, check your spam folder
 6. Time to run this Python code in the cloud
    1. Create an account in https://www.pythonanywhere.com/
    2. Go to the ***Files*** section
    3. Uplaod the file ***main.py***
    4. Create a new directory called ***docs*** from the left pane
    5. Upload the files ***birthdays.csv*** and ***letter.txt***
    6. Go to the ***Consoles*** section and click on ***Bash***
    7. Type ***python3 main.py*** to the console to run our code once again
    8. If there is no error, the email should be visible on the receiver side (i.e., ***RECEIVER_EMAIL***)
    9. Go to the ***Tasks*** section and schedule your task
    10. Determine the time (notice that it is UTC) and type ***python3 main.py*** to the small command window
    11. Click on the ***Create*** button and you are good to go :)
7. If everything went well until this point and someone's birthday is on that day, the ***Automated Birthday Reminder*** reminds you via email :100:

----

If you have any questions or problems, reach me out: berkturetken@sabanciuniv.edu :+1:
