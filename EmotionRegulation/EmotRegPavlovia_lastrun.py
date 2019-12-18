#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on December 18, 2019, at 09:33
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
psychopyVersion = '3.2.4'
expName = 'EmotRegPavlovia'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\tul00635\\Documents\\GitHub\\Self-Regulation-Psychopy-Files\\EmotionRegulation\\EmotRegPavlovia_lastrun.py',
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
    winType='pyglet', allowGUI=True, allowStencil=False,
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

# Initialize components for Routine "intro"
introClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='In this part of the study you will be given a regulation strategy to use while viewing various pictures.\n\nThen you will use a rating scale to indicate how you feel in the present moment. Use the mouse to select a rating, then press ENTER to move on. You will have 5 seconds to make a response once you see the rating scale.\n\nYou will first be completing a few practice rounds.\n\nWhen you are ready, press SPACE to start!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space = keyboard.Keyboard()

# Initialize components for Routine "isi"
isiClock = core.Clock()
Iti = visual.TextStim(win=win, name='Iti',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Cue"
CueClock = core.Clock()
cue = visual.TextStim(win=win, name='cue',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ISI = visual.TextStim(win=win, name='ISI',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Pic"
PicClock = core.Clock()
Image = visual.ImageStim(
    win=win,
    name='Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "ratings"
ratingsClock = core.Clock()
ratingQ = visual.TextStim(win=win, name='ratingQ',
    text='default text',
    font='Arial',
    pos=(0, 0.19), height=0.06, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=(-0.33, -0.1), height=0.039, wrapWidth=1.6, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0.33, -0.1), height=0.039, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rating_2 = visual.RatingScale(win=win, name='rating_2', marker='triangle', size=1.35, pos=[0.0, -0.38], low=1, high=5, labels=['1', '2', '3', '4', '5'], scale='')

# Initialize components for Routine "isi"
isiClock = core.Clock()
Iti = visual.TextStim(win=win, name='Iti',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "BeginInstr"
BeginInstrClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You will now begin the full task. \n\nPress SPACE to start!',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "isi"
isiClock = core.Clock()
Iti = visual.TextStim(win=win, name='Iti',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Cue"
CueClock = core.Clock()
cue = visual.TextStim(win=win, name='cue',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ISI = visual.TextStim(win=win, name='ISI',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Pic"
PicClock = core.Clock()
Image = visual.ImageStim(
    win=win,
    name='Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "ratings"
ratingsClock = core.Clock()
ratingQ = visual.TextStim(win=win, name='ratingQ',
    text='default text',
    font='Arial',
    pos=(0, 0.19), height=0.06, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=(-0.33, -0.1), height=0.039, wrapWidth=1.6, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0.33, -0.1), height=0.039, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rating_2 = visual.RatingScale(win=win, name='rating_2', marker='triangle', size=1.35, pos=[0.0, -0.38], low=1, high=5, labels=['1', '2', '3', '4', '5'], scale='')

# Initialize components for Routine "isi"
isiClock = core.Clock()
Iti = visual.TextStim(win=win, name='Iti',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TY"
TYClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Thank you for participating!\n\nYou have completed this part of the study',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
# update component parameters for each repeat
space.keys = []
space.rt = []
# keep track of which components have finished
introComponents = [Instructions, space]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
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
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
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
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "isi"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
Iti.setText('+')
# keep track of which components have finished
isiComponents = [Iti]
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
    
    # *Iti* updates
    if Iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Iti.frameNStart = frameN  # exact frame index
        Iti.tStart = t  # local t and not account for scr refresh
        Iti.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Iti, 'tStartRefresh')  # time at next scr refresh
        Iti.setAutoDraw(True)
    if Iti.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Iti.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            Iti.tStop = t  # not accounting for scr refresh
            Iti.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Iti, 'tStopRefresh')  # time at next scr refresh
            Iti.setAutoDraw(False)
    
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
thisExp.addData('Iti.started', Iti.tStartRefresh)
thisExp.addData('Iti.stopped', Iti.tStopRefresh)

# set up handler to look after randomisation of conditions etc
practiceLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('EmotionRegCues.csv', selection='0'),
    seed=None, name='practiceLoop')
thisExp.addLoop(practiceLoop)  # add the loop to the experiment
thisPracticeLoop = practiceLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
if thisPracticeLoop != None:
    for paramName in thisPracticeLoop:
        exec('{} = thisPracticeLoop[paramName]'.format(paramName))

for thisPracticeLoop in practiceLoop:
    currentLoop = practiceLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            exec('{} = thisPracticeLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Cue"-------
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    cue.setText('')
    ISI.setText('+')
    subID = int(expInfo['participant'])
    
    if subID%2==0:
        cue.setText(CueType1)
    if subID%2==1:
        cue.setText(CueType2)
    # keep track of which components have finished
    CueComponents = [cue, ISI]
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
            if tThisFlipGlobal > cue.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                cue.tStop = t  # not accounting for scr refresh
                cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue, 'tStopRefresh')  # time at next scr refresh
                cue.setAutoDraw(False)
        
        # *ISI* updates
        if ISI.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.setAutoDraw(True)
        if ISI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI.tStartRefresh + 2-frameTolerance:
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
    practiceLoop.addData('cue.started', cue.tStartRefresh)
    practiceLoop.addData('cue.stopped', cue.tStopRefresh)
    practiceLoop.addData('ISI.started', ISI.tStartRefresh)
    practiceLoop.addData('ISI.stopped', ISI.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('EmotionReg.csv', selection='0:3'),
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
        
        # ------Prepare to start Routine "Pic"-------
        routineTimer.add(8.000000)
        # update component parameters for each repeat
        Image.setSize((1.5, 1))
        Image.setImage(Picture)
        # keep track of which components have finished
        PicComponents = [Image]
        for thisComponent in PicComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PicClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Pic"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = PicClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PicClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Image* updates
            if Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Image.frameNStart = frameN  # exact frame index
                Image.tStart = t  # local t and not account for scr refresh
                Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Image, 'tStartRefresh')  # time at next scr refresh
                Image.setAutoDraw(True)
            if Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Image.tStartRefresh + 8-frameTolerance:
                    # keep track of stop time/frame for later
                    Image.tStop = t  # not accounting for scr refresh
                    Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Image, 'tStopRefresh')  # time at next scr refresh
                    Image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PicComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Pic"-------
        for thisComponent in PicComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('Image.started', Image.tStartRefresh)
        trials.addData('Image.stopped', Image.tStopRefresh)
        
        # ------Prepare to start Routine "ratings"-------
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        ratingQ.setText('How would you characterize your feelings at the present moment?')
        text_2.setText(LeftText)
        text_4.setText(RightText)
        rating_2.reset()
        # keep track of which components have finished
        ratingsComponents = [ratingQ, text_2, text_4, rating_2]
        for thisComponent in ratingsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ratingsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "ratings"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ratingsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ratingsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ratingQ* updates
            if ratingQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ratingQ.frameNStart = frameN  # exact frame index
                ratingQ.tStart = t  # local t and not account for scr refresh
                ratingQ.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratingQ, 'tStartRefresh')  # time at next scr refresh
                ratingQ.setAutoDraw(True)
            if ratingQ.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 5-frameTolerance:
                    # keep track of stop time/frame for later
                    ratingQ.tStop = t  # not accounting for scr refresh
                    ratingQ.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ratingQ, 'tStopRefresh')  # time at next scr refresh
                    ratingQ.setAutoDraw(False)
            
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
                if tThisFlipGlobal > text_2.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(False)
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(False)
            # *rating_2* updates
            if rating_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating_2.frameNStart = frameN  # exact frame index
                rating_2.tStart = t  # local t and not account for scr refresh
                rating_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating_2, 'tStartRefresh')  # time at next scr refresh
                rating_2.setAutoDraw(True)
            continueRoutine &= rating_2.noResponse  # a response ends the trial
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ratingsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ratings"-------
        for thisComponent in ratingsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('ratingQ.started', ratingQ.tStartRefresh)
        trials.addData('ratingQ.stopped', ratingQ.tStopRefresh)
        trials.addData('text_2.started', text_2.tStartRefresh)
        trials.addData('text_2.stopped', text_2.tStopRefresh)
        trials.addData('text_4.started', text_4.tStartRefresh)
        trials.addData('text_4.stopped', text_4.tStopRefresh)
        # store data for trials (TrialHandler)
        trials.addData('rating_2.response', rating_2.getRating())
        trials.addData('rating_2.rt', rating_2.getRT())
        trials.addData('rating_2.started', rating_2.tStart)
        trials.addData('rating_2.stopped', rating_2.tStop)
        
        # ------Prepare to start Routine "isi"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        Iti.setText('+')
        # keep track of which components have finished
        isiComponents = [Iti]
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
            
            # *Iti* updates
            if Iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Iti.frameNStart = frameN  # exact frame index
                Iti.tStart = t  # local t and not account for scr refresh
                Iti.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Iti, 'tStartRefresh')  # time at next scr refresh
                Iti.setAutoDraw(True)
            if Iti.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Iti.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Iti.tStop = t  # not accounting for scr refresh
                    Iti.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Iti, 'tStopRefresh')  # time at next scr refresh
                    Iti.setAutoDraw(False)
            
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
        trials.addData('Iti.started', Iti.tStartRefresh)
        trials.addData('Iti.stopped', Iti.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'practiceLoop'


# ------Prepare to start Routine "BeginInstr"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
BeginInstrComponents = [text, key_resp]
for thisComponent in BeginInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BeginInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "BeginInstr"-------
while continueRoutine:
    # get current time
    t = BeginInstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BeginInstrClock)
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
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BeginInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BeginInstr"-------
for thisComponent in BeginInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "BeginInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "isi"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
Iti.setText('+')
# keep track of which components have finished
isiComponents = [Iti]
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
    
    # *Iti* updates
    if Iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Iti.frameNStart = frameN  # exact frame index
        Iti.tStart = t  # local t and not account for scr refresh
        Iti.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Iti, 'tStartRefresh')  # time at next scr refresh
        Iti.setAutoDraw(True)
    if Iti.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Iti.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            Iti.tStop = t  # not accounting for scr refresh
            Iti.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Iti, 'tStopRefresh')  # time at next scr refresh
            Iti.setAutoDraw(False)
    
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
thisExp.addData('Iti.started', Iti.tStartRefresh)
thisExp.addData('Iti.stopped', Iti.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('EmotionRegCues.csv', selection='0:5'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Cue"-------
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    cue.setText('')
    ISI.setText('+')
    subID = int(expInfo['participant'])
    
    if subID%2==0:
        cue.setText(CueType1)
    if subID%2==1:
        cue.setText(CueType2)
    # keep track of which components have finished
    CueComponents = [cue, ISI]
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
            if tThisFlipGlobal > cue.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                cue.tStop = t  # not accounting for scr refresh
                cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue, 'tStopRefresh')  # time at next scr refresh
                cue.setAutoDraw(False)
        
        # *ISI* updates
        if ISI.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.setAutoDraw(True)
        if ISI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI.tStartRefresh + 2-frameTolerance:
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
    trials_2.addData('cue.started', cue.tStartRefresh)
    trials_2.addData('cue.stopped', cue.tStopRefresh)
    trials_2.addData('ISI.started', ISI.tStartRefresh)
    trials_2.addData('ISI.stopped', ISI.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    mainTrials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('EmotionReg.csv', selection=rows),
        seed=None, name='mainTrials')
    thisExp.addLoop(mainTrials)  # add the loop to the experiment
    thisMainTrial = mainTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMainTrial.rgb)
    if thisMainTrial != None:
        for paramName in thisMainTrial:
            exec('{} = thisMainTrial[paramName]'.format(paramName))
    
    for thisMainTrial in mainTrials:
        currentLoop = mainTrials
        # abbreviate parameter names if possible (e.g. rgb = thisMainTrial.rgb)
        if thisMainTrial != None:
            for paramName in thisMainTrial:
                exec('{} = thisMainTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Pic"-------
        routineTimer.add(8.000000)
        # update component parameters for each repeat
        Image.setSize((1.5, 1))
        Image.setImage(Picture)
        # keep track of which components have finished
        PicComponents = [Image]
        for thisComponent in PicComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PicClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Pic"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = PicClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PicClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Image* updates
            if Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Image.frameNStart = frameN  # exact frame index
                Image.tStart = t  # local t and not account for scr refresh
                Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Image, 'tStartRefresh')  # time at next scr refresh
                Image.setAutoDraw(True)
            if Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Image.tStartRefresh + 8-frameTolerance:
                    # keep track of stop time/frame for later
                    Image.tStop = t  # not accounting for scr refresh
                    Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Image, 'tStopRefresh')  # time at next scr refresh
                    Image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PicComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Pic"-------
        for thisComponent in PicComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        mainTrials.addData('Image.started', Image.tStartRefresh)
        mainTrials.addData('Image.stopped', Image.tStopRefresh)
        
        # ------Prepare to start Routine "ratings"-------
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        ratingQ.setText('How would you characterize your feelings at the present moment?')
        text_2.setText(LeftText)
        text_4.setText(RightText)
        rating_2.reset()
        # keep track of which components have finished
        ratingsComponents = [ratingQ, text_2, text_4, rating_2]
        for thisComponent in ratingsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ratingsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "ratings"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ratingsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ratingsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ratingQ* updates
            if ratingQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ratingQ.frameNStart = frameN  # exact frame index
                ratingQ.tStart = t  # local t and not account for scr refresh
                ratingQ.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratingQ, 'tStartRefresh')  # time at next scr refresh
                ratingQ.setAutoDraw(True)
            if ratingQ.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 5-frameTolerance:
                    # keep track of stop time/frame for later
                    ratingQ.tStop = t  # not accounting for scr refresh
                    ratingQ.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ratingQ, 'tStopRefresh')  # time at next scr refresh
                    ratingQ.setAutoDraw(False)
            
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
                if tThisFlipGlobal > text_2.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(False)
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(False)
            # *rating_2* updates
            if rating_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating_2.frameNStart = frameN  # exact frame index
                rating_2.tStart = t  # local t and not account for scr refresh
                rating_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating_2, 'tStartRefresh')  # time at next scr refresh
                rating_2.setAutoDraw(True)
            continueRoutine &= rating_2.noResponse  # a response ends the trial
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ratingsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ratings"-------
        for thisComponent in ratingsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        mainTrials.addData('ratingQ.started', ratingQ.tStartRefresh)
        mainTrials.addData('ratingQ.stopped', ratingQ.tStopRefresh)
        mainTrials.addData('text_2.started', text_2.tStartRefresh)
        mainTrials.addData('text_2.stopped', text_2.tStopRefresh)
        mainTrials.addData('text_4.started', text_4.tStartRefresh)
        mainTrials.addData('text_4.stopped', text_4.tStopRefresh)
        # store data for mainTrials (TrialHandler)
        mainTrials.addData('rating_2.response', rating_2.getRating())
        mainTrials.addData('rating_2.rt', rating_2.getRT())
        mainTrials.addData('rating_2.started', rating_2.tStart)
        mainTrials.addData('rating_2.stopped', rating_2.tStop)
        
        # ------Prepare to start Routine "isi"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        Iti.setText('+')
        # keep track of which components have finished
        isiComponents = [Iti]
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
            
            # *Iti* updates
            if Iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Iti.frameNStart = frameN  # exact frame index
                Iti.tStart = t  # local t and not account for scr refresh
                Iti.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Iti, 'tStartRefresh')  # time at next scr refresh
                Iti.setAutoDraw(True)
            if Iti.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Iti.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Iti.tStop = t  # not accounting for scr refresh
                    Iti.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Iti, 'tStopRefresh')  # time at next scr refresh
                    Iti.setAutoDraw(False)
            
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
        mainTrials.addData('Iti.started', Iti.tStartRefresh)
        mainTrials.addData('Iti.stopped', Iti.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'mainTrials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "TY"-------
# update component parameters for each repeat
# keep track of which components have finished
TYComponents = [text_3]
for thisComponent in TYComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TYClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "TY"-------
while continueRoutine:
    # get current time
    t = TYClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TYClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TYComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TY"-------
for thisComponent in TYComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "TY" was not non-slip safe, so reset the non-slip timer
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
