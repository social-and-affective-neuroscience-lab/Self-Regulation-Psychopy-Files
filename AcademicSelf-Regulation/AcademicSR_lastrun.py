#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on October 15, 2019, at 12:05
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
expName = 'AcademicSR'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\tul00635\\Documents\\GitHub\\Self-Regulation-Psychopy-Files\\AcademicSelf-Regulation\\AcademicSR_lastrun.py',
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

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instruct = visual.TextStim(win=win, name='instruct',
    text='In this part of the study, you will be choosing between answering practice questions for standardized tests, or playing a videogame. \n\nYou will be completing 5 rounds of the chosen option, and will then be given a chance to choose again.\n\nPrior to choosing, you will be given a regulation strategy to use. Please employ this strategy while making your decision.  \n\nPress SPACE to begin!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space = keyboard.Keyboard()

# Initialize components for Routine "Cue"
CueClock = core.Clock()
regCue = visual.TextStim(win=win, name='regCue',
    text='REGULATE',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Choice"
ChoiceClock = core.Clock()
choiceQ = visual.TextStim(win=win, name='choiceQ',
    text="Please indicate which option you would like to complete by pressing '1' for the choice on the left, or '2' for the choice on the right. ",
    font='Arial',
    pos=(0, 0.35), height=0.05, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
choiceResp = keyboard.Keyboard()
testChoice = visual.TextStim(win=win, name='testChoice',
    text='Practice Standardized Test Questions',
    font='Arial',
    pos=(-0.41, 0.15), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
videogameChoice = visual.TextStim(win=win, name='videogameChoice',
    text='Play a Videogame',
    font='Arial',
    pos=(0.41, 0.15), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
gre = visual.ImageStim(
    win=win,
    name='gre', 
    image='gre.png', mask=None,
    ori=0, pos=(-.41, 0.02), size=(0.3, 0.105),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
gmat = visual.ImageStim(
    win=win,
    name='gmat', 
    image='gmat.png', mask=None,
    ori=0, pos=(-0.41, -0.13), size=(0.3, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
lsat = visual.ImageStim(
    win=win,
    name='lsat', 
    image='lsat.png', mask=None,
    ori=0, pos=(-0.41, -0.27), size=(0.3, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
mcat = visual.ImageStim(
    win=win,
    name='mcat', 
    image='mcat.png', mask=None,
    ori=0, pos=(-0.41, -0.41), size=(0.3, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
game = visual.ImageStim(
    win=win,
    name='game', 
    image='game.png', mask=None,
    ori=0, pos=(0.41, -0.19), size=(0.4, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
doTestPractice = []
doGame = []
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "testQuestionsChoice"
testQuestionsChoiceClock = core.Clock()
testQChoice = visual.TextStim(win=win, name='testQChoice',
    text='What test would you like to practice questions for? Use the arrow keys to move up and down, then press ENTER to select.',
    font='Arial',
    pos=(0, 0.35), height=0.055, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='gre.png', mask=None,
    ori=0, pos=(0, 0.105), size=(0.3, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='gmat.png', mask=None,
    ori=0, pos=(0, -0.05), size=(0.3, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='lsat.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.3, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='mcat.png', mask=None,
    ori=0, pos=(0, -0.35), size=(0.3, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
upDown = keyboard.Keyboard()
polygon = visual.Rect(
    win=win, name='polygon',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1.0, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-6.0, interpolate=True)
enter = keyboard.Keyboard()

# Initialize components for Routine "testQs"
testQsClock = core.Clock()

# Initialize components for Routine "Game"
GameClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='videogame holder\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
# update component parameters for each repeat
space.keys = []
space.rt = []
# keep track of which components have finished
InstructionsComponents = [instruct, space]
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
    
    # *instruct* updates
    if instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct.frameNStart = frameN  # exact frame index
        instruct.tStart = t  # local t and not account for scr refresh
        instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct, 'tStartRefresh')  # time at next scr refresh
        instruct.setAutoDraw(True)
    
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
thisExp.addData('instruct.started', instruct.tStartRefresh)
thisExp.addData('instruct.stopped', instruct.tStopRefresh)
# check responses
if space.keys in ['', [], None]:  # No response was made
    space.keys = None
thisExp.addData('space.keys',space.keys)
if space.keys != None:  # we had a response
    thisExp.addData('space.rt', space.rt)
thisExp.addData('space.started', space.tStartRefresh)
thisExp.addData('space.stopped', space.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
AllTrials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='AllTrials')
thisExp.addLoop(AllTrials)  # add the loop to the experiment
thisAllTrial = AllTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAllTrial.rgb)
if thisAllTrial != None:
    for paramName in thisAllTrial:
        exec('{} = thisAllTrial[paramName]'.format(paramName))

for thisAllTrial in AllTrials:
    currentLoop = AllTrials
    # abbreviate parameter names if possible (e.g. rgb = thisAllTrial.rgb)
    if thisAllTrial != None:
        for paramName in thisAllTrial:
            exec('{} = thisAllTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Cue"-------
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CueComponents = [regCue]
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
        
        # *regCue* updates
        if regCue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            regCue.frameNStart = frameN  # exact frame index
            regCue.tStart = t  # local t and not account for scr refresh
            regCue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(regCue, 'tStartRefresh')  # time at next scr refresh
            regCue.setAutoDraw(True)
        if regCue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > regCue.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                regCue.tStop = t  # not accounting for scr refresh
                regCue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(regCue, 'tStopRefresh')  # time at next scr refresh
                regCue.setAutoDraw(False)
        
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
    AllTrials.addData('regCue.started', regCue.tStartRefresh)
    AllTrials.addData('regCue.stopped', regCue.tStopRefresh)
    
    # ------Prepare to start Routine "Choice"-------
    # update component parameters for each repeat
    choiceResp.keys = []
    choiceResp.rt = []
    blank.setText('')
    # keep track of which components have finished
    ChoiceComponents = [choiceQ, choiceResp, testChoice, videogameChoice, gre, gmat, lsat, mcat, game, blank]
    for thisComponent in ChoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Choice"-------
    while continueRoutine:
        # get current time
        t = ChoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ChoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *choiceQ* updates
        if choiceQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choiceQ.frameNStart = frameN  # exact frame index
            choiceQ.tStart = t  # local t and not account for scr refresh
            choiceQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choiceQ, 'tStartRefresh')  # time at next scr refresh
            choiceQ.setAutoDraw(True)
        if choiceQ.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                choiceQ.tStop = t  # not accounting for scr refresh
                choiceQ.frameNStop = frameN  # exact frame index
                win.timeOnFlip(choiceQ, 'tStopRefresh')  # time at next scr refresh
                choiceQ.setAutoDraw(False)
        
        # *choiceResp* updates
        waitOnFlip = False
        if choiceResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choiceResp.frameNStart = frameN  # exact frame index
            choiceResp.tStart = t  # local t and not account for scr refresh
            choiceResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choiceResp, 'tStartRefresh')  # time at next scr refresh
            choiceResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(choiceResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(choiceResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if choiceResp.status == STARTED:
            if bool(choiceQ.status == FINISHED):
                # keep track of stop time/frame for later
                choiceResp.tStop = t  # not accounting for scr refresh
                choiceResp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(choiceResp, 'tStopRefresh')  # time at next scr refresh
                choiceResp.status = FINISHED
        if choiceResp.status == STARTED and not waitOnFlip:
            theseKeys = choiceResp.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                choiceResp.keys = theseKeys.name  # just the last key pressed
                choiceResp.rt = theseKeys.rt
        
        # *testChoice* updates
        if testChoice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testChoice.frameNStart = frameN  # exact frame index
            testChoice.tStart = t  # local t and not account for scr refresh
            testChoice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testChoice, 'tStartRefresh')  # time at next scr refresh
            testChoice.setAutoDraw(True)
        if testChoice.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                testChoice.tStop = t  # not accounting for scr refresh
                testChoice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testChoice, 'tStopRefresh')  # time at next scr refresh
                testChoice.setAutoDraw(False)
        
        # *videogameChoice* updates
        if videogameChoice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            videogameChoice.frameNStart = frameN  # exact frame index
            videogameChoice.tStart = t  # local t and not account for scr refresh
            videogameChoice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(videogameChoice, 'tStartRefresh')  # time at next scr refresh
            videogameChoice.setAutoDraw(True)
        if videogameChoice.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                videogameChoice.tStop = t  # not accounting for scr refresh
                videogameChoice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(videogameChoice, 'tStopRefresh')  # time at next scr refresh
                videogameChoice.setAutoDraw(False)
        
        # *gre* updates
        if gre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gre.frameNStart = frameN  # exact frame index
            gre.tStart = t  # local t and not account for scr refresh
            gre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gre, 'tStartRefresh')  # time at next scr refresh
            gre.setAutoDraw(True)
        if gre.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                gre.tStop = t  # not accounting for scr refresh
                gre.frameNStop = frameN  # exact frame index
                win.timeOnFlip(gre, 'tStopRefresh')  # time at next scr refresh
                gre.setAutoDraw(False)
        
        # *gmat* updates
        if gmat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gmat.frameNStart = frameN  # exact frame index
            gmat.tStart = t  # local t and not account for scr refresh
            gmat.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gmat, 'tStartRefresh')  # time at next scr refresh
            gmat.setAutoDraw(True)
        if gmat.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                gmat.tStop = t  # not accounting for scr refresh
                gmat.frameNStop = frameN  # exact frame index
                win.timeOnFlip(gmat, 'tStopRefresh')  # time at next scr refresh
                gmat.setAutoDraw(False)
        
        # *lsat* updates
        if lsat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lsat.frameNStart = frameN  # exact frame index
            lsat.tStart = t  # local t and not account for scr refresh
            lsat.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lsat, 'tStartRefresh')  # time at next scr refresh
            lsat.setAutoDraw(True)
        if lsat.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                lsat.tStop = t  # not accounting for scr refresh
                lsat.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lsat, 'tStopRefresh')  # time at next scr refresh
                lsat.setAutoDraw(False)
        
        # *mcat* updates
        if mcat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mcat.frameNStart = frameN  # exact frame index
            mcat.tStart = t  # local t and not account for scr refresh
            mcat.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mcat, 'tStartRefresh')  # time at next scr refresh
            mcat.setAutoDraw(True)
        if mcat.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                mcat.tStop = t  # not accounting for scr refresh
                mcat.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mcat, 'tStopRefresh')  # time at next scr refresh
                mcat.setAutoDraw(False)
        
        # *game* updates
        if game.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            game.frameNStart = frameN  # exact frame index
            game.tStart = t  # local t and not account for scr refresh
            game.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(game, 'tStartRefresh')  # time at next scr refresh
            game.setAutoDraw(True)
        if game.status == STARTED:
            if bool(blank.status == FINISHED):
                # keep track of stop time/frame for later
                game.tStop = t  # not accounting for scr refresh
                game.frameNStop = frameN  # exact frame index
                win.timeOnFlip(game, 'tStopRefresh')  # time at next scr refresh
                game.setAutoDraw(False)
        if choiceResp.keys == '1':
            testChoice.setColor('green')
        if choiceResp.keys == '2':
            videogameChoice.setColor('green')
        
        if choiceResp.keys == '2' or choiceResp.keys == '1':
            choiceResp.status = FINISHED
        
        # *blank* updates
        if blank.status == NOT_STARTED and len(choiceResp.keys) > 0:
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
        for thisComponent in ChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Choice"-------
    for thisComponent in ChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AllTrials.addData('choiceQ.started', choiceQ.tStartRefresh)
    AllTrials.addData('choiceQ.stopped', choiceQ.tStopRefresh)
    # check responses
    if choiceResp.keys in ['', [], None]:  # No response was made
        choiceResp.keys = None
    AllTrials.addData('choiceResp.keys',choiceResp.keys)
    if choiceResp.keys != None:  # we had a response
        AllTrials.addData('choiceResp.rt', choiceResp.rt)
    AllTrials.addData('choiceResp.started', choiceResp.tStartRefresh)
    AllTrials.addData('choiceResp.stopped', choiceResp.tStopRefresh)
    AllTrials.addData('testChoice.started', testChoice.tStartRefresh)
    AllTrials.addData('testChoice.stopped', testChoice.tStopRefresh)
    AllTrials.addData('videogameChoice.started', videogameChoice.tStartRefresh)
    AllTrials.addData('videogameChoice.stopped', videogameChoice.tStopRefresh)
    AllTrials.addData('gre.started', gre.tStartRefresh)
    AllTrials.addData('gre.stopped', gre.tStopRefresh)
    AllTrials.addData('gmat.started', gmat.tStartRefresh)
    AllTrials.addData('gmat.stopped', gmat.tStopRefresh)
    AllTrials.addData('lsat.started', lsat.tStartRefresh)
    AllTrials.addData('lsat.stopped', lsat.tStopRefresh)
    AllTrials.addData('mcat.started', mcat.tStartRefresh)
    AllTrials.addData('mcat.stopped', mcat.tStopRefresh)
    AllTrials.addData('game.started', game.tStartRefresh)
    AllTrials.addData('game.stopped', game.tStopRefresh)
    videogameChoice.setColor('white')
    testChoice.setColor('white')
    
    if blank.status == FINISHED:
        choiceQ.setAutoDraw(False)
        testChoice.setAutoDraw(False)
        videogameChoice.setAutoDraw(False)
        gre.setAutoDraw(False)
        gmat.setAutoDraw(False)
        lsat.setAutoDraw(False)
        mcat.setAutoDraw(False)
        continueRoutine = False 
        
    if choiceResp.keys == '1':
        doTestPractice = 1
        doGame = 0
    if choiceResp.keys == '2':
        doTestPractice = 0
        doGame = 1
    AllTrials.addData('blank.started', blank.tStartRefresh)
    AllTrials.addData('blank.stopped', blank.tStopRefresh)
    # the Routine "Choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    QuestionTrials = data.TrialHandler(nReps=doTestPractice, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='QuestionTrials')
    thisExp.addLoop(QuestionTrials)  # add the loop to the experiment
    thisQuestionTrial = QuestionTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisQuestionTrial.rgb)
    if thisQuestionTrial != None:
        for paramName in thisQuestionTrial:
            exec('{} = thisQuestionTrial[paramName]'.format(paramName))
    
    for thisQuestionTrial in QuestionTrials:
        currentLoop = QuestionTrials
        # abbreviate parameter names if possible (e.g. rgb = thisQuestionTrial.rgb)
        if thisQuestionTrial != None:
            for paramName in thisQuestionTrial:
                exec('{} = thisQuestionTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "testQuestionsChoice"-------
        # update component parameters for each repeat
        upDown.keys = []
        upDown.rt = []
        polygon.setOpacity(1)
        polygon.setSize((0.32, 0.13))
        polygon.setOri(0)
        polygon.setLineWidth(8)
        y = 0
        '''
        
        if upDown.keys == '1':
            polygon.setPosition = [0, 0.105]
        elif upDown.keys == '2':
            polygon.setPosition = [0, -0.05]
        elif upDown.keys == '3':
            polygon.setPosition = [0, -0.2]
        elif upDown.keys == '4':
            polygon.setPosition = [0, -0.35]
            '''
        if upDown.keys == '1':
            y = 0.105
        elif upDown.keys == '2':
            y = -0.05
        elif upDown.keys == '3':
            y = -0.2
        elif upDown.keys == '4':
            y = -0.35
        enter.keys = []
        enter.rt = []
        # keep track of which components have finished
        testQuestionsChoiceComponents = [testQChoice, image, image_2, image_3, image_4, upDown, polygon, enter]
        for thisComponent in testQuestionsChoiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        testQuestionsChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "testQuestionsChoice"-------
        while continueRoutine:
            # get current time
            t = testQuestionsChoiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=testQuestionsChoiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *testQChoice* updates
            if testQChoice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                testQChoice.frameNStart = frameN  # exact frame index
                testQChoice.tStart = t  # local t and not account for scr refresh
                testQChoice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testQChoice, 'tStartRefresh')  # time at next scr refresh
                testQChoice.setAutoDraw(True)
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                image_2.setAutoDraw(True)
            
            # *image_3* updates
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                image_3.setAutoDraw(True)
            
            # *image_4* updates
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                image_4.setAutoDraw(True)
            
            # *upDown* updates
            waitOnFlip = False
            if upDown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                upDown.frameNStart = frameN  # exact frame index
                upDown.tStart = t  # local t and not account for scr refresh
                upDown.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(upDown, 'tStartRefresh')  # time at next scr refresh
                upDown.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(upDown.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(upDown.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if upDown.status == STARTED and not waitOnFlip:
                theseKeys = upDown.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    upDown.keys = theseKeys.name  # just the last key pressed
                    upDown.rt = theseKeys.rt
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and upDown.keys == '1' or upDown.keys == '2' or upDown.keys == '3' or upDown.keys == '4':
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:  # only update if drawing
                polygon.setPos([0,y], log=False)
            
            '''
            
            if upDown.keys == '1':
                polygon.setPosition = [0, 0.105]
            elif upDown.keys == '2':
                polygon.setPosition = [0, -0.05]
            elif upDown.keys == '3':
                polygon.setPosition = [0, -0.2]
            elif upDown.keys == '4':
                polygon.setPosition = [0, -0.35]
                '''
            if upDown.keys == '1':
                y = 0.105
            elif upDown.keys == '2':
                y = -0.05
            elif upDown.keys == '3':
                y = -0.2
            elif upDown.keys == '4':
                y = -0.35
            
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
            for thisComponent in testQuestionsChoiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "testQuestionsChoice"-------
        for thisComponent in testQuestionsChoiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        QuestionTrials.addData('testQChoice.started', testQChoice.tStartRefresh)
        QuestionTrials.addData('testQChoice.stopped', testQChoice.tStopRefresh)
        QuestionTrials.addData('image.started', image.tStartRefresh)
        QuestionTrials.addData('image.stopped', image.tStopRefresh)
        QuestionTrials.addData('image_2.started', image_2.tStartRefresh)
        QuestionTrials.addData('image_2.stopped', image_2.tStopRefresh)
        QuestionTrials.addData('image_3.started', image_3.tStartRefresh)
        QuestionTrials.addData('image_3.stopped', image_3.tStopRefresh)
        QuestionTrials.addData('image_4.started', image_4.tStartRefresh)
        QuestionTrials.addData('image_4.stopped', image_4.tStopRefresh)
        # check responses
        if upDown.keys in ['', [], None]:  # No response was made
            upDown.keys = None
        QuestionTrials.addData('upDown.keys',upDown.keys)
        if upDown.keys != None:  # we had a response
            QuestionTrials.addData('upDown.rt', upDown.rt)
        QuestionTrials.addData('upDown.started', upDown.tStartRefresh)
        QuestionTrials.addData('upDown.stopped', upDown.tStopRefresh)
        QuestionTrials.addData('polygon.started', polygon.tStartRefresh)
        QuestionTrials.addData('polygon.stopped', polygon.tStopRefresh)
        # check responses
        if enter.keys in ['', [], None]:  # No response was made
            enter.keys = None
        QuestionTrials.addData('enter.keys',enter.keys)
        if enter.keys != None:  # we had a response
            QuestionTrials.addData('enter.rt', enter.rt)
        QuestionTrials.addData('enter.started', enter.tStartRefresh)
        QuestionTrials.addData('enter.stopped', enter.tStopRefresh)
        # the Routine "testQuestionsChoice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        Questions5 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='Questions5')
        thisExp.addLoop(Questions5)  # add the loop to the experiment
        thisQuestions5 = Questions5.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisQuestions5.rgb)
        if thisQuestions5 != None:
            for paramName in thisQuestions5:
                exec('{} = thisQuestions5[paramName]'.format(paramName))
        
        for thisQuestions5 in Questions5:
            currentLoop = Questions5
            # abbreviate parameter names if possible (e.g. rgb = thisQuestions5.rgb)
            if thisQuestions5 != None:
                for paramName in thisQuestions5:
                    exec('{} = thisQuestions5[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "testQs"-------
            # update component parameters for each repeat
            # keep track of which components have finished
            testQsComponents = []
            for thisComponent in testQsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            testQsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "testQs"-------
            while continueRoutine:
                # get current time
                t = testQsClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=testQsClock)
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
                for thisComponent in testQsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "testQs"-------
            for thisComponent in testQsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "testQs" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'Questions5'
        
        thisExp.nextEntry()
        
    # completed doTestPractice repeats of 'QuestionTrials'
    
    
    # set up handler to look after randomisation of conditions etc
    GameTrials = data.TrialHandler(nReps=doGame, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='GameTrials')
    thisExp.addLoop(GameTrials)  # add the loop to the experiment
    thisGameTrial = GameTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGameTrial.rgb)
    if thisGameTrial != None:
        for paramName in thisGameTrial:
            exec('{} = thisGameTrial[paramName]'.format(paramName))
    
    for thisGameTrial in GameTrials:
        currentLoop = GameTrials
        # abbreviate parameter names if possible (e.g. rgb = thisGameTrial.rgb)
        if thisGameTrial != None:
            for paramName in thisGameTrial:
                exec('{} = thisGameTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Game"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        GameComponents = [text]
        for thisComponent in GameComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        GameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Game"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = GameClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=GameClock)
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
                if tThisFlipGlobal > text.tStartRefresh + 4-frameTolerance:
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
            for thisComponent in GameComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Game"-------
        for thisComponent in GameComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        GameTrials.addData('text.started', text.tStartRefresh)
        GameTrials.addData('text.stopped', text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doGame repeats of 'GameTrials'
    
    thisExp.nextEntry()
    
# completed 5 repeats of 'AllTrials'


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
