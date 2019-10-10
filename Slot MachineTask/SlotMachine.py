#slot machine game

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
expName = 'slotgame'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Jojo\\Downloads\\Helion Lab\\Experiment Files\\Slot MachineTask\\SlotMachine.py', savePickle=True, saveWideText=True,dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

endExpNow = False
frameTolerance = 0.001

win = visual.Window(size=(1024, 768), fullscr=True, screen=0, winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',blendMode='avg', useFBO=True, units='height')

expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

defaultKeyboard = keyboard.Keyboard()

Inst1 = visual.TextStim(win=win, name='Inst1', text='In this part of the study, you will be making a series of monetary decisions.\n\nYou will have the choice between taking a gamble,  which will be shown on the left ' +
    'side of the screen, or choosing a sure option, which will be on the right side of the screen. \n\nFor each gamble, you will have a 50% chance of winning money, while the sure option guarantees payoff. \n\nPress space to continue. ',
    font='Arial', pos=(0, 0), height=0.06, wrapWidth=1.5, color='white');

inst2 = visual.TextStim(win=win, text='default', font='Arial',pos=(0, 0), height=0.06, wrapWidth=1.6,color='white');
text = visual.TextStim(win=win, text='default',font='Arial',pos=(0, 0), height=0.1, color='white');
gambleAmt = visual.TextStim(win=win, text='default',font='Arial',pos=(-0.4, -0.15), height=0.09, color='white');
sureAmt = visual.TextStim(win=win, text='default',font='Arial', pos=(0.4, -0.15), height=0.09, color='white');
sureTex = visual.TextStim(win=win,text='default', font='Arial', pos=(0.4, 0.28), height=0.07,color='black');
gambleText = visual.TextStim(win=win,text='default text', font='Arial', pos=(-0.4, 0.28), height=0.07, color='black');
blank = visual.TextStim(win=win, text=None, font='Arial', pos=(0, 0), color='white');

enter = keyboard.Keyboard()
space = keyboard.Keyboard()
choice = keyboard.Keyboard()

decisionsClock = core.Clock()
instructions_2Clock = core.Clock()
cueClock = core.Clock()
ins1Clock = core.Clock()

globalClock = core.Clock()
routineTimer = core.CountdownTimer()

trials = data.TrialHandler(nReps=1, method='random', extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SlotMachine.xlsx'),seed=None)
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

    space.keys = []
    space.rt = []

    ins1Components = [Inst1, space]
    for thisComponent in ins1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ins1Clock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True
    
    while continueRoutine:
        t = ins1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ins1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if Inst1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            Inst1.frameNStart = frameN
            Inst1.tStart = t
            Inst1.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(Inst1, 'tStartRefresh')
            Inst1.setAutoDraw(True)
        
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
        for thisComponent in ins1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        
        if continueRoutine:
            win.flip()
    
    for thisComponent in ins1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Inst1.started', Inst1.tStartRefresh)
    trials.addData('Inst1.stopped', Inst1.tStopRefresh)
    if space.keys in ['', [], None]:
        space.keys = None
    trials.addData('space.keys',space.keys)
    if space.keys != None:
        trials.addData('space.rt', space.rt)
    trials.addData('space.started', space.tStartRefresh)
    trials.addData('space.stopped', space.tStopRefresh)
    routineTimer.reset()
    
    inst2.setText('Before each decision, you will be given a regulation strategy to use.\n\nYou will have three seconds to make your choice upon seeing the options. \n\nTo choose the gamble, press "1". To choose the sure option, press "2". '+
        '\n\nTo begin, press enter!')
    enter.keys = []
    enter.rt = []
    instructions_2Components = [inst2, enter]
    for thisComponent in instructions_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_2Clock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True
    
    while continueRoutine:
        t = instructions_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if inst2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            inst2.frameNStart = frameN
            inst2.tStart = t
            inst2.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(inst2, 'tStartRefresh')
            inst2.setAutoDraw(True)
        
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
        for thisComponent in instructions_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        
        if continueRoutine:
            win.flip()
    
    for thisComponent in instructions_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('inst2.started', inst2.tStartRefresh)
    trials.addData('inst2.stopped', inst2.tStopRefresh)
    if enter.keys in ['', [], None]:
        enter.keys = None
    trials.addData('enter.keys',enter.keys)
    if enter.keys != None:
        trials.addData('enter.rt', enter.rt)
    trials.addData('enter.started', enter.tStartRefresh)
    trials.addData('enter.stopped', enter.tStopRefresh)
    routineTimer.reset()
    
    decLoop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('SlotMachine.xlsx'),
        seed=None, name='decLoop')
    thisExp.addLoop(decLoop)
    thisDecLoop = decLoop.trialList[0]
    if thisDecLoop != None:
        for paramName in thisDecLoop:
            exec('{} = thisDecLoop[paramName]'.format(paramName))
    
    for thisDecLoop in decLoop:
        currentLoop = decLoop
        if thisDecLoop != None:
            for paramName in thisDecLoop:
                exec('{} = thisDecLoop[paramName]'.format(paramName))
        
        routineTimer.add(2.000000)
        text.setText(CueType)
        cueComponents = [text]
        for thisComponent in cueComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        cueClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine and routineTimer.getTime() > 0:
            t = cueClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=cueClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1

            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                text.frameNStart = frameN
                text.tStart = t
                text.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(text, 'tStartRefresh')
                text.setAutoDraw(True)
            if text.status == STARTED:
                if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
                    text.tStop = t 
                    text.frameNStop = frameN
                    win.timeOnFlip(text, 'tStopRefresh')
                    text.setAutoDraw(False)
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in cueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            
            if continueRoutine:
                win.flip()
        
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        decLoop.addData('text.started', text.tStartRefresh)
        decLoop.addData('text.stopped', text.tStopRefresh)
        
        routineTimer.add(5.000000)
        gambleAmt.setText(gamble)
        sureAmt.setText(sure)
        sureTex.setText('100% Chance')
        gambleText.setText('50% Chance')
        choice.keys = []
        choice.rt = []
        blank.setText('')
        decisionsComponents = [gambleAmt, sureAmt, sureTex, gambleText, choice, blank]
        for thisComponent in decisionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        decisionsClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine and routineTimer.getTime() > 0:
            t = decisionsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=decisionsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            
            if gambleAmt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                gambleAmt.frameNStart = frameN
                gambleAmt.tStart = t
                gambleAmt.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(gambleAmt, 'tStartRefresh')
                gambleAmt.setAutoDraw(True)
            if gambleAmt.status == STARTED:
                if tThisFlipGlobal > gambleAmt.tStartRefresh + 5-frameTolerance:
                    gambleAmt.tStop = t
                    gambleAmt.frameNStop = frameN
                    win.timeOnFlip(gambleAmt, 'tStopRefresh')
                    gambleAmt.setAutoDraw(False)
            
            if sureAmt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                sureAmt.frameNStart = frameN
                sureAmt.tStart = t
                sureAmt.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(sureAmt, 'tStartRefresh')
                sureAmt.setAutoDraw(True)
            if sureAmt.status == STARTED:
                if tThisFlipGlobal > sureAmt.tStartRefresh + 3-frameTolerance:
                    sureAmt.tStop = t
                    sureAmt.frameNStop = frameN
                    win.timeOnFlip(sureAmt, 'tStopRefresh')
                    sureAmt.setAutoDraw(False)
            
            if sureTex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                sureTex.frameNStart = frameN
                sureTex.tStart = t
                sureTex.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(sureTex, 'tStartRefresh')
                sureTex.setAutoDraw(True)
            if sureTex.status == STARTED:
                if tThisFlipGlobal > sureTex.tStartRefresh + 5-frameTolerance:
                    sureTex.tStop = t
                    sureTex.frameNStop = frameN
                    win.timeOnFlip(sureTex, 'tStopRefresh')
                    sureTex.setAutoDraw(False)
            
            if gambleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                gambleText.frameNStart = frameN
                gambleText.tStart = t
                gambleText.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(gambleText, 'tStartRefresh')
                gambleText.setAutoDraw(True)
            if gambleText.status == STARTED:
                if tThisFlipGlobal > gambleText.tStartRefresh + 5-frameTolerance:
                    gambleText.tStop = t 
                    gambleText.frameNStop = frameN
                    win.timeOnFlip(gambleText, 'tStopRefresh')
                    gambleText.setAutoDraw(False)
            
            waitOnFlip = False
            if choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                choice.frameNStart = frameN
                choice.tStart = t
                choice.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(choice, 'tStartRefresh')
                choice.status = STARTED
                waitOnFlip = True
                win.callOnFlip(choice.clock.reset)
                win.callOnFlip(choice.clearEvents, eventType='keyboard')
            if choice.status == STARTED:
                if tThisFlipGlobal > choice.tStartRefresh + 5-frameTolerance:
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
            if choice.keys == '1':
                gambleAmt.setColor("green")
                sureAmt.setColor('white')
            if choice.keys == '2':
                gambleAmt.setColor("white")
                sureAmt.setColor('green')
            
            if (blank.status == STARTED and t >= (blank.tStart + 1.5)) :
                blank.setAutoDraw(False);
                       
            if choice.keys == '1' or choice.keys == '2':
                choice.status = FINISHED
                    
            if (blank.status == FINISHED):
                gambleAmt.setAutoDraw(False)
                sureAmt.setAutoDraw(False)
                gambleText.setAutoDraw(False)
                sureTex.setAutoDraw(False)
                continueRoutine =(False)
                    
                    
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
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in decisionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            
            if continueRoutine:
                win.flip()
        
        for thisComponent in decisionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        if choice.keys in ['', [], None]:
            choice.keys = None
        decLoop.addData('choice.keys',choice.keys)
        if choice.keys != None:
            decLoop.addData('choice.rt', choice.rt)

        gambleAmt.setColor("white")
        sureAmt.setColor('white')
        thisExp.nextEntry()

    
    thisExp.nextEntry()

win.flip()

thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()
