#Moral Self Regulation Task

from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os
import sys

from psychopy.hardware import keyboard

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '3.2.0'
expName = 'MoralSR'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='', extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Jojo\\Downloads\\Helion Lab\\Experiment Files\\Moral Self-Regulation\\MoralSR.py',
    savePickle=True, saveWideText=True,dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

endExpNow = False
frameTolerance = 0.001

win = visual.Window(size=(1024, 768), fullscr=True, screen=0, winType='pyglet', allowGUI=True, allowStencil=False, monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, units='height')
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

defaultKeyboard = keyboard.Keyboard()

InstructionsClock = core.Clock()
InstText = visual.TextStim(win=win,text='default',font='Arial', pos=[0,0], height=1.0, wrapWidth=1.6, color='white');
space = keyboard.Keyboard()

CueClock = core.Clock()
cue = visual.TextStim(win=win, text='default',font='Arial', pos=(0, 0), height=0.07, wrapWidth = 1.5, color='white');

PracticeDilemmas_2Clock = core.Clock()
practiceQs = visual.TextStim(win=win, text='default', font='Arial',pos=(0, 0), height=0.06, wrapWidth=1.5,color='white');
space1 = keyboard.Keyboard()

ISIClock = core.Clock()
isi = visual.TextStim(win=win, text='+', font='Arial', pos=(0, 0), height=0.1, wrapWidth=None, color='white');

PracticeAnswersClock = core.Clock()
leftText = visual.TextStim(win=win,text='default',font='Arial', pos=(-0.5, 0.2), height=0.05, wrapWidth=None, color='white');
rightText = visual.TextStim(win=win, text='default',font='Arial', pos=(0.5, 0.2), height=0.05, wrapWidth=None,color='white');
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.4, pos=[0.0, -0.4], low=1, high=7, labels=['Completely Unacceptable', 'Completely Acceptable'], scale='')

isi2Clock = core.Clock()
isi_2 = visual.TextStim(win=win, text='+',font='Arial', pos=(0, 0), height=0.1, color='white');


MainDilemmasClock = core.Clock()
text = visual.TextStim(win=win,text='default',font='Arial',pos=(0, 0), height=0.06, wrapWidth=1.6, color='white');
key_resp_2 = keyboard.Keyboard()

ISIClock = core.Clock()
isi = visual.TextStim(win=win, text='+', font='Arial', pos=(0, 0), height=0.1, color='white');

MainAnswersClock = core.Clock()
leftText1 = visual.TextStim(win=win,text='default',font='Arial', pos=(-0.5, 0.2), height=0.05, wrapWidth=None,color='white');
rightText1 = visual.TextStim(win=win,text='default',font='Arial', pos=(0.5, 0.2), height=0.05, wrapWidth=None, color='white');
rating_2 = visual.RatingScale(win=win, marker='triangle', size=1.4, pos=[0.0, -0.4], low=1, high=7, labels=['"Completely Unacceptable', 'Completely Acceptable"'], tickHeight=-1)

ThankYouClock = core.Clock()
TY = visual.TextStim(win=win,text='Thank you for your participation!\n\nYou have completed this part of the study.', font='Arial', pos=(0, 0), height=0.08, color='white');

globalClock = core.Clock()
routineTimer = core.CountdownTimer()

IntroLoop = data.TrialHandler(nReps=1, method='sequential', extraInfo=expInfo, originPath=-1,trialList=data.importConditions('MoralSelfRegInst.xlsx'),
    seed=None, name='IntroLoop')
thisExp.addLoop(IntroLoop)
thisIntroLoop = IntroLoop.trialList[0]
if thisIntroLoop != None:
    for paramName in thisIntroLoop:
        exec('{} = thisIntroLoop[paramName]'.format(paramName))

for thisIntroLoop in IntroLoop:
    currentLoop = IntroLoop
    if thisIntroLoop != None:
        for paramName in thisIntroLoop:
            exec('{} = thisIntroLoop[paramName]'.format(paramName))
    
    InstText.setColor('white', colorSpace='rgb')
    InstText.setPos((0, 0))
    InstText.setText(Instructions)
    InstText.setFont('Arial')
    InstText.setHeight(0.04)
    space.keys = []
    space.rt = []
    InstructionsComponents = [InstText, space]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionsClock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True
    
    while continueRoutine:
        t = InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if InstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            InstText.frameNStart = frameN
            InstText.tStart = t
            InstText.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(InstText, 'tStartRefresh')
            InstText.setAutoDraw(True)
        
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
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()
    

    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if space.keys in ['', [], None]:
        space.keys = None
    IntroLoop.addData('space.keys',space.keys)
    if space.keys != None:
        IntroLoop.addData('space.rt', space.rt)
    routineTimer.reset()
    thisExp.nextEntry()
    
PracticeLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('moralRows.xlsx'),
    seed=None, name='PracticeLoop')
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

    
    PracticeQs = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('PracticeMoralSelfReg.csv', selection=rows),
        seed=None, name='PracticeQs')
    thisExp.addLoop(PracticeQs)
    thisPracticeQ = PracticeQs.trialList[0]
    if thisPracticeQ != None:
        for paramName in thisPracticeQ:
            exec('{} = thisPracticeQ[paramName]'.format(paramName))
    
    for thisPracticeQ in PracticeQs:
        currentLoop = PracticeQs
        if thisPracticeQ != None:
            for paramName in thisPracticeQ:
                exec('{} = thisPracticeQ[paramName]'.format(paramName))

        practiceQs.setText(PracticeDilemmas)
        space1.keys = []
        space1.rt = []
        PracticeDilemmas_2Components = [practiceQs, space1]
        for thisComponent in PracticeDilemmas_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeDilemmas_2Clock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine:
            t = PracticeDilemmas_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeDilemmas_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            if practiceQs.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                practiceQs.frameNStart = frameN
                practiceQs.tStart = t
                practiceQs.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(practiceQs, 'tStartRefresh')
                practiceQs.setAutoDraw(True)
            
            waitOnFlip = False
            if space1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                space1.frameNStart = frameN
                space1.tStart = t
                space1.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(space1, 'tStartRefresh')
                space1.status = STARTED
                waitOnFlip = True
                win.callOnFlip(space1.clock.reset)
                win.callOnFlip(space1.clearEvents, eventType='keyboard')
            if space1.status == STARTED and not waitOnFlip:
                theseKeys = space1.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]
                    
                    if "escape" == theseKeys:
                        endExpNow = True
                    space1.keys = theseKeys.name
                    space1.rt = theseKeys.rt
                    continueRoutine = False
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in PracticeDilemmas_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            
            if continueRoutine:
                win.flip()
        
        for thisComponent in PracticeDilemmas_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        routineTimer.reset()
        thisExp.nextEntry()
    
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
    ISIClock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            isi.frameNStart = frameN
            isi.tStart = t
            isi.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(isi, 'tStartRefresh')
            isi.setAutoDraw(True)
        if isi.status == STARTED:
            if tThisFlipGlobal > isi.tStartRefresh + 2-frameTolerance:
                isi.tStop = t
                isi.frameNStop = frameN
                win.timeOnFlip(isi, 'tStopRefresh')
                isi.setAutoDraw(False)
        
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()

    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    routineTimer.add(15.000000)
    cue.setText(CueInstructions)
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
            if tThisFlipGlobal > cue.tStartRefresh + 15-frameTolerance:
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
    ISIClock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            isi.frameNStart = frameN
            isi.tStart = t
            isi.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(isi, 'tStartRefresh')
            isi.setAutoDraw(True)
        if isi.status == STARTED:
            if tThisFlipGlobal > isi.tStartRefresh + 2-frameTolerance:
                isi.tStop = t
                isi.frameNStop = frameN
                win.timeOnFlip(isi, 'tStopRefresh')
                isi.setAutoDraw(False)
        
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()

    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    
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
        if thisPracticeA != None:
            for paramName in thisPracticeA:
                exec('{} = thisPracticeA[paramName]'.format(paramName))
        
        leftText.setText(PracticeLeftText)
        rightText.setText(PracticeRightText)
        rating.reset()
        PracticeAnswersComponents = [leftText, rightText, rating]
        for thisComponent in PracticeAnswersComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeAnswersClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine:
            t = PracticeAnswersClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeAnswersClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            
            if leftText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                leftText.frameNStart = frameN
                leftText.tStart = t 
                leftText.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(leftText, 'tStartRefresh')
                leftText.setAutoDraw(True)
            
            if rightText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                rightText.frameNStart = frameN
                rightText.tStart = t
                rightText.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(rightText, 'tStartRefresh')
                rightText.setAutoDraw(True)
            if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
                rating.frameNStart = frameN
                rating.tStart = t
                rating.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(rating, 'tStartRefresh')
                rating.setAutoDraw(True)
            continueRoutine &= rating.noResponse
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in PracticeAnswersComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            
            if continueRoutine:
                win.flip()
        
        for thisComponent in PracticeAnswersComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practiceAs.addData('rating.response', rating.getRating())
        practiceAs.addData('rating.rt', rating.getRT())
        thisExp.nextEntry()
    
    thisExp.nextEntry()

routineTimer.add(10.000000)

isi2Components = [isi_2]
for thisComponent in isi2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
isi2Clock.reset(-_timeToFirstFrame)
frameN = -1
continueRoutine = True

while continueRoutine and routineTimer.getTime() > 0:
    t = isi2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=isi2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    
    if isi_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        isi_2.frameNStart = frameN
        isi_2.tStart = t
        isi_2.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(isi_2, 'tStartRefresh')
        isi_2.setAutoDraw(True)
    if isi_2.status == STARTED:
        if tThisFlipGlobal > isi_2.tStartRefresh + 10-frameTolerance:
            isi_2.tStop = t
            isi_2.frameNStop = frameN
            win.timeOnFlip(isi_2, 'tStopRefresh')
            isi_2.setAutoDraw(False)
    
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in isi2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    
    if continueRoutine:
        win.flip()

for thisComponent in isi2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

MainLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('moralRows2.xlsx'),
    seed=None, name='MainLoop')
thisExp.addLoop(MainLoop)
thisMainLoop = MainLoop.trialList[0]
if thisMainLoop != None:
    for paramName in thisMainLoop:
        exec('{} = thisMainLoop[paramName]'.format(paramName))

for thisMainLoop in MainLoop:
    currentLoop = MainLoop
    if thisMainLoop != None:
        for paramName in thisMainLoop:
            exec('{} = thisMainLoop[paramName]'.format(paramName))
    
    MainQs = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('MoralSelfReg.csv', selection=rows2),
        seed=None, name='MainQs')
    thisExp.addLoop(MainQs)
    thisMainQ = MainQs.trialList[0]
    if thisMainQ != None:
        for paramName in thisMainQ:
            exec('{} = thisMainQ[paramName]'.format(paramName))
    
    for thisMainQ in MainQs:
        currentLoop = MainQs
        if thisMainQ != None:
            for paramName in thisMainQ:
                exec('{} = thisMainQ[paramName]'.format(paramName))

        text.setText(MainDilemmas)
        key_resp_2.keys = []
        key_resp_2.rt = []
        MainDilemmasComponents = [text, key_resp_2]
        for thisComponent in MainDilemmasComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MainDilemmasClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine:
            t = MainDilemmasClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MainDilemmasClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                text.frameNStart = frameN
                text.tStart = t
                text.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(text, 'tStartRefresh')
                text.setAutoDraw(True)
            
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                key_resp_2.frameNStart = frameN
                key_resp_2.tStart = t 
                key_resp_2.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(key_resp_2, 'tStartRefresh')
                key_resp_2.status = STARTED
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]
                    
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp_2.keys = theseKeys.name
                    key_resp_2.rt = theseKeys.rt
                    continueRoutine = False
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in MainDilemmasComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            
            if continueRoutine:
                win.flip()

        for thisComponent in MainDilemmasComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if key_resp_2.keys in ['', [], None]:
            key_resp_2.keys = None
        MainQs.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:
            MainQs.addData('key_resp_2.rt', key_resp_2.rt)

        routineTimer.reset()
        thisExp.nextEntry()
   
    routineTimer.add(2.000000)
    cue.setText(CueInstructions)
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
    ISIClock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            isi.frameNStart = frameN
            isi.tStart = t
            isi.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(isi, 'tStartRefresh')
            isi.setAutoDraw(True)
        if isi.status == STARTED:
            if tThisFlipGlobal > isi.tStartRefresh + 2-frameTolerance:
                isi.tStop = t
                isi.frameNStop = frameN
                win.timeOnFlip(isi, 'tStopRefresh')
                isi.setAutoDraw(False)
        
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        
        if continueRoutine:
            win.flip()

    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    trials_2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('MoralSelfReg.csv', selection=rows2),
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
        
        routineTimer.add(10.000000)
        leftText1.setText(MainLeftText)
        rightText1.setText(MainRightText)
        rating_2.reset()
        MainAnswersComponents = [leftText1, rightText1, rating_2]
        for thisComponent in MainAnswersComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MainAnswersClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine and routineTimer.getTime() > 0:
            t = MainAnswersClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MainAnswersClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1

            if leftText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                leftText1.frameNStart = frameN
                leftText1.tStart = t
                leftText1.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(leftText1, 'tStartRefresh')
                leftText1.setAutoDraw(True)
            if leftText1.status == STARTED:
                if tThisFlip > 10-frameTolerance:
                    leftText1.tStop = t
                    leftText1.frameNStop = frameN
                    win.timeOnFlip(leftText1, 'tStopRefresh')
                    leftText1.setAutoDraw(False)
            
            if rightText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                rightText1.frameNStart = frameN
                rightText1.tStart = t
                rightText1.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(rightText1, 'tStartRefresh')
                rightText1.setAutoDraw(True)
            if rightText1.status == STARTED:
                if tThisFlipGlobal > rightText1.tStartRefresh + 10-frameTolerance:
                    rightText1.tStop = t
                    rightText1.frameNStop = frameN
                    win.timeOnFlip(rightText1, 'tStopRefresh')
                    rightText1.setAutoDraw(False)
            if rating_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                rating_2.frameNStart = frameN
                rating_2.tStart = t
                rating_2.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(rating_2, 'tStartRefresh')
                rating_2.setAutoDraw(True)
            continueRoutine &= rating_2.noResponse
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in MainAnswersComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            
            if continueRoutine:
                win.flip()
        
        for thisComponent in MainAnswersComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('rating_2.response', rating_2.getRating())
        trials_2.addData('rating_2.rt', rating_2.getRT())

        thisExp.nextEntry()

    thisExp.nextEntry()


ThankYouComponents = [TY]
for thisComponent in ThankYouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThankYouClock.reset(-_timeToFirstFrame)
frameN = -1
continueRoutine = True


while continueRoutine:
    t = ThankYouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThankYouClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1

    if TY.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        TY.frameNStart = frameN
        TY.tStart = t
        TY.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(TY, 'tStartRefresh')
        TY.setAutoDraw(True)
    
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    
    if continueRoutine:
        win.flip()

for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
routineTimer.reset()

win.flip()

thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()