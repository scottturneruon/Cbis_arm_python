from microbit import *


def base(N,choice):
    if choice==1:
        pin0.write_digital(1)
        pin1.write_digital(0)
        sleep(N)
    if choice==2:
        pin0.write_digital(0)
        pin1.write_digital(1)
        sleep(N)

def shoulder(N,choice):
    if choice==1:
        pin8.write_digital(1)
        pin12.write_digital(0)
        sleep(N)
    if choice==2:
        pin8.write_digital(0)
        pin12.write_digital(1)
        sleep(N)
        
def elbow(N,choice):
    if choice==1:
        pin2.write_digital(1)
        pin13.write_digital(0)
        sleep(N)
    if choice==2:
        pin2.write_digital(0)
        pin13.write_digital(1)
        sleep(N)

def wrist(N,choice):
    if choice==1:
        pin14.write_digital(1)
        pin15.write_digital(0)
        sleep(N)
    if choice==2:
        pin14.write_digital(0)
        pin15.write_digital(1)
        sleep(N)

def motor5(N,choice):
    if choice==1:
        pin16.write_digital(1)
        pin11.write_digital(0)
        sleep(N)
    if choice==2:
        pin16.write_digital(0)
        pin11.write_digital(1)
        sleep(N)        
    
def stopIt(N):
    pin0.write_digital(0)
    pin1.write_digital(0)
    pin8.write_digital(0)
    pin12.write_digital(0)
    pin2.write_digital(0)
    pin13.write_digital(0)
    pin14.write_digital(0)
    pin15.write_digital(0)
    pin16.write_digital(0)
    pin11.write_digital(0)
    sleep(N)

while True:
    base(1000,2)
    stopIt(1000)
    base(1000,1)
    stopIt(1000)
    shoulder(1000,2)
    stopIt(1000)
    shoulder(1000,1)
    stopIt(1000)
    elbow(1000,2)
    stopIt(1000)
    elbow(1000,1)
    stopIt(1000)
    wrist(1000,2)
    stopIt(1000)
    wrist(1000,1)
    stopIt(1000)
    motor5(1000,2)
    stopIt(1000)
    motor5(1000,1)
    stopIt(1000)
