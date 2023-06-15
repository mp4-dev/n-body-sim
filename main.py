import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
player = pygame.Rect((300, 250, 50, 50))
run = True

# CONSTANTS
bigG = 6.67e-11
deltaT = 0.0001

class Body:
    def __init__(self, mass, pos, vel, acc, color):
        self.color = color
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.acc = acc
        
s1 = Body(10, [255, 255], [0, 0], [0, 0], (255, 255, 0))
s2 = Body(50, [134, 235], [0, 0], [0, 0], (123, 0, 255))

bodies = [s1, s2]

while run:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

    screen.fill("white")

    for body in bodies:
        force = [0, 0]
        for b in bodies:
            if (body.pos == b.pos):
                continue
            obs = [b.pos[0] - body.pos[0], b.pos[1] - body.pos[1]]
            distance = ((obs[0])**2 + (obs[1])**2)**(1/2)
            rHat = [obs[0]/distance, obs[1]/distance]
            absForce = bigG*body.mass*b.mass/distance
            force[0] += absForce*rHat[0]
            force[1] += absForce*rHat[1]
        body.acc[0] = force[0]/body.mass
        body.acc[1] = force[1]/body.mass
        body.vel[0] += body.acc[0]*deltaT
        body.vel[1] += body.acc[1]*deltaT
        body.pos[0] += body.vel[0]*deltaT
        body.pos[1] += body.pos[1] *deltaT


        
        pygame.draw.circle(screen, body.color, body.pos, body.mass)
    pygame.display.flip()
pygame.quit()
    

