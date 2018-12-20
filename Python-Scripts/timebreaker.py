import webbrowser
import time

total_num = 3
break_num = 0

print(time.ctime())

while(total_num > break_num):
	time.sleep(2)
	webbrowser.open("http://www.youtube.com")
	break_num = break_num + 1

