#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.0),
    on October 07, 2019, at 13:08
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.0'
expName = 'DelayDiscountPavlovia'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Jojo\\Downloads\\Helion Lab\\Experiment Files\\Delay Discounting\\DelayDiscountPavlovia.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instr"
InstrClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=1.6, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space = keyboard.Keyboard()

# Initialize components for Routine "Inst2"
Inst2Clock = core.Clock()
instruct2 = visual.TextStim(win=win, name='instruct2',
    text='You will be presented with two monetary offers, differing in the time at which you would receive the money. \n\nIf you would prefer the offer on the left, press "1"\n\nIf you would prefer the offer on the right, press "2"\n\nYou will have four seconds to make your choice once the offers are presented.\n\nFirst you will be playing some practice rounds. When you are ready, press ENTER to begin!',
    font='Arial',
    pos=(0, 0), height=0.065, wrapWidth=1.6, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
enter = keyboard.Keyboard()

# Initialize components for Routine "isi"
isiClock = core.Clock()
isi2 = visual.TextStim(win=win, name='isi2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PracticeCue"
PracticeCueClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='REGULATE',
    font='Arial',
    pos=(0, 0), height=0.13, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "isi"
isiClock = core.Clock()
isi2 = visual.TextStim(win=win, name='isi2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
Line = visual.Line(
    win=win, name='Line',
    start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=1.0, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
choice = keyboard.Keyboard()
ImmedMoneyAmt = visual.TextStim(win=win, name='ImmedMoneyAmt',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
DelayMoneyAmt = visual.TextStim(win=win, name='DelayMoneyAmt',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Immedtoday = visual.TextStim(win=win, name='Immedtoday',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
DelayTime = visual.TextStim(win=win, name='DelayTime',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
import numpy
from numpy import random

subID = int(expInfo['participant'])
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "BeginInst"
BeginInstClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='You will now begin the full task.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "isi"
isiClock = core.Clock()
isi2 = visual.TextStim(win=win, name='isi2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Cue"
CueClock = core.Clock()
cue = visual.TextStim(win=win, name='cue',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "isi"
isiClock = core.Clock()
isi2 = visual.TextStim(win=win, name='isi2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
Line = visual.Line(
    win=win, name='Line',
    start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=1.0, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
choice = keyboard.Keyboard()
ImmedMoneyAmt = visual.TextStim(win=win, name='ImmedMoneyAmt',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
DelayMoneyAmt = visual.TextStim(win=win, name='DelayMoneyAmt',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Immedtoday = visual.TextStim(win=win, name='Immedtoday',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
DelayTime = visual.TextStim(win=win, name='DelayTime',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
import numpy
from numpy import random

subID = int(expInfo['participant'])
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "Ending"
EndingClock = core.Clock()
ThankYou = visual.TextStim(win=win, name='ThankYou',
    text='Thank you for participating!\n\n\nYou have completed this part of the study',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instr"-------
# update component parameters for each repeat
Instructions.setColor('white', colorSpace='rgb')
Instructions.setPos((0, 0))
Instructions.setText('In this task you will be choosing between two different monetary rewards. \n\nYou will be given a regulation strategy prior to a block of trials. Please employ the strategy given while making decisions.\n\nPress SPACE to continue.\n')
Instructions.setFont('Arial')
Instructions.setHeight(0.065)
space.keys = []
space.rt = []
# keep track of which components have finished
InstrComponents = [Instructions, space]
for thisComponent in InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instr"-------
while continueRoutine:
    # get current time
    t = InstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        Instructions.setAutoDraw(True)
    
    # *space* updates
    waitOnFlip = False
    if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space.frameNStart = frameN  # exact frame index
        space.tStart = t  # local t and not account for scr refresh
        space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space, 'tStartRefresh')  # time at next scr refresh
        space.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space.status == STARTED and not waitOnFlip:
        theseKeys = space.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            space.keys = theseKeys.name  # just the last key pressed
            space.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr"-------
for thisComponent in InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions.started', Instructions.tStartRefresh)
thisExp.addData('Instructions.stopped', Instructions.tStopRefresh)
# check responses
if space.keys in ['', [], None]:  # No response was made
    space.keys = None
thisExp.addData('space.keys',space.keys)
if space.keys != None:  # we had a response
    thisExp.addData('space.rt', space.rt)
thisExp.addData('space.started', space.tStartRefresh)
thisExp.addData('space.stopped', space.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Inst2"-------
# update component parameters for each repeat
enter.keys = []
enter.rt = []
# keep track of which components have finished
Inst2Components = [instruct2, enter]
for thisComponent in Inst2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Inst2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Inst2"-------
while continueRoutine:
    # get current time
    t = Inst2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Inst2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct2* updates
    if instruct2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct2.frameNStart = frameN  # exact frame index
        instruct2.tStart = t  # local t and not account for scr refresh
        instruct2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct2, 'tStartRefresh')  # time at next scr refresh
        instruct2.setAutoDraw(True)
    
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
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Inst2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Inst2"-------
for thisComponent in Inst2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruct2.started', instruct2.tStartRefresh)
thisExp.addData('instruct2.stopped', instruct2.tStopRefresh)
# check responses
if enter.keys in ['', [], None]:  # No response was made
    enter.keys = None
thisExp.addData('enter.keys',enter.keys)
if enter.keys != None:  # we had a response
    thisExp.addData('enter.rt', enter.rt)
thisExp.addData('enter.started', enter.tStartRefresh)
thisExp.addData('enter.stopped', enter.tStopRefresh)
thisExp.nextEntry()
# the Routine "Inst2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "isi"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
isi2.setText('+')
# keep track of which components have finished
isiComponents = [isi2]
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
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *isi2* updates
    if isi2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        isi2.frameNStart = frameN  # exact frame index
        isi2.tStart = t  # local t and not account for scr refresh
        isi2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(isi2, 'tStartRefresh')  # time at next scr refresh
        isi2.setAutoDraw(True)
    if isi2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > isi2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            isi2.tStop = t  # not accounting for scr refresh
            isi2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(isi2, 'tStopRefresh')  # time at next scr refresh
            isi2.setAutoDraw(False)
    
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
thisExp.addData('isi2.started', isi2.tStartRefresh)
thisExp.addData('isi2.stopped', isi2.tStopRefresh)

# ------Prepare to start Routine "PracticeCue"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
PracticeCueComponents = [text]
for thisComponent in PracticeCueComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeCueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "PracticeCue"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = PracticeCueClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeCueClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracticeCueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracticeCue"-------
for thisComponent in PracticeCueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
PracticeLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DelayDiscountingAmt.csv', selection='0:3'),
    seed=None, name='PracticeLoop')
thisExp.addLoop(PracticeLoop)  # add the loop to the experiment
thisPracticeLoop = PracticeLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
if thisPracticeLoop != None:
    for paramName in thisPracticeLoop:
        exec('{} = thisPracticeLoop[paramName]'.format(paramName))

for thisPracticeLoop in PracticeLoop:
    currentLoop = PracticeLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            exec('{} = thisPracticeLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "isi"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    isi2.setText('+')
    # keep track of which components have finished
    isiComponents = [isi2]
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
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi2* updates
        if isi2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isi2.frameNStart = frameN  # exact frame index
            isi2.tStart = t  # local t and not account for scr refresh
            isi2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi2, 'tStartRefresh')  # time at next scr refresh
            isi2.setAutoDraw(True)
        if isi2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                isi2.tStop = t  # not accounting for scr refresh
                isi2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isi2, 'tStopRefresh')  # time at next scr refresh
                isi2.setAutoDraw(False)
        
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
    PracticeLoop.addData('isi2.started', isi2.tStartRefresh)
    PracticeLoop.addData('isi2.stopped', isi2.tStopRefresh)
    
    # ------Prepare to start Routine "Practice"-------
    # update component parameters for each repeat
    Line.setSize((3, 0.5))
    Line.setFillColor([-1.000,-1.000,-1.000])
    Line.setLineColor([-1.000,-1.000,-1.000])
    Line.setLineWidth(7)
    choice.keys = []
    choice.rt = []
    ImmedMoneyAmt.setColor('white', colorSpace='rgb')
    ImmedMoneyAmt.setPos((-0.41, 0.15))
    ImmedMoneyAmt.setText(ImMoney)
    ImmedMoneyAmt.setFont('Arial')
    ImmedMoneyAmt.setHeight(0.12)
    DelayMoneyAmt.setColor('white', colorSpace='rgb')
    DelayMoneyAmt.setPos((0.41, 0.15))
    DelayMoneyAmt.setText(DelayMoney)
    DelayMoneyAmt.setFont('Arial')
    DelayMoneyAmt.setHeight(0.12)
    Immedtoday.setColor('white', colorSpace='rgb')
    Immedtoday.setPos((-0.41, -0.1))
    Immedtoday.setText('today')
    Immedtoday.setFont('Arial')
    Immedtoday.setHeight(0.12)
    DelayTime.setColor('white', colorSpace='rgb')
    DelayTime.setPos((0.41, -0.1))
    DelayTime.setText(DelayDays)
    DelayTime.setFont('Arial')
    DelayTime.setHeight(0.12)
    
    if subID%2 == 1 :
        leftVarText = ('today')
        leftVarMoney = (ImMoney)
        rightVarText = (DelayDays)
        rightVarMoney = (DelayMoney)
    if subID%2 == 0:
        rightVarText= ('today')
        rightVarMoney= (ImMoney)
        leftVarText= (DelayDays)
        leftVarMoney= (DelayMoney)
    
    ImmedMoneyAmt.setText(leftVarMoney)
    DelayMoneyAmt.setText(rightVarMoney)
    Immedtoday.setText(leftVarText)
    DelayTime.setText(rightVarText)
    
    
    
    blank.setText('')
    # keep track of which components have finished
    PracticeComponents = [Line, choice, ImmedMoneyAmt, DelayMoneyAmt, Immedtoday, DelayTime, blank]
    for thisComponent in PracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Practice"-------
    while continueRoutine:
        # get current time
        t = PracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Line* updates
        if Line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Line.frameNStart = frameN  # exact frame index
            Line.tStart = t  # local t and not account for scr refresh
            Line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Line, 'tStartRefresh')  # time at next scr refresh
            Line.setAutoDraw(True)
        if Line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Line.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                Line.tStop = t  # not accounting for scr refresh
                Line.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Line, 'tStopRefresh')  # time at next scr refresh
                Line.setAutoDraw(False)
        
        # *choice* updates
        waitOnFlip = False
        if choice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            choice.frameNStart = frameN  # exact frame index
            choice.tStart = t  # local t and not account for scr refresh
            choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice, 'tStartRefresh')  # time at next scr refresh
            choice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(choice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > choice.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                choice.tStop = t  # not accounting for scr refresh
                choice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(choice, 'tStopRefresh')  # time at next scr refresh
                choice.status = FINISHED
        if choice.status == STARTED and not waitOnFlip:
            theseKeys = choice.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                choice.keys = theseKeys.name  # just the last key pressed
                choice.rt = theseKeys.rt
        
        # *ImmedMoneyAmt* updates
        if ImmedMoneyAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ImmedMoneyAmt.frameNStart = frameN  # exact frame index
            ImmedMoneyAmt.tStart = t  # local t and not account for scr refresh
            ImmedMoneyAmt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ImmedMoneyAmt, 'tStartRefresh')  # time at next scr refresh
            ImmedMoneyAmt.setAutoDraw(True)
        if ImmedMoneyAmt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ImmedMoneyAmt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                ImmedMoneyAmt.tStop = t  # not accounting for scr refresh
                ImmedMoneyAmt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ImmedMoneyAmt, 'tStopRefresh')  # time at next scr refresh
                ImmedMoneyAmt.setAutoDraw(False)
        
        # *DelayMoneyAmt* updates
        if DelayMoneyAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            DelayMoneyAmt.frameNStart = frameN  # exact frame index
            DelayMoneyAmt.tStart = t  # local t and not account for scr refresh
            DelayMoneyAmt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DelayMoneyAmt, 'tStartRefresh')  # time at next scr refresh
            DelayMoneyAmt.setAutoDraw(True)
        if DelayMoneyAmt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DelayMoneyAmt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                DelayMoneyAmt.tStop = t  # not accounting for scr refresh
                DelayMoneyAmt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(DelayMoneyAmt, 'tStopRefresh')  # time at next scr refresh
                DelayMoneyAmt.setAutoDraw(False)
        
        # *Immedtoday* updates
        if Immedtoday.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Immedtoday.frameNStart = frameN  # exact frame index
            Immedtoday.tStart = t  # local t and not account for scr refresh
            Immedtoday.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Immedtoday, 'tStartRefresh')  # time at next scr refresh
            Immedtoday.setAutoDraw(True)
        if Immedtoday.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Immedtoday.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                Immedtoday.tStop = t  # not accounting for scr refresh
                Immedtoday.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Immedtoday, 'tStopRefresh')  # time at next scr refresh
                Immedtoday.setAutoDraw(False)
        
        # *DelayTime* updates
        if DelayTime.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            DelayTime.frameNStart = frameN  # exact frame index
            DelayTime.tStart = t  # local t and not account for scr refresh
            DelayTime.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DelayTime, 'tStartRefresh')  # time at next scr refresh
            DelayTime.setAutoDraw(True)
        if DelayTime.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DelayTime.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                DelayTime.tStop = t  # not accounting for scr refresh
                DelayTime.frameNStop = frameN  # exact frame index
                win.timeOnFlip(DelayTime, 'tStopRefresh')  # time at next scr refresh
                DelayTime.setAutoDraw(False)
        
        if choice.keys == '1':
            ImmedMoneyAmt.setColor('green')
            Immedtoday.setColor('green')
        if choice.keys == '2':
            DelayTime.setColor('green')
            DelayMoneyAmt.setColor('green')
            
        if (choice.keys == '1' or choice.keys == '2') and blank.status == NOT_STARTED:
            blank.tStart = t
            blank.frameNStart = frameN
            blank.setAutoDraw(True)
        
        
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice"-------
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeLoop.addData('Line.started', Line.tStartRefresh)
    PracticeLoop.addData('Line.stopped', Line.tStopRefresh)
    # check responses
    if choice.keys in ['', [], None]:  # No response was made
        choice.keys = None
    PracticeLoop.addData('choice.keys',choice.keys)
    if choice.keys != None:  # we had a response
        PracticeLoop.addData('choice.rt', choice.rt)
    PracticeLoop.addData('choice.started', choice.tStartRefresh)
    PracticeLoop.addData('choice.stopped', choice.tStopRefresh)
    PracticeLoop.addData('ImmedMoneyAmt.started', ImmedMoneyAmt.tStartRefresh)
    PracticeLoop.addData('ImmedMoneyAmt.stopped', ImmedMoneyAmt.tStopRefresh)
    PracticeLoop.addData('DelayMoneyAmt.started', DelayMoneyAmt.tStartRefresh)
    PracticeLoop.addData('DelayMoneyAmt.stopped', DelayMoneyAmt.tStopRefresh)
    PracticeLoop.addData('Immedtoday.started', Immedtoday.tStartRefresh)
    PracticeLoop.addData('Immedtoday.stopped', Immedtoday.tStopRefresh)
    PracticeLoop.addData('DelayTime.started', DelayTime.tStartRefresh)
    PracticeLoop.addData('DelayTime.stopped', DelayTime.tStopRefresh)
    
    ImmedMoneyAmt.setColor('white')
    Immedtoday.setColor('white')
    DelayTime.setColor('white')
    DelayMoneyAmt.setColor('white')
    
    if (blank.status==FINISHED):
        ImmedMoneyAmt.setAutoDraw(False)
        Immedtoday.setAutoDraw(False)
        DelayTime.setAutoDraw(False)
        DelayMoneyAmt.setAutoDraw(False)
        Line.setAutoDraw(False)
    
    PracticeLoop.addData('blank.started', blank.tStartRefresh)
    PracticeLoop.addData('blank.stopped', blank.tStopRefresh)
    # the Routine "Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'PracticeLoop'


# ------Prepare to start Routine "BeginInst"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
BeginInstComponents = [text_2]
for thisComponent in BeginInstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BeginInstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "BeginInst"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BeginInstClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BeginInstClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BeginInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BeginInst"-------
for thisComponent in BeginInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
mainLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DelayDiscountingCues.csv'),
    seed=None, name='mainLoop')
thisExp.addLoop(mainLoop)  # add the loop to the experiment
thisMainLoop = mainLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
if thisMainLoop != None:
    for paramName in thisMainLoop:
        exec('{} = thisMainLoop[paramName]'.format(paramName))

for thisMainLoop in mainLoop:
    currentLoop = mainLoop
    # abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
    if thisMainLoop != None:
        for paramName in thisMainLoop:
            exec('{} = thisMainLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "isi"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    isi2.setText('+')
    # keep track of which components have finished
    isiComponents = [isi2]
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
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi2* updates
        if isi2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isi2.frameNStart = frameN  # exact frame index
            isi2.tStart = t  # local t and not account for scr refresh
            isi2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi2, 'tStartRefresh')  # time at next scr refresh
            isi2.setAutoDraw(True)
        if isi2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                isi2.tStop = t  # not accounting for scr refresh
                isi2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isi2, 'tStopRefresh')  # time at next scr refresh
                isi2.setAutoDraw(False)
        
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
    mainLoop.addData('isi2.started', isi2.tStartRefresh)
    mainLoop.addData('isi2.stopped', isi2.tStopRefresh)
    
    # ------Prepare to start Routine "Cue"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    cue.setText(CueType)
    # keep track of which components have finished
    CueComponents = [cue]
    for thisComponent in CueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Cue"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue* updates
        if cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue.frameNStart = frameN  # exact frame index
            cue.tStart = t  # local t and not account for scr refresh
            cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue, 'tStartRefresh')  # time at next scr refresh
            cue.setAutoDraw(True)
        if cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                cue.tStop = t  # not accounting for scr refresh
                cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue, 'tStopRefresh')  # time at next scr refresh
                cue.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Cue"-------
    for thisComponent in CueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mainLoop.addData('cue.started', cue.tStartRefresh)
    mainLoop.addData('cue.stopped', cue.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('DelayDiscountingAmt.csv', selection=rows),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "isi"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        isi2.setText('+')
        # keep track of which components have finished
        isiComponents = [isi2]
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
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *isi2* updates
            if isi2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                isi2.frameNStart = frameN  # exact frame index
                isi2.tStart = t  # local t and not account for scr refresh
                isi2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(isi2, 'tStartRefresh')  # time at next scr refresh
                isi2.setAutoDraw(True)
            if isi2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > isi2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    isi2.tStop = t  # not accounting for scr refresh
                    isi2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(isi2, 'tStopRefresh')  # time at next scr refresh
                    isi2.setAutoDraw(False)
            
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
        trials.addData('isi2.started', isi2.tStartRefresh)
        trials.addData('isi2.stopped', isi2.tStopRefresh)
        
        # ------Prepare to start Routine "Practice"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        Line.setSize((3, 0.5))
        Line.setFillColor([-1.000,-1.000,-1.000])
        Line.setLineColor([-1.000,-1.000,-1.000])
        Line.setLineWidth(7)
        choice.keys = []
        choice.rt = []
        ImmedMoneyAmt.setColor('white', colorSpace='rgb')
        ImmedMoneyAmt.setPos((-0.41, 0.15))
        ImmedMoneyAmt.setText(ImMoney)
        ImmedMoneyAmt.setFont('Arial')
        ImmedMoneyAmt.setHeight(0.12)
        DelayMoneyAmt.setColor('white', colorSpace='rgb')
        DelayMoneyAmt.setPos((0.41, 0.15))
        DelayMoneyAmt.setText(DelayMoney)
        DelayMoneyAmt.setFont('Arial')
        DelayMoneyAmt.setHeight(0.12)
        Immedtoday.setColor('white', colorSpace='rgb')
        Immedtoday.setPos((-0.41, -0.1))
        Immedtoday.setText('today')
        Immedtoday.setFont('Arial')
        Immedtoday.setHeight(0.12)
        DelayTime.setColor('white', colorSpace='rgb')
        DelayTime.setPos((0.41, -0.1))
        DelayTime.setText(DelayDays)
        DelayTime.setFont('Arial')
        DelayTime.setHeight(0.12)
        
        if subID%2 == 1 :
            leftVarText = ('today')
            leftVarMoney = (ImMoney)
            rightVarText = (DelayDays)
            rightVarMoney = (DelayMoney)
        if subID%2 == 0:
            rightVarText= ('today')
            rightVarMoney= (ImMoney)
            leftVarText= (DelayDays)
            leftVarMoney= (DelayMoney)
        
        ImmedMoneyAmt.setText(leftVarMoney)
        DelayMoneyAmt.setText(rightVarMoney)
        Immedtoday.setText(leftVarText)
        DelayTime.setText(rightVarText)
        
        
        
        blank.setText('')
        # keep track of which components have finished
        PracticeComponents = [Line, choice, ImmedMoneyAmt, DelayMoneyAmt, Immedtoday, DelayTime, blank]
        for thisComponent in PracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Practice"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = PracticeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Line* updates
            if Line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Line.frameNStart = frameN  # exact frame index
                Line.tStart = t  # local t and not account for scr refresh
                Line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Line, 'tStartRefresh')  # time at next scr refresh
                Line.setAutoDraw(True)
            if Line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Line.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Line.tStop = t  # not accounting for scr refresh
                    Line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Line, 'tStopRefresh')  # time at next scr refresh
                    Line.setAutoDraw(False)
            
            # *choice* updates
            waitOnFlip = False
            if choice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                choice.frameNStart = frameN  # exact frame index
                choice.tStart = t  # local t and not account for scr refresh
                choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choice, 'tStartRefresh')  # time at next scr refresh
                choice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(choice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if choice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > choice.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    choice.tStop = t  # not accounting for scr refresh
                    choice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(choice, 'tStopRefresh')  # time at next scr refresh
                    choice.status = FINISHED
            if choice.status == STARTED and not waitOnFlip:
                theseKeys = choice.getKeys(keyList=['1', '2'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    choice.keys = theseKeys.name  # just the last key pressed
                    choice.rt = theseKeys.rt
            
            # *ImmedMoneyAmt* updates
            if ImmedMoneyAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                ImmedMoneyAmt.frameNStart = frameN  # exact frame index
                ImmedMoneyAmt.tStart = t  # local t and not account for scr refresh
                ImmedMoneyAmt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ImmedMoneyAmt, 'tStartRefresh')  # time at next scr refresh
                ImmedMoneyAmt.setAutoDraw(True)
            if ImmedMoneyAmt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ImmedMoneyAmt.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    ImmedMoneyAmt.tStop = t  # not accounting for scr refresh
                    ImmedMoneyAmt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ImmedMoneyAmt, 'tStopRefresh')  # time at next scr refresh
                    ImmedMoneyAmt.setAutoDraw(False)
            
            # *DelayMoneyAmt* updates
            if DelayMoneyAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                DelayMoneyAmt.frameNStart = frameN  # exact frame index
                DelayMoneyAmt.tStart = t  # local t and not account for scr refresh
                DelayMoneyAmt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(DelayMoneyAmt, 'tStartRefresh')  # time at next scr refresh
                DelayMoneyAmt.setAutoDraw(True)
            if DelayMoneyAmt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > DelayMoneyAmt.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    DelayMoneyAmt.tStop = t  # not accounting for scr refresh
                    DelayMoneyAmt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(DelayMoneyAmt, 'tStopRefresh')  # time at next scr refresh
                    DelayMoneyAmt.setAutoDraw(False)
            
            # *Immedtoday* updates
            if Immedtoday.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Immedtoday.frameNStart = frameN  # exact frame index
                Immedtoday.tStart = t  # local t and not account for scr refresh
                Immedtoday.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Immedtoday, 'tStartRefresh')  # time at next scr refresh
                Immedtoday.setAutoDraw(True)
            if Immedtoday.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Immedtoday.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Immedtoday.tStop = t  # not accounting for scr refresh
                    Immedtoday.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Immedtoday, 'tStopRefresh')  # time at next scr refresh
                    Immedtoday.setAutoDraw(False)
            
            # *DelayTime* updates
            if DelayTime.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                DelayTime.frameNStart = frameN  # exact frame index
                DelayTime.tStart = t  # local t and not account for scr refresh
                DelayTime.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(DelayTime, 'tStartRefresh')  # time at next scr refresh
                DelayTime.setAutoDraw(True)
            if DelayTime.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > DelayTime.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    DelayTime.tStop = t  # not accounting for scr refresh
                    DelayTime.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(DelayTime, 'tStopRefresh')  # time at next scr refresh
                    DelayTime.setAutoDraw(False)
            
            if choice.keys == '1':
                ImmedMoneyAmt.setColor('green')
                Immedtoday.setColor('green')
            if choice.keys == '2':
                DelayTime.setColor('green')
                DelayMoneyAmt.setColor('green')
                
            if (choice.keys == '1' or choice.keys == '2') and blank.status == NOT_STARTED:
                blank.tStart = t
                blank.frameNStart = frameN
                blank.setAutoDraw(True)
            
            
            
            # *blank* updates
            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank.frameNStart = frameN  # exact frame index
                blank.tStart = t  # local t and not account for scr refresh
                blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
                blank.setAutoDraw(True)
            if blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    blank.tStop = t  # not accounting for scr refresh
                    blank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                    blank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Practice"-------
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('Line.started', Line.tStartRefresh)
        trials.addData('Line.stopped', Line.tStopRefresh)
        # check responses
        if choice.keys in ['', [], None]:  # No response was made
            choice.keys = None
        trials.addData('choice.keys',choice.keys)
        if choice.keys != None:  # we had a response
            trials.addData('choice.rt', choice.rt)
        trials.addData('choice.started', choice.tStartRefresh)
        trials.addData('choice.stopped', choice.tStopRefresh)
        trials.addData('ImmedMoneyAmt.started', ImmedMoneyAmt.tStartRefresh)
        trials.addData('ImmedMoneyAmt.stopped', ImmedMoneyAmt.tStopRefresh)
        trials.addData('DelayMoneyAmt.started', DelayMoneyAmt.tStartRefresh)
        trials.addData('DelayMoneyAmt.stopped', DelayMoneyAmt.tStopRefresh)
        trials.addData('Immedtoday.started', Immedtoday.tStartRefresh)
        trials.addData('Immedtoday.stopped', Immedtoday.tStopRefresh)
        trials.addData('DelayTime.started', DelayTime.tStartRefresh)
        trials.addData('DelayTime.stopped', DelayTime.tStopRefresh)
        
        ImmedMoneyAmt.setColor('white')
        Immedtoday.setColor('white')
        DelayTime.setColor('white')
        DelayMoneyAmt.setColor('white')
        
        if (blank.status==FINISHED):
            ImmedMoneyAmt.setAutoDraw(False)
            Immedtoday.setAutoDraw(False)
            DelayTime.setAutoDraw(False)
            DelayMoneyAmt.setAutoDraw(False)
            Line.setAutoDraw(False)
        
        trials.addData('blank.started', blank.tStartRefresh)
        trials.addData('blank.stopped', blank.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'mainLoop'


# ------Prepare to start Routine "Ending"-------
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndingComponents = [ThankYou]
for thisComponent in EndingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Ending"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThankYou* updates
    if ThankYou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ThankYou.frameNStart = frameN  # exact frame index
        ThankYou.tStart = t  # local t and not account for scr refresh
        ThankYou.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ThankYou, 'tStartRefresh')  # time at next scr refresh
        ThankYou.setAutoDraw(True)
    if ThankYou.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ThankYou.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            ThankYou.tStop = t  # not accounting for scr refresh
            ThankYou.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ThankYou, 'tStopRefresh')  # time at next scr refresh
            ThankYou.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ending"-------
for thisComponent in EndingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ThankYou.started', ThankYou.tStartRefresh)
thisExp.addData('ThankYou.stopped', ThankYou.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
