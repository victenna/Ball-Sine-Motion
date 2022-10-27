import pygame,sys,math,random
pygame.init()
screen = pygame.display.set_mode([1000,1000])
img = pygame.image.load('balls1.png')
img=pygame.transform.scale(img,(75,75))

img1 = pygame.image.load('balls11.png')
img1=pygame.transform.scale(img1,(75,75))
clock = pygame.time.Clock()
X,Y=102,681
dx=2
plotPoints = [(102,681)]
plotPoints1 = [(102,322)]
i=-1
angle=0
q=-1
ball_list=[0]*20

for i in range(20):
    ball_list[i]=pygame.image.load('balls'+str(i)+'.png')
    ball_list[i]=pygame.transform.scale(ball_list[i],(75,75))# заявляю изображение

while True:
    angle=angle-5
    screen.fill('gold')
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    X=X+dx

    Y=int(math.sin(X/640.0 * 4 * math.pi) * 200 )+500
    
    Y1=int(math.sin(X/640.0 * 4 * math.pi+math.pi) * 200 )+500
    if X==104:
        n=random.randint(0,19)
        m=random.randint(0,19)
    imgg=pygame.transform.rotate(ball_list[n],angle)
    
    imgg1=pygame.transform.rotate(ball_list[m],angle)
    
    rect=imgg.get_rect(center=(X,Y))
    plotPoints.append([X,Y])
    rect1=imgg1.get_rect(center=(X,Y1))
    plotPoints1.append([X,Y1])
    #print('plot=',plotPoints1)
    
    pygame.draw.line(screen,'black',(102,500),(980,500), 2)
    pygame.draw.line(screen,'black',(102,800),(102,100), 2)
    
    pygame.draw.lines(screen,'blue',False, plotPoints, 4)
    pygame.draw.lines(screen,'brown',False, plotPoints1, 4)
    
    if X>1000:
        pygame.draw.lines(screen,(255,0,0),False, plotPoints, 3)
        plotPoints.clear()
        X,Y=102,681
        Y1=322
        plotPoints = [(X,Y)]
        plotPoints1 = [(X,Y1)]
    screen.blit(imgg, rect)
    screen.blit(imgg1, rect1)
    #pygame.draw.rect(screen,'gold',rect,4)
    pygame.display.update()
    clock.tick(60)
    
