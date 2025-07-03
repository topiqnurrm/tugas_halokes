import math
import random
import sys
import os
import neat
import pygame

# Konstanta untuk ukuran layar
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# Dapatkan resolusi layar aktual
pygame.init()
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h

# Hitung scaling factor dengan mempertahankan aspek rasio
SCALE = min(SCREEN_WIDTH / WINDOW_WIDTH, SCREEN_HEIGHT / WINDOW_HEIGHT)

# Ukuran mobil yang disesuaikan dengan skala
CAR_SIZE_X = int(60 * SCALE)
CAR_SIZE_Y = int(60 * SCALE)

# Ukuran map yang disesuaikan
MAP_WIDTH = int(WINDOW_WIDTH * SCALE)
MAP_HEIGHT = int(WINDOW_HEIGHT * SCALE)

# Warna untuk deteksi tabrakan
BORDER_COLOR = (255, 255, 255, 255)

# Warna untuk background status
STATUS_BG_COLOR = (0, 0, 0, 180)  # Hitam dengan transparansi
STATUS_TEXT_COLOR = (255, 255, 255)  # Putih
STATUS_PADDING = int(20 * SCALE)  # Padding untuk background status

# Inisialisasi penghitung generasi
current_generation = 0

class Car:
    def __init__(self, sprite_path):
        # Memuat dan mengatur sprite mobil
        self.sprite = pygame.image.load(sprite_path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (CAR_SIZE_X, CAR_SIZE_Y))
        self.rotated_sprite = self.sprite 

        # Posisi awal mobil (disesuaikan dengan skala)
        self.position = [int(830 * SCALE), int(920 * SCALE)]
        self.angle = 0
        self.speed = 0
        self.speed_set = False

        # Menghitung titik tengah mobil
        self.center = [self.position[0] + CAR_SIZE_X / 2, self.position[1] + CAR_SIZE_Y / 2]

        # List untuk sensor radar
        self.radars = []
        self.drawing_radars = []

        # Status mobil
        self.alive = True
        self.distance = 0
        self.time = 0

    def draw(self, screen):
        screen.blit(self.rotated_sprite, self.position)
        self.draw_radar(screen)

    def draw_radar(self, screen):
        for radar in self.radars:
            position = radar[0]
            pygame.draw.line(screen, (0, 255, 0), self.center, position, 1)
            pygame.draw.circle(screen, (0, 255, 0), position, 5)

    def check_collision(self, game_map):
        self.alive = True
        for point in self.corners:
            # Memastikan point berada dalam batas layar
            x = min(max(int(point[0]), 0), MAP_WIDTH - 1)
            y = min(max(int(point[1]), 0), MAP_HEIGHT - 1)
            try:
                if game_map.get_at((x, y)) == BORDER_COLOR:
                    self.alive = False
                    break
            except IndexError:
                self.alive = False
                break

    def check_radar(self, degree, game_map):
        length = 0
        x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
        y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

        while length < int(300 * SCALE):
            try:
                if (x < 0 or x >= MAP_WIDTH or y < 0 or y >= MAP_HEIGHT or 
                    game_map.get_at((x, y)) == BORDER_COLOR):
                    break
            except IndexError:
                break
            
            length += 1
            x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
            y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

        dist = int(math.sqrt(math.pow(x - self.center[0], 2) + math.pow(y - self.center[1], 2)))
        self.radars.append([(x, y), dist])

    def update(self, game_map):
        if not self.speed_set:
            self.speed = 20 * SCALE
            self.speed_set = True

        # Update posisi dan rotasi
        self.rotated_sprite = self.rotate_center(self.sprite, self.angle)
        
        # Update posisi dengan batasan layar
        new_x = self.position[0] + math.cos(math.radians(360 - self.angle)) * self.speed
        new_y = self.position[1] + math.sin(math.radians(360 - self.angle)) * self.speed
        
        self.position[0] = max(0, min(new_x, MAP_WIDTH - CAR_SIZE_X))
        self.position[1] = max(0, min(new_y, MAP_HEIGHT - CAR_SIZE_Y))

        # Update center
        self.center = [int(self.position[0]) + CAR_SIZE_X / 2, int(self.position[1]) + CAR_SIZE_Y / 2]

        # Calculate corners
        length = 0.5 * CAR_SIZE_X
        left_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 30))) * length,
                   self.center[1] + math.sin(math.radians(360 - (self.angle + 30))) * length]
        right_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 150))) * length,
                    self.center[1] + math.sin(math.radians(360 - (self.angle + 150))) * length]
        left_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 210))) * length,
                      self.center[1] + math.sin(math.radians(360 - (self.angle + 210))) * length]
        right_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 330))) * length,
                       self.center[1] + math.sin(math.radians(360 - (self.angle + 330))) * length]
        self.corners = [left_top, right_top, left_bottom, right_bottom]

        self.check_collision(game_map)
        self.radars.clear()
        for d in range(-90, 120, 45):
            self.check_radar(d, game_map)

        # Update jarak
        self.distance += self.speed
        self.time += 1

    def get_data(self):
        radars = self.radars
        return_values = [0, 0, 0, 0, 0]
        for i, radar in enumerate(radars):
            return_values[i] = int(radar[1] / (30 * SCALE))
        return return_values

    def is_alive(self):
        return self.alive

    def get_reward(self):
        return self.distance / (CAR_SIZE_X / 2)

    def rotate_center(self, image, angle):
        rectangle = image.get_rect()
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_rectangle = rectangle.copy()
        rotated_rectangle.center = rotated_image.get_rect().center
        rotated_image = rotated_image.subsurface(rotated_rectangle).copy()
        return rotated_image
    pass

def draw_status_text(screen, text, font, position, padding=STATUS_PADDING):
    # Render teks
    text_surface = font.render(text, True, STATUS_TEXT_COLOR)
    text_rect = text_surface.get_rect()
    text_rect.center = position
    
    # Buat background surface dengan alpha channel
    bg_surface = pygame.Surface((text_rect.width + padding * 2, text_rect.height + padding), pygame.SRCALPHA)
    pygame.draw.rect(bg_surface, STATUS_BG_COLOR, bg_surface.get_rect(), border_radius=int(10 * SCALE))
    
    # Blit background dan teks
    bg_rect = bg_surface.get_rect(center=position)
    screen.blit(bg_surface, bg_rect)
    screen.blit(text_surface, text_rect)

def run_simulation(genomes, config):
    global current_generation
    current_generation += 1

    nets = []
    cars = []

    # Daftar gambar mobil
    car_sprites = ['mobil1.png', 'mobil2.png', 'mobil3.png', 'mobil4.png']

    # Inisialisasi layar dengan double buffering
    screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT), pygame.FULLSCREEN | pygame.DOUBLEBUF)
    pygame.display.set_caption("Car AI")
    
    # Optimasi pygame
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

    # Load dan skala map (Hilangkan # untuk ganti jalur)
    game_map = pygame.image.load('jalur1.png').convert_alpha()
    # game_map = pygame.image.load('jalur2.png').convert_alpha()
    # game_map = pygame.image.load('jalur3.png').convert_alpha()
    # game_map = pygame.image.load('jalur4.png').convert_alpha()
    # game_map = pygame.image.load('jalur5.png').convert_alpha()
    game_map = pygame.transform.scale(game_map, (MAP_WIDTH, MAP_HEIGHT))

    # Background
    background = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))
    background.fill((128, 128, 128))

    for i, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        
        # Pilih gambar mobil secara acak
        sprite_path = random.choice(car_sprites)
        cars.append(Car(sprite_path))

    # Font setup
    generation_font = pygame.font.SysFont("Arial", int(30 * SCALE))
    alive_font = pygame.font.SysFont("Arial", int(20 * SCALE))

    counter = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)

        # Update cars
        still_alive = 0
        for i, car in enumerate(cars):
            if car.is_alive():
                still_alive += 1
                car.update(game_map)
                genomes[i][1].fitness += car.get_reward()

                # AI controls
                output = nets[i].activate(car.get_data())
                choice = output.index(max(output))
                if choice == 0:
                    car.angle += 10
                elif choice == 1:
                    car.angle -= 10
                elif choice == 2:
                    if(car.speed - 2 >= 12 * SCALE):
                        car.speed -= 2
                else:
                    car.speed += 2

        if still_alive == 0:
            break

        counter += 1
        if counter == 30 * 40:
            break

        # Draw
        screen.blit(background, (0, 0))
        screen.blit(game_map, (0, 0))

        for car in cars:
            if car.is_alive():
                car.draw(screen)

        # Draw stats dengan background
        draw_status_text(
            screen,
            f"Generasi: {current_generation}",  # Ubah teks ini
            generation_font,
            (MAP_WIDTH // 2, MAP_HEIGHT // 2)
        )

        draw_status_text(
            screen,
            f"Mobil Aktif: {still_alive}",  # Ubah teks ini
            alive_font,
            (MAP_WIDTH // 2, (MAP_HEIGHT // 2) + int(40 * SCALE))
        )

        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)

if __name__ == "__main__":
    # Load konfigurasi NEAT
    config_path = "./config.txt"
    config = neat.config.Config(neat.DefaultGenome,
                              neat.DefaultReproduction,
                              neat.DefaultSpeciesSet,
                              neat.DefaultStagnation,
                              config_path)

    # Inisialisasi populasi dan reporter
    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)
    
    # Jalankan simulasi
    population.run(run_simulation, 1000)