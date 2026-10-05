import pygame
import sys

pygame.init()

# --------------------------------------------------
# WINDOW
# --------------------------------------------------
# PIXEL RAPPER
# --------------------------------------------------

def draw_rapper(x, y, style):

    # HEAD
    pygame.draw.rect(screen, (220, 170, 130), (x, y, 32, 32))

    # HAIR / HEAD STYLE

    if style == "cool":
        # Rasta locks
        pygame.draw.rect(screen, (20, 20, 20), (x, y, 32, 7))
        pygame.draw.rect(screen, (20, 20, 20), (x - 5, y + 4, 5, 14))
        pygame.draw.rect(screen, (20, 20, 20), (x - 2, y + 16, 5, 14))
        pygame.draw.rect(screen, (20, 20, 20), (x + 2, y + 5, 5, 15))
        pygame.draw.rect(screen, (20, 20, 20), (x + 7, y + 4, 5, 18))
        pygame.draw.rect(screen, (20, 20, 20), (x + 13, y + 5, 5, 16))
        pygame.draw.rect(screen, (20, 20, 20), (x + 19, y + 4, 5, 18))
        pygame.draw.rect(screen, (20, 20, 20), (x + 25, y + 5, 5, 15))
        pygame.draw.rect(screen, (20, 20, 20), (x + 30, y + 7, 5, 18))

    elif style == "player":
        # Player - default character
        pygame.draw.rect(screen, (55, 35, 20), (x + 2, y - 3, 28, 9))
        pygame.draw.rect(screen, (55, 35, 20), (x - 1, y + 2, 6, 9))
        pygame.draw.rect(screen, (55, 35, 20), (x + 27, y + 2, 6, 9))

    elif style == "superordinary":
        # Messy dark hair
        pygame.draw.rect(screen, (35, 25, 20), (x, y - 3, 32, 9))
        pygame.draw.rect(screen, (35, 25, 20), (x - 3, y + 2, 8, 13))
        pygame.draw.rect(screen, (35, 25, 20), (x + 24, y + 1, 8, 12))

    elif style == "small_l":
        # Oversized cap
        pygame.draw.rect(screen, (40, 70, 120), (x - 2, y - 5, 36, 8))
        pygame.draw.rect(screen, (40, 70, 120), (x + 3, y - 9, 25, 7))
        pygame.draw.rect(screen, (40, 70, 120), (x + 25, y + 1, 12, 4))

    elif style == "white_thought":
        # Brown / black messy hair
        pygame.draw.rect(screen, (45, 25, 15), (x, y - 3, 32, 9))
        pygame.draw.rect(screen, (25, 20, 15), (x - 2, y + 2, 7, 12))
        pygame.draw.rect(screen, (25, 20, 15), (x + 25, y + 1, 7, 10))

    elif style == "smartienem":
        # Short blond hair
        pygame.draw.rect(screen, (210, 190, 120), (x, y - 3, 32, 9))
        pygame.draw.rect(screen, (210, 190, 120), (x + 3, y - 7, 8, 7))
        pygame.draw.rect(screen, (210, 190, 120), (x + 13, y - 8, 8, 8))
        pygame.draw.rect(screen, (210, 190, 120), (x + 23, y - 5, 7, 6))

    elif style == "water_wrld":
        # Water WRLD - dark dreadlocks + blue streak
        pygame.draw.rect(screen, (18, 18, 22), (x, y - 4, 32, 10))

        # Dreadlocks
        pygame.draw.rect(screen, (18, 18, 22), (x - 5, y, 6, 15))
        pygame.draw.rect(screen, (18, 18, 22), (x - 3, y + 12, 6, 15))
        pygame.draw.rect(screen, (18, 18, 22), (x + 2, y - 1, 5, 18))
        pygame.draw.rect(screen, (18, 18, 22), (x + 7, y - 3, 5, 21))
        pygame.draw.rect(screen, (18, 18, 22), (x + 24, y - 2, 6, 20))
        pygame.draw.rect(screen, (18, 18, 22), (x + 29, y + 1, 6, 16))

        # Blue hair streak
        pygame.draw.rect(screen, (40, 120, 220), (x + 13, y - 5, 6, 13))
        pygame.draw.rect(screen, (40, 120, 220), (x + 16, y + 5, 5, 10))

        # Small face tattoos
        pygame.draw.rect(screen, (35, 35, 45), (x + 5, y + 20, 3, 3))
        pygame.draw.rect(screen, (35, 35, 45), (x + 24, y + 21, 3, 3))

    # SUNGLASSES - J. COOL
    if style == "cool":
        pygame.draw.rect(screen, (10, 10, 10), (x + 2, y + 12, 12, 6))
        pygame.draw.rect(screen, (10, 10, 10), (x + 18, y + 12, 12, 6))
        pygame.draw.rect(screen, (10, 10, 10), (x + 14, y + 14, 4, 3))

    # BODY

    if style == "player":
        # Player shirt
        pygame.draw.rect(screen, (45, 90, 150), (x - 4, y + 32, 40, 35))
        pygame.draw.rect(screen, (25, 55, 100), (x + 8, y + 40, 16, 18))

    elif style == "small_l":
        # Tiny rapper + huge hoodie
        pygame.draw.rect(screen, (55, 55, 65), (x - 10, y + 32, 52, 30))
        pygame.draw.rect(screen, (55, 55, 65), (x - 14, y + 38, 8, 20))
    elif style == "white_thought":
        # Blazer + white shirt
        pygame.draw.rect(screen, (30, 30, 35), (x - 4, y + 32, 40, 35))
        pygame.draw.rect(screen, (235, 235, 235), (x + 10, y + 34, 12, 30))
    elif style == "smartienem":
        # Hoodie
        pygame.draw.rect(screen, (80, 80, 85), (x - 4, y + 32, 40, 35))
        pygame.draw.rect(screen, (60, 60, 65), (x + 8, y + 32, 16, 8))
    elif style == "water_wrld":
        # Dark hoodie
        pygame.draw.rect(screen, (25, 30, 45), (x - 4, y + 32, 40, 35))
        pygame.draw.rect(screen, (40, 100, 160), (x + 9, y + 42, 14, 18))
    elif style == "superordinary":
        # Dark jacket
        pygame.draw.rect(screen, (35, 35, 45), (x - 4, y + 32, 40, 35))
        pygame.draw.rect(screen, (90, 90, 100), (x + 10, y + 34, 12, 30))
    else:
        # J. Cool body
        pygame.draw.rect(screen, (40, 40, 50), (x - 4, y + 32, 40, 35))

    # MIC

    pygame.draw.rect(screen, (170, 170, 170), (x + 36, y + 40, 5, 25))
    pygame.draw.circle(screen, (80, 80, 80), (x + 38, y + 38), 7)


# --------------------------------------------------
# DRAW BUTTON

WIDTH = 1152
HEIGHT = 648

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Freestyle Rap Simulator (Demo)")

clock = pygame.time.Clock()

# --------------------------------------------------
# COLORS
# --------------------------------------------------

BG = (12, 12, 18)
WHITE = (245, 245, 245)
GRAY = (150, 150, 160)
BUTTON = (35, 35, 48)
BUTTON_HOVER = (60, 60, 80)
RED = (190, 50, 50)
GREEN = (60, 190, 90)

# --------------------------------------------------
# FONTS
# --------------------------------------------------

title_font = pygame.font.Font(None, 64)
subtitle_font = pygame.font.Font(None, 40)
button_font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 24)

# --------------------------------------------------
# GAME STATE
# --------------------------------------------------

screen_name = "menu"
selected_rival = None
score = 0
current_round = 1
round_scores = []
money = 0
last_money_earned = 0

battle_phase = "countdown"
countdown_start = 0
battle_timer = 0
answer_start = 0

# --------------------------------------------------
# MENU BUTTONS
# --------------------------------------------------

menu_buttons = {
    "start": pygame.Rect(426, 300, 300, 65),
    "options": pygame.Rect(426, 385, 300, 65),
    "credits": pygame.Rect(426, 470, 300, 65)
}

# --------------------------------------------------
# RIVALS
# --------------------------------------------------

rivals = [
    ("J. Cool", "CAKEWALK", 20),
    ("Superordinary", "EASY", 15),
    ("Small L", "MEDIUM", 10),
    ("White Thought", "HARD", 5),
    ("Smartienem", "EXTREME", 3),
    ("Water WRLD", "IMPOSSIBLE", 1)
]

rival_buttons = []

for i in range(len(rivals)):
    rect = pygame.Rect(276, 155 + i * 72, 600, 58)
    rival_buttons.append(rect)

# --------------------------------------------------
# ANSWERS
# --------------------------------------------------

answer_buttons = [
    pygame.Rect(120, 500, 280, 70),
    pygame.Rect(436, 500, 280, 70),
    pygame.Rect(752, 500, 280, 70)
]

continue_button = pygame.Rect(
    426,
    550,
    300,
    55
)

rounds = [
    {
        "line1": "You walked to the mic like you're ready to fight,",
        "line2": "but your bars are so weak they could lose to a kite.",
        "question": "You look like a piece of sh*t, and even your rhymes don't ______",
        "answers": [
            "click",
            "hick",
            "fit"
        ],
        "correct": 2
    },
    {
        "line1": "You call yourself a rapper, that's a terrible joke,",
        "line2": "every bar that you spit makes the audience choke.",
        "question": "Your rap like a dehydrated fly, nobody cares if you ______",
        "answers": [
            "lie",
            "cry",
            "die"
        ],
        "correct": 1
    },
    {
        "line1": "Three rounds down, but you're still looking scared,",
        "line2": "you brought all that confidence and absolutely nothing prepared.",
        "question": "When the battle is over, I see you ______",
        "answers": [
            "lower",
            "hover",
            "rover"
        ],
        "correct": 0
    }
]

answers = rounds[0]["answers"]
correct_answer = rounds[0]["correct"]

# --------------------------------------------------
# DRAW BUTTON
# --------------------------------------------------

def draw_button(rect, text, mouse_pos):

    if rect.collidepoint(mouse_pos):
        color = BUTTON_HOVER
    else:
        color = BUTTON

    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=8
    )

    pygame.draw.rect(
        screen,
        GRAY,
        rect,
        2,
        border_radius=8
    )

    surface = button_font.render(
        text,
        True,
        WHITE
    )

    text_rect = surface.get_rect(
        center=rect.center
    )

    screen.blit(surface, text_rect)

# --------------------------------------------------
# MENU
# --------------------------------------------------

def draw_menu():

    screen.fill(BG)

    title = title_font.render(
        "FREESTYLE RAP SIMULATOR",
        True,
        WHITE
    )

    screen.blit(
        title,
        title.get_rect(
            center=(WIDTH // 2, 145)
        )
    )

    demo = subtitle_font.render(
        "(DEMO)",
        True,
        GRAY
    )

    screen.blit(
        demo,
        demo.get_rect(
            center=(WIDTH // 2, 205)
        )
    )

    mouse_pos = pygame.mouse.get_pos()

    draw_button(
        menu_buttons["start"],
        "START GAME",
        mouse_pos
    )

    draw_button(
        menu_buttons["options"],
        "OPTIONS",
        mouse_pos
    )

    draw_button(
        menu_buttons["credits"],
        "CREDITS",
        mouse_pos
    )

    company = small_font.render(
        "ADRAGON INDUSTRIES",
        True,
        GRAY
    )

    screen.blit(
        company,
        company.get_rect(
            center=(WIDTH // 2, HEIGHT - 35)
        )
    )

# --------------------------------------------------
# RIVAL SCREEN
# --------------------------------------------------

def draw_rivals():

    screen.fill(BG)

    title = title_font.render(
        "CHOOSE A RIVAL",
        True,
        WHITE
    )

    screen.blit(
        title,
        title.get_rect(
            center=(WIDTH // 2, 65)
        )
    )

    mouse_pos = pygame.mouse.get_pos()

    for i in range(len(rivals)):

        name, difficulty, seconds = rivals[i]
        rect = rival_buttons[i]

        if rect.collidepoint(mouse_pos):
            color = BUTTON_HOVER
        else:
            color = BUTTON

        pygame.draw.rect(
            screen,
            color,
            rect,
            border_radius=8
        )

        pygame.draw.rect(
            screen,
            GRAY,
            rect,
            2,
            border_radius=8
        )

        text = (
            str(i + 1)
            + ". "
            + name
            + "    |    "
            + difficulty
            + "    |    "
            + str(seconds)
            + " SEC"
        )

        surface = button_font.render(
            text,
            True,
            WHITE
        )

        screen.blit(
            surface,
            surface.get_rect(
                center=rect.center
            )
        )

    back = small_font.render(
        "ESC = BACK",
        True,
        GRAY
    )

    screen.blit(
        back,
        (30, HEIGHT - 35)
    )

# --------------------------------------------------
# BATTLE
# --------------------------------------------------

def draw_battle():

    global battle_phase
    global battle_timer
    global answer_start
    global score
    global current_round

    screen.fill((20, 12, 25))

    # TOP BAR

    rival_text = subtitle_font.render(
        selected_rival,
        True,
        WHITE
    )

    screen.blit(
        rival_text,
        (30, 25)
    )

    score_text = subtitle_font.render(
        "SCORE: " + str(score),
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (900, 25)
    )

    # CHARACTERS

    # CHARACTERS

    rival_styles = {
        "J. Cool": "cool",
        "Superordinary": "superordinary",
        "Small L": "small_l",
        "White Thought": "white_thought",
        "Smartienem": "smartienem",
        "Water WRLD": "water_wrld"
    }

    rival_style = rival_styles.get(
        selected_rival,
        "cool"
    )

    draw_rapper(285, 175, rival_style)
    draw_rapper(835, 175, "player")

    rival_name = subtitle_font.render(
        selected_rival,
        True,
        WHITE
    )

    screen.blit(
        rival_name,
        rival_name.get_rect(
            center=(301, 255)
        )
    )

    you_text = subtitle_font.render(
        "YOU",
        True,
        WHITE
    )

    screen.blit(
        you_text,
        you_text.get_rect(
            center=(850, 255)
        )
    )

    # COUNTDOWN

    if battle_phase == "countdown":

        elapsed = (
            pygame.time.get_ticks() - countdown_start
        ) / 1000

        number = 3 - int(elapsed)

        if number > 0:

            count_text = title_font.render(
                str(number),
                True,
                WHITE
            )

            screen.blit(
                count_text,
                count_text.get_rect(
                    center=(WIDTH // 2, 390)
                )
            )

        else:

            rap_text = title_font.render(
                "RAP!",
                True,
                GREEN
            )

            screen.blit(
                rap_text,
                rap_text.get_rect(
                    center=(WIDTH // 2, 390)
                )
            )

            if elapsed > 4:

                battle_phase = "opponent"
                battle_timer = pygame.time.get_ticks()

    # OPPONENT RAP

    elif battle_phase == "opponent":

        speaker = subtitle_font.render(
            selected_rival.upper() + ":",
            True,
            RED
        )

        screen.blit(
            speaker,
            speaker.get_rect(
                center=(WIDTH // 2, 350)
            )
        )

        current_data = rounds[current_round - 1]

        line1 = subtitle_font.render(
            current_data["line1"],
            True,
            WHITE
        )

        line2 = subtitle_font.render(
            current_data["line2"],
            True,
            WHITE
        )

        screen.blit(
            line1,
            line1.get_rect(
                center=(WIDTH // 2, 390)
            )
        )

        screen.blit(
            line2,
            line2.get_rect(
                center=(WIDTH // 2, 430)
            )
        )

        if pygame.time.get_ticks() - battle_timer > 2500:

            battle_phase = "answer"
            answer_start = pygame.time.get_ticks()
 
    # PLAYER ANSWER

    elif battle_phase == "answer":

        question1 = subtitle_font.render(
            "YOU:",
            True,
            GREEN
        )

        screen.blit(
            question1,
            question1.get_rect(
                center=(WIDTH // 2, 370)
            )
        )

        current_data = rounds[current_round - 1]

        question2 = small_font.render(
            current_data["question"],
            True,
            WHITE
        )

        screen.blit(
            question2,
            question2.get_rect(
                center=(WIDTH // 2, 420)
            )
        )

        mouse_pos = pygame.mouse.get_pos()

        for i in range(3):

            draw_button(
                answer_buttons[i],
                current_data["answers"][i],
                mouse_pos
            )

        # TIMER

        rival_data = None

        for rival in rivals:

            if rival[0] == selected_rival:
                rival_data = rival

        seconds = rival_data[2]

        elapsed = (
            pygame.time.get_ticks() - answer_start
        ) / 1000

        remaining = max(
            0,
            seconds - elapsed
        )

        timer_text = subtitle_font.render(
            str(round(remaining, 1)) + " SEC",
            True,
            RED if remaining <= 3 else WHITE
        )

        screen.blit(
            timer_text,
            timer_text.get_rect(
                center=(WIDTH // 2, 465)
            )
        )

        # TIMEOUT

        if remaining <= 0:

            round_points = -2
            score += round_points
            round_scores.append(round_points)

            if current_round < 3:
                current_round += 1
                battle_phase = "opponent"
                battle_timer = pygame.time.get_ticks()
            else:
                calculate_battle_money()
                battle_phase = "result"

    # RESULT

    elif battle_phase == "result":

        result_text = title_font.render(
            "BATTLE COMPLETE",
            True,
            WHITE
        )

        screen.blit(
            result_text,
            result_text.get_rect(
                center=(WIDTH // 2, 300)
            )
        )

        # ROUND SCORES

        for i, points in enumerate(round_scores):

            round_text = subtitle_font.render(
                "ROUND " + str(i + 1),
                True,
                WHITE
            )

            points_text = subtitle_font.render(
                ("+" if points > 0 else "") + str(points),
                True,
                GREEN if points > 0 else RED
            )

            screen.blit(
                round_text,
                (350, 330 + i * 35)
            )

            screen.blit(
                points_text,
                (750, 330 + i * 35)
            )

        # TOTAL SCORE

        total_text = subtitle_font.render(
            "TOTAL SCORE: " + str(score),
            True,
            WHITE
        )

        screen.blit(
            total_text,
            total_text.get_rect(
                center=(WIDTH // 2, 445)
            )
        )

        # MONEY

        earned_text = subtitle_font.render(
            "MONEY EARNED: $" + str(last_money_earned),
            True,
            GREEN if last_money_earned >= 0 else RED
        )

        screen.blit(
            earned_text,
            earned_text.get_rect(
                center=(WIDTH // 2, 480)
            )
        )

        total_money_text = subtitle_font.render(
            "TOTAL MONEY: $" + str(money),
            True,
            WHITE
        )

        screen.blit(
            total_money_text,
            total_money_text.get_rect(
                center=(WIDTH // 2, 515)
            )
        )

        mouse_pos = pygame.mouse.get_pos()

        draw_button(
            continue_button,
            "CONTINUE",
            mouse_pos
        )

# --------------------------------------------------
# MONEY REWARD
# --------------------------------------------------

def calculate_battle_money():

    global money
    global last_money_earned

    earned = 0

    for points in round_scores:

        if points == 1:
            earned += 20

        elif points == -1:
            earned += 0

        elif points == -2:
            earned -= 10

    money += earned
    last_money_earned = earned

    return earned

# --------------------------------------------------
# START BATTLE
# --------------------------------------------------

def start_battle():

    global battle_phase
    global countdown_start
    global score
    global current_round
    global round_scores

    score = 0
    current_round = 1
    round_scores = []
    battle_phase = "countdown"
    countdown_start = pygame.time.get_ticks()

# --------------------------------------------------
# MAIN LOOP
# --------------------------------------------------

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # KEYBOARD

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                if screen_name == "rivals":

                    screen_name = "menu"

                elif screen_name == "battle":

                    screen_name = "rivals"

                else:

                    running = False

        # MOUSE

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                # MENU

                if screen_name == "menu":

                    if menu_buttons["start"].collidepoint(
                        event.pos
                    ):

                        screen_name = "rivals"

                # RIVALS

                elif screen_name == "rivals":

                    for i in range(len(rivals)):

                        if rival_buttons[i].collidepoint(
                            event.pos
                        ):

                            selected_rival = rivals[i][0]

                            screen_name = "battle"

                            start_battle()

                # ANSWERS

                elif screen_name == "battle":

                    if battle_phase == "result":

                        if continue_button.collidepoint(event.pos):

                            screen_name = "rivals"

                    elif battle_phase == "answer":

                        for i in range(3):

                            if answer_buttons[i].collidepoint(
                                event.pos
                            ):

                                current_data = rounds[current_round - 1]

                                if i == current_data["correct"]:
                                    round_points = 1
                                else:
                                    round_points = -1

                                score += round_points
                                round_scores.append(round_points)

                                if current_round < 3:
                                    current_round += 1
                                    battle_phase = "opponent"
                                    battle_timer = pygame.time.get_ticks()
                                else:
                                    calculate_battle_money()
                                    battle_phase = "result"

    # DRAW

    if screen_name == "menu":

        draw_menu()

    elif screen_name == "rivals":

        draw_rivals()

    elif screen_name == "battle":

        draw_battle()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
pygame.quit()
sys.exit()
sys.exit()
