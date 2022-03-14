import os
import pyautogui
import time
import subprocess

# OPTIONS
opt_initial_run = True # True or False
opt_scale = False # NS or False
opt_fill = False # True or False
opt_remove_outlier = True # True or False
opt_remove_drift = False # True or False
opt_type = 'MAD' # AD, OAD, MAD, TD, or HD
opt_tau = 'DEC' # DEC, OCT, or ALL

absdir = r'E:\Research\12_Experiments\220228_VLBI 데이터 bernese 분석\ADEV_results'
absdir = r'E:\Research\12_Experiments\211013_5 TIC Freq 측정\DATA_post_for ADEV'
filename = 'LTG2-HM04_BER_COD_SMT.txt'
filename = 'E_freq_ch1_3.txt'

datatype = 'FREQ' # 'PHASE' or 'FREQ'

dt = 10
flag_start = True
if opt_initial_run:
    progdir = r'C:\Program Files (x86)\Hamilton Technical Services\Stable32\Stable32'

    if datatype == 'PHASE':
        a = subprocess.Popen([progdir, '-P', absdir+'\\'+filename])
    elif datatype == 'FREQ':
        a = subprocess.Popen([progdir, '-F', absdir+'\\'+filename])
    else:
        print("ERROR: Unexpected datatype: datatype must be 'PHASE' or 'FREQ'.")
    meayflag_start = False

if flag_start:
    if opt_initial_run:
        time.sleep(dt)
        
        # Window selecting columns from data    
        pyautogui.press('o')
        
        # Window selecting tau and multiplier
        pyautogui.press('o')
        time.sleep(dt)        
    
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
        if datatype == 'PHASE':
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
    pyautogui.press('y') # copy
    #pyautogui.press('c') # close
    
    
    
        
    
    
    
    
