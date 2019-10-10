#Food Craving
from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import os
import csv
import sys

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '3.0.7'
expName = 'FoodCraving'
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
    originPath='C:\\Users\\Jojo\\Downloads\\Helion Lab\\Experiment Files\\Food Regulation\\FoodCraving.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

endExpNow = False

win = visual.Window(size=(1024, 768), fullscr=True, screen=0,allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',blendMode='avg', useFBO=True, units='height')

expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0 

globalClock = core.Clock()
routineTimer = core.CountdownTimer()

#set up components
introClock=core.Clock()
InstText = visual.TextStim(win=win, text='In this part of the study you will be given a regulation strategy to use while viewing pictures of food.\n\nThen you will use a rating scale to ' +
    'indicate how much you are craving the food item.\n\nWhen you are ready, press space to start!', color='white', pos=(0,0), height=0.07, wrapWidth=1.3)
TYClock = core.Clock()
endText = visual.TextStim(win=win, text='Thank you for participating!\n\nYou have completed this part of the study.', font='Arial', pos=(0, 0), height=0.1, wrapWidth=None, color='white')

cueClock=core.Clock()
cueType= visual.TextStim(win=win, text='default', color='white', pos=(0,0), height=0.14)
ISIClock=core.Clock()
isi = visual.TextStim(win=win, text='+', color='white', pos=(0,0), height=0.1)
ImageClock=core.Clock()
foodPic=visual.ImageStim(win=win, image='sin', pos=(0,0))

ratingsClock = core.Clock()
question = visual.TextStim(win=win, text='How much are you craving this food?', font='Arial', pos=(0, 0.15), height=0.07, wrapWidth=None, color='white');
ratingScale = visual.RatingScale(win=win, marker='triangle', size=1.3, pos=[0.0, -0.4], low=1, high=7, labels=[''], scale='')
scaleMsg1 = visual.TextStim(win=win, text='Not at all', font='Arial', pos=(-0.45, -0.13), height=0.04, color='white');
scaleMsg2 = visual.TextStim(win=win, text='Very much', font='Arial', pos=(0.45, -0.13), height=0.04, color='white');


#isi function
def isiFunc():
    t = 0
    ISIClock.reset()
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    ISIComponents = [isi]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #begin isi
    while continueRoutine and routineTimer.getTime() > 0:
        t = ISIClock.getTime()
        frameN = frameN + 1
        
        if t >= 0.0 and isi.status == NOT_STARTED:
            isi.tStart = t
            isi.frameNStart = frameN
            isi.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75
        if isi.status == STARTED and t >= frameRemains:
            isi.setAutoDraw(False)
        
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
    
    #end isi
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            


#start running the intro screen
t = 0
introClock.reset()
frameN = -1
continueRoutine = True
space = event.BuilderKeyResponse()
introComponents = [InstText, space]
for thisComponent in introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

while continueRoutine:
    t = introClock.getTime()
    frameN = frameN + 1
    
    if t >= 0.0 and InstText.status == NOT_STARTED:
        InstText.tStart = t
        InstText.frameNStart = frameN
        InstText.setAutoDraw(True)
    
    if t >= 0.0 and space.status == NOT_STARTED:
        space.tStart = t
        space.frameNStart = frameN
        space.status = STARTED
        win.callOnFlip(space.clock.reset)
        event.clearEvents(eventType='keyboard')
    if space.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:
            space.keys = theseKeys[-1]
            space.rt = space.clock.getTime()
            continueRoutine = False
    
    if endExpNow or event.getKeys(keyList=["escape"]):
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
if space.keys in ['', [], None]:
    space.keys=None
thisExp.addData('space.keys',space.keys)
if space.keys != None:
    thisExp.addData('space.rt', space.rt)
thisExp.nextEntry()
routineTimer.reset()

trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('FoodReg.csv'),
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
    #regulation cue
    t = 0
    cueClock.reset()
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    cueType.setText(CueType)
    cueComponents = [cueType]
    for thisComponent in cueComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = cueClock.getTime()
        frameN = frameN + 1
        
        if t >= 0.0 and cueType.status == NOT_STARTED:
            cueType.tStart = t
            cueType.frameNStart = frameN
            cueType.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.7
        if cueType.status == STARTED and t >= frameRemains:
            cueType.setAutoDraw(False)
        
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    
    #food pics
    t = 0
    ImageClock.reset() 
    frameN = -1
    continueRoutine = True
    routineTimer.add(8.000000)
    foodPic.setImage(Picture)
    ImageComponents = [foodPic]
    for thisComponent in ImageComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = ImageClock.getTime()
        frameN = frameN + 1
        
        if t >= 0.0 and foodPic.status == NOT_STARTED:
            foodPic.tStart = t
            foodPic.frameNStart = frameN
            foodPic.setAutoDraw(True)
        frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75
        if foodPic.status == STARTED and t >= frameRemains:
            foodPic.setAutoDraw(False)
        
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in ImageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        
        if continueRoutine:
            win.flip()
    
    for thisComponent in ImageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    isiFunc()
    
    #ratings
    t = 0
    ratingsClock.reset()
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    question.setText('How much are you craving this food?')
    ratingScale.reset()
    scaleMsg1.setText('Not at all')
    scaleMsg2.setText('Very Much')
    ratingsComponents = [question, ratingScale, scaleMsg1, scaleMsg2]
    for thisComponent in ratingsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = ratingsClock.getTime()
        frameN = frameN + 1
        
        if t >= 0.0 and question.status == NOT_STARTED:
            question.tStart = t
            question.frameNStart = frameN
            question.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75
        if question.status == STARTED and t >= frameRemains:
            question.setAutoDraw(False)
        if t >= 0.0 and ratingScale.status == NOT_STARTED:
            ratingScale.tStart = t
            ratingScale.frameNStart = frameN
            ratingScale.setAutoDraw(True)
        continueRoutine &= ratingScale.noResponse
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75
        if ratingScale.status == STARTED and t >= frameRemains:
            ratingScale.setAutoDraw(False)
        
        if t >= 0.0 and scaleMsg1.status == NOT_STARTED:
            scaleMsg1.tStart = t
            scaleMsg1.frameNStart = frameN
            scaleMsg1.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75
        if scaleMsg1.status == STARTED and t >= frameRemains:
            scaleMsg1.setAutoDraw(False)
        
        if t >= 0.0 and scaleMsg2.status == NOT_STARTED:
            scaleMsg2.tStart = t
            scaleMsg2.frameNStart = frameN
            scaleMsg2.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75
        if scaleMsg2.status == STARTED and t >= frameRemains:
            scaleMsg2.setAutoDraw(False)
        
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    trials.addData('ratingScale.response', ratingScale.getRating())
    trials.addData('ratingScale.rt', ratingScale.getRT())
    
    isiFunc()

#endText
t= 0
TYClock.reset()
frameN = -1
continueRoutine = True
TYComponents = [endText]
for thisComponent in TYComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

while continueRoutine:
    t = TYClock.getTime()
    frameN = frameN + 1
    
    if t >= 0.0 and endText.status == NOT_STARTED:
        endText.tStart = t
        endText.frameNStart = frameN
        endText.setAutoDraw(True)
    
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in TYComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    
    if continueRoutine:
        win.flip()

for thisComponent in TYComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
routineTimer.reset()
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()

