#ntflx_attendance_automation

Automated attendance using Python and Selenium

GUIDELINES

1. Add an environmental variable with your login details as shown below:
    Open .zshrc and update the file with a json string named NTFLX_LOGIN.

2. Add the following line:
    export NTFLX_LOGIN = '{"mail":"<yourSchoolEmailAddress>", "pwrd":"<yourPassword>"}'
    
3. Install selenium by running "pip install Selenium" in the command line. 

4. To autologin,  run 'python3 ntflxlogin.py' in command line
