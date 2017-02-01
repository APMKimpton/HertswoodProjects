import time

loop1 = True

checker = int(input ("Write 1 for a stopwatch or 2 for a countdown :"))
if checker == 1:
    hours = int(input("Please enter the starting hours: "))
    mins = int(input("Please enter the starting minutes: "))
    secs = int(input("Please enter the starting seconds: "))
elif checker == 2:
    hours = int(input("Please enter the starting hours: "))
    mins = int(input("Please enter the starting minutes: "))
    secs = int(input("Please enter the starting seconds: "))
else:
    loop1 = False
    print("You did not enter enter either 1 or 2 - please restart the program!")


              
if checker == 1:
    while loop1:
        time.sleep(1)
        secs=secs+1
        if secs == 60:
            secs = 0
            mins = mins+1
        if mins == 60:
            mins = 0
            hours = hours+1
        
        if hours < 10:
            hours_txt = '0'+str(hours)
        else:
            hours_txt = str(hours)
        
        if mins < 10:
            mins_txt = '0'+str(mins)
        else:
            mins_txt = str(mins)

        if secs < 10:
            secs_txt = '0'+str(secs)
        else:
            secs_txt = str(secs)
        
        print(hours_txt+':'+mins_txt+':'+secs_txt)

              
elif checker == 2:
              
    while loop1:
        time.sleep(1)
        secs=secs-1
        if secs == 0:
            s3ecs = 59
            if mins == 0:
                mins = 0
                secs = 0
            else:
                mins = mins-1
                secs = 59
        if mins == 0:
            mins = 59
            if hours == 0:
                hours = 0
                mins = 0
            else:
                hours = hours-1
                mins = 59
        
        if hours < 10:
            hours_txt = '0'+str(hours)
        else:
            hours_txt = str(hours)
        
        if mins < 10:
            mins_txt = '0'+str(mins)
        else:
            mins_txt = str(mins)

        if secs < 10:
            secs_txt = '0'+str(secs)
        else:
            secs_txt = str(secs)

        if hours == 0:
            if mins == 0:
                if secs == 0:
                    print("Finished!")
                    loop1 = False
        if loop1 == True:
            print(hours_txt+':'+mins_txt+':'+secs_txt)
    



    
