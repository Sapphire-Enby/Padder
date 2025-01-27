#!/usr/bin/env python3
import launchpad_py as launchpad
import time
import json
from os.path import exists

debug = False 
def debugfun(og):
    if not debug:
        return og    
    def wrap(*args, **kwargs):
        result = og(*args, **kwargs)
        print(CACHE)
        return result
    return wrap
# Global Constants
CACHE = {}
COLMAP={0: (1, 0), 1: (2, 0), 2: (3, 0), 16: (1, 1), 17: (2, 2), 18: (3, 3), 32: (0, 1), 33: (0, 2), 34:(0, 3)}

# Helper Methods
lp = launchpad.Launchpad()
lp.Open()
def ClearRender():  # stops all lights
    lp.Reset()

def LightPad(padNum,colorTuple): #lights a single pad
    lp.LedCtrlRaw(padNum,colorTuple[0],colorTuple[1])

def RenderMap(profile):
    ClearRender()
    # leave function if not expected map
    if profile not in [CACHE,COLMAP]:
        return
    else: # otherwise light every pad in Map
        for k,v in profile.items():
            LightPad(k,v)

def StorePad(padNum,colorTuple):
    #  Places the desired changes into the Cache
    CACHE[padNum] = colorTuple

def ClearBuffer():
    lp.ButtonFlush() # Call this before getting pad input 

def getButton(querystr="Select a Square\n"):  # prompts for a pad, returns number
    time.sleep(1)
    ClearBuffer()
    print(querystr)
    button= None
    while True:
        button_press = lp.ButtonStateRaw()
        if button_press:  # If a button press is detected
            button, state = button_press[0], button_press[1]
            print(f"Button pressed: {button}, State: {'Pressed' if state else 'Released'}\n")
            ClearRender()
        time.sleep(0.10)  # Slight delay to avoid CPU overload
        if button is not None:
            time.sleep(1)
            return button 


def getPadNum():  # setup pad for location select, return selected pad
    ClearRender()
    RenderMap(CACHE)
    return(getButton("Pick a Square to Change\n"))

def getColor(): # setup pad for color select<
    #clearRender, then render COLMap, then getPadNum,
    ClearRender()
    RenderMap(COLMAP)
    colIndex=getButton("Pick a Color to Copy\n") # defaults to blank
    return(COLMAP.get(colIndex,(0,0)))

@debugfun
def GetStore_n_Render():
    key=getPadNum()
    value=getColor()
    StorePad(key,value)
    RenderMap(CACHE)

def PromptLoad():
    while True:
        try:
            responce = input("Load Previous config? y/n: \n>")
            if responce not in ['n','y']:
                continue
            elif responce == 'n':
                return None
            else:
                fileData=QueryFileLoad()
                toLoad = ProcessRawLoad(fileData)
                return toLoad        
        except FileNotFoundError:
            continue




def QueryFileLoad():
    try:
        responce = input("enter filename \n>")
        with open(responce,'r') as config:
            out=json.load(config)
            print(out)
            return out
    except FileNotFoundError:
        print("file not found\n")
        raise
def ProcessRawLoad(fileData):
    outDict= {int(k):tuple(v) for k,v in fileData.items()}
    print(outDict)
    return outDict

def SavePrompt():
    while True:
        ans = input('save? y/n \n>')
        if ans != 'y':
            break
        try:
            SaveQuery()
            return
        except KeyboardInterrupt:
            print("save abandoned\n")   

def SaveQuery():
    while True:
        try:
            ft = input('name Save \n>')
            if exists(ft) and input('Overwrite? \n>') !='y' :
                continue
            global CACHE
            with open(ft,'w') as config:
                json.dump(CACHE, config)
            print(f"saving file {config}\n")
            return
        except KeyboardInterrupt:
            print("canceling save\n")
            raise
def ClearPrompt():
    while True:
            try:
                ans = input("clear map before end process? \n>")
                if ans not in ['n','y']:
                    print("invalid Try again \n")
                    continue
                if ans == 'y':
                    ClearRender()
                    break
                else:
                    break
            except KeyboardInterrupt:
                break

def CloseProcess():
    SavePrompt()
    ClearPrompt()
    lp.Close()

   
"""
>loadCache():
    since initally writting this down, this became a whole process
    not a single method, its in the notebook, has user input loops
    with try excepts and shit.
    remember you have to cast the key as int and value as tuple before
    storing them. but this needs to be many smaller methods
>saveCache():
    previous versions have sucessfully saved a dict to JSON
    go back and scrape
_
"""
def main():
    global CACHE
    if (mapCopy := PromptLoad()):
        CACHE=mapCopy
        RenderMap(CACHE)
    while True:
        try:
            GetStore_n_Render()
        except KeyboardInterrupt:
            break
    CloseProcess()

if __name__ == "__main__":
    main()
