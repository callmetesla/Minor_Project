fr1=1
fr2=2
fl1=3
fl2=4
rr1=5
rr2=6
rl1=7
rl2=8
def forward():
    print("Going Forward")
    GPIO.output(fr1,GPIO.HIGH)
    GPIO.output(fr2,GPIO.LOW)

    GPIO.output(fl1,GPIO.HIGH)
    GPIO.output(fl2,GPIO.LOW)
    
    GPIO.output(rr1,GPIO.HIGH)
    GPIO.output(rr2,GPIO.LOW)
    
    GPIO.output(rl1,GPIO.HIGH)
    GPIO.output(rl2,GPIO.LOW)

def backward():
    print("Going Backward")
    GPIO.output(fr2,GPIO.HIGH)
    GPIO.output(fr1,GPIO.LOW)

    GPIO.output(fl2,GPIO.HIGH)
    GPIO.output(fl1,GPIO.LOW)
    
    GPIO.output(rr2,GPIO.HIGH)
    GPIO.output(rr1,GPIO.LOW)
    
    GPIO.output(rl2,GPIO.HIGH)
    GPIO.output(rl1,GPIO.LOW)

def right():
    print("Going right")
    GPIO.output(fr2,GPIO.HIGH)
    GPIO.output(fr1,GPIO.LOW)

    GPIO.output(fl1,GPIO.HIGH)
    GPIO.output(fl2,GPIO.LOW)
    
    GPIO.output(rr2,GPIO.HIGH)
    GPIO.output(rr1,GPIO.LOW)
    
    GPIO.output(rl1,GPIO.HIGH)
    GPIO.output(rl2,GPIO.LOW)

def left():
    print("Going left")
    GPIO.output(fr1,GPIO.HIGH)
    GPIO.output(fr2,GPIO.LOW)

    GPIO.output(fl2,GPIO.HIGH)
    GPIO.output(fl1,GPIO.LOW)
    
    GPIO.output(rr1,GPIO.HIGH)
    GPIO.output(rr2,GPIO.LOW)
    
    GPIO.output(rl2,GPIO.HIGH)
    GPIO.output(rl1,GPIO.LOW)

def stop():
    print("stop")
    GPIO.output(fr1,GPIO.HIGH)
    GPIO.output(fr2,GPIO.HIGH)

    GPIO.output(fl1,GPIO.HIGH)
    GPIO.output(fl2,GPIO.HIGH)
    
    GPIO.output(rr1,GPIO.HIGH)
    GPIO.output(rr2,GPIO.HIGH)
    
    GPIO.output(rl1,GPIO.HIGH)
    GPIO.output(rl2,GPIO.HIGH)
