#Emotion Regulation Task

from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os
import sys

from psychopy.hardware import keyboard

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '3.2.0'
expName = 'EmotRegPavlovia'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='', extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Jojo\\Downloads\\Helion Lab\\Experiment Files\\Emotion Regulation\\EmotRegPavlovia.py',
    savePickle=True, saveWideText=True, dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

endExpNow = False
frameTolerance = 0.001


win = visual.Window( size=(1024, 768), fullscr=True, screen=0, winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb', blendMode='avg', useFBO=True, units='height')
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

defaultKeyboard = keyboard.Keyboard()

introClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='In this part of the study you will be given a regulation strategy to use while viewing various pictures.\n\nThen you will use a rating scale to categorize your emotions.\n\nYou will first be completing a few practice rounds.\n\nWhen you are ready, press space to start!',
    font='Arial',pos=(0, 0), height=0.07, wrapWidth=1.5, color='white');
space = keyboard.Keyboard()

isiClock = core.Clock()
Iti = visual.TextStim(win=win, text='default',font='Arial', pos=(0, 0), height=0.1, color='white');

BeginInstrClock = core.Clock()
text = visual.TextStim(win=win, text='You will now complete the full task. \n\nPress space to begin!', font='Arial', pos=(0, 0), height=0.08, wrapWidth=1.5,color='white');

CueClock = core.Clock()
cue = visual.TextStim(win=win, text='default', font='Arial', pos=(0, 0), height=0.1, color='white');
ISI = visual.TextStim(win=win, text='default',font='Arial', pos=(0, 0), height=0.1, color='white');

PicClock = core.Clock()
Image = visual.ImageStim(win=win,image='sin',pos=(0, 0), size=1.0, color=[1,1,1], texRes=128, interpolate=True)

ratingsClock = core.Clock()
ratingQ = visual.TextStim(win=win, text='default',font='Arial', pos=(0, 0.1), height=0.07, wrapWidth=1.5, color='white');
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.4, pos=[0.0, -0.4], low=1, high=7, labels=['Very negative', ' Very positive'], scale='')

globalClock = core.Clock()
routineTimer = core.CountdownTimer()


space.keys = []
space.rt = []
introComponents = [Instructions, space]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)
frameN = -1
continueRoutine = True

while continueRoutine:
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
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
    
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    
    if continueRoutine:
        win.flip()

for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.nextEntry()
routineTimer.reset()

practiceLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('EmotionRegCues.csv', selection='0'),
    seed=None, name='practiceLoop')
thisExp.addLoop(practiceLoop)
thisPracticeLoop = practiceLoop.trialList[0]
if thisPracticeLoop != None:
    for paramName in thisPracticeLoop:
        exec('{} = thisPracticeLoop[paramName]'.format(paramName))

for thisPracticeLoop in practiceLoop:
    currentLoop = practiceLoop
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            exec('{} = thisPracticeLoop[paramName]'.format(paramName))
    
    routineTimer.add(4.000000)
    cue.setText(CueType)
    ISI.setText('+')
    CueComponents = [cue, ISI]
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
        
        if ISI.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            ISI.frameNStart = frameN
            ISI.tStart = t
            ISI.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(ISI, 'tStartRefresh')
            ISI.setAutoDraw(True)
        if ISI.status == STARTED:
            if tThisFlipGlobal > ISI.tStartRefresh + 2-frameTolerance:
                ISI.tStop = t
                ISI.frameNStop = frameN
                win.timeOnFlip(ISI, 'tStopRefresh')
                ISI.setAutoDraw(False)
        
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
    
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('EmotionReg.csv', selection='0:3'),
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
        
        routineTimer.add(8.000000)
        Image.setSize((1.5, 1))
        Image.setImage(Picture)
        PicComponents = [Image]
        for thisComponent in PicComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PicClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine and routineTimer.getTime() > 0:
            t = PicClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PicClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            
            if Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                Image.frameNStart = frameN
                Image.tStart = t
                Image.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(Image, 'tStartRefresh')
                Image.setAutoDraw(True)
            if Image.status == STARTED:
                if tThisFlipGlobal > Image.tStartRefresh + 8-frameTolerance:
                    Image.tStop = t
                    Image.frameNStop = frameN
                    win.timeOnFlip(Image, 'tStopRefresh')
                    Image.setAutoDraw(False)
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in PicComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            
            if continueRoutine:
                win.flip()

        for thisComponent in PicComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        routineTimer.add(3.000000)
        ratingQ.setText('How would you characterize your feelings at the present moment?')
        rating.reset()
        ratingsComponents = [ratingQ, rating]
        for thisComponent in ratingsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ratingsClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine and routineTimer.getTime() > 0:
            t = ratingsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ratingsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            
            if ratingQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                ratingQ.frameNStart = frameN
                ratingQ.tStart = t
                ratingQ.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(ratingQ, 'tStartRefresh')
                ratingQ.setAutoDraw(True)
            if ratingQ.status == STARTED:
                if tThisFlip > 3-frameTolerance:
                    ratingQ.tStop = t
                    ratingQ.frameNStop = frameN
                    win.timeOnFlip(ratingQ, 'tStopRefresh')
                    ratingQ.setAutoDraw(False)
            if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
                rating.frameNStart = frameN
                rating.tStart = t
                rating.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(rating, 'tStartRefresh')
                rating.setAutoDraw(True)
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in ratingsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            
            if continueRoutine:
                win.flip()

        for thisComponent in ratingsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('rating.response', rating.getRating())
        trials.addData('rating.rt', rating.getRT())

        
        routineTimer.add(2.000000)
        Iti.setText('+')
        isiComponents = [Iti]
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
            if Iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                Iti.frameNStart = frameN
                Iti.tStart = t
                Iti.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(Iti, 'tStartRefresh')
                Iti.setAutoDraw(True)
            if Iti.status == STARTED:
                if tThisFlipGlobal > Iti.tStartRefresh + 2-frameTolerance:
                    Iti.tStop = t
                    Iti.frameNStop = frameN
                    win.timeOnFlip(Iti, 'tStopRefresh')
                    Iti.setAutoDraw(False)
            
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
        thisExp.nextEntry()
        
    
    thisExp.nextEntry()

routineTimer.add(2.500000)

BeginInstrComponents = [text]
for thisComponent in BeginInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
spacebar = event.BuilderKeyResponse()
BeginInstrClock.reset(-_timeToFirstFrame)
frameN = -1
continueRoutine = True

for thisComponent in BeginInstrComponents:
   if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
while continueRoutine:
    t = BeginInstrClock.getTime()
    frameN = frameN + 1
        
    if t >= 0.0 and text.status == NOT_STARTED:
        text.tStart = t
        text.frameNStart = frameN
        text.setAutoDraw(True)
        
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
    for thisComponent in BeginInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break 
        
    if continueRoutine:
        win.flip()

for thisComponent in BeginInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('EmotionRegCues.csv', selection='0:5'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)
thisTrial_2 = trials_2.trialList[0]
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    routineTimer.add(4.000000)
    cue.setText(CueType)
    ISI.setText('+')
    CueComponents = [cue, ISI]
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
        
        if ISI.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            ISI.frameNStart = frameN
            ISI.tStart = t
            ISI.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(ISI, 'tStartRefresh')
            ISI.setAutoDraw(True)
        if ISI.status == STARTED:
            if tThisFlipGlobal > ISI.tStartRefresh + 2-frameTolerance:
                ISI.tStop = t
                ISI.frameNStop = frameN
                win.timeOnFlip(ISI, 'tStopRefresh')
                ISI.setAutoDraw(False)
        
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
    
    mainTrials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('EmotionReg.csv', selection=rows),
        seed=None, name='mainTrials')
    thisExp.addLoop(mainTrials)
    thisMainTrial = mainTrials.trialList[0]
    if thisMainTrial != None:
        for paramName in thisMainTrial:
            exec('{} = thisMainTrial[paramName]'.format(paramName))
    
    for thisMainTrial in mainTrials:
        currentLoop = mainTrials
        if thisMainTrial != None:
            for paramName in thisMainTrial:
                exec('{} = thisMainTrial[paramName]'.format(paramName))
        
        routineTimer.add(8.000000)
        Image.setSize((1.5, 1))
        Image.setImage(Picture)
        PicComponents = [Image]
        for thisComponent in PicComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PicClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine and routineTimer.getTime() > 0:
            t = PicClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PicClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            
            if Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                Image.frameNStart = frameN
                Image.tStart = t
                Image.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(Image, 'tStartRefresh')
                Image.setAutoDraw(True)
            if Image.status == STARTED:
                if tThisFlipGlobal > Image.tStartRefresh + 8-frameTolerance:
                    Image.tStop = t
                    Image.frameNStop = frameN
                    win.timeOnFlip(Image, 'tStopRefresh')
                    Image.setAutoDraw(False)
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in PicComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break

            if continueRoutine:
                win.flip()

        for thisComponent in PicComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        routineTimer.add(3.000000)
        ratingQ.setText('How would you characterize your feelings at the present moment?')
        rating.reset()
        ratingsComponents = [ratingQ, rating]
        for thisComponent in ratingsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ratingsClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine and routineTimer.getTime() > 0:
            t = ratingsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ratingsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            
            if ratingQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                ratingQ.frameNStart = frameN
                ratingQ.tStart = t
                ratingQ.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(ratingQ, 'tStartRefresh')
                ratingQ.setAutoDraw(True)
            if ratingQ.status == STARTED:
                if tThisFlip > 3-frameTolerance:
                    ratingQ.tStop = t
                    ratingQ.frameNStop = frameN
                    win.timeOnFlip(ratingQ, 'tStopRefresh')
                    ratingQ.setAutoDraw(False)
            if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
                rating.frameNStart = frameN
                rating.tStart = t
                rating.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(rating, 'tStartRefresh')
                rating.setAutoDraw(True)
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in ratingsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            
            if continueRoutine:
                win.flip()
        
        for thisComponent in ratingsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        mainTrials.addData('rating.response', rating.getRating())
        mainTrials.addData('rating.rt', rating.getRT())
        thisExp.nextEntry()
    
    thisExp.nextEntry()

win.flip()

thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()
