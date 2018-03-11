def initialize():
    #Motor Input pins
    fr1=1
    fr2=2
    fl1=3
    fl2=4
    rr1=5
    rr2=6
    rl1=7
    rl2=8
    #Motor Enables
    fre=22
    frl=22
    rre=22
    rrl=22
    #Motor Init
    GPIO.setup(fr1,GPIO.OUT)
    GPIO.setup(fr2,GPIO.OUT)
    GPIO.setup(fl1,GPIO.OUT)
    GPIO.setup(fl2,GPIO.OUT)
    GPIO.setup(rr1,GPIO.OUT)
    GPIO.setup(rr2,GPIO.OUT)
    GPIO.setup(rl1,GPIO.OUT)
    GPIO.setup(rl2,GPIO.OUT)
    #Motor Enables
    GPIO.setup(fre,GPIO.OUT)
    p1=GPIO.PWM(fre,100)
    GPIO.setup(fle,GPIO.OUT)
    p2=GPIO.PWM(fle,100)
    GPIO.setup(rre,GPIO.OUT)
    p3=GPIO.PWM(rre,100)
    GPIO.setup(rle,GPIO.OUT)
    p4=GPIO.PWM(rle,100)
    #Running at 50% Duty Cycle
    p1.start(50)
    p2.start(50)
    p3.start(50)
    p4.start(50)

