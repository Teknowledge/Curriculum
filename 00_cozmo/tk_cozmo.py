# A Simplified Cozmo API
# Used for the Teknowledge Curriculum (teknowledge.xyz)
# Erik Pintar, Dec 2016


import sys
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import random


# the function where you write the program!

def cozmoFunction(sdk_conn):
  global robot
  robot = sdk_conn.wait_for_robot()
  # WRITE YOUR CODE HERE!
  celebrate()














# this is used at the bottom to start it all
def cozmoDoThisFunction(cozmoFunction):
  cozmo.setup_basic_logging()
  try:
    cozmo.connect(cozmoFunction)
  except cozmo.ConnectionError as e:
    sys.exit("A connection error occurred: %s" % e)


# basic movement functions for lab 1
# see http://cozmosdk.anki.com/docs/generated/cozmo.robot.html

# desiredHeight - a number from 0 to 100 (min height to max height)
def moveLiftToHeight(desiredHeight):
  percentHeight = desiredHeight / 100.0
  robot.set_lift_height(percentHeight).wait_for_completed()

# desiredHeight - a number from 0 to 100 (min height to max height)
def moveHeadToHeight(desiredHeight):
  maxAngle = cozmo.robot.MAX_HEAD_ANGLE.degrees
  minAngle = cozmo.robot.MIN_HEAD_ANGLE.degrees
  headAngleRange =  maxAngle - minAngle
  percentHeight = desiredHeight / 100.0
  headAngleDegrees = percentHeight*headAngleRange + minAngle
  headAngle = cozmo.util.degrees(headAngleDegrees)
  robot.set_head_angle(headAngle).wait_for_completed()

# distance - in millimeters
def moveForward(distance):
  robot.drive_straight(distance_mm(distance), speed_mmps(100)).wait_for_completed()

# degreesToTurn - positive for left turn, negative for right
def turnInDegrees(degreesToTurn):
  robot.turn_in_place(degrees(degreesToTurn)).wait_for_completed()
  # maybe use:
  #drive_wheels(l_wheel_speed, r_wheel_speed, l_wheel_acc=None, r_wheel_acc=None, duration=None)


# fun functions

# make Cozmo say a given string, like "Hello World"
def say(text):
  robot.say_text(text).wait_for_completed()

def playAnimation(anim_name):
  robot.play_anim(name=anim_name).wait_for_completed()

def celebrate():
  celebrations = [
    "anim_greeting_happy_03_head_angle_20",
    "anim_reacttoblock_ask_01_head_angle_20",
    "anim_memorymatch_successhand_cozmo_01",
    "anim_memorymatch_solo_successgame_player_01",
    "anim_greeting_happy_03_head_angle_40",
    "anim_speedtap_wingame_intensity02_01",
    "anim_meetcozmo_celebration_02_head_angle_-20",
    "anim_memorymatch_successhand_cozmo_04",
    "anim_sparking_success_01",
    "anim_sparking_success_02",
    "anim_rtpkeepaway_playeryes_02",
    "anim_reacttoblock_success_01"]
  randomAnimation = random.choice(celebrations)
  playAnimation(randomAnimation)

def doSomethingRandom():
  randomCoolAnimations = [
    "anim_freeplay_reacttoface_like_01",
    "anim_memorymatch_failgame_cozmo_01",
    "anim_petdetection_misc_01_head_angle_40",
    "anim_petdetection_dog_02_head_angle_20",
    "anim_memorymatch_failgame_player_02",
    "anim_memorymatch_failhand_player_03",
    "anim_petdetection_dog_01_head_angle_40",
    "anim_bored_event_03",
    "anim_speedtap_loseround_intensity01_01",
    "anim_reacttocliff_edgeliftup_01",
    "anim_memorymatch_reacttopattern_standard_01",
    "anim_cozmosays_getout_short_01",
    "anim_meetcozmo_celebration_02_head_angle_40",
    "anim_memorymatch_reacttopattern_standard_01_-22.5",
    "anim_meetcozmo_celebration",
  ]
  randomAnimation = random.choice(randomCoolAnimations)
  playAnimation(randomAnimation)

def solution():
  # 1 - Hello World
  say("Hello World")
  celebrate()
  # 2 - Hello Master Coder
  moveHeadToHeight(0)
  moveForward(100)
  moveHeadToHeight(100)
  say("Hello Master Coder")
  moveForward(-100)
  celebrate()
  # 3 - Moving Around: Completing The Square
  # BONUS: triangle, star shape!
  moveLiftToHeight(0)
  for i in range(4):
    moveForward(50)
    turnInDegrees(-90) # right turn
  celebrate()
  # 4 - Letter Of Your First Name (letter E below)
  # BONUS: letter of your last name...your whole name?
  say("I will now make the letter E")
  moveLiftToHeight(0)
  moveForward(50)
  turnInDegrees(-90)
  moveForward(50)
  turnInDegrees(-90)
  moveForward(30)
  moveForward(-30)
  turnInDegrees(90)
  moveForward(50)
  turnInDegrees(-90)
  moveForward(50)
  celebrate()
  # 5 - move block back and forth forever
  # Note: requires block to be set up in front of Cozmo
  # BONUS: move two blocks back and forth in an X pattern
  moveLiftToHeight(0)
  moveForward(100)
  moveLiftToHeight(100)
  turnInDegrees(180)
  moveForward(200)
  moveLiftToHeight(0)
  moveForward(-100)
  celebrate()

cozmoDoThisFunction(cozmoFunction)
