/****************************** 
 * Delaydiscountpavlovia Test *
 ******************************/

import { PsychoJS } from 'https://pavlovia.org/lib/core.js';
import * as core from 'https://pavlovia.org/lib/core.js';
import { TrialHandler } from 'https://pavlovia.org/lib/data.js';
import { Scheduler } from 'https://pavlovia.org/lib/util.js';
import * as util from 'https://pavlovia.org/lib/util.js';
import * as visual from 'https://pavlovia.org/lib/visual.js';
import { Sound } from 'https://pavlovia.org/lib/sound.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'DelayDiscountPavlovia';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InstrRoutineBegin);
flowScheduler.add(InstrRoutineEachFrame);
flowScheduler.add(InstrRoutineEnd);
flowScheduler.add(Inst2RoutineBegin);
flowScheduler.add(Inst2RoutineEachFrame);
flowScheduler.add(Inst2RoutineEnd);
flowScheduler.add(isiRoutineBegin);
flowScheduler.add(isiRoutineEachFrame);
flowScheduler.add(isiRoutineEnd);
flowScheduler.add(PracticeCueRoutineBegin);
flowScheduler.add(PracticeCueRoutineEachFrame);
flowScheduler.add(PracticeCueRoutineEnd);
const PracticeLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(PracticeLoopLoopBegin, PracticeLoopLoopScheduler);
flowScheduler.add(PracticeLoopLoopScheduler);
flowScheduler.add(PracticeLoopLoopEnd);
flowScheduler.add(BeginInstRoutineBegin);
flowScheduler.add(BeginInstRoutineEachFrame);
flowScheduler.add(BeginInstRoutineEnd);
const mainLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(mainLoopLoopBegin, mainLoopLoopScheduler);
flowScheduler.add(mainLoopLoopScheduler);
flowScheduler.add(mainLoopLoopEnd);
flowScheduler.add(EndingRoutineBegin);
flowScheduler.add(EndingRoutineEachFrame);
flowScheduler.add(EndingRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.0';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

function experimentInit() {
  // Initialize components for Routine "Instr"
  InstrClock = new util.Clock();
  Instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instructions',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  space = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Inst2"
  Inst2Clock = new util.Clock();
  instruct2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct2',
    text: 'You will be presented with two monetary offers, differing in the time at which you would receive the money. \n\nIf you would prefer the offer on the left, press "1"\n\nIf you would prefer the offer on the right, press "2"\n\nYou will have four seconds to make your choice once the offers are presented.\n\nFirst you will be playing some practice rounds. When you are ready, press ENTER to begin!',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.065,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  enter = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "isi"
  isiClock = new util.Clock();
  isi2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'isi2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "PracticeCue"
  PracticeCueClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'REGULATE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.13,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "isi"
  isiClock = new util.Clock();
  isi2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'isi2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Practice"
  PracticeClock = new util.Clock();
  Line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Line',
    units: 'from exp settings',
    vertices: [[-[1.0, 1.0][0]/2.0, 0], [+[1.0, 1.0][0]/2.0, 0]],
    ori: 90, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  choice = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  ImmedMoneyAmt = new visual.TextStim({
    win: psychoJS.window,
    name: 'ImmedMoneyAmt',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  DelayMoneyAmt = new visual.TextStim({
    win: psychoJS.window,
    name: 'DelayMoneyAmt',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  Immedtoday = new visual.TextStim({
    win: psychoJS.window,
    name: 'Immedtoday',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  DelayTime = new visual.TextStim({
    win: psychoJS.window,
    name: 'DelayTime',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  subID = parseInt(expInfo['participant'])
  blank = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  // Initialize components for Routine "BeginInst"
  BeginInstClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'You will now begin the full task.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "isi"
  isiClock = new util.Clock();
  isi2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'isi2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Cue"
  CueClock = new util.Clock();
  cue = new visual.TextStim({
    win: psychoJS.window,
    name: 'cue',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "isi"
  isiClock = new util.Clock();
  isi2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'isi2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Practice"
  PracticeClock = new util.Clock();
  Line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Line',
    units: 'from exp settings',
    vertices: [[-[1.0, 1.0][0]/2.0, 0], [+[1.0, 1.0][0]/2.0, 0]],
    ori: 90, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  choice = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  ImmedMoneyAmt = new visual.TextStim({
    win: psychoJS.window,
    name: 'ImmedMoneyAmt',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  DelayMoneyAmt = new visual.TextStim({
    win: psychoJS.window,
    name: 'DelayMoneyAmt',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  Immedtoday = new visual.TextStim({
    win: psychoJS.window,
    name: 'Immedtoday',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  DelayTime = new visual.TextStim({
    win: psychoJS.window,
    name: 'DelayTime',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  subID = parseInt(expInfo['participant'])
  blank = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  // Initialize components for Routine "Ending"
  EndingClock = new util.Clock();
  ThankYou = new visual.TextStim({
    win: psychoJS.window,
    name: 'ThankYou',
    text: 'Thank you for participating!\n\n\nYou have completed this part of the study',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function InstrRoutineBegin() {
  //------Prepare to start Routine 'Instr'-------
  t = 0;
  InstrClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  Instructions.setColor(new util.Color('white'));
  Instructions.setPos([0, 0]);
  Instructions.setText('In this task you will be choosing between two different monetary rewards. \n\nYou will be given a regulation strategy prior to a block of trials. Please employ the strategy given while making decisions.\n\nPress SPACE to continue.\n');
  Instructions.setFont('Arial');
  Instructions.setHeight(0.065);
  space.keys = undefined;
  space.rt = undefined;
  // keep track of which components have finished
  InstrComponents = [];
  InstrComponents.push(Instructions);
  InstrComponents.push(space);
  
  for (const thisComponent of InstrComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

function InstrRoutineEachFrame() {
  //------Loop for each frame of Routine 'Instr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = InstrClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Instructions* updates
  if (t >= 0.0 && Instructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Instructions.tStart = t;  // (not accounting for frame time here)
    Instructions.frameNStart = frameN;  // exact frame index
    Instructions.setAutoDraw(true);
  }

  
  // *space* updates
  if (t >= 0.0 && space.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    space.tStart = t;  // (not accounting for frame time here)
    space.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { space.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { space.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { space.clearEvents(); });
  }

  if (space.status === PsychoJS.Status.STARTED) {
    let theseKeys = space.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      space.keys = theseKeys[0].name;  // just the last key pressed
      space.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of InstrComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function InstrRoutineEnd() {
  //------Ending Routine 'Instr'-------
  for (const thisComponent of InstrComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('space.keys', space.keys);
  if (typeof space.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('space.rt', space.rt);
      routineTimer.reset();
      }
  
  space.stop();
  // the Routine "Instr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function Inst2RoutineBegin() {
  //------Prepare to start Routine 'Inst2'-------
  t = 0;
  Inst2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  enter.keys = undefined;
  enter.rt = undefined;
  // keep track of which components have finished
  Inst2Components = [];
  Inst2Components.push(instruct2);
  Inst2Components.push(enter);
  
  for (const thisComponent of Inst2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

function Inst2RoutineEachFrame() {
  //------Loop for each frame of Routine 'Inst2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Inst2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instruct2* updates
  if (t >= 0.0 && instruct2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct2.tStart = t;  // (not accounting for frame time here)
    instruct2.frameNStart = frameN;  // exact frame index
    instruct2.setAutoDraw(true);
  }

  
  // *enter* updates
  if (t >= 0.0 && enter.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    enter.tStart = t;  // (not accounting for frame time here)
    enter.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { enter.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { enter.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { enter.clearEvents(); });
  }

  if (enter.status === PsychoJS.Status.STARTED) {
    let theseKeys = enter.getKeys({keyList: ['return'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      enter.keys = theseKeys[0].name;  // just the last key pressed
      enter.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of Inst2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function Inst2RoutineEnd() {
  //------Ending Routine 'Inst2'-------
  for (const thisComponent of Inst2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('enter.keys', enter.keys);
  if (typeof enter.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('enter.rt', enter.rt);
      routineTimer.reset();
      }
  
  enter.stop();
  // the Routine "Inst2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function isiRoutineBegin() {
  //------Prepare to start Routine 'isi'-------
  t = 0;
  isiClock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.000000);
  // update component parameters for each repeat
  isi2.setText('+');
  // keep track of which components have finished
  isiComponents = [];
  isiComponents.push(isi2);
  
  for (const thisComponent of isiComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

function isiRoutineEachFrame() {
  //------Loop for each frame of Routine 'isi'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = isiClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *isi2* updates
  if (t >= 0.0 && isi2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    isi2.tStart = t;  // (not accounting for frame time here)
    isi2.frameNStart = frameN;  // exact frame index
    isi2.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (isi2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    isi2.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of isiComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function isiRoutineEnd() {
  //------Ending Routine 'isi'-------
  for (const thisComponent of isiComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

function PracticeCueRoutineBegin() {
  //------Prepare to start Routine 'PracticeCue'-------
  t = 0;
  PracticeCueClock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  PracticeCueComponents = [];
  PracticeCueComponents.push(text);
  
  for (const thisComponent of PracticeCueComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

function PracticeCueRoutineEachFrame() {
  //------Loop for each frame of Routine 'PracticeCue'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = PracticeCueClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of PracticeCueComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function PracticeCueRoutineEnd() {
  //------Ending Routine 'PracticeCue'-------
  for (const thisComponent of PracticeCueComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

function PracticeLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  PracticeLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'DelayDiscountingAmt.csv', '0:3'),
    seed: undefined, name: 'PracticeLoop'});
  psychoJS.experiment.addLoop(PracticeLoop); // add the loop to the experiment
  currentLoop = PracticeLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPracticeLoop of PracticeLoop) {
    thisScheduler.add(importConditions(PracticeLoop));
    thisScheduler.add(isiRoutineBegin);
    thisScheduler.add(isiRoutineEachFrame);
    thisScheduler.add(isiRoutineEnd);
    thisScheduler.add(PracticeRoutineBegin);
    thisScheduler.add(PracticeRoutineEachFrame);
    thisScheduler.add(PracticeRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

function PracticeLoopLoopEnd() {
  psychoJS.experiment.removeLoop(PracticeLoop);

  return Scheduler.Event.NEXT;
}

function mainLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  mainLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'DelayDiscountingCues.csv',
    seed: undefined, name: 'mainLoop'});
  psychoJS.experiment.addLoop(mainLoop); // add the loop to the experiment
  currentLoop = mainLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisMainLoop of mainLoop) {
    thisScheduler.add(importConditions(mainLoop));
    thisScheduler.add(isiRoutineBegin);
    thisScheduler.add(isiRoutineEachFrame);
    thisScheduler.add(isiRoutineEnd);
    thisScheduler.add(CueRoutineBegin);
    thisScheduler.add(CueRoutineEachFrame);
    thisScheduler.add(CueRoutineEnd);
    const trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    thisScheduler.add(trialsLoopScheduler);
    thisScheduler.add(trialsLoopEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'DelayDiscountingAmt.csv', rows),
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(isiRoutineBegin);
    thisScheduler.add(isiRoutineEachFrame);
    thisScheduler.add(isiRoutineEnd);
    thisScheduler.add(PracticeRoutineBegin);
    thisScheduler.add(PracticeRoutineEachFrame);
    thisScheduler.add(PracticeRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

function mainLoopLoopEnd() {
  psychoJS.experiment.removeLoop(mainLoop);

  return Scheduler.Event.NEXT;
}

function PracticeRoutineBegin() {
  //------Prepare to start Routine 'Practice'-------
  t = 0;
  PracticeClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  Line.setSize([3, 0.5]);
  Line.setFillColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
  Line.setLineColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
  Line.setLineWidth(7);
  choice.keys = undefined;
  choice.rt = undefined;
  ImmedMoneyAmt.setColor(new util.Color('white'));
  ImmedMoneyAmt.setPos([(- 0.41), 0.15]);
  ImmedMoneyAmt.setText(ImMoney);
  ImmedMoneyAmt.setFont('Arial');
  ImmedMoneyAmt.setHeight(0.12);
  DelayMoneyAmt.setColor(new util.Color('white'));
  DelayMoneyAmt.setPos([0.41, 0.15]);
  DelayMoneyAmt.setText(DelayMoney);
  DelayMoneyAmt.setFont('Arial');
  DelayMoneyAmt.setHeight(0.12);
  Immedtoday.setColor(new util.Color('white'));
  Immedtoday.setPos([(- 0.41), (- 0.1)]);
  Immedtoday.setText('today');
  Immedtoday.setFont('Arial');
  Immedtoday.setHeight(0.12);
  DelayTime.setColor(new util.Color('white'));
  DelayTime.setPos([0.41, (- 0.1)]);
  DelayTime.setText(DelayDays);
  DelayTime.setFont('Arial');
  DelayTime.setHeight(0.12);
  if (subID%2 ==1 ) {
      leftVarText =('today');
      leftVarMoney =(ImMoney);
      rightVarText = (DelayDays);
      rightVarMoney = (DelayMoney);
      }
  if (subID%2 == 0) {
      leftVarText = (DelayDays);
      leftVarMoney = (DelayMoney);
      rightVarText = ('today');
      rightVarMoney = (ImMoney);
      }
  
  ImmedMoneyAmt.setText(leftVarMoney);
  DelayMoneyAmt.setText(rightVarMoney);
  Immedtoday.setText(leftVarText);
  DelayTime.setText(rightVarText);
  blank.setText('');
  // keep track of which components have finished
  PracticeComponents = [];
  PracticeComponents.push(Line);
  PracticeComponents.push(choice);
  PracticeComponents.push(ImmedMoneyAmt);
  PracticeComponents.push(DelayMoneyAmt);
  PracticeComponents.push(Immedtoday);
  PracticeComponents.push(DelayTime);
  PracticeComponents.push(blank);
  
  for (const thisComponent of PracticeComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

function PracticeRoutineEachFrame() {
  //------Loop for each frame of Routine 'Practice'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = PracticeClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Line* updates
  if (t >= 0.0 && Line.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Line.tStart = t;  // (not accounting for frame time here)
    Line.frameNStart = frameN;  // exact frame index
    Line.setAutoDraw(true);
  }

  frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Line.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Line.setAutoDraw(false);
  }
  
  // *choice* updates
  if (t >= 0 && choice.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    choice.tStart = t;  // (not accounting for frame time here)
    choice.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { choice.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { choice.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { choice.clearEvents(); });
  }

  frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (choice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    choice.status = PsychoJS.Status.FINISHED;
  }

  if (choice.status === PsychoJS.Status.STARTED) {
    let theseKeys = choice.getKeys({keyList: ['1', '2'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      choice.keys = theseKeys[0].name;  // just the last key pressed
      choice.rt = theseKeys[0].rt;
    }
  }
  
  
  // *ImmedMoneyAmt* updates
  if (t >= 0 && ImmedMoneyAmt.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    ImmedMoneyAmt.tStart = t;  // (not accounting for frame time here)
    ImmedMoneyAmt.frameNStart = frameN;  // exact frame index
    ImmedMoneyAmt.setAutoDraw(true);
  }

  frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (ImmedMoneyAmt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    ImmedMoneyAmt.setAutoDraw(false);
  }
  
  // *DelayMoneyAmt* updates
  if (t >= 0 && DelayMoneyAmt.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    DelayMoneyAmt.tStart = t;  // (not accounting for frame time here)
    DelayMoneyAmt.frameNStart = frameN;  // exact frame index
    DelayMoneyAmt.setAutoDraw(true);
  }

  frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (DelayMoneyAmt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    DelayMoneyAmt.setAutoDraw(false);
  }
  
  // *Immedtoday* updates
  if (t >= 0 && Immedtoday.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Immedtoday.tStart = t;  // (not accounting for frame time here)
    Immedtoday.frameNStart = frameN;  // exact frame index
    Immedtoday.setAutoDraw(true);
  }

  frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Immedtoday.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Immedtoday.setAutoDraw(false);
  }
  
  // *DelayTime* updates
  if (t >= 0 && DelayTime.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    DelayTime.tStart = t;  // (not accounting for frame time here)
    DelayTime.frameNStart = frameN;  // exact frame index
    DelayTime.setAutoDraw(true);
  }

  frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (DelayTime.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    DelayTime.setAutoDraw(false);
  }
  
  if (choice.keys == '1') {
      ImmedMoneyAmt.setColor('green');
      Immedtoday.setColor('green');
      }
  if (choice.keys == '2'){
      DelayTime.setColor('green');
      DelayMoneyAmt.setColor('green');
      }
  if (choice.keys == '1' or choice.keys == '2') and blank.status == NOT_STARTED {
      blank.tStart = t;
      blank.frameNStart = frameN;
      blank.setAutoDraw(True);
      }
  
  // *blank* updates
  if (t >= 0.0 && blank.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    blank.tStart = t;  // (not accounting for frame time here)
    blank.frameNStart = frameN;  // exact frame index
    blank.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (blank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    blank.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of PracticeComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function PracticeRoutineEnd() {
  //------Ending Routine 'Practice'-------
  for (const thisComponent of PracticeComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('choice.keys', choice.keys);
  if (typeof choice.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('choice.rt', choice.rt);
      }
  
  choice.stop();
  
  ImmedMoneyAmt.setColor('white');
  Immedtoday.setColor('white');
  DelayTime.setColor('white');
  DelayMoneyAmt.setColor('white');
  
  if (blank.status==FINISHED){
      ImmedMoneyAmt.setAutoDraw(False);
      Immedtoday.setAutoDraw(False);
      DelayTime.setAutoDraw(False);
      DelayMoneyAmt.setAutoDraw(False);
      Line.setAutoDraw(False);
      }
  return Scheduler.Event.NEXT;
}

function BeginInstRoutineBegin() {
  //------Prepare to start Routine 'BeginInst'-------
  t = 0;
  BeginInstClock.reset(); // clock
  frameN = -1;
  routineTimer.add(3.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  BeginInstComponents = [];
  BeginInstComponents.push(text_2);
  
  for (const thisComponent of BeginInstComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

function BeginInstRoutineEachFrame() {
  //------Loop for each frame of Routine 'BeginInst'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = BeginInstClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_2* updates
  if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_2.tStart = t;  // (not accounting for frame time here)
    text_2.frameNStart = frameN;  // exact frame index
    text_2.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_2.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of BeginInstComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function BeginInstRoutineEnd() {
  //------Ending Routine 'BeginInst'-------
  for (const thisComponent of BeginInstComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

function CueRoutineBegin() {
  //------Prepare to start Routine 'Cue'-------
  t = 0;
  CueClock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.000000);
  // update component parameters for each repeat
  cue.setText(CueType);
  // keep track of which components have finished
  CueComponents = [];
  CueComponents.push(cue);
  
  for (const thisComponent of CueComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

function CueRoutineEachFrame() {
  //------Loop for each frame of Routine 'Cue'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = CueClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cue* updates
  if (t >= 0.0 && cue.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cue.tStart = t;  // (not accounting for frame time here)
    cue.frameNStart = frameN;  // exact frame index
    cue.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cue.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of CueComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function CueRoutineEnd() {
  //------Ending Routine 'Cue'-------
  for (const thisComponent of CueComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

function EndingRoutineBegin() {
  //------Prepare to start Routine 'Ending'-------
  t = 0;
  EndingClock.reset(); // clock
  frameN = -1;
  routineTimer.add(5.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  EndingComponents = [];
  EndingComponents.push(ThankYou);
  
  for (const thisComponent of EndingComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

function EndingRoutineEachFrame() {
  //------Loop for each frame of Routine 'Ending'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = EndingClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *ThankYou* updates
  if (t >= 0.0 && ThankYou.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    ThankYou.tStart = t;  // (not accounting for frame time here)
    ThankYou.frameNStart = frameN;  // exact frame index
    ThankYou.setAutoDraw(true);
  }

  frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (ThankYou.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    ThankYou.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of EndingComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function EndingRoutineEnd() {
  //------Ending Routine 'Ending'-------
  for (const thisComponent of EndingComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}

function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
