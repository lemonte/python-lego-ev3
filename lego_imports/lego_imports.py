#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
from pybricks.iodevices import LUMPDevice, DCMotor


class LegoImports:

  """INICIA A CLASSE MOTOR  MOTOR(PORT)  PORTA DO MOTOR """
  def __init__(self):
    print("#### IMPORTANDO CLASSES DO LEGO ####")

  def getMotor(self):
    return Motor
  
  def getPorta(self):
    return Port

  def getStop(self):
    return Stop
  
  def getColorSensor(self):
    return ColorSensor
  
  def getLUMPDevice(self):
    return LUMPDevice
  
  def getUltrasonicSensor(self):
    return UltrasonicSensor

  def getDCMotor(self):
    return DCMotor
  
  def getDirection(self):
    return Direction

  def getDriveBase(self):
    return DriveBase

  def getEv3Brick(self):
    return EV3Brick