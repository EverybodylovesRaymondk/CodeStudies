import requests
from datetime import datetime as dt
import webbrowser

print(dt.now())

urls = {"Confluence":'https://app.icetech.io/confluence',"Jira":'https://app.icetech.io/jira'}

dt_string = dt.now().strftime("%b %d %H:%M")
f = open("OUTPUT.TXT","w")

for k,u in urls.items():
    response = requests.get(u)
    status = response.status_code


    if status != 200:
        x = (dt_string,k + ' is off line ['+str(status)+']')
        outputF = x[0] +' '+ x[1]
        f.write(outputF + '\n')
    else:
        y = (dt_string,k + ' is online ['+str(status)+']')
        outputS = y[0] +' '+ y[1]
        f.write(outputS + '\n')
        #open_google = webbrowser.get('windows-default').open(u)
f.close()
print(dt.now())