import pygame, pyperclip
pygame.init()

screen = pygame.display.set_mode((1050, 1050))
pygame.display.set_caption("Electric")

run = True

class Matrix:
    def __init__(self, size):
        self.matrix = [[0 for i in range(size[0])] for j in range(size[1])]

    def show(self):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                if self.matrix[y][x]:
                    if x % 2 == 1 and y % 2 == 1:
                        if x > 0:
                            if self.matrix[y][x - 1]:
                                pygame.draw.rect(screen, (255, 255, 255), (x * 50 - 25, y * 50 + 15, 50, 20))

                        if x < len(self.matrix[y]) - 1:
                            if self.matrix[y][x + 1]:
                                pygame.draw.rect(screen, (255, 255, 255), (x * 50 + 25, y * 50 + 15, 50, 20))

                        if y > 0:
                            if self.matrix[y - 1][x]:
                                pygame.draw.rect(screen, (255, 255, 255), (x * 50 + 15, y * 50 - 25, 20, 50))

                        if y < len(self.matrix) - 1:
                            if self.matrix[y + 1][x]:
                                pygame.draw.rect(screen, (255, 255, 255), (x * 50 + 15, y * 50 + 25, 20, 50))
                                
                        #pygame.draw.rect(screen, (255, 255, 255), (x * 50 + 15, y * 50 + 15, 20, 20))
                        pygame.draw.circle(screen, (255, 255, 255), (x * 50 + 25, y * 50 + 25), 10)
                    """else:
                        pygame.draw.rect(screen, (255, 0, 0), (x * 50 + 15, y * 50 + 15, 20, 20))"""

    def get(self, x, y):
        return self.matrix[y][x]
    
    def set(self, x, y, value):
        self.matrix[y][x] = value

    def export(self):
        string = ""
        for y in range(1, len(self.matrix), 2):
            for x in range(1, len(self.matrix[y]), 2):
                if self.matrix[y][x] == 1:
                    value = 0

                    if x > 0:
                        if self.matrix[y][x - 1]:
                            value += 2

                    if x < len(self.matrix[y]) - 1:
                        if self.matrix[y][x + 1]:
                            value += 1

                    if y > 0:
                        if self.matrix[y - 1][x]:
                            value += 8

                    if y < len(self.matrix) - 1:
                        if self.matrix[y + 1][x]:
                            value += 4

                    if value == 0:
                        string += " "
                    if value == 1:
                        string += "╶"
                    if value == 2:
                        string += "╴"
                    if value == 3:
                        string += "―"
                    if value == 4:
                        string += "╷"
                    if value == 5: 
                        string += "┌"
                    if value == 6:
                        string += "┐"
                    if value == 7:
                        string += "┬"
                    if value == 8:
                        string += "╵"
                    if value == 9:
                        string += "└"
                    if value == 10:
                        string += "┘"
                    if value == 11:
                        string += "┴"
                    if value == 12:
                        string += "│"
                    if value == 13:
                        string += "├"
                    if value == 14:
                        string += "┤"
                    if value == 15:
                        string += "┼"

                else:
                    string += " "

            string += "\n"
        pyperclip.copy(string)

matrix = Matrix([21, 21])

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_c] and pygame.key.get_pressed()[pygame.K_LCTRL]:
                matrix.export()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                x //= 50
                y //= 50
                if matrix.get(x, y):
                    matrix.set(x, y, 0)
                else:
                    matrix.set(x, y, 1)

    screen.fill((4, 3, 72))

    for y in range(0, screen.get_width(), 50):
        if y % 100 == 0:
            pygame.draw.line(screen, (0, 0, 150), (25, y + 25), (screen.get_width() - 25, y + 25))
        else:
            pygame.draw.line(screen, (200, 200, 200), (25, y + 25), (screen.get_width() - 25, y + 25))

    for x in range(0, screen.get_height(), 50):
        if x % 100 == 0:
            pygame.draw.line(screen, (0, 0, 150), (x + 25, 25), (x + 25, screen.get_height() - 25))
        else:
            pygame.draw.line(screen, (200, 200, 200), (x + 25, 25), (x + 25, screen.get_height() - 25))

    matrix.show()

    pygame.display.flip()