#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.0),
    on September 10, 2019, at 15:27
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
expName = 'Experiment1'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Jojo\\Downloads\\Helion Lab\\Experiment Files\\CardTask\\CardTaskFinal1.py',
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
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Welcome = visual.TextStim(win=win, name='Welcome',
    text='Welcome to the experiment!\n\nIn this first part of the task, you will be playing a simple game \nin which you will have the chance to earn some money.\n\nPress the spacebar to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
response1 = keyboard.Keyboard()

# Initialize components for Routine "firstITI"
firstITIClock = core.Clock()
firstTrialITI = visual.TextStim(win=win, name='firstTrialITI',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "code_2"
code_2Clock = core.Clock()
nRepsblock1=0
nRepsblock2=0

# Initialize components for Routine "Reward_Trial"
Reward_TrialClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.5, 1.0)[0], height=(0.5, 1.0)[1],
    ori=0, pos=(0, 0),
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
response2 = keyboard.Keyboard()
ISI = visual.TextStim(win=win, name='ISI',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "RewardOutcome"
RewardOutcomeClock = core.Clock()
polygon2_2 = visual.Rect(
    win=win, name='polygon2_2',
    width=(0.5, 1.0)[0], height=(0.5, 1.0)[1],
    ori=0, pos=(0, 0),
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
feedback1_2 = visual.TextStim(win=win, name='feedback1_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
arrow1_2 = visual.TextStim(win=win, name='arrow1_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ITI_2 = visual.TextStim(win=win, name='ITI_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Punishment_trial"
Punishment_trialClock = core.Clock()
rectangle = visual.Rect(
    win=win, name='rectangle',
    width=(0.5, 1)[0], height=(0.5, 1)[1],
    ori=0, pos=(0, 0),
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text1 = visual.TextStim(win=win, name='text1',
    text='?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
response3 = keyboard.Keyboard()
ISI2 = visual.TextStim(win=win, name='ISI2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "PunishmentOutcome"
PunishmentOutcomeClock = core.Clock()
rectangle2_2 = visual.Rect(
    win=win, name='rectangle2_2',
    width=(0.5, 1)[0], height=(0.5, 1)[1],
    ori=0, pos=(0, 0),
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
feedback2_2 = visual.TextStim(win=win, name='feedback2_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
arrow2_2 = visual.TextStim(win=win, name='arrow2_2',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=0.2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ITI2_2 = visual.TextStim(win=win, name='ITI2_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "EndText"
EndTextClock = core.Clock()
Finished = visual.TextStim(win=win, name='Finished',
    text='Thanks for playing!\n\nYou earned $6.00!\n\nPlease let the experimenter know you have finished the first part of the task',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
# update component parameters for each repeat
response1.keys = []
response1.rt = []
# keep track of which components have finished
InstructionsComponents = [Welcome, response1]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome* updates
    if Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome.frameNStart = frameN  # exact frame index
        Welcome.tStart = t  # local t and not account for scr refresh
        Welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome, 'tStartRefresh')  # time at next scr refresh
        Welcome.setAutoDraw(True)
    
    # *response1* updates
    waitOnFlip = False
    if response1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        response1.frameNStart = frameN  # exact frame index
        response1.tStart = t  # local t and not account for scr refresh
        response1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response1, 'tStartRefresh')  # time at next scr refresh
        response1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(response1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(response1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if response1.status == STARTED and not waitOnFlip:
        theseKeys = response1.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            response1.keys = theseKeys.name  # just the last key pressed
            response1.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welcome.started', Welcome.tStartRefresh)
thisExp.addData('Welcome.stopped', Welcome.tStopRefresh)
# check responses
if response1.keys in ['', [], None]:  # No response was made
    response1.keys = None
thisExp.addData('response1.keys',response1.keys)
if response1.keys != None:  # we had a response
    thisExp.addData('response1.rt', response1.rt)
thisExp.addData('response1.started', response1.tStartRefresh)
thisExp.addData('response1.stopped', response1.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "firstITI"-------
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
firstITIComponents = [firstTrialITI]
for thisComponent in firstITIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
firstITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "firstITI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = firstITIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=firstITIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *firstTrialITI* updates
    if firstTrialITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        firstTrialITI.frameNStart = frameN  # exact frame index
        firstTrialITI.tStart = t  # local t and not account for scr refresh
        firstTrialITI.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(firstTrialITI, 'tStartRefresh')  # time at next scr refresh
        firstTrialITI.setAutoDraw(True)
    if firstTrialITI.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > firstTrialITI.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            firstTrialITI.tStop = t  # not accounting for scr refresh
            firstTrialITI.frameNStop = frameN  # exact frame index
            win.timeOnFlip(firstTrialITI, 'tStopRefresh')  # time at next scr refresh
            firstTrialITI.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in firstITIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "firstITI"-------
for thisComponent in firstITIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('firstTrialITI.started', firstTrialITI.tStartRefresh)
thisExp.addData('firstTrialITI.stopped', firstTrialITI.tStopRefresh)

# set up handler to look after randomisation of conditions etc
alltrials = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('spreadsheet5.xlsx'),
    seed=None, name='alltrials')
thisExp.addLoop(alltrials)  # add the loop to the experiment
thisAlltrial = alltrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAlltrial.rgb)
if thisAlltrial != None:
    for paramName in thisAlltrial:
        exec('{} = thisAlltrial[paramName]'.format(paramName))

for thisAlltrial in alltrials:
    currentLoop = alltrials
    # abbreviate parameter names if possible (e.g. rgb = thisAlltrial.rgb)
    if thisAlltrial != None:
        for paramName in thisAlltrial:
            exec('{} = thisAlltrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "code_2"-------
    # update component parameters for each repeat
    if selectBlock==1:
     nRepsblock1=1
     nRepsblock2=0
    elif selectBlock==2:
     nRepsblock1=0
     nRepsblock2=1
    # keep track of which components have finished
    code_2Components = []
    for thisComponent in code_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    code_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "code_2"-------
    while continueRoutine:
        # get current time
        t = code_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=code_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in code_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "code_2"-------
    for thisComponent in code_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "code_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Reward = data.TrialHandler(nReps=nRepsblock1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Reward')
    thisExp.addLoop(Reward)  # add the loop to the experiment
    thisReward = Reward.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisReward.rgb)
    if thisReward != None:
        for paramName in thisReward:
            exec('{} = thisReward[paramName]'.format(paramName))
    
    for thisReward in Reward:
        currentLoop = Reward
        # abbreviate parameter names if possible (e.g. rgb = thisReward.rgb)
        if thisReward != None:
            for paramName in thisReward:
                exec('{} = thisReward[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Reward_Trial"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        response2.keys = []
        response2.rt = []
        # keep track of which components have finished
        Reward_TrialComponents = [polygon, text, response2, ISI]
        for thisComponent in Reward_TrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Reward_TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Reward_Trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Reward_TrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Reward_TrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
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
                if tThisFlipGlobal > text.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # *response2* updates
            waitOnFlip = False
            if response2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response2.frameNStart = frameN  # exact frame index
                response2.tStart = t  # local t and not account for scr refresh
                response2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response2, 'tStartRefresh')  # time at next scr refresh
                response2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > response2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    response2.tStop = t  # not accounting for scr refresh
                    response2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(response2, 'tStopRefresh')  # time at next scr refresh
                    response2.status = FINISHED
            if response2.status == STARTED and not waitOnFlip:
                theseKeys = response2.getKeys(keyList=['1', '2'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    response2.keys = theseKeys.name  # just the last key pressed
                    response2.rt = theseKeys.rt
            
            # *ISI* updates
            if ISI.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                ISI.frameNStart = frameN  # exact frame index
                ISI.tStart = t  # local t and not account for scr refresh
                ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                ISI.setAutoDraw(True)
            if ISI.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ISI.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    ISI.tStop = t  # not accounting for scr refresh
                    ISI.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ISI, 'tStopRefresh')  # time at next scr refresh
                    ISI.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Reward_TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Reward_Trial"-------
        for thisComponent in Reward_TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Reward.addData('polygon.started', polygon.tStartRefresh)
        Reward.addData('polygon.stopped', polygon.tStopRefresh)
        Reward.addData('text.started', text.tStartRefresh)
        Reward.addData('text.stopped', text.tStopRefresh)
        # check responses
        if response2.keys in ['', [], None]:  # No response was made
            response2.keys = None
        Reward.addData('response2.keys',response2.keys)
        if response2.keys != None:  # we had a response
            Reward.addData('response2.rt', response2.rt)
        Reward.addData('response2.started', response2.tStartRefresh)
        Reward.addData('response2.stopped', response2.tStopRefresh)
        outcome = []
        if response2.keys == '1':
            outcome = np.random.randint(1,4);
        elif response2.keys == '2':
            outcome = np.random.randint(6,9);
        else:
            outcome = "No Response";
        
        money = []
        color = []
        if response2.keys == '1':
            money = '+$0.50';
            color = [-1.0,1.0,-1.0];
        elif response2.keys == '2':
            money = '+$0.50';
            color = [-1.0,1.0,-1.0];
        else:
            money = '#';
            color = [1.0,1.0,1.0];
        Reward.addData('ISI.started', ISI.tStartRefresh)
        Reward.addData('ISI.stopped', ISI.tStopRefresh)
        
        # ------Prepare to start Routine "RewardOutcome"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        arrow1_2.setColor(color, colorSpace='rgb')
        arrow1_2.setText(money)
        # keep track of which components have finished
        RewardOutcomeComponents = [polygon2_2, feedback1_2, arrow1_2, ITI_2]
        for thisComponent in RewardOutcomeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RewardOutcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "RewardOutcome"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = RewardOutcomeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RewardOutcomeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon2_2* updates
            if polygon2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                polygon2_2.frameNStart = frameN  # exact frame index
                polygon2_2.tStart = t  # local t and not account for scr refresh
                polygon2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon2_2, 'tStartRefresh')  # time at next scr refresh
                polygon2_2.setAutoDraw(True)
            if polygon2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon2_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon2_2.tStop = t  # not accounting for scr refresh
                    polygon2_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon2_2, 'tStopRefresh')  # time at next scr refresh
                    polygon2_2.setAutoDraw(False)
            
            # *feedback1_2* updates
            if feedback1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                feedback1_2.frameNStart = frameN  # exact frame index
                feedback1_2.tStart = t  # local t and not account for scr refresh
                feedback1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback1_2, 'tStartRefresh')  # time at next scr refresh
                feedback1_2.setAutoDraw(True)
            if feedback1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback1_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback1_2.tStop = t  # not accounting for scr refresh
                    feedback1_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback1_2, 'tStopRefresh')  # time at next scr refresh
                    feedback1_2.setAutoDraw(False)
            if feedback1_2.status == STARTED:  # only update if drawing
                feedback1_2.setText(outcome, log=False)
            
            # *arrow1_2* updates
            if arrow1_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                arrow1_2.frameNStart = frameN  # exact frame index
                arrow1_2.tStart = t  # local t and not account for scr refresh
                arrow1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow1_2, 'tStartRefresh')  # time at next scr refresh
                arrow1_2.setAutoDraw(True)
            if arrow1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > arrow1_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    arrow1_2.tStop = t  # not accounting for scr refresh
                    arrow1_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(arrow1_2, 'tStopRefresh')  # time at next scr refresh
                    arrow1_2.setAutoDraw(False)
            
            # *ITI_2* updates
            if ITI_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                ITI_2.frameNStart = frameN  # exact frame index
                ITI_2.tStart = t  # local t and not account for scr refresh
                ITI_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_2, 'tStartRefresh')  # time at next scr refresh
                ITI_2.setAutoDraw(True)
            if ITI_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_2.tStop = t  # not accounting for scr refresh
                    ITI_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ITI_2, 'tStopRefresh')  # time at next scr refresh
                    ITI_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RewardOutcomeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "RewardOutcome"-------
        for thisComponent in RewardOutcomeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Reward.addData('polygon2_2.started', polygon2_2.tStartRefresh)
        Reward.addData('polygon2_2.stopped', polygon2_2.tStopRefresh)
        Reward.addData('feedback1_2.started', feedback1_2.tStartRefresh)
        Reward.addData('feedback1_2.stopped', feedback1_2.tStopRefresh)
        Reward.addData('arrow1_2.started', arrow1_2.tStartRefresh)
        Reward.addData('arrow1_2.stopped', arrow1_2.tStopRefresh)
        Reward.addData('ITI_2.started', ITI_2.tStartRefresh)
        Reward.addData('ITI_2.stopped', ITI_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nRepsblock1 repeats of 'Reward'
    
    
    # set up handler to look after randomisation of conditions etc
    Loss = data.TrialHandler(nReps=nRepsblock2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Loss')
    thisExp.addLoop(Loss)  # add the loop to the experiment
    thisLos = Loss.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLos.rgb)
    if thisLos != None:
        for paramName in thisLos:
            exec('{} = thisLos[paramName]'.format(paramName))
    
    for thisLos in Loss:
        currentLoop = Loss
        # abbreviate parameter names if possible (e.g. rgb = thisLos.rgb)
        if thisLos != None:
            for paramName in thisLos:
                exec('{} = thisLos[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Punishment_trial"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        response3.keys = []
        response3.rt = []
        # keep track of which components have finished
        Punishment_trialComponents = [rectangle, text1, response3, ISI2]
        for thisComponent in Punishment_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Punishment_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Punishment_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Punishment_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Punishment_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rectangle* updates
            if rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rectangle.frameNStart = frameN  # exact frame index
                rectangle.tStart = t  # local t and not account for scr refresh
                rectangle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rectangle, 'tStartRefresh')  # time at next scr refresh
                rectangle.setAutoDraw(True)
            if rectangle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rectangle.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    rectangle.tStop = t  # not accounting for scr refresh
                    rectangle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rectangle, 'tStopRefresh')  # time at next scr refresh
                    rectangle.setAutoDraw(False)
            
            # *text1* updates
            if text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text1.frameNStart = frameN  # exact frame index
                text1.tStart = t  # local t and not account for scr refresh
                text1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
                text1.setAutoDraw(True)
            if text1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text1.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text1.tStop = t  # not accounting for scr refresh
                    text1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text1, 'tStopRefresh')  # time at next scr refresh
                    text1.setAutoDraw(False)
            
            # *response3* updates
            waitOnFlip = False
            if response3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response3.frameNStart = frameN  # exact frame index
                response3.tStart = t  # local t and not account for scr refresh
                response3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response3, 'tStartRefresh')  # time at next scr refresh
                response3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > response3.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    response3.tStop = t  # not accounting for scr refresh
                    response3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(response3, 'tStopRefresh')  # time at next scr refresh
                    response3.status = FINISHED
            if response3.status == STARTED and not waitOnFlip:
                theseKeys = response3.getKeys(keyList=['1', '2'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    response3.keys = theseKeys.name  # just the last key pressed
                    response3.rt = theseKeys.rt
            
            # *ISI2* updates
            if ISI2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                ISI2.frameNStart = frameN  # exact frame index
                ISI2.tStart = t  # local t and not account for scr refresh
                ISI2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI2, 'tStartRefresh')  # time at next scr refresh
                ISI2.setAutoDraw(True)
            if ISI2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ISI2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    ISI2.tStop = t  # not accounting for scr refresh
                    ISI2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ISI2, 'tStopRefresh')  # time at next scr refresh
                    ISI2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Punishment_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Punishment_trial"-------
        for thisComponent in Punishment_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Loss.addData('rectangle.started', rectangle.tStartRefresh)
        Loss.addData('rectangle.stopped', rectangle.tStopRefresh)
        Loss.addData('text1.started', text1.tStartRefresh)
        Loss.addData('text1.stopped', text1.tStopRefresh)
        # check responses
        if response3.keys in ['', [], None]:  # No response was made
            response3.keys = None
        Loss.addData('response3.keys',response3.keys)
        if response3.keys != None:  # we had a response
            Loss.addData('response3.rt', response3.rt)
        Loss.addData('response3.started', response3.tStartRefresh)
        Loss.addData('response3.stopped', response3.tStopRefresh)
        outcome = []
        if response3.keys == '1':
            outcome = np.random.randint(6,9);
        elif response3.keys == '2':
            outcome = np.random.randint(1,4);
        else:
            outcome = "No Response";
        
        money = []
        color = []
        if response3.keys == '1':
            money = '-$0.25';
            color = [1.0,-1.0,-1.0];
        elif response3.keys == '2':
            money = '-$0.25';
            color = [1.0,-1.0,-1.0];
        else:
            money = '#';
            color = [1.0,1.0,1.0];
        Loss.addData('ISI2.started', ISI2.tStartRefresh)
        Loss.addData('ISI2.stopped', ISI2.tStopRefresh)
        
        # ------Prepare to start Routine "PunishmentOutcome"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        feedback2_2.setText(outcome)
        arrow2_2.setColor(color, colorSpace='rgb')
        arrow2_2.setText(money)
        # keep track of which components have finished
        PunishmentOutcomeComponents = [rectangle2_2, feedback2_2, arrow2_2, ITI2_2]
        for thisComponent in PunishmentOutcomeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PunishmentOutcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "PunishmentOutcome"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = PunishmentOutcomeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PunishmentOutcomeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rectangle2_2* updates
            if rectangle2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                rectangle2_2.frameNStart = frameN  # exact frame index
                rectangle2_2.tStart = t  # local t and not account for scr refresh
                rectangle2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rectangle2_2, 'tStartRefresh')  # time at next scr refresh
                rectangle2_2.setAutoDraw(True)
            if rectangle2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rectangle2_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    rectangle2_2.tStop = t  # not accounting for scr refresh
                    rectangle2_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rectangle2_2, 'tStopRefresh')  # time at next scr refresh
                    rectangle2_2.setAutoDraw(False)
            
            # *feedback2_2* updates
            if feedback2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                feedback2_2.frameNStart = frameN  # exact frame index
                feedback2_2.tStart = t  # local t and not account for scr refresh
                feedback2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback2_2, 'tStartRefresh')  # time at next scr refresh
                feedback2_2.setAutoDraw(True)
            if feedback2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback2_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback2_2.tStop = t  # not accounting for scr refresh
                    feedback2_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback2_2, 'tStopRefresh')  # time at next scr refresh
                    feedback2_2.setAutoDraw(False)
            
            # *arrow2_2* updates
            if arrow2_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                arrow2_2.frameNStart = frameN  # exact frame index
                arrow2_2.tStart = t  # local t and not account for scr refresh
                arrow2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow2_2, 'tStartRefresh')  # time at next scr refresh
                arrow2_2.setAutoDraw(True)
            if arrow2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > arrow2_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    arrow2_2.tStop = t  # not accounting for scr refresh
                    arrow2_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(arrow2_2, 'tStopRefresh')  # time at next scr refresh
                    arrow2_2.setAutoDraw(False)
            
            # *ITI2_2* updates
            if ITI2_2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                ITI2_2.frameNStart = frameN  # exact frame index
                ITI2_2.tStart = t  # local t and not account for scr refresh
                ITI2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI2_2, 'tStartRefresh')  # time at next scr refresh
                ITI2_2.setAutoDraw(True)
            if ITI2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI2_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI2_2.tStop = t  # not accounting for scr refresh
                    ITI2_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ITI2_2, 'tStopRefresh')  # time at next scr refresh
                    ITI2_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PunishmentOutcomeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PunishmentOutcome"-------
        for thisComponent in PunishmentOutcomeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Loss.addData('rectangle2_2.started', rectangle2_2.tStartRefresh)
        Loss.addData('rectangle2_2.stopped', rectangle2_2.tStopRefresh)
        Loss.addData('feedback2_2.started', feedback2_2.tStartRefresh)
        Loss.addData('feedback2_2.stopped', feedback2_2.tStopRefresh)
        Loss.addData('arrow2_2.started', arrow2_2.tStartRefresh)
        Loss.addData('arrow2_2.stopped', arrow2_2.tStopRefresh)
        Loss.addData('ITI2_2.started', ITI2_2.tStartRefresh)
        Loss.addData('ITI2_2.stopped', ITI2_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nRepsblock2 repeats of 'Loss'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'alltrials'


# ------Prepare to start Routine "EndText"-------
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
# keep track of which components have finished
EndTextComponents = [Finished, key_resp_2]
for thisComponent in EndTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "EndText"-------
while continueRoutine:
    # get current time
    t = EndTextClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndTextClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Finished* updates
    if Finished.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Finished.frameNStart = frameN  # exact frame index
        Finished.tStart = t  # local t and not account for scr refresh
        Finished.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Finished, 'tStartRefresh')  # time at next scr refresh
        Finished.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys = theseKeys.name  # just the last key pressed
            key_resp_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndText"-------
for thisComponent in EndTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Finished.started', Finished.tStartRefresh)
thisExp.addData('Finished.stopped', Finished.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndText" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
