

<h3>Automated attendance using Python and Selenium</h3>

<ul>
<li> This service is used to automate checking into class online 30 minutes before it starts.</li>
<li> The selenium web-scraping library was used to effectuate this implementation and the process automated using a cron job on raspberry pi.</li> 
<li> Alternatively, the process can be ran manually by running a bash script. </li>
</ul>
GUIDELINES
<ol>
    <li><p>Add an environmental variable with your login details as shown below:</p>
        <p>Open .zshrc and update the file with a json string named NTFLX_LOGIN.</p>
    </li>

<li><p>Add the following line:</p>
    <p>export NTFLX_LOGIN = '{"mail":"'<yourSchoolEmailAddress>'", "pwrd":"'<yourPassword>'"}'</p>
</li>
    
<li>Install selenium by running "pip install Selenium" in the command line. </li>

<li>To autologin,  run 'python3 ntflxlogin.py' in command line</li>
</ol>
