#Dictator Game

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import os
import sys

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

globalClock = core.Clock()
routineTimer = core.CountdownTimer()


psychopyVersion = '3.0.7'
expName = 'DictatorGame'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Jojo\\Downloads\\HelionLab\\ExperimentFiles\\DictatorGame.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

endExpNow = False

win = visual.Window(
    size=[1024, 768], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

#set up compoonents
InstructionsClock = core.Clock()
InstText = visual.TextStim(win=win, text='In this part of the study you will be involved in monetary decisions.\n\n In the following trials, you will randomly be chosen as a Sender or a Receiver.\n\n'+
    "As a Sender, you will be making a decision to allocate money for yourself and another person. As a Receiver, you will be receiving another player's offers.\n\n" + 
    'Press space to continue.',font='Arial',pos=[0,0], height=0.08, wrapWidth=1.6,color='white');

InstText2 = visual.TextStim(win=win, text="You have randomly been chosen as a Sender and have been given $10 to use. Another person in the experiment with whom you were matched was randomly chosen to be a Receiver. " +
    "\n\nYou have the opportunity to divide your $10 with the Receiver in any way you see fit. No one else can give money to this person. You may give them all or none of the money," +
    "or any amount in between, using increments of $1.\n\nThus you can divide the money in any of the following ways: \n10 - 0,  9 - 1,  8 - 2,  7 - 3,  6 - 4,  5 - 5,  4 - 6,  3 - 7,  2 - 8,  1 - 9,  0 - 10." ,
     font='Arial',pos=[0,0.3], height=0.08, wrapWidth=1.6,color='white');

textResponse = visual.TextStim(win=win, text='default text', height=0.09, color='white', pos=[-0.1,-0.5], wrapWidth=1.5)
inputText = ''
gatherTextClock = core.Clock()


#run Instructions
t = 0
InstructionsClock.reset()
frameN = -1
continueRoutine = True
space = event.BuilderKeyResponse()
InstructionsComponents = [InstText, space]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
        
while continueRoutine:
    t = InstructionsClock.getTime()
    frameN = frameN + 1
           
    if t >= 0.0 and InstText.status == NOT_STARTED:
        InstText.tStart = t
        InstText.frameNStart = frameN
        InstText.setAutoDraw(True)
          
    if t >= 0.0 and space.status == NOT_STARTED:
        space.tStart = t
        space.frameNStart = frameN
        space.status = STARTED
        win.callOnFlip(space.clock.reset)
        event.clearEvents(eventType='keyboard')
    if space.keys == 'space':
        continueRoutine=False
    if space.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
            
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:
            space.keys = theseKeys[-1]
            space.rt = space.clock.getTime()
            continueRoutine = False
            
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
            
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
            
    if continueRoutine:
        win.flip()
        
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if space.keys =='space':
    continueRoutine=False
if space.keys in ['', [], None]:
    space.keys=None

routineTimer.reset()
thisExp.nextEntry()

trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DictatorGame.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)
thisTrial = trials.trialList[0]
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    t = 0
    gatherTextClock.reset()
    frameN = -1
    continueRoutine = True
    theseKeys=""
    shift_flag = False
    key_resp_3 = event.BuilderKeyResponse()
    gatherTextComponents = [textResponse, key_resp_3]
    for thisComponent in gatherTextComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    while continueRoutine:
        t = gatherTextClock.getTime()
        frameN = frameN + 1
        n= len(theseKeys)
        i = 0
        while i < n:
            
            if theseKeys[i] == 'return':
                continueRoutine = False
                break
           
            elif theseKeys[i] == 'backspace':
                inputText = inputText[:-1]
                i = i + 1
            
            
            else:
                if len(theseKeys[i]) == 1:
                    if shift_flag:
                        inputText += chr( ord(theseKeys[i]) - ord(' '))
                        shift_flag = False
                    else:
                        inputText += theseKeys[i]
            
                i = i + 1
        if t >= 0.0 and InstText2.status == NOT_STARTED:
            InstText2.tStart = t
            InstText2.frameNStart = frameN
            InstText2.setAutoDraw(True)
            
        if t >= 0.0 and textResponse.status == NOT_STARTED:
            textResponse.tStart = t
            textResponse.frameNStart = frameN
            textResponse.setAutoDraw(True)
        if textResponse.status == STARTED:
            textResponse.setText((word + inputText), log=False)

            
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            key_resp_3.tStart = t
            key_resp_3.frameNStart = frameN
            key_resp_3.status = STARTED
            win.callOnFlip(key_resp_3.clock.reset)
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys()
                
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:
                key_resp_3.keys.extend(theseKeys)
                key_resp_3.rt.append(key_resp_3.clock.getTime())
            
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
            
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in gatherTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
            
        if continueRoutine:
            win.flip()
        
    for thisComponent in gatherTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('inputText', inputText)
    inputText=""
    if key_resp_3.keys in ['', [], None]:
        key_resp_3.keys=None
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    routineTimer.reset()
    thisExp.nextEntry()

