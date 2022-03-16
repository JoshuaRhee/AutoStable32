import clipboard
import csv
import os
import pyautogui
import subprocess
import time

# OPTIONS
opt_scale = 'NS' # NS or False
opt_fill = False # True or False
opt_remove_outlier = True # True or False
opt_remove_drift = False # True or False
opt_type = 'OAD' # AD, OAD, MAD, TD, or HD
opt_tau = 'ALL' # DEC, OCT, or ALL
dt = 3 # delay time [s] to wait for loading

f=open("input_list.csv","r")
reader = csv.reader(f)
for line in reader:
    absdir = line[0]
    filename = line[1]
    datatype = line[2]
    tau = line[3]

    progdir = r'C:\Program Files (x86)\Hamilton Technical Services\Stable32\Stable32'
    command = f'{progdir} -F {absdir}/{filename} -T {tau} -O SKIP'
    a = subprocess.Popen([progdir, '-'+datatype, absdir+'/'+filename, '-T', tau, '-O', 'SKIP'])

    # Scale
    if opt_scale:
        pyautogui.press('alt')
        pyautogui.press('e') # edit
        pyautogui.press('s') # scale
        pyautogui.press('m') # multiplier
        if opt_scale == 'NS':
            pyautogui.typewrite('+1e-09')
        else:
            pyautogui.typewrite('+1e0')
        pyautogui.hotkey('alt','o') # OK
        time.sleep(dt)
    
    # Fill
    if opt_fill:
        pyautogui.press('alt')
        pyautogui.press('e') # edit
        pyautogui.press('f') # fill
        pyautogui.press('o') # OK
        time.sleep(dt)
    
    # Check
    if opt_remove_outlier:
        # Convert first
        if datatype == 'P':
            pyautogui.press('alt')
            pyautogui.press('e') # edit
            pyautogui.press('c') # convert
            pyautogui.press('alt')
            pyautogui.press('p') # phase to freq
            pyautogui.press('o') # OK
            time.sleep(dt)
        pyautogui.press('alt')
        pyautogui.press('a') # analysis
        pyautogui.press('c') # check
        pyautogui.press('a') # calc
        time.sleep(dt)
        pyautogui.press('l') # all
        pyautogui.press('a') # calc
        time.sleep(dt)
        pyautogui.press('c') # close
    
    # Drift
    if opt_remove_drift:
        pyautogui.press('alt')
        pyautogui.press('a') # analysis
        pyautogui.press('d') # drift
        pyautogui.press('a') # calc
        time.sleep(dt)
        pyautogui.press('r') # remove drift
        pyautogui.press('a') # calc
        time.sleep(dt)
        pyautogui.press('c') # close
    
    # Run
    pyautogui.press('alt')
    pyautogui.press('a') # analysis
    pyautogui.press('r') # run
    pyautogui.press('v') # variance type
    pyautogui.press('home') # go to top of the list
    if opt_type == 'AD':
        pyautogui.press('a')
    elif opt_type == 'OAD':
        pyautogui.press('o')
    elif opt_type == 'MAD':
        pyautogui.press('m')
    elif opt_type == 'TD':
        pyautogui.press('t')
    elif opt_type == 'HD':
        pyautogui.press('h')
    else:
        pass
    pyautogui.hotkey('shift','tab')
    if opt_tau == 'DEC':
        pyautogui.press('e') # decade
    elif opt_tau == 'OCT':
        pyautogui.press('t') # octave
    else:
        pyautogui.press('u') # all tau
    pyautogui.press('a') # calc
    time.sleep(dt)
    pyautogui.press('y') # copy
    
    copied_table = clipboard.paste()
    if not os.path.exists('OUTPUTS'):
        os.makedirs('OUTPUTS')
    outputfile = open('OUTPUTS/'+filename[:-4]+'.txt', 'w')
    outputfile.write(copied_table)
    outputfile.close()
    
    pyautogui.press('c') # close
    pyautogui.press('alt')
    pyautogui.press('f') # file
    pyautogui.press('x') # exit
    time.sleep(dt)
    print('Process for '+filename + ' is done.')
print('All processes are done.')