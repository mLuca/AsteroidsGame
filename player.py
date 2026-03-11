import circleshape, pygame
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_RADIUS, PLAYER_TURN_SPEED, LINE_WIDTH
from shot import Shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
        self.forward = pygame.Vector2(0, 1).rotate(self.rotation)
    
    def triangle(self):
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + self.forward * self.radius
        b = self.position - self.forward * self.radius - right
        c = self.position - self.forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH )
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        self.position += self.forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shoot_cooldown <= 0:
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            shot_position = self.position + (self.forward * self.radius)
            new_shot = Shot(shot_position.x, shot_position.y)
            new_shot.velocity = self.forward * PLAYER_SHOOT_SPEED


    def update(self, dt):
        self.shoot_cooldown = self.shoot_cooldown - dt if self.shoot_cooldown > 0 else 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.forward = pygame.Vector2(0, 1).rotate(self.rotation)