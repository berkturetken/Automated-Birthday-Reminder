# Automated Birthday Reminder (ABR)

## How to use ABR? Instructions for Dummies

1. Clone the repo to a desired folder.
2. Create a file called ***birthdays.csv***. On a side not, recall that CSV stands for **C**omma **S**eperated **V**alues. Therefore, do not forget to seperate values with commas :)
    1. The structure of a CSV file should be as follows:
    
        name  | month | day
        ----- | ----- | ----
        jake  |   1   |  15
        amy   |   11  |  8
    2. Place the file inside the ***docs*** folder in the project. Note that there is no ***birthdays.csv*** file available in the repository not to leak any (maybe even sensitive?) information.
3. If you would like to test the script in your local machine, follow the steps below:
    1. Open the project in your favorite IDE or code editor.
    2. [Suggestion] Create a new Gmail or Hotmail account for security reasons that are explained later in the document.
    3. Create your own ***.env*** file and put the values for the ***berkturetken1_gmail*** and ***berkturetken1_pwd*** fields which corresponds to the ***MY_EMAIL*** and ***PWD*** global variables in the code, respectively.
    4. If your email provider is different than Gmail, then find its SMTP information from the internet and change ***line#41*** in the code accordingly. Some of the common email providers are listed here:
    
        Gmail           | Hotmail        | Yahoo                | Airmail
        --------------- | -------------- | -------------------- | --------------------
        smtp.gmail.com  | smtp.live.com  | smtp.mail.yahoo.com  | mail.airmail.net
    5. [Suggestion] Edit the email message in the `docs/letter.txt` file if you would like to change the content of the email. In other words, do as you please!
    6. Run the project: ***python3 main.py***
4. If you do not encounter an error, that's perfect :) Otherwise, check the bullet points below if you are trying to send an email from Gmail:
    1.  Double check the global variables, especially ***PWD***, whether there are any typos or not.
    2.  Double check the other hard-coded areas.
    3.  Make sure you enter the correct email provider.
    4.  Make sure you enabled ***Less Secure Apps*** from Gmail settings. Go to Gmail → Click on top-right corner → Manage Your Google Account → Security → Scroll down → Turn on Less Secure App Access. Enabling ***Less Secure App Access*** makes your account more vulnerable. Therefore, I highly recommend you to create a new (dummy) account!
    5.  Go to the following website: https://accounts.google.com/DisplayUnlockCaptcha. Click ***Continue*** and then you should see ***Account access enabled*** message.
    6.  Change the port number in the following line: `with smtplib.SMTP("smtp.gmail.com", port=587) as connection`. Normally, no need for a port number but that didn't work in my case...
    7.  If you come to this step, sorry but ran out of solution :(
 5. [Suggestion] If you do not encounter an error but also cannot see the email, check your spam folder.
6. If everything went well until this point and someone's birthday is on that day, the ***ABR*** reminds you via email :100:

----

If you have any questions or problems, reach me out via berkturetken1@gmail.com :+1:
