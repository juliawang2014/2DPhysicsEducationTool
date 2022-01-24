# import pygame
from numpy import true_divide
import pygame
from math import sqrt

class force:
    def __init__(self):
        pass
    def calculateForce(self, mass, acceleration):
        force = mass*acceleration
        return force

class drag:
    def __init__(self):
        pass
    def calculateDrag(self, coefficient, density, velocity, area):
        drag = coefficient*density*(sqrt(velocity)/2)*area
        return drag

class friction:
    def __init__(self):
        pass
    def calculateFriction (self, coefficientFriction, normalFroce):
        friction = coefficientFriction*normalFroce
        return friction

class normalForce:
    def __init__(self):
        pass
    def calculateNormalForce (self, mass, gravity):
        normalForce = mass*gravity
        return normalForce

class springForce:
    def __init__(self):
        pass
    def calculateSpringForce (self, constant, equilibrium, displacement):
        springForce = constant*(displacement - equilibrium)
        return springForce

class elasticEnergy:
    def __init__(self):
        pass
    def calculateElasticEnergy (self, constant, displacement):
        elasticEnergy = (1/2)*constant*sqrt(displacement)
        return elasticEnergy

class inelasticCollisons:
    def __init__(self):
        pass
    def calculateInelasticCollision (self, mass1, mass2, initialV1, initialV2):
        inelasticCollisons = (mass1*initialV1 + mass2*initialV2)/(mass1 + mass2)
        return inelasticCollisons
