# A Simplified Cozmo API
# Used for the Teknowledge Curriculum (teknowledge.xyz)
# Erik Pintar, Dec 2016


import sys
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import random
import asyncio
import time


# the function where you write the program!

def cozmoFunction(sdk_conn):
  global conn
  conn = sdk_conn
  global robot
  robot = sdk_conn.wait_for_robot()
  time.sleep(0.5) # to make sure everything is detected
  # WRITE YOUR CODE HERE!
  solution()




def solution():
  # 1 - celebrate when you see a face
  # while True:
  #   face = getFaceIfSeen()
  #   if (face):
  #     celebrate()
  # 2 - tell me what I am feeling if it is not neutral
  # while True:
  #   face = getFaceIfSeen()
  #   if (face):
  #     expression = getFacialExpression(face)
  #     if (expression):
  #       say(expression)
  # 3 - change color of the cube that cozmo sees (extra: cycle colors)
  # while True:
  #   cube = getCubeIfSeen()
  #   if (cube):
  #     setCubeColor(cube, getRandomColor())
  # 4 - set cubes to three different colors then have cozmo tell you which
  #   color cube he sees
  # cube1 = getCube(1)
  # setCubeColor(cube1, (255,0,0))
  # cube2 = getCube(2)
  # setCubeColor(cube2, (0,255,0))
  # cube3 = getCube(3)
  # setCubeColor(cube3, (0,0,255))
  # while True:
  #   cube = getCubeIfSeen()
  #   if (cube == cube1):
  #     say("red cube")
  #   if (cube == cube2):
  #     say("green cube")
  #   if (cube == cube3):
  #     say("blue cube")
  # 5 - make a game where cozmo tells you to show him a color cube
  # cube1 = getCube(1)
  # setCubeColor(cube1, (255,0,0))
  # cube2 = getCube(2)
  # setCubeColor(cube2, (0,255,0))
  # cube3 = getCube(3)
  # setCubeColor(cube3, (0,0,255))
  # wantCube = None
  # while True:
  #   if (not wantCube):
  #     wantCube = getRandomCube()
  #     if (wantCube == cube1):
  #       say("show me red")
  #     if (wantCube == cube2):
  #       say("show me green")
  #     if (wantCube == cube3):
  #       say("show me blue")
  #   else:
  #     cube = getCubeIfSeen()
  #     if (cube == wantCube):
  #       say("good job")
  #       wantCube = None
  #     else:
  #       say("no that is wrong")
  # BONUS CHALLENGE: make a game where you have to show a color cube AND
  #   a facial expression at the same time
  # cube1 = getCube(1)
  # setCubeColor(cube1, (255,0,0))
  # cube2 = getCube(2)
  # setCubeColor(cube2, (0,255,0))
  # cube3 = getCube(3)
  # setCubeColor(cube3, (0,0,255))
  # wantCube = None
  # while True:
  #   if (not wantCube):
  #     wantCube = getRandomCube()
  #     wantExpression = getRandomExpression()
  #     if (wantCube == cube1):
  #       colorStr = "show me red"
  #     elif (wantCube == cube2):
  #       colorStr = "show me green"
  #     elif (wantCube == cube3):
  #       colorStr = "show me blue"
  #     say(colorStr + " and be " + wantExpression)
  #   else:
  #     cube = getCubeIfSeen()
  #     if (cube == wantCube):
  #       face = getFaceIfSeen()
  #       if (face):
  #         expression = getFacialExpression(face)
  #         if (expression == wantExpression):
  #           say("good job")
  #           wantCube = None
  #         elif (expression):
  #           say("don't be "+ expression + " but be " + wantExpression)
  #     elif (cube):
  #       say("wrong cube. " + colorStr)

# alternative function used at the bottom to start it all but with CAMERA
def cozmoDoThisFunctionWithCameraFeed(cozmoFunction):
  cozmo.setup_basic_logging()
  try:
    cozmo.connect_with_tkviewer(cozmoFunction, force_on_top=True)
  except cozmo.ConnectionError as e:
    sys.exit("A connection error occurred: %s" % e)

# this is usually used at the bottom to start it all
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


# lab 2 functions - cozmo noticing things


# timeout - how many seconds it should wait to see a face
# returns Face object if seen, otherwise None
def getFaceIfSeen(timeout=0.1):
  try:
    face = robot.world.wait_for_observed_face(timeout=timeout)
    return face
  except asyncio.TimeoutError:
    return None

# enable (optional) - True/False whether to enable facial expression detection
#   (which slows down processing time)
def detectFacialExpressions(enable=True):
  robot.enable_facial_expression_estimation(enable=enable)

# face - a Face object
# returns a string or None, one of ["happy", "sad", "surprised", "angry", None]
# returns None is face is "neutral"
def getFacialExpression(face):
  return face.expression if face.expression != "neutral" else None

# returns random expression of ["happy", "sad", "surprised", "angry"]
def getRandomExpression():
  return random.choice(["happy", "sad", "surprised", "angry"])

# timeout - how many seconds it should wait to see a cube
# returns Cube object if seen, otherwise None
def getCubeIfSeen(timeout=0.1):
  try:
    cube = robot.world.wait_for_observed_light_cube(timeout=timeout)
    return cube
  except asyncio.TimeoutError:
    return None

# n - number of the cube, one of [1,2,3]
def getCube(n):
  if n == 1:
    return robot.world.light_cubes.get(cozmo.objects.LightCube1Id)
  elif n == 2:
    return robot.world.light_cubes.get(cozmo.objects.LightCube2Id)
  elif n == 3:
    return robot.world.light_cubes.get(cozmo.objects.LightCube3Id)
  else:
    print("You tried to get a cube number that doesn't exist! number:", n)

# returns a random cube of cube 1, 2, or 3
def getRandomCube():
  return random.choice([getCube(1), getCube(2), getCube(3)])

# returns a random color tuple, like (33,205,176)
def getRandomColor():
  return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# cube - a Cube object
# rgbTuple - a red-green-blue tuple like (0,255,0) which is green
#   (use numbers 0-255 only)
# turns the cube lights on to the specified color
def setCubeColor(cube, rgbTuple):
  color = cozmo.lights.Color(rgb=rgbTuple)
  cube.set_lights(cozmo.lights.Light(on_color=color))
  
# cube - a Cube object
# turns the cube lights off
def setCubeLightOff(cube):
  cube.set_lights(cozmo.lights.off_light)


cozmoDoThisFunctionWithCameraFeed(cozmoFunction)
