import pygame

ii = int(input('Number(from 0 to 49): '))
cvet = input('Color: ')
if ii < 1 or ii > 49:
    print('Do svyazi')
else:
    pygame.init()
    screen = pygame.display.set_mode((850, 500))
    pygame.display.set_caption('Cvet risovat onlain')
    screen.fill((40, 40, 40))
    font = pygame.font.Font(None, 16)

    square = pygame.Surface((60, 60))
    square.fill((70, 70, 70))

    str = [10, 80, 150, 220, 290, 360, 430]
    stb = [10, 80, 150, 220, 290, 360, 430]

    num = 1

    squares = []
    xs = []
    ys = []

    for ely in str:
        for elx in stb:
            screen.blit(square, (elx, ely))
            numofsq = font.render(f'{num}', True, (150, 150, 150))
            if num < 10:
                screen.blit(numofsq, (elx + 52, ely + 49))
            else:
                screen.blit(numofsq, (elx + 46, ely + 49))

            xs.append(elx)
            ys.append(ely)
            squares.append(square)

            num += 1

    squares[ii].fill(f'{cvet}')
    '''
    noojx = noojy = 0
    noojx = ((a % 7) - 1)
    noojy = (a // 7)
    '''
    screen.blit(squares[ii], (xs[ii - 1], ys[ii - 1]))

    numofsq = font.render(f'{ii}', True, (150, 150, 150))
    if ii < 10:
        screen.blit(numofsq, (xs[ii - 1] + 52, ys[ii - 1] + 49))
    else:
        screen.blit(numofsq, (xs[ii - 1] + 46, ys[ii - 1] + 49))
    run = True
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
