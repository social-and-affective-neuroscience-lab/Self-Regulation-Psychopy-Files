#Moral Binary Task

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

psychopyVersion = '3.2.0'
expName = 'MoralSRBinaryChoice'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Jojo\\Downloads\\Helion Lab\\Experiment Files\\Moral Self-Regulation\\MoralSRBinaryChoice.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False
frameTolerance = 0.001

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb', blendMode='avg', useFBO=True, units='height')

expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

defaultKeyboard = keyboard.Keyboard()

InstructionsClock = core.Clock()
InstText = visual.TextStim(win=win, text='default text', font='Arial',
    pos=[0,0], height=1.0, wrapWidth=1.6, color='white');
space = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
isi = visual.TextStim(win=win,text='+',font='Arial', pos=(0, 0), height=0.1, wrapWidth=None, color='white');

# Initialize components for Routine "PracticeDilemmas_2"
PracticeDilemmas_2Clock = core.Clock()
practiceQs = visual.TextStim(win=win, text='default text', font='Arial', pos=(0, 0), height=0.06, wrapWidth=1.6, color='white');
space1 = keyboard.Keyboard()

ISIClock = core.Clock()
isi = visual.TextStim(win=win, text='+',font='Arial',pos=(0, 0), height=0.1, wrapWidth=None, color='white');

# Initialize components for Routine "Cue"
CueClock = core.Clock()
cue = visual.TextStim(win=win, text='default text',
    font='Arial', pos=(0, 0), height=0.065, wrapWidth=1.5, ori=0, 
    color='white');

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
isi = visual.TextStim(win=win, name='isi',
    text='+', font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white');

# Initialize components for Routine "PracticeAnswers"
PracticeAnswersClock = core.Clock()
key_resp = keyboard.Keyboard()
conBlank = visual.TextStim(win=win,  text=None, font='Arial', pos=(0, 0), height=0.1, wrapWidth=None, color='white');
RemText = visual.TextStim(win=win, name='RemText',
    text='default text',
    font='Arial',pos=(0, 0.35), height=0.055, wrapWidth=1.5, ori=0, 
    color='white');
leftText = visual.TextStim(win=win, name='leftText',
    text='default text',
    font='Arial',
    pos=(-0.5, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white');
rightText = visual.TextStim(win=win, name='rightText',
    text='default text',
    font='Arial',
    pos=(0.5, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white');
Yes = visual.TextStim(win=win, name='Yes',
    text='default text', font='Arial',
    pos=(0, -0.24), height=0.05, wrapWidth=2.5, color='white');
No = visual.TextStim(win=win, name='No',
    text='default text',
    font='Arial',
    pos=(0.0, -0.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
Question = visual.TextStim(win=win, name='Question',
    text='default text',
    font='Arial',
    pos=(0, -0.15), height=0.055, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "isi2"
isi2Clock = core.Clock()
isi_2 = visual.TextStim(win=win, name='isi_2',
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
    pos=(0, 0), height=0.06, wrapWidth=1.6, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
isi = visual.TextStim(win=win, name='isi',
    text='+',
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
    pos=(0, 0), height=0.065, wrapWidth=1.5, ori=0, 
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

# Initialize components for Routine "PracticeAnswers"
PracticeAnswersClock = core.Clock()
key_resp = keyboard.Keyboard()
conBlank = visual.TextStim(win=win, name='conBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white');
RemText = visual.TextStim(win=win, name='RemText',
    text='default text',
    font='Arial',
    pos=(0, 0.35), height=0.055, wrapWidth=1.5, ori=0, 
    color='white');
leftText = visual.TextStim(win=win, name='leftText',
    text='default text',
    font='Arial', pos=(-0.5, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white');
rightText = visual.TextStim(win=win, name='rightText',
    text='default text',
    font='Arial',
    pos=(0.5, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white');
Yes = visual.TextStim(win=win, name='Yes',
    text="Implement the plan ('y')",
    font='Arial', pos=(0, -0.27), height=0.05, wrapWidth=2.5, ori=0, 
    color='white');
No = visual.TextStim(win=win, name='No',
    text="Do nothing ('n')",
    font='Arial',
    pos=(0.0, -0.37), height=0.05, wrapWidth=None, ori=0, 
    color='white');
Question = visual.TextStim(win=win, name='Question',
    text='default text',font='Arial',
    pos=(0, -0.15), height=0.055, wrapWidth=None, ori=0, 
    color='white');

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
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, color='white');

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
        trialList=data.importConditions('PracticeMoralSelfReg.csv', selection=rows),
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
        practiceQs.setText(PracticeDilemmas)
        space1.keys = []
        space1.rt = []
        # keep track of which components have finished
        PracticeDilemmas_2Components = [practiceQs, space1]
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
        
    
    # ------Prepare to start Routine "ISI"-------
    routineTimer.add(2.000000)
    ISIComponents = [isi]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    
    # ------Prepare to start Routine "Cue"-------
    routineTimer.add(15.000000)
    # update component parameters for each repeat
    cue.setText(CueInstructions1)
    subID = int(expInfo['participant'])
    
    if subID%2==0:
        cue.setText(CueInstructions1)
    if subID%2==1:
        cue.setText(CueInstructions2)
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
            if tThisFlipGlobal > cue.tStartRefresh + 15-frameTolerance:
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
    
    for thisComponent in CueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeLoop.addData('cue.started', cue.tStartRefresh)
    PracticeLoop.addData('cue.stopped', cue.tStopRefresh)
    
    practiceAs = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('PracticeMoralSelfReg.csv', selection=rows),
        seed=None, name='practiceAs')
    thisExp.addLoop(practiceAs)
    thisPracticeA = practiceAs.trialList[0]
    if thisPracticeA != None:
        for paramName in thisPracticeA:
            exec('{} = thisPracticeA[paramName]'.format(paramName))
    
    for thisPracticeA in practiceAs:
        currentLoop = practiceAs
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeA.rgb)
        if thisPracticeA != None:
            for paramName in thisPracticeA:
                exec('{} = thisPracticeA[paramName]'.format(paramName))
        
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
        
        # ------Prepare to start Routine "PracticeAnswers"-------
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        conBlank.setText('')
        RemText.setText(Reminder)
        leftText.setText(PracticeLeftText)
        rightText.setText(PracticeRightText)
        Question.setText('What do you do?')
        # keep track of which components have finished
        PracticeAnswersComponents = [key_resp, conBlank, RemText, leftText, rightText, Yes, No, Question]
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
            
            # *Question* updates
            if Question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Question.frameNStart = frameN  # exact frame index
                Question.tStart = t  # local t and not account for scr refresh
                Question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Question, 'tStartRefresh')  # time at next scr refresh
                Question.setAutoDraw(True)
            if Question.status == STARTED:
                if bool(conBlank.status == FINISHED):
                    # keep track of stop time/frame for later
                    Question.tStop = t  # not accounting for scr refresh
                    Question.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Question, 'tStopRefresh')  # time at next scr refresh
                    Question.setAutoDraw(False)
            
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
       
        Yes.setColor('white')
        No.setColor('white')
        
        if conBlank.status == FINISHED:
            leftText.setAutoDraw(False)
            rightText.setAutoDraw(False)
            Yes.setAutoDraw(False)
            No.setAutoDraw(False)
            RemText.setAutoDraw(False)
            Question.setAutoDraw(False)
            continueRoutine = False 
        routineTimer.reset()
        thisExp.nextEntry()
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'PracticeLoop'


# ------Prepare to start Routine "isi2"-------
routineTimer.add(10.000000)

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
        if tThisFlipGlobal > isi_2.tStartRefresh + 10-frameTolerance:
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

# set up handler to look after randomisation of conditions etc
MainLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('moralRows2.xlsx'),
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
    
    # set up handler to look after randomisation of conditions etc
    MainQs = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('MoralSelfReg.csv', selection=rows2),
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
        text.setText(MainDilemmas)
        key_resp_2.keys = []
        key_resp_2.rt = []
        # keep track of which components have finished
        MainDilemmasComponents = [text, key_resp_2]
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
    
    # ------Prepare to start Routine "Cue"-------
    routineTimer.add(15.000000)
    # update component parameters for each repeat
    cue.setText(CueInstructions1)
    subID = int(expInfo['participant'])
    
    if subID%2==0:
        cue.setText(CueInstructions1)
    if subID%2==1:
        cue.setText(CueInstructions2)
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
            if tThisFlipGlobal > cue.tStartRefresh + 15-frameTolerance:
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
    MainLoop.addData('cue.started', cue.tStartRefresh)
    MainLoop.addData('cue.stopped', cue.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('MoralSelfReg.csv', selection=rows2),
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
        
        # ------Prepare to start Routine "PracticeAnswers"-------
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        conBlank.setText('')
        RemText.setText(Reminder)
        leftText.setText(PracticeLeftText)
        rightText.setText(PracticeRightText)
        Yes.setText('Implement the plan')
        No.setText('Do nothing')
        Question.setText('What do you do?')
        # keep track of which components have finished
        PracticeAnswersComponents = [key_resp, conBlank, RemText, leftText, rightText, Yes, No, Question]
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
            
            # *Question* updates
            if Question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Question.frameNStart = frameN  # exact frame index
                Question.tStart = t  # local t and not account for scr refresh
                Question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Question, 'tStartRefresh')  # time at next scr refresh
                Question.setAutoDraw(True)
            if Question.status == STARTED:
                if bool(conBlank.status == FINISHED):
                    # keep track of stop time/frame for later
                    Question.tStop = t  # not accounting for scr refresh
                    Question.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Question, 'tStopRefresh')  # time at next scr refresh
                    Question.setAutoDraw(False)
            
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
        trials_2.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials_2.addData('key_resp.rt', key_resp.rt)
        trials_2.addData('key_resp.started', key_resp.tStartRefresh)
        trials_2.addData('key_resp.stopped', key_resp.tStopRefresh)
        trials_2.addData('conBlank.started', conBlank.tStartRefresh)
        trials_2.addData('conBlank.stopped', conBlank.tStopRefresh)
        trials_2.addData('RemText.started', RemText.tStartRefresh)
        trials_2.addData('RemText.stopped', RemText.tStopRefresh)
        trials_2.addData('leftText.started', leftText.tStartRefresh)
        trials_2.addData('leftText.stopped', leftText.tStopRefresh)
        trials_2.addData('rightText.started', rightText.tStartRefresh)
        trials_2.addData('rightText.stopped', rightText.tStopRefresh)
        trials_2.addData('Yes.started', Yes.tStartRefresh)
        trials_2.addData('Yes.stopped', Yes.tStopRefresh)
        trials_2.addData('No.started', No.tStartRefresh)
        trials_2.addData('No.stopped', No.tStopRefresh)
        
        Yes.setColor('white')
        No.setColor('white')
        
        if conBlank.status == FINISHED:
            leftText.setAutoDraw(False)
            rightText.setAutoDraw(False)
            Yes.setAutoDraw(False)
            No.setAutoDraw(False)
            RemText.setAutoDraw(False)
            Question.setAutoDraw(False)
            continueRoutine = False 
        trials_2.addData('Question.started', Question.tStartRefresh)
        trials_2.addData('Question.stopped', Question.tStopRefresh)
        # the Routine "PracticeAnswers" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
    
    
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
