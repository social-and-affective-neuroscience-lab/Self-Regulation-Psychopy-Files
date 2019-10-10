#Delay Discounting Task

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random
import os
import sys 
import secrets


_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '3.0.7'
expName = 'Delay Discounting'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Jojo\\Downloads\\DelayDiscounting1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

endExpNow = False 

win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, allowGUI=True, allowStencil=False, monitor='testMonitor', color=[0,0,0], colorSpace='rgb', blendMode='avg', useFBO=True)

expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0


IntroductionClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='default',font='Arial',pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, color='white');
IntroText1 = ("In this task you will be choosing between two different monetary rewards. \n\nYou will be given a regulation strategy prior to a block of trials. Please employ the strategy given while making decisions.\n\nPress SPACE to continue.")
IntroText2 = ('You will be presented with two monetary offers, differing in the time at which you would receive the money. \n\nIf you would prefer the offer on the left, press "q"\n\nIf you would prefer the offer on the right, press "p"\n\nYou will have four '+
    'seconds to make your choice once the offers are presented.\n\nFirst you will be playing some practice rounds. When you are ready, press SPACE to begin!');


ChoiceClock = core.Clock()
leftText = visual.TextStim(win=win, name='leftText', text='default', font='Arial',
    pos=(-0.45, -0.2), height=0.16, wrapWidth=None, color='white');

rightText = visual.TextStim(win=win, name='rightText', text='default', font='Arial',
    pos=(0.45, -0.2), height=0.16, wrapWidth=None, color='white');

rightMoney = visual.TextStim(win=win, name='rightMoney', text='default', font='Arial', 
    pos=(0.45, 0.05), height=0.16, wrapWidth=None, color='white');

leftMoney = visual.TextStim(win=win, name='leftMoney', text='default', font='Arial', 
    pos=(-0.45, 0.05), height=0.16, wrapWidth=None, color='white');

blank = visual.TextStim(win=win, name='blank', text=None, pos=(0, 0));

ISIClock = core.Clock()
ISI = visual.TextStim(win=win, name='ISI', text='+', pos=(0, 0), height=0.2, color='white');

CueClock=core.Clock()
Cue = visual.TextStim(win=win, text='default Text', color='white', pos=(0,0), height=0.25)


Thank_YouClock = core.Clock()
ThankYou = visual.TextStim(win=win, name='ThankYou', text='Thank you for participating!\n\nNow you will be answering a couple of questions about your experience during the task. \n\nPress space to continue',
 font='Arial',pos=(0, 0), height=0.1, wrapWidth=None, color='white');

Q1Clock = core.Clock()
Question1 = visual.TextStim(win=win, name='Question1',
    text='How likely were you to choose a delayed reward over an immediate reward?', font='Arial', wrapWidth=1.1,
    pos=(0, 0.3), height=0.1, color='white');

scale_msg1 = visual.TextStim(win=win, name='scale_msg1', text='Very Unlikely (1)', font='Arial',
    pos=(-0.5, -0.3), height=0.07, color='white');

scale_msg2 = visual.TextStim(win=win, name='scale_msg2', text='Very Likely (7)', font='Arial',
    pos=(0.5, -0.3), height=0.07, color='white');

scale_msg3 = visual.TextStim(win=win, name='scale_msg3', text='Neutral', font='Arial', pos=(0, -0.3),
    height=0.07, color='white');

rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.5, pos=[0.0, -0.4],
    low=1, high=7, labels=['Very Unlikely', ' Unlikely', ' Somewhat Unlikely', ' Neutral', ' Somewhat Likely', ' Likely', ' Very Likely'], scale='')

# components q2
Q2Clock = core.Clock()
Question2 = visual.TextStim(win=win, name='Question2',
    text='How likely were you to choose an immediate reward over a delayed reward?', font='Arial',wrapWidth=1.1,
    pos=(0, 0.3), height=0.12, color='white');
scale1 = visual.TextStim(win=win, name='scale1', text='Very Unlikely (1)', font='Arial',
    pos=(-0.5, -0.28), height=0.07, color='white');
scale2 = visual.TextStim(win=win, name='scale2', text='Neutral',font='Arial', pos=(0, -0.28),
    height=0.07, color='white');
scale3 = visual.TextStim(win=win, name='text', text='Very Likely (7)', font='Arial',
    pos=(0.5, -0.28), height=0.07, color='white');

rating_2 = visual.RatingScale(win=win, name='rating_2', marker='triangle', size=1.5, pos=[0.0, -0.45], low=1, high=7, labels=['Very Unlikely', ' Unlikely', ' Somewhat Unlikely', ' Neutral', ' Somewhat Likely', ' Likely', ' Very Likely'], scale='')

EndingClock = core.Clock()
EndingText = visual.TextStim(win=win, name='end', text='Thank you for your participation! You are finished with this part of the study.', 
    font='Arial', wrapWidth=1.1, pos=(0,0), height=0.1, color='white');

globalClock = core.Clock()
routineTimer = core.CountdownTimer() 


#Intro function
def intro(textVar):
    
    t = 0
    IntroductionClock.reset()
    Instructions.setText(textVar)
    frameN = -1
    continueRoutine = True
    spacebar = event.BuilderKeyResponse()
    IntroductionComponents = [Instructions, spacebar]
    for thisComponent in IntroductionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    while continueRoutine:
        t = IntroductionClock.getTime()
        frameN = frameN + 1
        
        if t >= 0.0 and Instructions.status == NOT_STARTED:
            Instructions.tStart = t
            Instructions.frameNStart = frameN
            Instructions.setAutoDraw(True)
        
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
        for thisComponent in IntroductionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break 
        
        if continueRoutine:
            win.flip()

    for thisComponent in IntroductionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if spacebar.keys in ['', [], None]:
        spacebar.keys=None
    thisExp.addData('spacebar.keys',spacebar.keys)
    if spacebar.keys != None:
        thisExp.addData('spacebar.rt', spacebar.rt)
    thisExp.nextEntry()
    routineTimer.reset()

#choice routine loop
Loop = data.TrialHandler(nReps=6, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DelayDiscountingCues.csv'),
    seed=None, name='Loop')

def cue(cueText):
    t = 0
    CueClock.reset()
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    Cue.setText(cueText)
    CueComponents = [Cue]
    for thisComponent in CueComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = CueClock.getTime()
        frameN = frameN + 1
        
        if t >= 0.0 and Cue.status == NOT_STARTED:
            Cue.tStart = t
            Cue.frameNStart = frameN
            Cue.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75
        if Cue.status == STARTED and t >= frameRemains:
            Cue.setAutoDraw(False)
        
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    thisExp.nextEntry()

leftVarText=[]
leftVarMoney = []
rightVarText = []
rightVarMoney = []
def choice(leftVarText, leftVarMoney, rightVarText, rightVarMoney):
    t = 0
    ChoiceClock.reset()
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.0000)
    leftText.setText(leftVarText)
    rightText.setText(rightVarText)
    rightMoney.setText(rightVarMoney)
    leftMoney.setText(leftVarMoney)
    responses = event.BuilderKeyResponse()
    blank.setText('')
    ChoiceComponents = [leftText, rightText, rightMoney, leftMoney, responses, blank]
    for thisComponent in ChoiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    while continueRoutine:
        t = ChoiceClock.getTime()
        frameN = frameN + 1
        
        if t >= 0.0 and leftText.status == NOT_STARTED:
            leftText.tStart = t
            leftText.frameNStart = frameN
            leftText.setAutoDraw(True)
        
        if t >= 0.0 and rightText.status == NOT_STARTED:
            rightText.tStart = t
            rightText.frameNStart = frameN
            rightText.setAutoDraw(True)
        
        if t >= 0.0 and rightMoney.status == NOT_STARTED:
            rightMoney.tStart = t
            rightMoney.frameNStart = frameN
            rightMoney.setAutoDraw(True)
        
        if t >= 0.0 and leftMoney.status == NOT_STARTED:
            leftMoney.tStart = t
            leftMoney.frameNStart = frameN
            leftMoney.setAutoDraw(True)
        
        if t >= 0.0 and responses.status == NOT_STARTED:
            responses.tStart = t
            responses.frameNStart = frameN
            responses.status = STARTED
            win.callOnFlip(responses.clock.reset) 
            event.clearEvents(eventType='keyboard')
        if responses.status == STARTED and bool(blank.status == STARTED):
            responses.status = FINISHED
        if responses.status == STARTED:
            theseKeys = event.getKeys(keyList=['q', 'p'])
            
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:
                responses.keys = theseKeys[-1] 
                responses.rt = responses.clock.getTime()
        
        if responses.keys == 'p':
            rightMoney.setColor("green")
            rightText.setColor('green')
        if responses.keys == 'q':
            leftMoney.setColor("green")
            leftText.setColor('green')

        if leftText.status == STARTED and t>= 3.000:
            leftText.setAutoDraw(False)
            rightText.setAutoDraw(False)
            leftMoney.setAutoDraw(False)
            rightMoney.setAutoDraw(False)
            blank.setAutoDraw(False)
            continueRoutine= False

        if (blank.status == STARTED and t >= (blank.tStart + 1.0)) :
           blank.setAutoDraw(False);
           
        if responses.keys == 'p' or responses.keys == 'q':
            responses.status = FINISHED
        
        if (blank.status == FINISHED):
            rightText.setAutoDraw(False)
            rightMoney.setAutoDraw(False)
            leftMoney.setAutoDraw(False)
            leftText.setAutoDraw(False)
            continueRoutine =False
        
        
        if (responses.keys == 'p' or responses.keys == 'q') and blank.status == NOT_STARTED:
            blank.tStart = t
            blank.frameNStart = frameN
            blank.setAutoDraw(True)

        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in ChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        
        if continueRoutine:
            win.flip()
    
    for thisComponent in ChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if responses.keys in ['', [], None]:
        responses.keys=None
    Loop.addData('responses.keys',responses.keys)
    if responses.keys != None:
        Loop.addData('responses.rt', responses.rt)
        
    if blank.status == FINISHED:
        leftMoney.setAutoDraw(False)
        rightMoney.setAutoDraw(False)
        leftText.setAutoDraw(False)
        rightText.setAutoDraw(False)
    
    leftMoney.setColor('white')
    rightMoney.setColor('white')
    leftText.setColor('white')
    rightText.setColor('white')
    
    routineTimer.reset()

def isi(textVar2):
    t = 0
    ISIClock.reset()
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    ISI.setText(textVar2)
    ISIComponents = [ISI]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = ISIClock.getTime()
        frameN = frameN + 1
        
        if t >= 0.0 and ISI.status == NOT_STARTED:
            ISI.tStart = t
            ISI.frameNStart = frameN
            ISI.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75
        if ISI.status == STARTED and t >= frameRemains:
            ISI.setAutoDraw(False)
        
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    thisExp.nextEntry()

intro(IntroText1)
intro(IntroText2)

PracticeLoop = data.TrialHandler(nReps=1, method='random', extraInfo=expInfo, originPath=-1, trialList=data.importConditions('DelayDiscountingCues.csv', selection='0'), seed=None)
thisExp.addLoop(PracticeLoop)
thisLoop = PracticeLoop.trialList[0]
if thisLoop != None:
    for paramName in thisLoop:
        exec('{} = thisLoop[paramName]'.format(paramName))

ChoiceLoop = data.TrialHandler(nReps=1, method='random', extraInfo=expInfo, originPath=-1, trialList=data.importConditions('DelayDiscountingAmt.csv', selection='0:3'), seed=None)


for thisLoop in PracticeLoop:
    currentLoop = PracticeLoop
    if thisLoop != None:
        for paramName in thisLoop:
            exec('{} = thisLoop[paramName]'.format(paramName))
    
    cue(CueType)
    
   
    thisExp.addLoop(ChoiceLoop)
    thisLoop=ChoiceLoop.trialList[0]
    
    if thisLoop != None:
        for paramName in thisLoop:
            exec('{} = thisLoop[paramName]'.format(paramName))
    for thisLoop in ChoiceLoop:
        currentLoop = ChoiceLoop
        if thisLoop !=None:
            for paramName in thisLoop:
                exec('{} = thisLoop[paramName]'.format(paramName))
        
        
        subID = int(expInfo['participant'])
        if subID%2 == 0 :
            leftVarText = (DelayDays)
            leftVarMoney = (DelayMoney)
            rightVarText = ('today')
            rightVarMoney = (ImMoney)

        if subID%2 == 1:
            rightVarText= (DelayDays)
            rightVarMoney= (DelayMoney)
            leftVarText= ('today')
            leftVarMoney= (ImMoney)
        
        choice(leftVarText, leftVarMoney, rightVarText, rightVarMoney)
        isi("+")

intro("You will now complete the full task. \n\nPress SPACE to begin!")


trials = data.TrialHandler(nReps=1, method='random',extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DelayDiscountingCues.csv', selection=rows),
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
    
    cue(CueType)
    isi("+")

    
    trials_2 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('DelayDiscountingAmt.csv', selection = rows),
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
        
        subID = int(expInfo['participant'])
        if subID%2 == 0 :
            leftVarText = (DelayDays)
            leftVarMoney = (DelayMoney)
            rightVarText = ('today')
            rightVarMoney = (ImMoney)

        if subID%2 == 1:
            rightVarText= (DelayDays)
            rightVarMoney= (DelayMoney)
            leftVarText= ('today')
            leftVarMoney= (ImMoney)
        choice(leftVarText, leftVarMoney, rightVarText, rightVarMoney)

        isi("+")
        
    thisExp.nextEntry()


thisExp.addLoop(Loop)
thisLoop = Loop.trialList[0]
if thisLoop != None:
    for paramName in thisLoop:
        exec('{} = thisLoop[paramName]'.format(paramName))

for thisLoop in Loop:
    currentLoop = Loop
    if thisLoop != None:
        for paramName in thisLoop:
            exec('{} = thisLoop[paramName]'.format(paramName))
            
            
    cue(CueType)
    
    thisExp.addLoop(ChoiceLoop)
    thisLoop=ChoiceLoop.trialList[0]
    if thisLoop != None:
        for paramName in thisLoop:
            exec('{} = thisLoop[paramName]'.format(paramName))
    for thisLoop in ChoiceLoop:
        currentLoop = ChoiceLoop
        if thisLoop !=None:
            for paramName in thisLoop:
                exec('{} = thisLoop[paramName]'.format(paramName))
        
        choice(leftVarText, leftVarMoney, rightVarText, rightVarMoney)
        isi("+")
    

#Thank you routine
t = 0
Thank_YouClock.reset()
frameN = -1
continueRoutine = True
key_resp_2 = event.BuilderKeyResponse()
Thank_YouComponents = [ThankYou, key_resp_2]
for thisComponent in Thank_YouComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#start ty routine
while continueRoutine:
    t = Thank_YouClock.getTime()
    frameN = frameN + 1
    
    if t >= 0.0 and ThankYou.status == NOT_STARTED:
        ThankYou.tStart = t
        ThankYou.frameNStart = frameN
        ThankYou.setAutoDraw(True)
    
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN 
        key_resp_2.status = STARTED
        win.callOnFlip(key_resp_2.clock.reset)
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0: 
            key_resp_2.keys = theseKeys[-1]
            key_resp_2.rt = key_resp_2.clock.getTime()
            continueRoutine = False
    
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in Thank_YouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break 
            
    if continueRoutine:
        win.flip()

#end ty routine
for thisComponent in Thank_YouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

if key_resp_2.keys in ['', [], None]:
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
routineTimer.reset()

#q loop
questions = data.TrialHandler(nReps=1, method='sequential', extraInfo=expInfo, originPath=-1,
    trialList=[None], seed=None, name='questions')
thisExp.addLoop(questions)
thisQuestion = questions.trialList[0] 

if thisQuestion != None:
    for paramName in thisQuestion:
        exec('{} = thisQuestion[paramName]'.format(paramName))

for thisQuestion in questions:
    currentLoop = questions
    if thisQuestion != None:
        for paramName in thisQuestion:
            exec('{} = thisQuestion[paramName]'.format(paramName))

    t = 0
    Q1Clock.reset()
    frameN = -1
    continueRoutine = True
    rating.reset()
    Q1Components = [Question1, scale_msg1, scale_msg2, scale_msg3, rating]
    for thisComponent in Q1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    while continueRoutine:
        t = Q1Clock.getTime()
        frameN = frameN + 1
        
        if t >= 0.0 and Question1.status == NOT_STARTED:
            Question1.tStart = t
            Question1.frameNStart = frameN
            Question1.setAutoDraw(True)
        
        if t >= 0.0 and scale_msg1.status == NOT_STARTED:
            scale_msg1.tStart = t
            scale_msg1.frameNStart = frameN
            scale_msg1.setAutoDraw(True)
        
        if t >= 0.0 and scale_msg2.status == NOT_STARTED:
            scale_msg2.tStart = t
            scale_msg2.frameNStart = frameN
            scale_msg2.setAutoDraw(True)
        
        if t >= 0.0 and scale_msg3.status == NOT_STARTED:
            scale_msg3.tStart = t
            scale_msg3.frameNStart = frameN
            scale_msg3.setAutoDraw(True)
        if t >= 0.0 and rating.status == NOT_STARTED:
            rating.tStart = t
            rating.frameNStart = frameN
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse
        
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in Q1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break 
        
        if continueRoutine:
            win.flip()
    
    # end q1
    for thisComponent in Q1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    questions.addData('rating.response', rating.getRating())
    questions.addData('rating.rt', rating.getRT())
    questions.addData('rating.history', rating.getHistory())
    routineTimer.reset()
    
    #q2
    t = 0
    Q2Clock.reset()
    frameN = -1
    continueRoutine = True
    rating_2.reset()
    Q2Components = [Question2, scale1, scale2, scale3, rating_2]
    for thisComponent in Q2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # begin q2
    while continueRoutine:
        t = Q2Clock.getTime()
        frameN = frameN + 1 
        
        if t >= 0.0 and Question2.status == NOT_STARTED:
            Question2.tStart = t
            Question2.frameNStart = frameN
            Question2.setAutoDraw(True)
        
        if t >= 0.0 and scale1.status == NOT_STARTED:
            scale1.tStart = t
            scale1.frameNStart = frameN
            scale1.setAutoDraw(True)
        
        if t >= 0.0 and scale2.status == NOT_STARTED:
            scale2.tStart = t
            scale2.frameNStart = frameN
            scale2.setAutoDraw(True)
        
        if t >= 0.0 and scale3.status == NOT_STARTED:
            scale3.tStart = t
            scale3.frameNStart = frameN
            scale3.setAutoDraw(True)
        if t >= 0.0 and rating_2.status == NOT_STARTED:
            rating_2.tStart = t
            rating_2.frameNStart = frameN
            rating_2.setAutoDraw(True)
        continueRoutine &= rating_2.noResponse
        
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in Q2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        
        if continueRoutine:
            win.flip()

    for thisComponent in Q2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    questions.addData('rating_2.response', rating_2.getRating())
    questions.addData('rating_2.rt', rating_2.getRT())
    routineTimer.reset()
    thisExp.nextEntry()
    
#end text routine
t = 0
EndingClock.reset()
frameN = -1
continueRoutine = True
EndingComponents = [EndingText]
for thisComponent in EndingComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

while continueRoutine:
    t = EndingClock.getTime()
    frameN = frameN + 1
    
    if t >= 0.0 and EndingText.status == NOT_STARTED:
        EndingText.tStart = t
        EndingText.frameNStart = frameN
        EndingText.setAutoDraw(True)
    
   
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in EndingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break 
            
    if continueRoutine:
        win.flip()

for thisComponent in EndingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

thisExp.nextEntry()
routineTimer.reset()

thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()

#close down
thisExp.abort()
win.close()
core.quit()
