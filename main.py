import pygame, pyperclip
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Electric")

run = True

class Matrix:
    def __init__(self, size):
        self.matrix = [[0 for i in range(size[0])] for j in range(size[1])]

    def show(self):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                if self.matrix[y][x] == 2:
                    pygame.draw.rect(screen, (255, 255, 255), (x * 50, y * 50, 50, 50))
                if self.matrix[y][x] >= 1:
                    pygame.draw.rect(screen, (255, 0, 0), (x * 50, y * 50, 20, 20))

    def get(self, x, y):
        return self.matrix[y][x]
    
    def set(self, x, y, value):
        self.matrix[y][x] = value

    def export(self):
        string = ""
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                if self.matrix[y][x] == 2:
                    value = 0

                    if x > 0:
                        if self.matrix[y][x - 1] > 0:
                            value += 2

                    if x < len(self.matrix[y]) - 1:
                        if self.matrix[y][x + 1] > 0:
                            value += 1

                    if y > 0:
                        if self.matrix[y - 1][x] > 0:
                            value += 8

                    if y < len(self.matrix) - 1:
                        if self.matrix[y + 1][x] > 0:
                            value += 4

                    if value == 0:
                        string += " "
                    if value == 1:
                    #    string += "╶"
                        string += " "
                    if value == 2:
                    #    string += "╴"
                        string += " "
                    if value == 3:
                        string += "―"
                    if value == 4:
                    #    string += "╷"
                        string += " "
                    if value == 5: 
                        string += "┌"
                    if value == 6:
                        string += "┐"
                    if value == 7:
                        string += "┬"
                    if value == 8:
                    #    string += "╵"
                        string += " "
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

matrix = Matrix([16, 16])

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
                if matrix.get(x, y) == 2:
                    matrix.set(x, y, 0)
                else:
                    matrix.set(x, y, 2)

            if pygame.mouse.get_pressed()[2]:
                x, y = pygame.mouse.get_pos()
                x //= 50
                y //= 50
                if matrix.get(x, y) == 1:
                    matrix.set(x, y, 0)
                else:
                    matrix.set(x, y, 1)

    screen.fill((0, 0, 0))

    for y in range(0, 800, 50):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (800, y))

    for x in range(0, 800, 50):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, 800))

    matrix.show()

    pygame.display.flip()