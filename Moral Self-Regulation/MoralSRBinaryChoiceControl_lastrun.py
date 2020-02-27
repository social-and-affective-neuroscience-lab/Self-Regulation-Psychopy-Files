#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on February 27, 2020, at 09:54
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
expName = 'MoralSRBinaryChoice'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\tul00635\\Documents\\GitHub\\Self-Regulation-Psychopy-Files\\Moral Self-Regulation\\MoralSRBinaryChoiceControl_lastrun.py',
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

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstText = visual.TextStim(win=win, name='InstText',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
isi = visual.TextStim(win=win, name='isi',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PracticeDilemmas_2"
PracticeDilemmas_2Clock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.29), size=(0.28, 0.23),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
practiceQs = visual.TextStim(win=win, name='practiceQs',
    text='default text',
    font='Arial',
    pos=(0, -0.07), height=0.04, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
space1 = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
isi = visual.TextStim(win=win, name='isi',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PracticeAnswers"
PracticeAnswersClock = core.Clock()
key_resp = keyboard.Keyboard()
conBlank = visual.TextStim(win=win, name='conBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
leftText = visual.TextStim(win=win, name='leftText',
    text='default text',
    font='Arial',
    pos=(0.41, 0.05), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rightText = visual.TextStim(win=win, name='rightText',
    text='default text',
    font='Arial',
    pos=(0.46, -0.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Yes = visual.TextStim(win=win, name='Yes',
    text='default text',
    font='Arial',
    pos=(0, -0.28), height=0.04, wrapWidth=2.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
No = visual.TextStim(win=win, name='No',
    text='default text',
    font='Arial',
    pos=(0.0, -0.36), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
RemText = visual.TextStim(win=win, name='RemText',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
import numpy
from numpy import random

earnings = 0
earningsStr = "$" + str(earnings)
subID = int(expInfo['participant'])

FiftyGamble = [1,0]
SixtyGamble = [1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]
ThirtyGamble = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]

earning=0
choseCode = []
chanceResult = []

#probability =[]
def gamProbability(GroupProb):
    probs = int(GroupProb)
    if probs == 65:
        probability = SixtyGamble
        print('65% chance')
    if probs == 35:
        probability = ThirtyGamble
        print('35% chance')
    if probs == 50:
        probability = FiftyGamble
        print('50% chance')
def gambleFunc(GroupProb):
    probs = int(GroupProb)
    if probs == 65:
        probability = SixtyGamble
        print('65% chance')
    if probs == 35:
        probability = ThirtyGamble
        print('35% chance')
    if probs == 50:
        probability = FiftyGamble
        print('50% chance')
    result = random.choice(probability)
    print('Chance result:')
    print(result)
sureGroup = visual.TextStim(win=win, name='sureGroup',
    text='default text',
    font='Arial',
    pos=(-0.43, 0.0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
isi = visual.TextStim(win=win, name='isi',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
FeedbackVar = visual.TextStim(win=win, name='FeedbackVar',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
isi = visual.TextStim(win=win, name='isi',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "isi2"
isi2Clock = core.Clock()
isi_2 = visual.TextStim(win=win, name='isi_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "BeginInstr"
BeginInstrClock = core.Clock()
instructions2 = visual.TextStim(win=win, name='instructions2',
    text='You will now begin the main part of the task.\n\nPress SPACE to start!',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
isi = visual.TextStim(win=win, name='isi',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MainDilemmas"
MainDilemmasClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, -0.07), height=0.04, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.29), size=(0.28, 0.23),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
isi = visual.TextStim(win=win, name='isi',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MainAnswers_2"
MainAnswers_2Clock = core.Clock()
key_resp_3 = keyboard.Keyboard()
conBlank2 = visual.TextStim(win=win, name='conBlank2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
RemText2 = visual.TextStim(win=win, name='RemText2',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
leftText2 = visual.TextStim(win=win, name='leftText2',
    text='default text',
    font='Arial',
    pos=(0.41, 0.05), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rightText2 = visual.TextStim(win=win, name='rightText2',
    text='default text',
    font='Arial',
    pos=(0.46, -0.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
yes2 = visual.TextStim(win=win, name='yes2',
    text='default text',
    font='Arial',
    pos=(0, -0.28), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
no2 = visual.TextStim(win=win, name='no2',
    text='default text',
    font='Arial',
    pos=(0.0, -0.36), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
import numpy
from numpy import random

earnings = 0
earningsStr = "$" + str(earnings)
subID = int(expInfo['participant'])

FiftyGamble = [1,0]
SixtyGamble = [1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]
ThirtyGamble = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]

earning=0
choseCode = []
chanceResult = []

#probability =[]
def gamProbability(GroupProb):
    probs = int(GroupProb)
    if probs == 65:
        probability = SixtyGamble
        print('65% chance')
    if probs == 35:
        probability = ThirtyGamble
        print('35% chance')
    if probs == 50:
        probability = FiftyGamble
        print('50% chance')
def gambleFunc(GroupProb):
    probs = int(GroupProb)
    if probs == 65:
        probability = SixtyGamble
        print('65% chance')
    if probs == 35:
        probability = ThirtyGamble
        print('35% chance')
    if probs == 50:
        probability = FiftyGamble
        print('50% chance')
    result = random.choice(probability)
    print('Chance result:')
    print(result)
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=(-0.43, 0.0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
isi = visual.TextStim(win=win, name='isi',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
FeedbackVar = visual.TextStim(win=win, name='FeedbackVar',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
isi = visual.TextStim(win=win, name='isi',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ThankYou"
ThankYouClock = core.Clock()
TY = visual.TextStim(win=win, name='TY',
    text='Thank you for your participation!\n\nYou have completed this part of the study.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
IntroLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('MoralSelfRegInst.xlsx'),
    seed=None, name='IntroLoop')
thisExp.addLoop(IntroLoop)  # add the loop to the experiment
thisIntroLoop = IntroLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIntroLoop.rgb)
if thisIntroLoop != None:
    for paramName in thisIntroLoop:
        exec('{} = thisIntroLoop[paramName]'.format(paramName))

for thisIntroLoop in IntroLoop:
    currentLoop = IntroLoop
    # abbreviate parameter names if possible (e.g. rgb = thisIntroLoop.rgb)
    if thisIntroLoop != None:
        for paramName in thisIntroLoop:
            exec('{} = thisIntroLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions"-------
    # update component parameters for each repeat
    InstText.setColor('white', colorSpace='rgb')
    InstText.setPos((0, 0))
    InstText.setText(Instructions)
    InstText.setFont('Arial')
    InstText.setHeight(0.04)
    space.keys = []
    space.rt = []
    # keep track of which components have finished
    InstructionsComponents = [InstText, space]
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
        
        # *InstText* updates
        if InstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstText.frameNStart = frameN  # exact frame index
            InstText.tStart = t  # local t and not account for scr refresh
            InstText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstText, 'tStartRefresh')  # time at next scr refresh
            InstText.setAutoDraw(True)
        
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
    IntroLoop.addData('InstText.started', InstText.tStartRefresh)
    IntroLoop.addData('InstText.stopped', InstText.tStopRefresh)
    # check responses
    if space.keys in ['', [], None]:  # No response was made
        space.keys = None
    IntroLoop.addData('space.keys',space.keys)
    if space.keys != None:  # we had a response
        IntroLoop.addData('space.rt', space.rt)
    IntroLoop.addData('space.started', space.tStartRefresh)
    IntroLoop.addData('space.stopped', space.tStopRefresh)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'IntroLoop'


# set up handler to look after randomisation of conditions etc
PracticeLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('moralRows.csv'),
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
    
    # ------Prepare to start Routine "ISI"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [isi]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi* updates
        if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isi.frameNStart = frameN  # exact frame index
            isi.tStart = t  # local t and not account for scr refresh
            isi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi, 'tStartRefresh')  # time at next scr refresh
            isi.setAutoDraw(True)
        if isi.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                isi.tStop = t  # not accounting for scr refresh
                isi.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isi, 'tStopRefresh')  # time at next scr refresh
                isi.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeLoop.addData('isi.started', isi.tStartRefresh)
    PracticeLoop.addData('isi.stopped', isi.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    PracticeQs = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('PracticeMoralSelfReg.xlsx', selection='0:5'),
        seed=None, name='PracticeQs')
    thisExp.addLoop(PracticeQs)  # add the loop to the experiment
    thisPracticeQ = PracticeQs.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeQ.rgb)
    if thisPracticeQ != None:
        for paramName in thisPracticeQ:
            exec('{} = thisPracticeQ[paramName]'.format(paramName))
    
    for thisPracticeQ in PracticeQs:
        currentLoop = PracticeQs
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeQ.rgb)
        if thisPracticeQ != None:
            for paramName in thisPracticeQ:
                exec('{} = thisPracticeQ[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "PracticeDilemmas_2"-------
        # update component parameters for each repeat
        image.setImage('skydivers.jpg')
        practiceQs.setText(PracticeDilemmas)
        space1.keys = []
        space1.rt = []
        # keep track of which components have finished
        PracticeDilemmas_2Components = [image, practiceQs, space1]
        for thisComponent in PracticeDilemmas_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeDilemmas_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "PracticeDilemmas_2"-------
        while continueRoutine:
            # get current time
            t = PracticeDilemmas_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeDilemmas_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            
            # *practiceQs* updates
            if practiceQs.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practiceQs.frameNStart = frameN  # exact frame index
                practiceQs.tStart = t  # local t and not account for scr refresh
                practiceQs.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practiceQs, 'tStartRefresh')  # time at next scr refresh
                practiceQs.setAutoDraw(True)
            
            # *space1* updates
            waitOnFlip = False
            if space1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                space1.frameNStart = frameN  # exact frame index
                space1.tStart = t  # local t and not account for scr refresh
                space1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space1, 'tStartRefresh')  # time at next scr refresh
                space1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(space1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(space1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if space1.status == STARTED and not waitOnFlip:
                theseKeys = space1.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    space1.keys = theseKeys.name  # just the last key pressed
                    space1.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeDilemmas_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeDilemmas_2"-------
        for thisComponent in PracticeDilemmas_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        PracticeQs.addData('image.started', image.tStartRefresh)
        PracticeQs.addData('image.stopped', image.tStopRefresh)
        PracticeQs.addData('practiceQs.started', practiceQs.tStartRefresh)
        PracticeQs.addData('practiceQs.stopped', practiceQs.tStopRefresh)
        # check responses
        if space1.keys in ['', [], None]:  # No response was made
            space1.keys = None
        PracticeQs.addData('space1.keys',space1.keys)
        if space1.keys != None:  # we had a response
            PracticeQs.addData('space1.rt', space1.rt)
        PracticeQs.addData('space1.started', space1.tStartRefresh)
        PracticeQs.addData('space1.stopped', space1.tStopRefresh)
        # the Routine "PracticeDilemmas_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'PracticeQs'
    
    
    # ------Prepare to start Routine "ISI"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [isi]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi* updates
        if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isi.frameNStart = frameN  # exact frame index
            isi.tStart = t  # local t and not account for scr refresh
            isi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi, 'tStartRefresh')  # time at next scr refresh
            isi.setAutoDraw(True)
        if isi.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                isi.tStop = t  # not accounting for scr refresh
                isi.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isi, 'tStopRefresh')  # time at next scr refresh
                isi.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeLoop.addData('isi.started', isi.tStartRefresh)
    PracticeLoop.addData('isi.stopped', isi.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    practiceAs = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('PracticeMoralSelfReg.xlsx', selection='0:5'),
        seed=None, name='practiceAs')
    thisExp.addLoop(practiceAs)  # add the loop to the experiment
    thisPracticeA = practiceAs.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeA.rgb)
    if thisPracticeA != None:
        for paramName in thisPracticeA:
            exec('{} = thisPracticeA[paramName]'.format(paramName))
    
    for thisPracticeA in practiceAs:
        currentLoop = practiceAs
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeA.rgb)
        if thisPracticeA != None:
            for paramName in thisPracticeA:
                exec('{} = thisPracticeA[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "PracticeAnswers"-------
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        conBlank.setText('')
        leftText.setText(PracticeLeftText)
        rightText.setText(PracticeRightText)
        Yes.setText("Implement the plan ('y')")
        No.setText("Do nothing ('n')")
        RemText.setText(Reminder)
        sureGroup.setText(sureGroupText)
        # keep track of which components have finished
        PracticeAnswersComponents = [key_resp, conBlank, leftText, rightText, Yes, No, RemText, sureGroup]
        for thisComponent in PracticeAnswersComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeAnswersClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "PracticeAnswers"-------
        while continueRoutine:
            # get current time
            t = PracticeAnswersClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeAnswersClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                theseKeys = key_resp.getKeys(keyList=['y', 'n'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp.keys = theseKeys.name  # just the last key pressed
                    key_resp.rt = theseKeys.rt
            
            # *conBlank* updates
            if conBlank.status == NOT_STARTED and len(key_resp.keys) > 0:
                # keep track of start time/frame for later
                conBlank.frameNStart = frameN  # exact frame index
                conBlank.tStart = t  # local t and not account for scr refresh
                conBlank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(conBlank, 'tStartRefresh')  # time at next scr refresh
                conBlank.setAutoDraw(True)
            if conBlank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > conBlank.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    conBlank.tStop = t  # not accounting for scr refresh
                    conBlank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(conBlank, 'tStopRefresh')  # time at next scr refresh
                    conBlank.setAutoDraw(False)
            
            # *leftText* updates
            if leftText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftText.frameNStart = frameN  # exact frame index
                leftText.tStart = t  # local t and not account for scr refresh
                leftText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftText, 'tStartRefresh')  # time at next scr refresh
                leftText.setAutoDraw(True)
            if leftText.status == STARTED:
                if bool(conBlank.status == FINISHED):
                    # keep track of stop time/frame for later
                    leftText.tStop = t  # not accounting for scr refresh
                    leftText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftText, 'tStopRefresh')  # time at next scr refresh
                    leftText.setAutoDraw(False)
            
            # *rightText* updates
            if rightText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightText.frameNStart = frameN  # exact frame index
                rightText.tStart = t  # local t and not account for scr refresh
                rightText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightText, 'tStartRefresh')  # time at next scr refresh
                rightText.setAutoDraw(True)
            if rightText.status == STARTED:
                if bool(conBlank.status == FINISHED):
                    # keep track of stop time/frame for later
                    rightText.tStop = t  # not accounting for scr refresh
                    rightText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightText, 'tStopRefresh')  # time at next scr refresh
                    rightText.setAutoDraw(False)
            
            # *Yes* updates
            if Yes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Yes.frameNStart = frameN  # exact frame index
                Yes.tStart = t  # local t and not account for scr refresh
                Yes.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Yes, 'tStartRefresh')  # time at next scr refresh
                Yes.setAutoDraw(True)
            if Yes.status == STARTED:
                if bool(conBlank.status == FINISHED):
                    # keep track of stop time/frame for later
                    Yes.tStop = t  # not accounting for scr refresh
                    Yes.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Yes, 'tStopRefresh')  # time at next scr refresh
                    Yes.setAutoDraw(False)
            
            # *No* updates
            if No.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                No.frameNStart = frameN  # exact frame index
                No.tStart = t  # local t and not account for scr refresh
                No.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(No, 'tStartRefresh')  # time at next scr refresh
                No.setAutoDraw(True)
            if No.status == STARTED:
                if bool(conBlank.status == FINISHED):
                    # keep track of stop time/frame for later
                    No.tStop = t  # not accounting for scr refresh
                    No.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(No, 'tStopRefresh')  # time at next scr refresh
                    No.setAutoDraw(False)
            
            # *RemText* updates
            if RemText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RemText.frameNStart = frameN  # exact frame index
                RemText.tStart = t  # local t and not account for scr refresh
                RemText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RemText, 'tStartRefresh')  # time at next scr refresh
                RemText.setAutoDraw(True)
            if RemText.status == STARTED:
                if bool(conBlank.status == FINISHED):
                    # keep track of stop time/frame for later
                    RemText.tStop = t  # not accounting for scr refresh
                    RemText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(RemText, 'tStopRefresh')  # time at next scr refresh
                    RemText.setAutoDraw(False)
            
            if key_resp.keys == 'y':
                Yes.setColor('red')
            if key_resp.keys == 'n':
                No.setColor('red')
                
            #if (key_resp.keys == 'y' or key_resp.keys == 'n') and conBlank.status == NOT_STARTED:
            #    conBlank.tStart = t
            #    conBlank.frameNStart = frameN
            #    conBlank.setAutoDraw(True)
            
            if key_resp.keys == 'y' or key_resp.keys == 'n':
                key_resp.status = FINISHED
            
            # *sureGroup* updates
            if sureGroup.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sureGroup.frameNStart = frameN  # exact frame index
                sureGroup.tStart = t  # local t and not account for scr refresh
                sureGroup.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sureGroup, 'tStartRefresh')  # time at next scr refresh
                sureGroup.setAutoDraw(True)
            if sureGroup.status == STARTED:
                if bool(conBlank.status == FINISHED):
                    # keep track of stop time/frame for later
                    sureGroup.tStop = t  # not accounting for scr refresh
                    sureGroup.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sureGroup, 'tStopRefresh')  # time at next scr refresh
                    sureGroup.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeAnswersComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeAnswers"-------
        for thisComponent in PracticeAnswersComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        practiceAs.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            practiceAs.addData('key_resp.rt', key_resp.rt)
        practiceAs.addData('key_resp.started', key_resp.tStartRefresh)
        practiceAs.addData('key_resp.stopped', key_resp.tStopRefresh)
        practiceAs.addData('conBlank.started', conBlank.tStartRefresh)
        practiceAs.addData('conBlank.stopped', conBlank.tStopRefresh)
        practiceAs.addData('leftText.started', leftText.tStartRefresh)
        practiceAs.addData('leftText.stopped', leftText.tStopRefresh)
        practiceAs.addData('rightText.started', rightText.tStartRefresh)
        practiceAs.addData('rightText.stopped', rightText.tStopRefresh)
        practiceAs.addData('Yes.started', Yes.tStartRefresh)
        practiceAs.addData('Yes.stopped', Yes.tStopRefresh)
        practiceAs.addData('No.started', No.tStartRefresh)
        practiceAs.addData('No.stopped', No.tStopRefresh)
        practiceAs.addData('RemText.started', RemText.tStartRefresh)
        practiceAs.addData('RemText.stopped', RemText.tStopRefresh)
        if key_resp.keys == 'y':
            choseCode = 1
        if key_resp.keys == 'n':
            choseCode = 0
        
        if choseCode == 0 :  
            print('Chose to do nothing, play out the probability ')
            probs = int(GroupProb)
            if probs == 65:
                probability = SixtyGamble
                print('65% gamble')
            if probs == 35:
                probability = ThirtyGamble
                print('35% gamble')
            if probs == 50:
                probability = FiftyGamble
                print('50% gamble')
            result = random.choice(probability)
            print('Chance result:')
            print(result)
            if result == 1:   #win
                print('The group escaped!')
                print(earnings)
                chanceResult = (" were saved.")
            if result == 0: #lose
                print('The group died! :(')
                chanceResult = (' died.')
        
        
        
        Yes.setColor('white')
        No.setColor('white')
        
        if conBlank.status == FINISHED:
            leftText.setAutoDraw(False)
            rightText.setAutoDraw(False)
            Yes.setAutoDraw(False)
            No.setAutoDraw(False)
            sureGroup.setAutoDraw(False)
            RemText.setAutoDraw(False)
        #    Question.setAutoDraw(False)
            continueRoutine = False 
        practiceAs.addData('sureGroup.started', sureGroup.tStartRefresh)
        practiceAs.addData('sureGroup.stopped', sureGroup.tStopRefresh)
        # the Routine "PracticeAnswers" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ISI"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [isi]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *isi* updates
            if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                isi.frameNStart = frameN  # exact frame index
                isi.tStart = t  # local t and not account for scr refresh
                isi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(isi, 'tStartRefresh')  # time at next scr refresh
                isi.setAutoDraw(True)
            if isi.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > isi.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    isi.tStop = t  # not accounting for scr refresh
                    isi.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(isi, 'tStopRefresh')  # time at next scr refresh
                    isi.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practiceAs.addData('isi.started', isi.tStartRefresh)
        practiceAs.addData('isi.stopped', isi.tStopRefresh)
        
        # ------Prepare to start Routine "Feedback"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        FeedbackVar.setColor('white', colorSpace='rgb')
        FeedbackVar.setPos((0, 0))
        FeedbackVar.setText('default')
        FeedbackVar.setFont('Arial')
        FeedbackVar.setHeight(0.07)
        groupNum = int(GroupNumber)
        numPeople = str(groupNum)
        groupResult = str(chanceResult)
        nounStr = str(Noun)
        resultGroup = (numPeople + nounStr + groupResult)
        
        if choseCode == 1:
            FeedbackVar.setText(ChosePlan)
            
        if choseCode == 0:
            FeedbackVar.setText(ChoseNothing + resultGroup)
        # keep track of which components have finished
        FeedbackComponents = [FeedbackVar]
        for thisComponent in FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FeedbackVar* updates
            if FeedbackVar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FeedbackVar.frameNStart = frameN  # exact frame index
                FeedbackVar.tStart = t  # local t and not account for scr refresh
                FeedbackVar.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FeedbackVar, 'tStartRefresh')  # time at next scr refresh
                FeedbackVar.setAutoDraw(True)
            if FeedbackVar.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FeedbackVar.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    FeedbackVar.tStop = t  # not accounting for scr refresh
                    FeedbackVar.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FeedbackVar, 'tStopRefresh')  # time at next scr refresh
                    FeedbackVar.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practiceAs.addData('FeedbackVar.started', FeedbackVar.tStartRefresh)
        practiceAs.addData('FeedbackVar.stopped', FeedbackVar.tStopRefresh)
        
        # ------Prepare to start Routine "ISI"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [isi]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *isi* updates
            if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                isi.frameNStart = frameN  # exact frame index
                isi.tStart = t  # local t and not account for scr refresh
                isi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(isi, 'tStartRefresh')  # time at next scr refresh
                isi.setAutoDraw(True)
            if isi.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > isi.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    isi.tStop = t  # not accounting for scr refresh
                    isi.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(isi, 'tStopRefresh')  # time at next scr refresh
                    isi.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practiceAs.addData('isi.started', isi.tStartRefresh)
        practiceAs.addData('isi.stopped', isi.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'practiceAs'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'PracticeLoop'


# ------Prepare to start Routine "isi2"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
isi2Components = [isi_2]
for thisComponent in isi2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
isi2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "isi2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = isi2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=isi2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *isi_2* updates
    if isi_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        isi_2.frameNStart = frameN  # exact frame index
        isi_2.tStart = t  # local t and not account for scr refresh
        isi_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(isi_2, 'tStartRefresh')  # time at next scr refresh
        isi_2.setAutoDraw(True)
    if isi_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > isi_2.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            isi_2.tStop = t  # not accounting for scr refresh
            isi_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(isi_2, 'tStopRefresh')  # time at next scr refresh
            isi_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in isi2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "isi2"-------
for thisComponent in isi2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('isi_2.started', isi_2.tStartRefresh)
thisExp.addData('isi_2.stopped', isi_2.tStopRefresh)

# ------Prepare to start Routine "BeginInstr"-------
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
# keep track of which components have finished
BeginInstrComponents = [instructions2, key_resp_4]
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
    
    # *instructions2* updates
    if instructions2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions2.frameNStart = frameN  # exact frame index
        instructions2.tStart = t  # local t and not account for scr refresh
        instructions2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2, 'tStartRefresh')  # time at next scr refresh
        instructions2.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_4.keys = theseKeys.name  # just the last key pressed
            key_resp_4.rt = theseKeys.rt
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
thisExp.addData('instructions2.started', instructions2.tStartRefresh)
thisExp.addData('instructions2.stopped', instructions2.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "BeginInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
MainLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('moralRows2.csv'),
    seed=None, name='MainLoop')
thisExp.addLoop(MainLoop)  # add the loop to the experiment
thisMainLoop = MainLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
if thisMainLoop != None:
    for paramName in thisMainLoop:
        exec('{} = thisMainLoop[paramName]'.format(paramName))

for thisMainLoop in MainLoop:
    currentLoop = MainLoop
    # abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
    if thisMainLoop != None:
        for paramName in thisMainLoop:
            exec('{} = thisMainLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ISI"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [isi]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi* updates
        if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isi.frameNStart = frameN  # exact frame index
            isi.tStart = t  # local t and not account for scr refresh
            isi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi, 'tStartRefresh')  # time at next scr refresh
            isi.setAutoDraw(True)
        if isi.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                isi.tStop = t  # not accounting for scr refresh
                isi.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isi, 'tStopRefresh')  # time at next scr refresh
                isi.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    MainLoop.addData('isi.started', isi.tStartRefresh)
    MainLoop.addData('isi.stopped', isi.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    MainQs = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('PracticeMoralSelfReg.xlsx', selection=rows2),
        seed=None, name='MainQs')
    thisExp.addLoop(MainQs)  # add the loop to the experiment
    thisMainQ = MainQs.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMainQ.rgb)
    if thisMainQ != None:
        for paramName in thisMainQ:
            exec('{} = thisMainQ[paramName]'.format(paramName))
    
    for thisMainQ in MainQs:
        currentLoop = MainQs
        # abbreviate parameter names if possible (e.g. rgb = thisMainQ.rgb)
        if thisMainQ != None:
            for paramName in thisMainQ:
                exec('{} = thisMainQ[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "MainDilemmas"-------
        # update component parameters for each repeat
        text.setText(PracticeDilemmas)
        key_resp_2.keys = []
        key_resp_2.rt = []
        image_2.setImage(MainPicture)
        # keep track of which components have finished
        MainDilemmasComponents = [text, key_resp_2, image_2]
        for thisComponent in MainDilemmasComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MainDilemmasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "MainDilemmas"-------
        while continueRoutine:
            # get current time
            t = MainDilemmasClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MainDilemmasClock)
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
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                image_2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MainDilemmasComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MainDilemmas"-------
        for thisComponent in MainDilemmasComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        MainQs.addData('text.started', text.tStartRefresh)
        MainQs.addData('text.stopped', text.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        MainQs.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            MainQs.addData('key_resp_2.rt', key_resp_2.rt)
        MainQs.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        MainQs.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        MainQs.addData('image_2.started', image_2.tStartRefresh)
        MainQs.addData('image_2.stopped', image_2.tStopRefresh)
        # the Routine "MainDilemmas" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'MainQs'
    
    
    # ------Prepare to start Routine "ISI"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [isi]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi* updates
        if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isi.frameNStart = frameN  # exact frame index
            isi.tStart = t  # local t and not account for scr refresh
            isi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi, 'tStartRefresh')  # time at next scr refresh
            isi.setAutoDraw(True)
        if isi.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                isi.tStop = t  # not accounting for scr refresh
                isi.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isi, 'tStopRefresh')  # time at next scr refresh
                isi.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    MainLoop.addData('isi.started', isi.tStartRefresh)
    MainLoop.addData('isi.stopped', isi.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('PracticeMoralSelfReg.xlsx', selection=rows2),
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
        
        # ------Prepare to start Routine "MainAnswers_2"-------
        # update component parameters for each repeat
        key_resp_3.keys = []
        key_resp_3.rt = []
        conBlank2.setText('')
        RemText2.setText(Reminder)
        leftText2.setText(PracticeLeftText)
        rightText2.setText(PracticeRightText)
        yes2.setText("Implement the plan ('y')")
        no2.setText("Do nothing ('n')")
        text_2.setText(sureGroupText)
        # keep track of which components have finished
        MainAnswers_2Components = [key_resp_3, conBlank2, RemText2, leftText2, rightText2, yes2, no2, text_2]
        for thisComponent in MainAnswers_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MainAnswers_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "MainAnswers_2"-------
        while continueRoutine:
            # get current time
            t = MainAnswers_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MainAnswers_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['y', 'n'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp_3.keys = theseKeys.name  # just the last key pressed
                    key_resp_3.rt = theseKeys.rt
            
            # *conBlank2* updates
            if conBlank2.status == NOT_STARTED and len(key_resp_3.keys) > 0:
                # keep track of start time/frame for later
                conBlank2.frameNStart = frameN  # exact frame index
                conBlank2.tStart = t  # local t and not account for scr refresh
                conBlank2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(conBlank2, 'tStartRefresh')  # time at next scr refresh
                conBlank2.setAutoDraw(True)
            if conBlank2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > conBlank2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    conBlank2.tStop = t  # not accounting for scr refresh
                    conBlank2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(conBlank2, 'tStopRefresh')  # time at next scr refresh
                    conBlank2.setAutoDraw(False)
            
            # *RemText2* updates
            if RemText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RemText2.frameNStart = frameN  # exact frame index
                RemText2.tStart = t  # local t and not account for scr refresh
                RemText2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RemText2, 'tStartRefresh')  # time at next scr refresh
                RemText2.setAutoDraw(True)
            if RemText2.status == STARTED:
                if bool(conBlank2.status == FINISHED):
                    # keep track of stop time/frame for later
                    RemText2.tStop = t  # not accounting for scr refresh
                    RemText2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(RemText2, 'tStopRefresh')  # time at next scr refresh
                    RemText2.setAutoDraw(False)
            
            # *leftText2* updates
            if leftText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftText2.frameNStart = frameN  # exact frame index
                leftText2.tStart = t  # local t and not account for scr refresh
                leftText2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftText2, 'tStartRefresh')  # time at next scr refresh
                leftText2.setAutoDraw(True)
            if leftText2.status == STARTED:
                if bool(conBlank2.status == FINISHED):
                    # keep track of stop time/frame for later
                    leftText2.tStop = t  # not accounting for scr refresh
                    leftText2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftText2, 'tStopRefresh')  # time at next scr refresh
                    leftText2.setAutoDraw(False)
            
            # *rightText2* updates
            if rightText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightText2.frameNStart = frameN  # exact frame index
                rightText2.tStart = t  # local t and not account for scr refresh
                rightText2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightText2, 'tStartRefresh')  # time at next scr refresh
                rightText2.setAutoDraw(True)
            if rightText2.status == STARTED:
                if bool(conBlank2.status == FINISHED):
                    # keep track of stop time/frame for later
                    rightText2.tStop = t  # not accounting for scr refresh
                    rightText2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightText2, 'tStopRefresh')  # time at next scr refresh
                    rightText2.setAutoDraw(False)
            
            # *yes2* updates
            if yes2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                yes2.frameNStart = frameN  # exact frame index
                yes2.tStart = t  # local t and not account for scr refresh
                yes2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(yes2, 'tStartRefresh')  # time at next scr refresh
                yes2.setAutoDraw(True)
            if yes2.status == STARTED:
                if bool(conBlank2.status == FINISHED):
                    # keep track of stop time/frame for later
                    yes2.tStop = t  # not accounting for scr refresh
                    yes2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(yes2, 'tStopRefresh')  # time at next scr refresh
                    yes2.setAutoDraw(False)
            
            # *no2* updates
            if no2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                no2.frameNStart = frameN  # exact frame index
                no2.tStart = t  # local t and not account for scr refresh
                no2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no2, 'tStartRefresh')  # time at next scr refresh
                no2.setAutoDraw(True)
            if no2.status == STARTED:
                if bool(conBlank2.status == FINISHED):
                    # keep track of stop time/frame for later
                    no2.tStop = t  # not accounting for scr refresh
                    no2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(no2, 'tStopRefresh')  # time at next scr refresh
                    no2.setAutoDraw(False)
            
            if key_resp_3.keys == 'y':
                yes2.setColor('red')
            if key_resp_3.keys == 'n':
                no2.setColor('red')
                
            #if (key_resp.keys == 'y' or key_resp.keys == 'n') and conBlank.status == NOT_STARTED:
            #    conBlank.tStart = t
            #    conBlank.frameNStart = frameN
            #    conBlank.setAutoDraw(True)
            
            if key_resp_3.keys == 'y' or key_resp_3.keys == 'n':
                key_resp_3.status = FINISHED
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            if text_2.status == STARTED:
                if bool(conBlank2.status == FINISHED):
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
            for thisComponent in MainAnswers_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MainAnswers_2"-------
        for thisComponent in MainAnswers_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trials_2.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials_2.addData('key_resp_3.rt', key_resp_3.rt)
        trials_2.addData('key_resp_3.started', key_resp_3.tStartRefresh)
        trials_2.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
        trials_2.addData('conBlank2.started', conBlank2.tStartRefresh)
        trials_2.addData('conBlank2.stopped', conBlank2.tStopRefresh)
        trials_2.addData('RemText2.started', RemText2.tStartRefresh)
        trials_2.addData('RemText2.stopped', RemText2.tStopRefresh)
        trials_2.addData('leftText2.started', leftText2.tStartRefresh)
        trials_2.addData('leftText2.stopped', leftText2.tStopRefresh)
        trials_2.addData('rightText2.started', rightText2.tStartRefresh)
        trials_2.addData('rightText2.stopped', rightText2.tStopRefresh)
        trials_2.addData('yes2.started', yes2.tStartRefresh)
        trials_2.addData('yes2.stopped', yes2.tStopRefresh)
        trials_2.addData('no2.started', no2.tStartRefresh)
        trials_2.addData('no2.stopped', no2.tStopRefresh)
        if key_resp_3.keys == 'y':
            choseCode = 1
        if key_resp_3.keys == 'n':
            choseCode = 0
        
        if choseCode == 0 :  
            print('Chose to do nothing, play out the probability ')
            probs = int(GroupProb)
            if probs == 65:
                probability = SixtyGamble
                print('65% gamble')
            if probs == 35:
                probability = ThirtyGamble
                print('35% gamble')
            if probs == 50:
                probability = FiftyGamble
                print('50% gamble')
            result = random.choice(probability)
            print('Chance result:')
            print(result)
            if result == 1:   #win
                print('The group escaped!')
                print(earnings)
                chanceResult = (" were saved.")
            if result == 0: #lose
                print('The group died! :(')
                chanceResult = (' died.')
        
        
        
        yes2.setColor('white')
        no2.setColor('white')
        
        if conBlank2.status == FINISHED:
            leftText2.setAutoDraw(False)
            rightText2.setAutoDraw(False)
            yes2.setAutoDraw(False)
            no2.setAutoDraw(False)
            text_2.setAutoDraw(False)
            RemText2.setAutoDraw(False)
            #Question2.setAutoDraw(False)
            continueRoutine = False 
        trials_2.addData('text_2.started', text_2.tStartRefresh)
        trials_2.addData('text_2.stopped', text_2.tStopRefresh)
        # the Routine "MainAnswers_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ISI"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [isi]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *isi* updates
            if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                isi.frameNStart = frameN  # exact frame index
                isi.tStart = t  # local t and not account for scr refresh
                isi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(isi, 'tStartRefresh')  # time at next scr refresh
                isi.setAutoDraw(True)
            if isi.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > isi.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    isi.tStop = t  # not accounting for scr refresh
                    isi.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(isi, 'tStopRefresh')  # time at next scr refresh
                    isi.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('isi.started', isi.tStartRefresh)
        trials_2.addData('isi.stopped', isi.tStopRefresh)
        
        # ------Prepare to start Routine "Feedback"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        FeedbackVar.setColor('white', colorSpace='rgb')
        FeedbackVar.setPos((0, 0))
        FeedbackVar.setText('default')
        FeedbackVar.setFont('Arial')
        FeedbackVar.setHeight(0.07)
        groupNum = int(GroupNumber)
        numPeople = str(groupNum)
        groupResult = str(chanceResult)
        nounStr = str(Noun)
        resultGroup = (numPeople + nounStr + groupResult)
        
        if choseCode == 1:
            FeedbackVar.setText(ChosePlan)
            
        if choseCode == 0:
            FeedbackVar.setText(ChoseNothing + resultGroup)
        # keep track of which components have finished
        FeedbackComponents = [FeedbackVar]
        for thisComponent in FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FeedbackVar* updates
            if FeedbackVar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FeedbackVar.frameNStart = frameN  # exact frame index
                FeedbackVar.tStart = t  # local t and not account for scr refresh
                FeedbackVar.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FeedbackVar, 'tStartRefresh')  # time at next scr refresh
                FeedbackVar.setAutoDraw(True)
            if FeedbackVar.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FeedbackVar.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    FeedbackVar.tStop = t  # not accounting for scr refresh
                    FeedbackVar.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FeedbackVar, 'tStopRefresh')  # time at next scr refresh
                    FeedbackVar.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('FeedbackVar.started', FeedbackVar.tStartRefresh)
        trials_2.addData('FeedbackVar.stopped', FeedbackVar.tStopRefresh)
        
        # ------Prepare to start Routine "ISI"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [isi]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *isi* updates
            if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                isi.frameNStart = frameN  # exact frame index
                isi.tStart = t  # local t and not account for scr refresh
                isi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(isi, 'tStartRefresh')  # time at next scr refresh
                isi.setAutoDraw(True)
            if isi.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > isi.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    isi.tStop = t  # not accounting for scr refresh
                    isi.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(isi, 'tStopRefresh')  # time at next scr refresh
                    isi.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('isi.started', isi.tStartRefresh)
        trials_2.addData('isi.stopped', isi.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'MainLoop'


# ------Prepare to start Routine "ThankYou"-------
# update component parameters for each repeat
# keep track of which components have finished
ThankYouComponents = [TY]
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
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TY* updates
    if TY.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TY.frameNStart = frameN  # exact frame index
        TY.tStart = t  # local t and not account for scr refresh
        TY.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TY, 'tStartRefresh')  # time at next scr refresh
        TY.setAutoDraw(True)
    
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
thisExp.addData('TY.started', TY.tStartRefresh)
thisExp.addData('TY.stopped', TY.tStopRefresh)
# the Routine "ThankYou" was not non-slip safe, so reset the non-slip timer
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
