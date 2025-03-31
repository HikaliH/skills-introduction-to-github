#fish thing! hopefully it still works!
#Background
app.background = ('lightCyan')
#white part on top
Rect(0, 0, 400, 40, fill='white')
#list for background colors
backgrounds = ['lightCyan', 'black', 'dodgerBlue', 'darkBlue', 'white']
#variable for which phase it's in
app.phase2 = False
#variable for if the feeding button is clicked
app.feeding = False
# group for fish
shoal = Group()
#variable for the OnSteps function
app.stepsPerSecond = 30
#fish color buttons
fishButtons = list()
red = Polygon(17, 20, 30, 10, 52, 30, 52, 10, 30, 30, fill="red")
fishButtons.append(red)
orange = Polygon(57, 20, 70, 10, 92, 30, 92, 10, 70, 30, fill="orange")
fishButtons.append(orange)
yellow = Polygon(97, 20, 110, 10, 132, 30, 132, 10, 110, 30, fill="gold")
fishButtons.append(yellow)
green = Polygon(137, 20, 150, 10, 172, 30, 172, 10, 150, 30, fill="green")
fishButtons.append(green)
blue = Polygon(177, 20, 190, 10, 212, 30, 212, 10, 190, 30, fill="blue")
fishButtons.append(blue)
purple = Polygon(217, 20, 230, 10, 252, 30, 252, 10, 230, 30, fill="purple")
fishButtons.append(purple)
#"click to choose a color, then click here!" label
clickColor = Label("click a fish to choose a color, then click here!", 200, 200, visible=True, size = 15)

#variable for current fish color
app.fishColor = ""

#function for drawing fish
def drawFish(color, x, y):
    fish = Polygon (x, y, x+13, y-10, x+35, y+10, x+35, y-10, x+13, y+10, fill = color, visible = True)
    #random point for when I scatter them
    fish.goalX = randrange(10, 380)
    fish.goalY = randrange(80, 380)
    if -30<=fish.goalX-x<=30:
        fish.goalX = randrange(10, 390)
    if -30<=fish.goalY-y<=30:
        fish.goalY = randrange(80, 380)
#add to group
    shoal.add(fish)
#label for clear
clear = Label("Clear all", 285, 10)
#label for background
backgroundLabel = Label("Background", 295, 27)
#label for next
next = Label("Next", 370, 20)
#label for +speed
addSpeed = Label("coffee", 120, 20, visible = False)
minusSpeed = Label('naptime', 200, 20, visible = False)
#everything that happens when you click somewhere
def onMouseRelease(mouseX, mouseY):
    #everything for 
    if app.phase2 == False:
#removes 'click to choose color' label
        clickColor.visible = False
    #changes current fish color if you click on fish button
        if mouseY<40:
            if (red.hits(mouseX, mouseY) == True):
                app.fishColor = "red"
            elif (orange.hits(mouseX, mouseY) == True):
                app.fishColor = "orange"
            elif (yellow.hits(mouseX, mouseY) == True):
                app.fishColor = "gold"
            elif (green.hits(mouseX, mouseY) == True):
                app.fishColor = "green"
            elif (blue.hits(mouseX, mouseY) == True):
                app.fishColor = "blue"
            elif (purple.hits(mouseX, mouseY) == True):
                app.fishColor = "purple"
                #clear button
            elif (clear.hits(mouseX, mouseY) == True):
                shoal.clear()
                #changes background when label is clicked,
            elif (backgroundLabel.hits(mouseX, mouseY) == True):
                backgrounds.append(backgrounds[0])
                backgrounds.remove(backgrounds[0])
                app.background = backgrounds[0]
        #does nothing if a color hasn't been selected yet
        elif 50 <= mouseY <= 390:
            if app.fishColor == "":
                pass
            #draws fish with current selected color 
            else:
                drawFish(app.fishColor, mouseX-17, mouseY)
 #hides the food when you release the mouse if currently feeding, and in phase 2
    else:
        if app.feeding == True:
            food.centerX=-10
            food.centerY=-10
#buttons for phase 2
feedLabel = Label('feed', 20, 20, visible = False)
resetLabel = Label('reset', 60, 20, visible = False)
def onMousePress(mouseX, mouseY):
    #if you click next and it's phase 1 it starts phase 2 and hides and reveals all the right buttons
    if app.phase2 == False:
        if next.hits(mouseX, mouseY):
            app.phase2 = True
            clear.visible = False
            backgroundLabel.visible = False
            next.visible = False
            resetLabel.visible = True
            addSpeed.visible = True
            minusSpeed.visible = True
            for buttons in fishButtons:
                buttons.visible = False
            feedLabel.visible = True
            
    #makes the feed button work
    if app.phase2 == True:
        if feedLabel.hits(mouseX, mouseY):
            if app.feeding == False:
                app.feeding = True
            else:
                app.feeding = False
                #reseting to phase 1 if reset label is clicked, hiding and revealing buttons
        if resetLabel.hits(mouseX, mouseY):
            app.stepsPerSecond = 30
            app.phase2 = False
            shoal.clear()
            clear.visible = True
            backgroundLabel.visible = True
            for buttons in fishButtons:
                buttons.visible = True
                feedLabel.visible = False
            resetLabel.visible = False
            app.feeding = False
            next.visible = True
            addSpeed.visible = False
            minusSpeed.visible = False
        if addSpeed.hits(mouseX, mouseY):
            app.stepsPerSecond+=10
        if minusSpeed.hits(mouseX, mouseY):
            app.stepsPerSecond-=10
#global variable for mouseX and mouseY for the onStep feeding function
app.mouseX = 0
app.mouseY = 0
#fish food
food = Circle(-10, -10, 5, fill='peru')
def onMouseDrag(mouseX, mouseY):
    #updating mouseX and mouseY global variables
    app.mouseX = mouseX
    app.mouseY = mouseY
    #moving the food
    if app.feeding == True:
        food.centerX=mouseX
        food.centerY=mouseY
#def for making fish turn and move towards a point
def moveFish(fish, X, Y):
    if fish.centerY<=Y:
        if fish.centerX<=X:
            fish.rotateAngle+=(-135-fish.rotateAngle)/5
            fish.centerY+=1
            fish.centerX+=1
        else:
            fish.rotateAngle+=(-45-fish.rotateAngle)/5
            fish.centerY+=1
            fish.centerX-=1
    elif fish.centerX<=X:
        fish.rotateAngle+=(135-fish.rotateAngle)/5
        fish.centerY-=1
        fish.centerX+=1
    else:
        fish.rotateAngle+=(45-fish.rotateAngle)/5
        fish.centerY-=1
        fish.centerX-=1
#making fish constantly move
def onStep():
    #if currently feeding move fish toward food
    if food.centerX!=-10:
            food.centerX=app.mouseX
            food.centerY=app.mouseY
            for fish in shoal:
                moveFish(fish, app.mouseX, app.mouseY)
    #scattering fish if not currently feeding
    else:
        for fish in shoal:
            if distance(fish.goalX, fish.goalY, fish.centerX, fish.centerY)<10:
                fish.goalX = randrange(10, 390)
                for i in range(5):
                    if -100<=fish.goalX-fish.centerX<100:
                        fish.goalX = randrange(10, 390)
                fish.goalY = randrange(80, 380)
                for i in range (5):
                    if -100<=fish.goalY-fish.centerY<100:
                        fish.goalY = randrange(80, 380)
            else:
                moveFish(fish, fish.goalX, fish.goalY)
