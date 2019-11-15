#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
expName = 'TrustGame'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\tul00635\\Documents\\GitHub\\Self-Regulation-Psychopy-Files\\Dictator Game\\TrustGame.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False 
frameTolerance = 0.001

# Setup the Window
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
    frameDur = 1.0 / 60.0  # could not measure, so guess

defaultKeyboard = keyboard.Keyboard()

IntroClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='In this task, you will be playing a game with two other people. They will be represented by unique profile pictures.\nEach trial you will be playing with one of the other people.\nYou will be given $5 to use every trial. You have the option to give any dollar amount, from $0-$5, to the other player.\n\nWhatever money you choose to give will be tripled. Then the other player will be told to make the same choice-giving some amount of the now-tripled money back to you.\nThe trials are independent, meaning that money will not be compounded and you will start with $5 each trial. At the end of the task, one of the trials will be selected at random for payment.\nWhen you are ready to begin, press SPACE!',
    font='Arial',
    pos=(0, 0), height=0.045, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
begin = keyboard.Keyboard()

CueClock = core.Clock()
cueText = visual.TextStim(win=win, text='default text',
    font='Arial',
    pos=(0, 0), height=0.14, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

sendMoney1Clock = core.Clock()
sendInstructions = visual.TextStim(win=win, text='dt', font='Arial', pos=(0, 0), height=0.07, wrapWidth=1.4, color='white');
Player1Name = visual.TextStim(win=win, text='Player 1', font='Arial', pos=(0, 0.35), height=0.15, wrapWidth=None, color='white', colorSpace='rgb');
Player1Pic = visual.ImageStim(
    win=win,
    name='Player1Pic', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

Giver1Clock = core.Clock()
Feedback = visual.TextStim(win=win, name='Feedback',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

sendMoney2Clock = core.Clock()
sendInst2 = visual.TextStim(win=win, name='sendInst2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Player2Name = visual.TextStim(win=win, name='Player2',
    text='default text',
    font='Arial',
    pos=(0, 0.35), height=0.13, wrapWidth=None, ori=0, 
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

Giver2Clock = core.Clock()
Feedback2 = visual.TextStim(win=win, name='Feedback2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=1.4, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

globalClock = core.Clock() 
routineTimer = core.CountdownTimer() 
textResponse = visual.TextStim(win=win, text='default text', height=0.09, color='white', pos=[-0.1,-0.5], wrapWidth=1.5)
inputText = ''
gatherTextClock = core.Clock()

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
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroClock.reset(-_timeToFirstFrame)
frameN = -1
continueRoutine = True

# -------Run Routine "Intro"-------
while continueRoutine:
    t = IntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(Instructions, 'tStartRefresh')
        Instructions.setAutoDraw(True)
    
    # *begin* updates
    waitOnFlip = False
    if begin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
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
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if begin.keys in ['', [], None]:  # No response was made
    begin.keys = None
thisExp.addData('begin.keys',begin.keys)
if begin.keys != None:  # we had a response
    thisExp.addData('begin.rt', begin.rt)
thisExp.nextEntry()
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

CueLoop = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,trialList = data.importConditions('DictatorGame.xlsx'),
    seed=None, name='CueLoop')
thisExp.addLoop(CueLoop)  # add the loop to the experiment
thisCueLoop = CueLoop.trialList[0]
if thisCueLoop != None:
    for paramName in thisCueLoop:
        exec('{} = thisCueLoop[paramName]'.format(paramName))

for thisCueLoop in CueLoop:
    currentLoop = CueLoop
    # abbreviate parameter names if possible (e.g. rgb = thisCueLoop.rgb)
    if thisCueLoop != None:
        for paramName in thisCueLoop:
            exec('{} = thisCueLoop[paramName]'.format(paramName))
    

    routineTimer.add(5.000000)
    # update component parameters for each repeat
    cueText.setText(CueType)
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
    
    # -------Run Routine "Cue"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1         

        if cueText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cueText.frameNStart = frameN  # exact frame index
            cueText.tStart = t  # local t and not account for scr refresh
            cueText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cueText, 'tStartRefresh')  # time at next scr refresh
            cueText.setAutoDraw(True)
        if cueText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cueText.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                cueText.tStop = t  # not accounting for scr refresh
                cueText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cueText, 'tStopRefresh')  # time at next scr refresh
                cueText.setAutoDraw(False)
        
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
    
    # set up handler to look after randomisation of conditions etc
    SelfishGiver = data.TrialHandler(nReps=5, method='random', 
        extraInfo=expInfo, originPath=-1,trialList = data.importConditions('DictatorGame.xlsx'),
        seed=None, name='SelfishGiver')
    thisExp.addLoop(SelfishGiver)  # add the loop to the experiment
    thisSelfishGiver = SelfishGiver.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSelfishGiver.rgb)
    if thisSelfishGiver != None:
        for paramName in thisSelfishGiver:
            exec('{} = thisSelfishGiver[paramName]'.format(paramName))
    
    for thisSelfishGiver in SelfishGiver:
        currentLoop = SelfishGiver
        # abbreviate parameter names if possible (e.g. rgb = thisSelfishGiver.rgb)
        if thisSelfishGiver != None:
            for paramName in thisSelfishGiver:
                exec('{} = thisSelfishGiver[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "sendMoney1"-------
        # update component parameters for each repeat
        sendInstructions.setText('You have been given$5 to use. You have the opportunity to send money to Player 1. You may give them all or none of the money, or any amount in between, using increments of $1. Therefore you can choose to give them $0, $1, $2, $3, $4, or $5.\nThe amount of money you send to them will be tripled, and Player 1 will then make a similar choice to give some money amount back to you. \n\nPlease indicate how many dollars you would like to give Player 1 : ') 
        key_resp_3 = event.BuilderKeyResponse()
        Player1Pic.setPos((0, 0.35))
        Player1Pic.setSize((0.3, 0.3))
        Player1Pic.setImage('1patterns.png')
        # keep track of which components have finished
        sendMoney1Components = [sendInstructions, Player1, Player1Pic, textResponse, key_resp_3]
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
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            t = 0
            gatherTextClock.reset()
            continueRoutine = True
            theseKeys=""
            shift_flag = False
#            gatherTextComponents = [textResponse, key_resp_3]
#            for thisComponent in gatherTextComponents:
#                if hasattr(thisComponent, 'status'):
            t = gatherTextClock.getTime()
            n= len(theseKeys)
            i = 0
            while i < n:
            
                if theseKeys[i] == 'return':
                    continueRoutine = False
                    break
            
                elif theseKeys[i] == 'backspace':
                    inputText = inputText[:-1]
                    i = i + 1
            
            
                else:
                    if len(theseKeys[i]) == 1:
                        if shift_flag:
                            inputText += chr( ord(theseKeys[i]) - ord(' '))
                            shift_flag = False
                        else:
                            inputText += theseKeys[i]
            
                    i = i + 1
            # *sendInstructions* updates
            if sendInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sendInstructions.frameNStart = frameN  # exact frame index
                sendInstructions.tStart = t  # local t and not account for scr refresh
                sendInstructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sendInstructions, 'tStartRefresh')  # time at next scr refresh
                sendInstructions.setAutoDraw(True)
            if t >= 0.0 and textResponse.status == NOT_STARTED:
                textResponse.tStart = t
                textResponse.frameNStart = frameN
                textResponse.setAutoDraw(True)
            if textResponse.status == STARTED:
                textResponse.setText((textTypePlayer1 + inputText), log=False)

            
            if t >= 0.0 and key_resp_3.status == NOT_STARTED:
                key_resp_3.tStart = t
                key_resp_3.frameNStart = frameN
                key_resp_3.status = STARTED
                win.callOnFlip(key_resp_3.clock.reset)
                event.clearEvents(eventType='keyboard')
            if key_resp_3.status == STARTED:
                theseKeys = event.getKeys()
            # *Player1* updates
            if Player1Name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Player1Name.frameNStart = frameN  # exact frame index
                Player1Name.tStart = t  # local t and not account for scr refresh
                Player1Name.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Player1, 'tStartRefresh')  # time at next scr refresh
                Player1Name.setAutoDraw(True)
            
            # *Player1Pic* updates
            if Player1Pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Player1Pic.frameNStart = frameN  # exact frame index
                Player1Pic.tStart = t  # local t and not account for scr refresh
                Player1Pic.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Player1Pic, 'tStartRefresh')  # time at next scr refresh
                Player1Pic.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sendMoney1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sendMoney1"-------
        for thisComponent in sendMoney1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        inputText=""
        if key_resp_3.keys in ['', [], None]:
            key_resp_3.keys=None
        SelfishGiver.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:
            SelfishGiver.addData('key_resp_3.rt', key_resp_3.rt)
        # the Routine "sendMoney1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Giver1"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        Feedback.setText("You gave Player 1 \n\n Player 1 received varPlaceholder\n\nPlayer 1 chose to give you varplaceholder2")
        # keep track of which components have finished
        Giver1Components = [Feedback]
        for thisComponent in Giver1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
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
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                if tThisFlipGlobal > Feedback.tStartRefresh + 4-frameTolerance:
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
                thisExp.addData('inputText', inputText)

        thisExp.nextEntry()
        
    # completed 5 repeats of 'SelfishGiver'
    
    
    # set up handler to look after randomisation of conditions etc
    GenerousGiver = data.TrialHandler(nReps=5, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='GenerousGiver')
    thisExp.addLoop(GenerousGiver)  # add the loop to the experiment
    thisGenerousGiver = GenerousGiver.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGenerousGiver.rgb)
    if thisGenerousGiver != None:
        for paramName in thisGenerousGiver:
            exec('{} = thisGenerousGiver[paramName]'.format(paramName))
    
    for thisGenerousGiver in GenerousGiver:
        currentLoop = GenerousGiver
        # abbreviate parameter names if possible (e.g. rgb = thisGenerousGiver.rgb)
        if thisGenerousGiver != None:
            for paramName in thisGenerousGiver:
                exec('{} = thisGenerousGiver[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "sendMoney2"-------
        # update component parameters for each repeat
        sendInst2.setText('You have been given$5 to use. You have the opportunity to send money to Player 1. You may give them all or none of the money, or any amount in between, using increments of $1. Therefore you can choose to give them $0, $1, $2, $3, $4, or $5.\nThe amount of money you send to them will be tripled, and Player 1 will then make a similar choice to give some money amount back to you. \n\nPlease type how much money you would like to give Player 1 : ')
        Player2Name.setText('Player 2')
        Player2Pic.setPos((0, 0.35))
        Player2Pic.setSize((0.3, 0.3))
        Player2Pic.setImage('3pattern.png')
        key_resp_4 = event.BuilderKeyResponse()
        # keep track of which components have finished
        sendMoney2Components = [sendInst2, Player2, Player2Pic,textResponse, key_resp_4]
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
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            t = 0
            gatherTextClock.reset()
            continueRoutine = True
            theseKeys=""
            shift_flag = False
            t = gatherTextClock.getTime()
            n= len(theseKeys)
            i = 0
            while i < n:
            
                if theseKeys[i] == 'return':
                    continueRoutine = False
                    break
            
                elif theseKeys[i] == 'backspace':
                    inputText = inputText[:-1]
                    i = i + 1
            
            
                else:
                    if len(theseKeys[i]) == 1:
                        if shift_flag:
                            inputText += chr( ord(theseKeys[i]) - ord(' '))
                            shift_flag = False
                        else:
                            inputText += theseKeys[i]
            
                    i = i + 1
            # *sendInst2* updates
            if sendInst2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sendInst2.frameNStart = frameN  # exact frame index
                sendInst2.tStart = t  # local t and not account for scr refresh
                sendInst2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sendInst2, 'tStartRefresh')  # time at next scr refresh
                sendInst2.setAutoDraw(True)
            if t >= 0.0 and textResponse.status == NOT_STARTED:
                textResponse.tStart = t
                textResponse.frameNStart = frameN
                textResponse.setAutoDraw(True)
            if textResponse.status == STARTED:
                textResponse.setText((textTypePlayer2 + inputText), log=False)
           
            if t >= 0.0 and key_resp_4.status == NOT_STARTED:
                key_resp_4.tStart = t
                key_resp_4.frameNStart = frameN
                key_resp_4.status = STARTED
                win.callOnFlip(key_resp_4.clock.reset)
                event.clearEvents(eventType='keyboard')
            if key_resp_3.status == STARTED:
                theseKeys = event.getKeys()
            # *Player2* updates
            if Player2Name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Player2Name.frameNStart = frameN  # exact frame index
                Player2Name.tStart = t  # local t and not account for scr refresh
                Player2Name.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Player2, 'tStartRefresh')  # time at next scr refresh
                Player2Name.setAutoDraw(True)
            
            # *Player2Pic* updates
            if Player2Pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Player2Pic.frameNStart = frameN  # exact frame index
                Player2Pic.tStart = t  # local t and not account for scr refresh
                Player2Pic.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Player2Pic, 'tStartRefresh')  # time at next scr refresh
                Player2Pic.setAutoDraw(True)
            
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
                
        thisExp.addData('inputText', inputText)
        inputText=""
        if key_resp_4.keys in ['', [], None]:
            key_resp_4.keys=None
        GenerousGiver.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:
            GenerousGiver.addData('key_resp_4.rt', key_resp_4.rt)
        # the Routine "sendMoney2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Giver2"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        Feedback2.setText("You gave Player 2 Player 2 received player 2 chose to give you ")
        # keep track of which components have finished
        Giver2Components = [Feedback2]
        for thisComponent in Giver2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Giver2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Giver2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Giver2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Giver2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Feedback2* updates
            if Feedback2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Feedback2.frameNStart = frameN  # exact frame index
                Feedback2.tStart = t  # local t and not account for scr refresh
                Feedback2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback2, 'tStartRefresh')  # time at next scr refresh
                Feedback2.setAutoDraw(True)
            if Feedback2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Feedback2.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Feedback2.tStop = t  # not accounting for scr refresh
                    Feedback2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Feedback2, 'tStopRefresh')  # time at next scr refresh
                    Feedback2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
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
        
    # completed 5 repeats of 'GenerousGiver'
    
    thisExp.nextEntry()
    
# completed 5 repeats of 'CueLoop'


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
