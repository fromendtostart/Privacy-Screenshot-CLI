import pyautogui, sys, cv2, numpy, time

width, height= pyautogui.size()
taskbarHeight = 48
tabHeight = 29

if len(sys.argv) < 2:
    print("Not enough arguments!")
    sys.exit()
task = sys.argv[1]
if(task == "normal"):
    region = (0,0,1920,1080)
elif(task=="tabs"):
    region = (0, tabHeight, width, height)
elif(task=="taskbar"):
    region = (0, 0, width, height-taskbarHeight)
elif(task=="both"):
    region = (0, tabHeight, width, height-taskbarHeight)

image = pyautogui.screenshot(time.sleep(float(1.0)), region = region)
image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR) 
try : 
    cv2.imwrite(f"{task}.png", image) 
    print(f"{task} saved succesfully!")
except :
    print("Unable to save image!")



