#Slot Machine Task

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os
import sys

from psychopy.hardware import keyboard

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '3.2.0'
expName = 'SlotMachTest'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='', extraInfo=expInfo, runtimeInfo=None, originPath='C:\\Users\\Jojo\\Downloads\\Helion Lab\\Experiment Files\\Slot MachineTask\\SlotMachTest.py',
    savePickle=True, saveWideText=True, dataFileName=filename)

logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)
global endExpNow

endExpNow = False

frameTolerance = 0.001

win = visual.Window(size=(1024, 768), fullscr=True, screen=0, winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb', blendMode='avg', useFBO=True, units='height')
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

defaultKeyboard = keyboard.Keyboard()

InstrClock = core.Clock()
Instructions = visual.TextStim(win=win, text='default text', font='Arial',pos=[0,0], height=0.065, wrapWidth=1.6, color='white');
space = keyboard.Keyboard()

Inst2Clock = core.Clock()
instruct2 = visual.TextStim(win=win,text='You will be given regulation instructions prior to a block of trials. Please employ the strategy while making your decision. \n\nYou will have three seconds to make your choice upon seeing the options. \n\nTo choose the gamble, press "1". To choose the sure option, press "2".\n\nYou will first be playing some practice rounds. To begin the practice, press enter!',
    font='Arial',pos=(0, 0), height=0.065, wrapWidth=1.6,color='white');
enter = keyboard.Keyboard()

isiClock = core.Clock()
isi2 = visual.TextStim(win=win, text='+', font='Arial',pos=(0, 0), height=0.1, color='white');

PracticeCueClock = core.Clock()
text = visual.TextStim(win=win,text='REGULATE',font='Arial', pos=(0, 0), height=0.13, color='white');

isiClock = core.Clock()
isi2 = visual.TextStim(win=win, text='+', font='Arial', pos=(0, 0), height=0.1, color='white');

PracticeClock = core.Clock()
polygon = visual.Line(win=win, start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),ori=90, pos=(0, 0),lineWidth=1.0, lineColor=1.0, fillColor=1.0, interpolate=True)

IntroductionClock = core.Clock()
choice = keyboard.Keyboard()
PractGambleAmt = visual.TextStim(win=win, text='default', font='Arial', pos=[-0.43,-0.1], height=0.11, color='white');
PracticeSureAmt = visual.TextStim(win=win, text='default',font='Arial', pos=[0.43, -0.1], height=0.11, color='white');
PractGambleProb = visual.TextStim(win=win, text='default',font='Arial', pos=[-0.43,0.3], height=0.13, color='white');
SureProb = visual.TextStim(win=win, text='default',font='Arial',pos=[0.43,0.3], height=0.13, color='white');
blank = visual.TextStim(win=win, text=None,pos=(0, 0), height=0.1);

BeginInstClock = core.Clock()
text_2 = visual.TextStim(win=win, text='You will now complete the full task.\n\nPress space to begin!',font='Arial',pos=(0, 0), height=0.1, wrapWidth=1.5, color='white');

isiClock = core.Clock()
isi2 = visual.TextStim(win=win,text='default',font='Arial',pos=(0, 0), height=0.1, wrapWidth=None, color='white');

CueClock = core.Clock()
cue = visual.TextStim(win=win, text='default', font='Arial',pos=(0, 0), height=0.15, color='white');

isiClock = core.Clock()
isi2 = visual.TextStim(win=win,text='default', font='Arial', pos=(0, 0), height=0.1, color='white');

MainClock = core.Clock()
choice2 = keyboard.Keyboard()
sureAmt = visual.TextStim(win=win, text='default',font='Arial',pos=(0.43, -0.1), height=0.11, color='white');
gambleAmt = visual.TextStim(win=win,text='default',font='Arial', pos=(-0.43, -0.1), height=0.11, color='white');
GambleProbability = visual.TextStim(win=win, text='default',font='Arial', pos=(-0.43, 0.3), height=0.13, color='white');
sureProb = visual.TextStim(win=win, text='default',font='Arial',pos=(0.43, 0.3), height=0.13, wrapWidth=None, color='white');
blank2 = visual.TextStim(win=win, text=None,font='Arial',pos=(0, 0), height=0.01);
WinLose = visual.TextStim(win=win, text='default', color='white', height=0.08, pos=(0,0))
moneyBank = visual.Rect(win=win,width=(0.38, 0.21)[0], height=(0.38, 0.21)[1], pos=(0.63, -0.38),lineWidth=7, lineColor='black',fillColor=[0.004,0.004,0.004], opacity=1, depth=-2.0, interpolate=True)

globalClock = core.Clock()
routineTimer = core.CountdownTimer()

def isi():
    routineTimer.add(2.000000)
    isi2.setText('+')
    isiComponents = [isi2]
    for thisComponent in isiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isiClock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = isiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if isi2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            isi2.frameNStart = frameN
            isi2.tStart = t
            isi2.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(isi2, 'tStartRefresh')
            isi2.setAutoDraw(True)
        if isi2.status == STARTED:
            if tThisFlipGlobal > isi2.tStartRefresh + 2-frameTolerance:
                isi2.tStop = t
                isi2.frameNStop = frameN
                win.timeOnFlip(isi2, 'tStopRefresh')
                isi2.setAutoDraw(False)
        
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        
        if continueRoutine:
            win.flip()

    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


leftVarText=[]
leftVarMoney = []
rightVarText = []
rightVarMoney = []
def choiceFunc(leftVarMoney, leftVarText, rightVarMoney, rightVarText):
    polygon.setSize((3, 0.5))
    polygon.setFillColor('black')
    polygon.setLineColor('black')
    polygon.setLineWidth(7)
    choice.keys = []
    choice.rt = []
    gambleAmt.setText(leftVarMoney)
    sureAmt.setText(rightVarMoney)
    GambleProbability.setText(leftVarText)
    SureProb.setText(rightVarText)

    if choice.keys == '1':
        gambleAmt.setColor('green')
    if choice.keys == '2':
        sureAmt.setColor('green')
    if choice.keys == '1' or choice.keys == '2':
        choice.status = FINISHED
        
    if (choice.keys == '1' or choice.keys == '2') and blank.status == NOT_STARTED:
        blank.tStart = t
        blank.frameNStart = frameN
        blank.setAutoDraw(True)
    blank.setText('')
    
    PracticeComponents = [polygon, choice, gambleAmt, sureAmt, GambleProbability, sureProb, blank, moneyBank] #horLine]
    for thisComponent in PracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeClock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True
    while continueRoutine:
        t = PracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            polygon.frameNStart = frameN
            polygon.tStart = t
            polygon.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(polygon, 'tStartRefresh')
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            if tThisFlipGlobal > polygon.tStartRefresh + 4-frameTolerance:
                polygon.tStop = t
                polygon.frameNStop = frameN
                win.timeOnFlip(polygon, 'tStopRefresh')
                polygon.setAutoDraw(False)
                
        if moneyBank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            moneyBank.frameNStart = frameN
            moneyBank.tStart = t
            moneyBank.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(moneyBank, 'tStartRefresh')
            moneyBank.setAutoDraw(True)
        if moneyBank.status == STARTED:
            if tThisFlipGlobal > moneyBank.tStartRefresh + 4-frameTolerance:
                moneyBank.tStop = t
                moneyBank.frameNStop = frameN 
                win.timeOnFlip(moneyBank, 'tStopRefresh') 
                moneyBank.setAutoDraw(False)
        
        waitOnFlip = False
        if choice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            choice.frameNStart = frameN
            choice.tStart = t
            choice.tStartRefresh = tThisFlipGlobal 
            win.timeOnFlip(choice, 'tStartRefresh')
            choice.status = STARTED
            waitOnFlip = True
            win.callOnFlip(choice.clock.reset)
            win.callOnFlip(choice.clearEvents, eventType='keyboard') 
        if choice.status == STARTED:
            if tThisFlipGlobal > choice.tStartRefresh + 4-frameTolerance:
                choice.tStop = t
                choice.frameNStop = frameN 
                win.timeOnFlip(choice, 'tStopRefresh')
                choice.status = FINISHED
        if choice.status == STARTED and not waitOnFlip:
            theseKeys = choice.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]
                
                if "escape" == theseKeys:
                    endExpNow = True
                choice.keys = theseKeys.name
                choice.rt = theseKeys.rt
        
        if gambleAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            gambleAmt.frameNStart = frameN
            gambleAmt.tStart = t
            gambleAmt.tStartRefresh = tThisFlipGlobal 
            win.timeOnFlip(gambleAmt, 'tStartRefresh')
            gambleAmt.setAutoDraw(True)
        if gambleAmt.status == STARTED:
            if tThisFlipGlobal > gambleAmt.tStartRefresh + 4-frameTolerance:
                gambleAmt.tStop = t
                gambleAmt.frameNStop = frameN
                win.timeOnFlip(gambleAmt, 'tStopRefresh')
                gambleAmt.setAutoDraw(False)
        
        if sureAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            sureAmt.frameNStart = frameN
            sureAmt.tStart = t
            sureAmt.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(sureAmt, 'tStartRefresh') 
            sureAmt.setAutoDraw(True)
        if sureAmt.status == STARTED:
            if tThisFlipGlobal > sureAmt.tStartRefresh + 4-frameTolerance:
                sureAmt.tStop = t
                sureAmt.frameNStop = frameN
                win.timeOnFlip(sureAmt, 'tStopRefresh')
                sureAmt.setAutoDraw(False)
        
        if GambleProbability.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            GambleProbability.frameNStart = frameN
            GambleProbability.tStart = t
            GambleProbability.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(GambleProbability, 'tStartRefresh')
            GambleProbability.setAutoDraw(True)
        if GambleProbability.status == STARTED:
            if tThisFlipGlobal > GambleProbability.tStartRefresh + 4-frameTolerance:
                GambleProbability.tStop = t
                GambleProbability.frameNStop = frameN
                win.timeOnFlip(GambleProbability, 'tStopRefresh')
                GambleProbability.setAutoDraw(False)
        
        if SureProb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            SureProb.frameNStart = frameN
            SureProb.tStart = t 
            SureProb.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(SureProb, 'tStartRefresh')
            SureProb.setAutoDraw(True)
        if SureProb.status == STARTED:
            if tThisFlipGlobal > SureProb.tStartRefresh + 4-frameTolerance:
                SureProb.tStop = t
                SureProb.frameNStop = frameN 
                win.timeOnFlip(SureProb, 'tStopRefresh')
                SureProb.setAutoDraw(False)
        if choice.keys == '1':
            gambleAmt.setColor('green')
        if choice.keys == '2':
            sureAmt.setColor('green')
        if choice.keys == '1' or choice.keys == '2':
            choice.status = FINISHED
            
        if (choice.keys == '1' or choice.keys == '2') and blank.status == NOT_STARTED:
            blank.tStart = t
            blank.frameNStart = frameN
            blank.setAutoDraw(True)
        
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            blank.frameNStart = frameN
            blank.tStart = t
            blank.tStartRefresh = tThisFlipGlobal 
            win.timeOnFlip(blank, 'tStartRefresh') 
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            if tThisFlipGlobal > blank.tStartRefresh + 1.5-frameTolerance:
                blank.tStop = t 
                blank.frameNStop = frameN 
                win.timeOnFlip(blank, 'tStopRefresh')
                blank.setAutoDraw(False)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        
        if continueRoutine:
            win.flip()
    
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)





Instructions.setText('In this part of the study, you will be making a series of monetary decisions.\n\nYou will have the choice between taking a gamble,  which will be shown on the left side of the screen, or choosing a sure option, which will be on the right side of the screen. \n\nFor each gamble, you will have a chance of either winning money or winning nothing, while the sure option guarantees payoff. \n\nPress space to continue. ')
InstrComponents = [Instructions, space]
for thisComponent in InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstrClock.reset(-_timeToFirstFrame)
frameN = -1
continueRoutine = True

while continueRoutine:
    t = InstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        Instructions.frameNStart = frameN
        Instructions.tStart = t
        Instructions.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(Instructions, 'tStartRefresh')
        Instructions.setAutoDraw(True)
    
    waitOnFlip = False
    if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        space.frameNStart = frameN
        space.tStart = t
        space.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(space, 'tStartRefresh')
        space.status = STARTED
        waitOnFlip = True
        win.callOnFlip(space.clock.reset)
        win.callOnFlip(space.clearEvents, eventType='keyboard')
    if space.status == STARTED and not waitOnFlip:
        theseKeys = space.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]
            
            if "escape" == theseKeys:
                endExpNow = True
            space.keys = theseKeys.name
            space.rt = theseKeys.rt
            continueRoutine = False
    
    if defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break 
    if continueRoutine:
        win.flip()

for thisComponent in InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.nextEntry()
routineTimer.reset()


enter.keys = []
enter.rt = []
Inst2Components = [instruct2, enter]
for thisComponent in Inst2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Inst2Clock.reset(-_timeToFirstFrame)
frameN = -1
continueRoutine = True

while continueRoutine:
    t = Inst2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Inst2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1

    if instruct2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        instruct2.frameNStart = frameN
        instruct2.tStart = t
        instruct2.tStartRefresh = tThisFlipGlobal 
        win.timeOnFlip(instruct2, 'tStartRefresh')
        instruct2.setAutoDraw(True)
    
    waitOnFlip = False
    if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        enter.frameNStart = frameN
        enter.tStart = t
        enter.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(enter, 'tStartRefresh')
        enter.status = STARTED
        waitOnFlip = True
        win.callOnFlip(enter.clock.reset)
        win.callOnFlip(enter.clearEvents, eventType='keyboard')
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]
            
            if "escape" == theseKeys:
                endExpNow = True
            enter.keys = theseKeys.name
            enter.rt = theseKeys.rt
            continueRoutine = False
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in Inst2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    
    if continueRoutine:
        win.flip()

for thisComponent in Inst2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


thisExp.nextEntry()
routineTimer.reset()

routineTimer.add(2.000000)
isi()


routineTimer.add(2.000000)
PracticeCueComponents = [text]
for thisComponent in PracticeCueComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeCueClock.reset(-_timeToFirstFrame)
frameN = -1
continueRoutine = True

while continueRoutine and routineTimer.getTime() > 0:
    t = PracticeCueClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeCueClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1 
    
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        text.frameNStart = frameN  # exact frame index
        text.tStart = t
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
            text.tStop = t
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in PracticeCueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    
    if continueRoutine:
        win.flip()

for thisComponent in PracticeCueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


PracticeLoop = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PracticeSlotMach.csv', selection='0:3'),seed=None)
thisExp.addLoop(PracticeLoop)
thisPracticeLoop = PracticeLoop.trialList[0]
if thisPracticeLoop != None:
    for paramName in thisPracticeLoop:
        exec('{} = thisPracticeLoop[paramName]'.format(paramName))

for thisPracticeLoop in PracticeLoop:
    currentLoop = PracticeLoop
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            exec('{} = thisPracticeLoop[paramName]'.format(paramName))
    routineTimer.add(2.000000)
    isi2.setText('+')
    isiComponents = [isi2]
    for thisComponent in isiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isiClock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = isiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if isi2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            isi2.frameNStart = frameN
            isi2.tStart = t
            isi2.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(isi2, 'tStartRefresh')
            isi2.setAutoDraw(True)
        if isi2.status == STARTED:
            if tThisFlipGlobal > isi2.tStartRefresh + 2-frameTolerance:
                isi2.tStop = t
                isi2.frameNStop = frameN
                win.timeOnFlip(isi2, 'tStopRefresh')
                isi2.setAutoDraw(False)
        
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        
        if continueRoutine:
            win.flip()

    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    
    polygon.setSize((3, 0.5))
    polygon.setFillColor('black')
    polygon.setLineColor('black')
    polygon.setLineWidth(7)
    choice.keys = []
    choice.rt = []
    if choice.keys == '1':
        gambleAmt.setColor('green')
    if choice.keys == '2':
        sureAmt.setColor('green')
    if choice.keys == '1' or choice.keys == '2':
        choice.status = FINISHED
        
    if (choice.keys == '1' or choice.keys == '2') and blank.status == NOT_STARTED:
        blank.tStart = t
        blank.frameNStart = frameN
        blank.setAutoDraw(True)
    blank.setText('')
   
    PracticeComponents = [polygon, choice, gambleAmt, sureAmt, GambleProbability, SureProb, blank, moneyBank]
    for thisComponent in PracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    subID = int(expInfo['participant'])
    if subID%2 == 0 :
        leftVarText = (gambleWinLoss)
        leftVarMoney = (gamble)
        rightVarText = (sureWinLoss)
        rightVarMoney = (sure)
    if subID%2 == 1:
        rightVarText= (gambleWinLoss)
        rightVarMoney= (gamble)
        leftVarText= (sureWinLoss)
        leftVarMoney= (sure)
   
    gambleAmt.setText(leftVarMoney)
    sureAmt.setText(rightVarMoney)
    GambleProbability.setText(leftVarText)
    SureProb.setText(rightVarText)

    if choice.keys == '1':
        gambleAmt.setColor('green')
    if choice.keys == '2':
        sureAmt.setColor('green')
    if choice.keys == '1' or choice.keys == '2':
        choice.status = FINISHED
        
    if (choice.keys == '1' or choice.keys == '2') and blank.status == NOT_STARTED:
        blank.tStart = t
        blank.frameNStart = frameN
        blank.setAutoDraw(True)
    
    PracticeComponents = [polygon, choice, gambleAmt, sureAmt, GambleProbability, sureProb, blank, moneyBank] #horLine]
    for thisComponent in PracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeClock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True
    while continueRoutine:
        t = PracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            polygon.frameNStart = frameN
            polygon.tStart = t
            polygon.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(polygon, 'tStartRefresh')
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            if tThisFlipGlobal > polygon.tStartRefresh + 4-frameTolerance:
                polygon.tStop = t
                polygon.frameNStop = frameN
                win.timeOnFlip(polygon, 'tStopRefresh')
                polygon.setAutoDraw(False)
                
        if moneyBank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            moneyBank.frameNStart = frameN
            moneyBank.tStart = t
            moneyBank.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(moneyBank, 'tStartRefresh')
            moneyBank.setAutoDraw(True)
        if moneyBank.status == STARTED:
            if tThisFlipGlobal > moneyBank.tStartRefresh + 4-frameTolerance:
                moneyBank.tStop = t
                moneyBank.frameNStop = frameN 
                win.timeOnFlip(moneyBank, 'tStopRefresh') 
                moneyBank.setAutoDraw(False)
        
        waitOnFlip = False
        if choice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            choice.frameNStart = frameN
            choice.tStart = t
            choice.tStartRefresh = tThisFlipGlobal 
            win.timeOnFlip(choice, 'tStartRefresh')
            choice.status = STARTED
            waitOnFlip = True
            win.callOnFlip(choice.clock.reset)
            win.callOnFlip(choice.clearEvents, eventType='keyboard') 
        if choice.status == STARTED:
            if tThisFlipGlobal > choice.tStartRefresh + 4-frameTolerance:
                choice.tStop = t
                choice.frameNStop = frameN 
                win.timeOnFlip(choice, 'tStopRefresh')
                choice.status = FINISHED
        if choice.status == STARTED and not waitOnFlip:
            theseKeys = choice.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]
                
                if "escape" == theseKeys:
                    endExpNow = True
                choice.keys = theseKeys.name
                choice.rt = theseKeys.rt
        
        if gambleAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            gambleAmt.frameNStart = frameN
            gambleAmt.tStart = t
            gambleAmt.tStartRefresh = tThisFlipGlobal 
            win.timeOnFlip(gambleAmt, 'tStartRefresh')
            gambleAmt.setAutoDraw(True)
        if gambleAmt.status == STARTED:
            if tThisFlipGlobal > gambleAmt.tStartRefresh + 4-frameTolerance:
                gambleAmt.tStop = t
                gambleAmt.frameNStop = frameN
                win.timeOnFlip(gambleAmt, 'tStopRefresh')
                gambleAmt.setAutoDraw(False)
        
        if sureAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            sureAmt.frameNStart = frameN
            sureAmt.tStart = t
            sureAmt.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(sureAmt, 'tStartRefresh') 
            sureAmt.setAutoDraw(True)
        if sureAmt.status == STARTED:
            if tThisFlipGlobal > sureAmt.tStartRefresh + 4-frameTolerance:
                sureAmt.tStop = t
                sureAmt.frameNStop = frameN
                win.timeOnFlip(sureAmt, 'tStopRefresh')
                sureAmt.setAutoDraw(False)
        
        if GambleProbability.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            GambleProbability.frameNStart = frameN
            GambleProbability.tStart = t
            GambleProbability.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(GambleProbability, 'tStartRefresh')
            GambleProbability.setAutoDraw(True)
        if GambleProbability.status == STARTED:
            if tThisFlipGlobal > GambleProbability.tStartRefresh + 4-frameTolerance:
                GambleProbability.tStop = t
                GambleProbability.frameNStop = frameN
                win.timeOnFlip(GambleProbability, 'tStopRefresh')
                GambleProbability.setAutoDraw(False)
        
        if SureProb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            SureProb.frameNStart = frameN
            SureProb.tStart = t 
            SureProb.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(SureProb, 'tStartRefresh')
            SureProb.setAutoDraw(True)
        if SureProb.status == STARTED:
            if tThisFlipGlobal > SureProb.tStartRefresh + 4-frameTolerance:
                SureProb.tStop = t
                SureProb.frameNStop = frameN 
                win.timeOnFlip(SureProb, 'tStopRefresh')
                SureProb.setAutoDraw(False)
        if choice.keys == '1':
            gambleAmt.setColor('green')
        if choice.keys == '2':
            sureAmt.setColor('green')
        if choice.keys == '1' or choice.keys == '2':
            choice.status = FINISHED
            
        if (choice.keys == '1' or choice.keys == '2') and blank.status == NOT_STARTED:
            blank.tStart = t
            blank.frameNStart = frameN
            blank.setAutoDraw(True)
        
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            blank.frameNStart = frameN
            blank.tStart = t
            blank.tStartRefresh = tThisFlipGlobal 
            win.timeOnFlip(blank, 'tStartRefresh') 
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            if tThisFlipGlobal > blank.tStartRefresh + 1.5-frameTolerance:
                blank.tStop = t 
                blank.frameNStop = frameN 
                win.timeOnFlip(blank, 'tStopRefresh')
                blank.setAutoDraw(False)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        
        if continueRoutine:
            win.flip()
    
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    if choice.keys in ['', [], None]:
        choice.keys = None
    PracticeLoop.addData('choice.keys',choice.keys)
    if choice.keys != None:  # we had a response
        PracticeLoop.addData('choice.rt', choice.rt)
    
    PractGambleAmt.setColor('white')
    PracticeSureAmt.setColor('white')
    
    if (blank.status==FINISHED):
        gambleAmt.setAutoDraw(False)
        sureAmt.setAutoDraw(False)
        SureProb.setAutoDraw(False)
        GambleProbability.setAutoDraw(False)
        polygon.setAutoDraw(False)

    routineTimer.reset()
    thisExp.nextEntry()

        
t = 0
IntroductionClock.reset()
Instructions.setText("You will now complete the full task. \n\nPress space to begin!")
frameN = -1
continueRoutine = True
spacebar = event.BuilderKeyResponse()
IntroductionComponents = [Instructions, spacebar]
for thisComponent in IntroductionComponents:
   if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
while continueRoutine:
    t = IntroductionClock.getTime()
    frameN = frameN + 1
        
    if t >= 0.0 and Instructions.status == NOT_STARTED:
        Instructions.tStart = t
        Instructions.frameNStart = frameN
        Instructions.setAutoDraw(True)
        
    if t >= 0.0 and spacebar.status == NOT_STARTED:
        spacebar.tStart = t
        spacebar.frameNStart = frameN
        spacebar.status = STARTED
        win.callOnFlip(spacebar.clock.reset)
        event.clearEvents(eventType='keyboard')
    if spacebar.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
           
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0: 
            spacebar.keys = theseKeys[-1]
            spacebar.rt = spacebar.clock.getTime()
            continueRoutine = False
        
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in IntroductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break 
        
    if continueRoutine:
        win.flip()

for thisComponent in IntroductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.nextEntry()
routineTimer.reset()

mainLoop = data.TrialHandler(nReps=1, method='sequential', extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PracticeSlotMach.csv'),
    seed=None, name='mainLoop')
thisExp.addLoop(mainLoop)
thisMainLoop = mainLoop.trialList[0]
if thisMainLoop != None:
    for paramName in thisMainLoop:
        exec('{} = thisMainLoop[paramName]'.format(paramName))


for thisMainLoop in mainLoop:
    currentLoop = mainLoop
    if thisMainLoop != None:
        for paramName in thisMainLoop:
            exec('{} = thisMainLoop[paramName]'.format(paramName))
    
    routineTimer.add(2.000000)
    isi2.setText('+')
    isiComponents = [isi2]
    for thisComponent in isiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isiClock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = isiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if isi2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            isi2.frameNStart = frameN  # exact frame index
            isi2.tStart = t
            isi2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi2, 'tStartRefresh')  # time at next scr refresh
            isi2.setAutoDraw(True)
        if isi2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi2.tStartRefresh + 2-frameTolerance:
                isi2.tStop = t  # not accounting for scr refresh
                isi2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isi2, 'tStopRefresh')  # time at next scr refresh
                isi2.setAutoDraw(False)
        
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    routineTimer.add(2.000000)
    cue.setText(CueType)
    CueComponents = [cue]
    for thisComponent in CueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CueClock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = CueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            cue.frameNStart = frameN
            cue.tStart = t
            cue.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(cue, 'tStartRefresh')
            cue.setAutoDraw(True)
        if cue.status == STARTED:
            if tThisFlipGlobal > cue.tStartRefresh + 2-frameTolerance:
                cue.tStop = t
                cue.frameNStop = frameN
                win.timeOnFlip(cue, 'tStopRefresh')
                cue.setAutoDraw(False)
        
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in CueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        
        if continueRoutine:
            win.flip()
    
    for thisComponent in CueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    trials = data.TrialHandler(nReps=1, method='random', extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('SlotMachine.csv', selection=Rows), seed=None, name='trials')
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
                
        
        choiceFunc(leftVarMoney, leftVarText, rightVarMoney, rightVarText)
        
        for thisComponent in MainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if choice2.keys in ['', [], None]:
            choice2.keys = None
        trials.addData('choice2.keys',choice2.keys)
        if choice2.keys != None:
            trials.addData('choice2.rt', choice2.rt)

        gambleAmt.setColor('white')
        sureAmt.setColor('white')
        
        if (blank.status==FINISHED):
            gambleAmt.setAutoDraw(False)
            sureAmt.setAutoDraw(False)
            sureProb.setAutoDraw(False)
            GambleProbability.setAutoDraw(False)
        routineTimer.reset()
        thisExp.nextEntry()
    thisExp.nextEntry()

win.flip()

thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()