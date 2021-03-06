#TrustGame

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np 
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os 
import sys

from psychopy.hardware import keyboard

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '3.2.4'
expName = 'TrustGame'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr() 
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\tul00635\\Documents\\GitHub\\Self-Regulation-Psychopy-Files\\Dictator Game\\TrustGame.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING) 

endExpNow = False 
frameTolerance = 0.001 

win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0 

defaultKeyboard = keyboard.Keyboard()

IntroClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='In this task, you will be playing a game with two other people. They will be represented by unique profile pictures.\n\nEach trial you will be playing with one of the other people.\nYou will be given $5 to use every trial. You have the option to give any dollar amount, from $0-$5, to the other player.\n\nThe amount that you choose to give will be tripled, and therefore the other player will receive 3x the amount of money you give. Then the other player will be told to make the same choice-giving some amount of the now-tripled money back to you.\nThe trials are independent, meaning that money will not be compounded and you will start with $5 each trial. At the end of the task, one of the trials will be selected at random for payment.\n\nWhen you are ready to begin, press SPACE!',
    font='Arial',
    pos=(0, 0), height=0.045, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR', depth=0.0);
begin = keyboard.Keyboard()

isiClock = core.Clock()
isiText = visual.TextStim(win=win, text='+', font='Arial', pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1);

CueClock = core.Clock()
cueText = visual.TextStim(win=win, text=None, font='Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb');

isiClock = core.Clock()
isiText = visual.TextStim(win=win, name='isiText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

sendMoney1Clock = core.Clock()
sendInstructions = visual.TextStim(win=win, name='sendInstructions', text='default text',
    font='Arial',
    pos=(0, -0.11), height=0.04, wrapWidth=1.4,color='white', colorSpace='rgb');
Player1Name = visual.TextStim(win=win, name='Player1Name',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Player1Pic = visual.ImageStim(
    win=win,
    name='Player1Pic', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
enter = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Arial',
    pos=(0, -0.35), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ID = expInfo['participant']
subID = int(ID)

dollarSign = visual.TextStim(win=win, name='dollarSign',
    text='default text',
    font='Arial',
    pos=(-0.05, -0.35), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

Giver1Clock = core.Clock()
import random
Feedback = visual.TextStim(win=win, name='Feedback',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "isi"
isiClock = core.Clock()
isiText = visual.TextStim(win=win, name='isiText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

sendMoney2Clock = core.Clock()
sendInst2 = visual.TextStim(win=win, name='sendInst2',
    text='default text',
    font='Arial',
    pos=(0, -0.11), height=0.04, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Player2Name = visual.TextStim(win=win, name='Player2Name',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Player2Pic = visual.ImageStim(
    win=win,
    name='Player2Pic', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Arial',
    pos=(0, -0.35), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
enter2 = keyboard.Keyboard()
dollar2 = visual.TextStim(win=win, name='dollar2',
    text='default text',
    font='Arial',
    pos=(-0.05, -0.35), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

Giver2Clock = core.Clock()
import random
Feedback2 = visual.TextStim(win=win, text='default text',
    font='Arial', pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb');

ThankYouClock = core.Clock()
tyText = visual.TextStim(win=win, text='Thank you for playing!', font='Arial', pos=(0, 0), height=0.1, wrapWidth=None, color='white', colorSpace='rgb');


globalClock = core.Clock() 
routineTimer = core.CountdownTimer() 

# ------Prepare to start Routine "Intro"-------
begin.keys = []
begin.rt = []
IntroComponents = [Instructions, begin]
for thisComponent in IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Intro"-------
while continueRoutine:
    t = IntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1     
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        Instructions.setAutoDraw(True)
    
    waitOnFlip = False
    if begin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        begin.frameNStart = frameN  # exact frame index
        begin.tStart = t  # local t and not account for scr refresh
        begin.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin, 'tStartRefresh')  # time at next scr refresh
        begin.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin.status == STARTED and not waitOnFlip:
        theseKeys = begin.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            begin.keys = theseKeys.name  # just the last key pressed
            begin.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if begin.keys in ['', [], None]:  # No response was made
    begin.keys = None
thisExp.addData('begin.keys',begin.keys)
if begin.keys != None:  # we had a response
    thisExp.addData('begin.rt', begin.rt)
thisExp.addData('begin.started', begin.tStartRefresh)
thisExp.addData('begin.stopped', begin.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

CueLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DictatorGame.xlsx'),
    seed=None, name='CueLoop')
thisExp.addLoop(CueLoop)  # add the loop to the experiment
thisCueLoop = CueLoop.trialList[0]
if thisCueLoop != None:
    for paramName in thisCueLoop:
        exec('{} = thisCueLoop[paramName]'.format(paramName))

for thisCueLoop in CueLoop:
    currentLoop = CueLoop
    if thisCueLoop != None:
        for paramName in thisCueLoop:
            exec('{} = thisCueLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "isi"-------
    routineTimer.add(2.000000)
    isiComponents = [isiText]
    for thisComponent in isiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "isi"-------
    while continueRoutine and routineTimer.getTime() > 0:
        t = isiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1 
        
        # *isiText* updates
        if isiText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isiText.frameNStart = frameN  # exact frame index
            isiText.tStart = t 
            isiText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isiText, 'tStartRefresh')  # time at next scr refresh
            isiText.setAutoDraw(True)
        if isiText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isiText.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                isiText.tStop = t  # not accounting for scr refresh
                isiText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isiText, 'tStopRefresh')  # time at next scr refresh
                isiText.setAutoDraw(False)
        
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
    
    # ------Prepare to start Routine "Cue"-------
    routineTimer.add(6.000000)
    cueText.setText('')
    if subID%2==0:
        cueText.setText(CueType1)
    if subID%2==1:
        cueText.setText(CueType2)
    CueComponents = [cueText]
    for thisComponent in CueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = CueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if cueText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            cueText.frameNStart = frameN  # exact frame index
            cueText.tStart = t  
            cueText.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(cueText, 'tStartRefresh')
            cueText.setAutoDraw(True)
        if cueText.status == STARTED:
            if tThisFlipGlobal > cueText.tStartRefresh + 6-frameTolerance:
                cueText.tStop = t 
                cueText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cueText, 'tStopRefresh')  # time at next scr refresh
                cueText.setAutoDraw(False)
        
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Cue"-------
    for thisComponent in CueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "isi"-------
    routineTimer.add(2.000000)
    isiComponents = [isiText]
    for thisComponent in isiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "isi"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = isiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1 
        if isiText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isiText.frameNStart = frameN  # exact frame index
            isiText.tStart = t  # local t and not account for scr refresh
            isiText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isiText, 'tStartRefresh')  # time at next scr refresh
            isiText.setAutoDraw(True)
        if isiText.status == STARTED:
            if tThisFlipGlobal > isiText.tStartRefresh + 2-frameTolerance:
                isiText.tStop = t  # not accounting for scr refresh
                isiText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isiText, 'tStopRefresh')  # time at next scr refresh
                isiText.setAutoDraw(False)
        
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    randomPresent = data.TrialHandler(nReps= 1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('spreadsheet5.xlsx', selection=Rows),
        seed=None, name='randomPresent')
    thisExp.addLoop(randomPresent)  # add the loop to the experiment
    thisRandomPresent = randomPresent.trialList[0]
    if thisRandomPresent != None:
        for paramName in thisRandomPresent:
            exec('{} = thisRandomPresent[paramName]'.format(paramName))
    
    for thisRandomPresent in randomPresent:
        currentLoop = randomPresent
        # abbreviate parameter names if possible (e.g. rgb = thisRandomPresent.rgb)
        if thisRandomPresent != None:
            for paramName in thisRandomPresent:
                exec('{} = thisRandomPresent[paramName]'.format(paramName))
        
        SelfishGiver = data.TrialHandler(nReps=nReps1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='SelfishGiver')
        thisExp.addLoop(SelfishGiver)  # add the loop to the experiment
        thisSelfishGiver = SelfishGiver.trialList[0]  # so we can initialise stimuli with some values
        if thisSelfishGiver != None:
            for paramName in thisSelfishGiver:
                exec('{} = thisSelfishGiver[paramName]'.format(paramName))
        
        for thisSelfishGiver in SelfishGiver:
            currentLoop = SelfishGiver
            if thisSelfishGiver != None:
                for paramName in thisSelfishGiver:
                    exec('{} = thisSelfishGiver[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "sendMoney1"-------
            sendInstructions.setText('You have been given $5 to use. You have the opportunity to send money to Player 1. You may give them all or none of the money, or any amount in between, using increments of $1. Therefore you can choose to give them $0, $1, $2, $3, $4, or $5.\nThe amount of money you send to them will be tripled, and Player 1 will then have the opportunity to give some money amount back to you. \n\n\nPlease indicate how many dollars you will give to Player 1:\n')
            Player1Name.setText('Player 1')
            Player1Pic.setPos((0, 0.36))
            Player1Pic.setSize((0.2, 0.2))
            Player1Pic.setImage('1patterns.png')
            enter.keys = []
            enter.rt = []
            text.setText('')
            modify = False
            text.text = ''
            event.clearEvents('keyboard')
            giveMoney = 0
            if subID%2==0:
                Player1Pic.setImage('3pattern.png')
            if subID%2==1:
                Player1Pic.setImage('1patterns.png')
            dollarSign.setText('$')
            sendMoney1Components = [sendInstructions, Player1Name, Player1Pic, enter, text, dollarSign]
            for thisComponent in sendMoney1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            sendMoney1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "sendMoney1"-------
            while continueRoutine:
                # get current time
                t = sendMoney1Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=sendMoney1Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1
                
                # *sendInstructions* updates
                if sendInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sendInstructions.frameNStart = frameN  # exact frame index
                    sendInstructions.tStart = t  # local t and not account for scr refresh
                    sendInstructions.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sendInstructions, 'tStartRefresh')  # time at next scr refresh
                    sendInstructions.setAutoDraw(True)
                
                # *Player1Name* updates
                if Player1Name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Player1Name.frameNStart = frameN  # exact frame index
                    Player1Name.tStart = t  # local t and not account for scr refresh
                    Player1Name.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Player1Name, 'tStartRefresh')  # time at next scr refresh
                    Player1Name.setAutoDraw(True)
                
                # *Player1Pic* updates
                if Player1Pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Player1Pic.frameNStart = frameN  # exact frame index
                    Player1Pic.tStart = t  # local t and not account for scr refresh
                    Player1Pic.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Player1Pic, 'tStartRefresh')  # time at next scr refresh
                    Player1Pic.setAutoDraw(True)
                
                # *enter* updates
                waitOnFlip = False
                if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    enter.frameNStart = frameN  # exact frame index
                    enter.tStart = t  # local t and not account for scr refresh
                    enter.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(enter, 'tStartRefresh')  # time at next scr refresh
                    enter.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(enter.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if enter.status == STARTED and not waitOnFlip:
                    theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        
                        # check for quit:
                        if "escape" == theseKeys:
                            endExpNow = True
                        enter.keys = theseKeys.name  # just the last key pressed
                        enter.rt = theseKeys.rt
                        continueRoutine = False
                
                # *text* updates
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    text.setAutoDraw(True)
                keys = event.getKeys(keyList=['0','1','2','3','4','5','return', 'backspace'])
                if len(keys):
                    if 'backspace' in keys:
                        text.text = text.text[:-1]
                    elif 'return' in keys:
                        continueRoutine = False
                    else:
                        if modify:
                            text.text = text.text + keys[0].upper()
                            modify = False
                        else:
                            text.text = text.text + keys[0]
                if '5' in keys:
                    giveMoney = 5
                if '4' in keys:
                    giveMoney = 4
                if '3' in keys:
                    giveMoney = 3
                if '2' in keys:
                    giveMoney =2
                if '1' in keys:
                    giveMoney = 1
                if '0' in keys:
                    giveMoney = 0
                if '' in keys:
                    giveMoney = 0
                    

                if dollarSign.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    dollarSign.frameNStart = frameN  # exact frame index
                    dollarSign.tStart = t  # local t and not account for scr refresh
                    dollarSign.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dollarSign, 'tStartRefresh')  # time at next scr refresh
                    dollarSign.setAutoDraw(True)
                
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sendMoney1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "sendMoney1"-------
            for thisComponent in sendMoney1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

            if enter.keys in ['', [], None]:  # No response was made
                enter.keys = None
            SelfishGiver.addData('enter.keys',enter.keys)
            if enter.keys != None:  # we had a response
                SelfishGiver.addData('enter.rt', enter.rt)
            thisExp.addData("typedWord", text.text)
            
                
            print(giveMoney)
            giveMoneyStr = "$" + str(giveMoney)
            routineTimer.reset()
            
            # ------Prepare to start Routine "Giver1"-------
            routineTimer.add(5.000000)
            backTransfer = 0
            receiveMoney = giveMoney * 3
            receiveMoneyStr = '$' + str(receiveMoney)
            
            array1 = [0,1]
            array2 = [0,1,2]
            array3 = [1,2,3,4]
            array4 = [2,3,4,5]
            array5 = [3,4,5,6,7]
            if giveMoney == 0:
                backTransfer = 0
            if giveMoney == 1:
                backTransfer = random.choice(array1)
            if giveMoney == 2:
                backTransfer = random.choice(array2)
            if giveMoney == 3:
                backTransfer = random.choice(array3)
            if giveMoney == 4:
                backTransfer = random.choice(array4)
            if giveMoney == 5:
                backTransfer = random.choice(array5)
            
            backTransferStr = "$" + str(backTransfer)
            
            textString = ("You gave Player 1 " + giveMoneyStr + "\n\nPlayer 1 received  "+ receiveMoneyStr + "\n\nPlayer 1 chose to give you "+ backTransferStr)
            Feedback.setText(textString)
            Giver1Components = [Feedback]
            for thisComponent in Giver1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Giver1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "Giver1"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Giver1Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Giver1Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1 
                
                # *Feedback* updates
                if Feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Feedback.frameNStart = frameN  # exact frame index
                    Feedback.tStart = t  # local t and not account for scr refresh
                    Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Feedback, 'tStartRefresh')  # time at next scr refresh
                    Feedback.setAutoDraw(True)
                if Feedback.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Feedback.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        Feedback.tStop = t  # not accounting for scr refresh
                        Feedback.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Feedback, 'tStopRefresh')  # time at next scr refresh
                        Feedback.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Giver1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Giver1"-------
            for thisComponent in Giver1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.nextEntry()

        
        # ------Prepare to start Routine "isi"-------
        routineTimer.add(2.000000)
        isiComponents = [isiText]
        for thisComponent in isiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        isiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "isi"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = isiClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=isiClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1 
            if isiText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                isiText.frameNStart = frameN  # exact frame index
                isiText.tStart = t  # local t and not account for scr refresh
                isiText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(isiText, 'tStartRefresh')  # time at next scr refresh
                isiText.setAutoDraw(True)
            if isiText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > isiText.tStartRefresh + 2-frameTolerance:
                    isiText.tStop = t  # not accounting for scr refresh
                    isiText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(isiText, 'tStopRefresh')  # time at next scr refresh
                    isiText.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in isiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "isi"-------
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # set up handler to look after randomisation of conditions etc
        GenerousGiver = data.TrialHandler(nReps=nReps2, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='GenerousGiver')
        thisExp.addLoop(GenerousGiver)  # add the loop to the experiment
        thisGenerousGiver = GenerousGiver.trialList[0] 
        if thisGenerousGiver != None:
            for paramName in thisGenerousGiver:
                exec('{} = thisGenerousGiver[paramName]'.format(paramName))
        
        for thisGenerousGiver in GenerousGiver:
            currentLoop = GenerousGiver
            if thisGenerousGiver != None:
                for paramName in thisGenerousGiver:
                    exec('{} = thisGenerousGiver[paramName]'.format(paramName))
            
            sendInst2.setText('You have been given $5 to use. You have the opportunity to send money to Player 2. You may give them all or none of the money, or any amount in between, using increments of $1. Therefore you can choose to give them $0, $1, $2, $3, $4, or $5.\nThe amount of money you send to them will be tripled, and Player 2 will then have the opportunity to give some money amount back to you. \n\nPlease type how much money you would like to give Player 2 : ')
            Player2Name.setText('Player 2')
            Player2Pic.setPos((0, 0.36))
            Player2Pic.setSize((0.2, 0.2))
            Player2Pic.setImage('3pattern.png')
            enter2.keys = []
            enter2.rt = []
            if subID%2==0:
                Player2Pic.setImage('1patterns.png')
            if subID%2==1:
                Player2Pic.setImage('3pattern.png')
                
            
            modify = False
            text_2.text = ''
            event.clearEvents('keyboard')
            giveMoney = 0
            
            dollar2.setText('$')
            sendMoney2Components = [sendInst2, Player2Name, Player2Pic, text_2, enter2, dollar2]
            for thisComponent in sendMoney2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            sendMoney2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "sendMoney2"-------
            while continueRoutine:
                # get current time
                t = sendMoney2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=sendMoney2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1
                if sendInst2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sendInst2.frameNStart = frameN  # exact frame index
                    sendInst2.tStart = t  # local t and not account for scr refresh
                    sendInst2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sendInst2, 'tStartRefresh')  # time at next scr refresh
                    sendInst2.setAutoDraw(True)
                
                # *Player2Name* updates
                if Player2Name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Player2Name.frameNStart = frameN  # exact frame index
                    Player2Name.tStart = t  # local t and not account for scr refresh
                    Player2Name.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Player2Name, 'tStartRefresh')  # time at next scr refresh
                    Player2Name.setAutoDraw(True)
                
                # *Player2Pic* updates
                if Player2Pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Player2Pic.frameNStart = frameN  # exact frame index
                    Player2Pic.tStart = t  # local t and not account for scr refresh
                    Player2Pic.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Player2Pic, 'tStartRefresh')  # time at next scr refresh
                    Player2Pic.setAutoDraw(True)
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                
                # *enter2* updates
                waitOnFlip = False
                if enter2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    enter2.frameNStart = frameN  # exact frame index
                    enter2.tStart = t  # local t and not account for scr refresh
                    enter2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(enter2, 'tStartRefresh')  # time at next scr refresh
                    enter2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(enter2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(enter2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if enter2.status == STARTED and not waitOnFlip:
                    theseKeys = enter2.getKeys(keyList=['return'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        
                        # check for quit:
                        if "escape" == theseKeys:
                            endExpNow = True
                        enter2.keys = theseKeys.name  # just the last key pressed
                        enter2.rt = theseKeys.rt
                        # a response ends the routine
                        continueRoutine = False
                keys = event.getKeys(keyList=['0','1','2','3','4','5','return', 'backspace'])
                if len(keys):
                    if 'backspace' in keys:
                        text_2.text = text_2.text[:-1]
                    elif 'return' in keys:
                        continueRoutine = False
                    else:
                        if modify:
                            text_2.text = text_2.text + keys[0].upper()
                            modify = False
                        else:
                            text_2.text = text_2.text + keys[0]
                if '5' in keys:
                    giveMoney = 5
                if '4' in keys:
                    giveMoney = 4
                if '3' in keys:
                    giveMoney = 3
                if '2' in keys:
                    giveMoney =2
                if '1' in keys:
                    giveMoney = 1
                if '0' in keys:
                    giveMoney = 0
                if '' in keys:
                    giveMoney = 0
                    
                if dollar2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    dollar2.frameNStart = frameN  # exact frame index
                    dollar2.tStart = t  # local t and not account for scr refresh
                    dollar2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dollar2, 'tStartRefresh')  # time at next scr refresh
                    dollar2.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sendMoney2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "sendMoney2"-------
            for thisComponent in sendMoney2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

            if enter2.keys in ['', [], None]:  # No response was made
                enter2.keys = None
            GenerousGiver.addData('enter2.keys',enter2.keys)
            if enter2.keys != None:  # we had a response
                GenerousGiver.addData('enter2.rt', enter2.rt)
            thisExp.addData("typedWord", text_2.text)
            
                
            print(giveMoney)
            
            giveMoneyStr = "$" + str(giveMoney)
            routineTimer.reset()
            
            # ------Prepare to start Routine "Giver2"-------
            routineTimer.add(5.000000)
            backTransfer = 0
            receiveMoney = giveMoney * 3
            receiveMoneyStr = '$' + str(receiveMoney)
            
            array1 = [1,2]
            array2 = [3,4,5]
            array3 = [4,5,6,7]
            array4 = [6,7,8,9,10]
            array5 = [8,9,10,11,12]
            if giveMoney == 0:
                backTransfer = 0
            if giveMoney == 1:
                backTransfer = random.choice(array1)
            if giveMoney == 2:
                backTransfer = random.choice(array2)
            if giveMoney == 3:
                backTransfer = random.choice(array3)
            if giveMoney == 4:
                backTransfer = random.choice(array4)
            if giveMoney == 5:
                backTransfer = random.choice(array5)
            
            backTransferStr = "$" + str(backTransfer)
            
            text2 = ("You gave Player 2 " + giveMoneyStr + "\n\nPlayer 2 received  "+ receiveMoneyStr + "\n\nPlayer 2 chose to give you "+ backTransferStr)
            Feedback2.setText(text2)
            Giver2Components = [Feedback2]
            for thisComponent in Giver2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Giver2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Giver2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Giver2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1 
                if Feedback2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Feedback2.frameNStart = frameN  # exact frame index
                    Feedback2.tStart = t  # local t and not account for scr refresh
                    Feedback2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Feedback2, 'tStartRefresh')  # time at next scr refresh
                    Feedback2.setAutoDraw(True)
                if Feedback2.status == STARTED:
                    if tThisFlipGlobal > Feedback2.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        Feedback2.tStop = t
                        Feedback2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Feedback2, 'tStopRefresh')  # time at next scr refresh
                        Feedback2.setAutoDraw(False)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Giver2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Giver2"-------
            for thisComponent in Giver2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            GenerousGiver.addData('Feedback2.started', Feedback2.tStartRefresh)
            GenerousGiver.addData('Feedback2.stopped', Feedback2.tStopRefresh)
            thisExp.nextEntry()

        thisExp.nextEntry()
    
    thisExp.nextEntry()
    

# ------Prepare to start Routine "ThankYou"-------
ThankYouComponents = [tyText]
for thisComponent in ThankYouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThankYouClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ThankYou"-------
while continueRoutine:
    # get current time
    t = ThankYouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThankYouClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1     
    # *tyText* updates
    if tyText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tyText.frameNStart = frameN  # exact frame index
        tyText.tStart = t  # local t and not account for scr refresh
        tyText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tyText, 'tStartRefresh')  # time at next scr refresh
        tyText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ThankYou"-------
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tyText.started', tyText.tStartRefresh)
thisExp.addData('tyText.stopped', tyText.tStopRefresh)
# the Routine "ThankYou" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

win.flip()

thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()
