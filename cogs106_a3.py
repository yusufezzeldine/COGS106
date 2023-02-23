# -*- coding: utf-8 -*-
"""COGS106_A3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tJiCr2quO2g-QS2LFFVaWYthL84t27MH
"""

#Creating a non-smelly version of the Signal Detection Class

from scipy.special import ndtri

class SignalDetection:
  def __init__(self,hits,misses,false_alarms,correct_rejections):
    # Define variables
    self.hits = hits
    self.misses = misses
    self.false_alarms = false_alarms
    self.correct_rejections = correct_rejections
  
  def hit_rate(self):
    # Calculates the Hit Rate
    return (self.hits / (self.hits + self.misses))

  def false_alarm_rate(self):
    # Calculates the False Alarm Rate 
    return (self.false_alarms / (self.false_alarms + self.correct_rejections))
  
  def d_prime(self):
    # Calculates the d-Prime value
    return (ndtri(self.hit_rate()) - ndtri(self.false_alarm_rate()))
  
  def criterion(self):
    # Calculates the Criterion value
    return (-0.5 * (ndtri(self.hit_rate()) + ndtri(self.false_alarm_rate())))

## Testing if the class works correctly, and if the objects can be corrupted

import unittest
import numpy as np
import matplotlib.pyplot as plt

class TestSignalDetection(unittest.TestCase):
    def test_d_prime_zero(self):
        sd   = SignalDetection(15, 5, 15, 5)
        expected = 0
        obtained = sd.d_prime()
        # Compare calculated and expected d-prime
        self.assertAlmostEqual(obtained, expected, places=6)
    def test_d_prime_nonzero(self):
        sd   = SignalDetection(15, 10, 15, 5)
        expected = -0.421142647060282
        obtained = sd.d_prime()
        # Compare calculated and expected d-prime
        self.assertAlmostEqual(obtained, expected, places=6)
    def test_criterion_zero(self):
        sd   = SignalDetection(5, 5, 5, 5)
        # Calculate expected criterion        
        expected = 0
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertAlmostEqual(obtained, expected, places=6)
    def test_criterion_nonzero(self):
        sd   = SignalDetection(15, 10, 15, 5)
        # Calculate expected criterion        
        expected = -0.463918426665941
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertAlmostEqual(obtained, expected, places=6)
    def test_object_corruption(self):
        sd   = SignalDetection(15, 5, 15, 5)
        expected = sd.d_prime()
        sd.hits = 1824
        sd.misses = 1248
        sd.false_alarms = 1248
        sd.correct_rejections = 2142
        obtained = sd.d_prime()
        # Compare original and corrupted d-prime
        self.assertAlmostEqual(obtained, expected, places=6)

if __name__ == '__main__':
    unittest.main(argv=['ignored'], exit=False)

#Fixing the Signal Detection Class to prevent objects from being corrupted

class SignalDetection:
  def __init__(self,hits,misses,false_alarms,correct_rejections):
    # Define variables
    self.__hits = hits
    self.__misses = misses
    self.__false_alarms = false_alarms
    self.__correct_rejections = correct_rejections
  
  def hit_rate(self):
    # Calculates the Hit Rate
    return (self.__hits / (self.__hits + self.__misses))

  def false_alarm_rate(self):
    # Calculates the False Alarm Rate 
    return (self.__false_alarms / (self.__false_alarms + self.__correct_rejections))
  
  def d_prime(self):
    # Calculates the d-Prime value
    return (ndtri(self.hit_rate()) - ndtri(self.false_alarm_rate()))
  
  def criterion(self):
    # Calculates the Criterion value
    return (-0.5 * (ndtri(self.hit_rate()) + ndtri(self.false_alarm_rate())))

## Running the test again to see if the objects are non-corruptable now

import unittest
import numpy as np
import matplotlib.pyplot as plt

class TestSignalDetection(unittest.TestCase):
    def test_d_prime_zero(self):
        sd   = SignalDetection(15, 5, 15, 5)
        expected = 0
        obtained = sd.d_prime()
        # Compare calculated and expected d-prime
        self.assertAlmostEqual(obtained, expected, places=6)
    def test_d_prime_nonzero(self):
        sd   = SignalDetection(15, 10, 15, 5)
        expected = -0.421142647060282
        obtained = sd.d_prime()
        # Compare calculated and expected d-prime
        self.assertAlmostEqual(obtained, expected, places=6)
    def test_criterion_zero(self):
        sd   = SignalDetection(5, 5, 5, 5)
        # Calculate expected criterion        
        expected = 0
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertAlmostEqual(obtained, expected, places=6)
    def test_criterion_nonzero(self):
        sd   = SignalDetection(15, 10, 15, 5)
        # Calculate expected criterion        
        expected = -0.463918426665941
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertAlmostEqual(obtained, expected, places=6)
    def test_object_corruption(self):
        sd   = SignalDetection(15, 5, 15, 5)
        expected = sd.d_prime()
        sd.__hits = 1824
        sd.__misses = 1248
        sd.__false_alarms = 1248
        sd.__correct_rejections = 2142
        obtained = sd.d_prime()
        # Compare original and corrupted d-prime
        self.assertAlmostEqual(obtained, expected, places=6)

if __name__ == '__main__':
    unittest.main(argv=['ignored'], exit=False)

# Overload + and * operators for SignalDetection class 

class SignalDetection:
  def __init__(self,hits,misses,false_alarms,correct_rejections):
    # Define variables
    self.__hits = hits
    self.__misses = misses
    self.__false_alarms = false_alarms
    self.__correct_rejections = correct_rejections
  
  def hit_rate(self):
    # Calculates the Hit Rate
    return (self.__hits / (self.__hits + self.__misses))

  def false_alarm_rate(self):
    # Calculates the False Alarm Rate 
    return (self.__false_alarms / (self.__false_alarms + self.__correct_rejections))
  
  def d_prime(self):
    # Calculates the d-Prime value
    return (ndtri(self.hit_rate()) - ndtri(self.false_alarm_rate()))
  
  def criterion(self):
    # Calculates the Criterion value
    return (-0.5 * (ndtri(self.hit_rate()) + ndtri(self.false_alarm_rate())))

  def __add__(self, other):
    return SignalDetection(self.__hits + other.__hits, self.__misses + other.__misses, self.__false_alarms + other.__false_alarms, self.__correct_rejections + other.__correct_rejections)

  def __mul__(self, scalar):
    return SignalDetection(self.__hits * scalar, self.__misses * scalar, self.__false_alarms * scalar, self.__correct_rejections * scalar)

# Updated unit test to include + and * operators 
import unittest

class TestSignalDetection(unittest.TestCase):

    def test_d_prime_zero(self):
        sd   = SignalDetection(15, 5, 15, 5)
        expected = 0
        obtained = sd.d_prime()
        # Compare calculated and expected d-prime
        self.assertAlmostEqual(obtained, expected, places=10)

    def test_d_prime_nonzero(self):
        sd   = SignalDetection(15, 10, 15, 5)
        expected = -0.421142647060282
        obtained = sd.d_prime()
        # Compare calculated and expected d-prime
        self.assertAlmostEqual(obtained, expected, places=10)

    def test_criterion_zero(self):
        sd   = SignalDetection(5, 5, 5, 5)
        # Calculate expected criterion
        expected = 0
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertAlmostEqual(obtained, expected, places=10)

    def test_criterion_nonzero(self):
        sd   = SignalDetection(15, 10, 15, 5)
        # Calculate expected criterion
        expected = -0.463918426665941
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertAlmostEqual(obtained, expected, places=10)

    def test_addition(self):
        sd = SignalDetection(1, 1, 2, 1) + SignalDetection(2, 1, 1, 3)
        expected = SignalDetection(3, 2, 3, 4).criterion()
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertEqual(obtained, expected)

    def test_multiplication(self):
        sd = SignalDetection(1, 2, 3, 1) * 4
        expected = SignalDetection(4, 8, 12, 4).criterion()
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertEqual(obtained, expected)

if __name__ == '__main__':
    unittest.main(argv=['ignored'], exit=False)

# Introduce method to plot ROC curve in SignalDetection class

class SignalDetection:
  def __init__(self,hits,misses,false_alarms,correct_rejections):
    # Define variables
    self.__hits = hits
    self.__misses = misses
    self.__false_alarms = false_alarms
    self.__correct_rejections = correct_rejections
  
  def hit_rate(self):
    # Calculates the Hit Rate
    return (self.__hits / (self.__hits + self.__misses))

  def false_alarm_rate(self):
    # Calculates the False Alarm Rate 
    return (self.__false_alarms / (self.__false_alarms + self.__correct_rejections))
  
  def d_prime(self):
    # Calculates the d-Prime value
    return (ndtri(self.hit_rate()) - ndtri(self.false_alarm_rate()))
  
  def criterion(self):
    # Calculates the Criterion value
    return (-0.5 * (ndtri(self.hit_rate()) + ndtri(self.false_alarm_rate())))

  def __add__(self, other):
    return SignalDetection(self.__hits + other.__hits, self.__misses + other.__misses, self.__false_alarms + other.__false_alarms, self.__correct_rejections + other.__correct_rejections)

  def __mul__(self, scalar):
    return SignalDetection(self.__hits * scalar, self.__misses * scalar, self.__false_alarms * scalar, self.__correct_rejections * scalar)
  
  def plot_ROC(self):
    plt.plot([0,self.false_alarm_rate(),1], [0,self.hit_rate(),1])
    plt.xlabel("False Positive")
    plt.ylabel("True Positive")
    plt.show()

sd = SignalDetection(10,2,5,20)
sd.plot_ROC()