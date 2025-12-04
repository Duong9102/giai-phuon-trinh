import pygame
import random

# --- 1. Thiết lập Cấu hình ---
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Cơ Bản")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont('Arial', 40)

# --- 2. Hằng số và Biến ---
# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Chim
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_size = 30
bird_movement = 0
gravity = 0.5
jump_strength = -10

# Ống
pipe_width = 70
pipe_gap = 200
pipe_speed = 5
pipe_list = []
pipe_spawn_time = 1500  # Đơn vị ms
last_pipe_spawn = pygame.time.get_ticks()

# Trạng thái game
game_active = True
score = 0
high_score = 0

# --- 3. Hàm tạo Ống ---
def create_pipe():
    # Tạo chiều cao ngẫu nhiên cho khe hở
    random_pipe_pos = random.randint(200, SCREEN_HEIGHT - 200)
    bottom_pipe = pygame.Rect(SCREEN_WIDTH, random_pipe_pos + pipe_gap // 2, pipe_width, SCREEN_HEIGHT)
    top_pipe = pygame.Rect(SCREEN_WIDTH, 0, pipe_width, random_pipe_pos - pipe_gap // 2)
    return bottom_pipe, top_pipe

# --- 4. Hàm di chuyển Ống ---
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= pipe_speed
    # Loại bỏ các ống đã ra khỏi màn hình
    return [pipe for pipe in pipes if pipe.right > 0]

# --- 5. Hàm vẽ Ống ---
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= SCREEN_HEIGHT: # Ống dưới
            pygame.draw.rect(screen, GREEN, pipe)
        else: # Ống trên
            pygame.draw.rect(screen, GREEN, pipe)

# --- 6. Hàm kiểm tra va chạm ---
def check_collision(pipes, bird_rect):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False  # Va chạm -> Game Over
    
    # Kiểm tra va chạm sàn và trần
    if bird_rect.top <= -100 or bird_rect.bottom >= SCREEN_HEIGHT: # Giữ chim ở trong màn hình (có thể thay đổi)
        return False
        
    return True # Không va chạm

# --- 7. Hàm cập nhật điểm số ---
def update_score(pipes, score):
    for pipe in pipes:
        # Nếu ống đã vượt qua giữa chim và chưa được tính điểm
        if pipe.centerx < bird_x and pipe.centerx > bird_x - pipe_speed and pipe.bottom >= SCREEN_HEIGHT:
            score += 0.5 # Cộng 0.5 vì mỗi cặp ống là 2 rect (trên, dưới)
            if score == int(score):
                return int(score) # Chỉ trả về khi điểm là số nguyên (qua cả cặp ống)
    return int(score)

# --- 8. Hàm hiển thị điểm số ---
def display_score(score, high_score, y_pos):
    score_surface = FONT.render(f'Score: {int(score)}', True, BLACK)
    screen.blit(score_surface, (10, y_pos))
    
    high_score_surface = FONT.render(f'High Score: {int(high_score)}', True, BLACK)
    screen.blit(high_score_surface, (10, y_pos + 40))

# --- 9. Hàm bắt đầu lại game ---
def reset_game():
    global bird_y, bird_movement, pipe_list, game_active, score
    
    bird_y = SCREEN_HEIGHT // 2
    bird_movement = 0
    pipe_list = []
    game_active = True
    score = 0

# --- 10. Vòng lặp Game Chính ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if game_active:
                    # Nhảy
                    bird_movement = jump_strength
                else:
                    # Bắt đầu lại game
                    reset_game()

    screen.fill(BLUE) # Nền màu xanh

    if game_active:
        # 1. Chim
        bird_movement += gravity
        bird_y += bird_movement
        bird_rect = pygame.Rect(bird_x, int(bird_y), bird_size, bird_size)
        pygame.draw.circle(screen, RED, bird_rect.center, bird_size // 2)

        # 2. Ống
        now = pygame.time.get_ticks()
        if now - last_pipe_spawn > pipe_spawn_time:
            pipe_list.extend(create_pipe())
            last_pipe_spawn = now
            
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # 3. Va chạm
        game_active = check_collision(pipe_list, bird_rect)

        # 4. Điểm số
        score = update_score(pipe_list, score)
        display_score(score, high_score, 10)
        
        # Cập nhật High Score khi game đang chạy
        if score > high_score:
            high_score = score
            
    else:
        # Game Over
        game_over_surface = FONT.render('GAME OVER', True, RED)
        screen.blit(game_over_surface, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
        
        # Hiển thị High Score cuối cùng
        display_score(score, high_score, SCREEN_HEIGHT // 2 + 50)
        
        restart_surface = FONT.render('Press SPACE to Restart', True, BLACK)
        screen.blit(restart_surface, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 100))
        
    
    pygame.display.update()
    clock.tick(60) # Giới hạn khung hình ở 60 FPS

pygame.quit()