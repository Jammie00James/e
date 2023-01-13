import main as play
p = 1

while(p ==1 ):
    try:
        play.operate() 
    except KeyboardInterrupt:
        p = 0
    except:
        print("restarting")
    else:
        print("running fine")
        p = 0

