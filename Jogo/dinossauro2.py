import pygame
import random

# Inicializa o Pygame
pygame.init()

# Definindo as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Configurações da tela
largura_tela = 800
altura_tela = 300
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo do Dinossauro")

# Configurações do jogo
velocidade_jogo = 22
gravidade = 1
altura_salto = 20  # Ajuste a altura do pulo
vidas = 3

# Define o relógio para controlar a velocidade do jogo
relogio = pygame.time.Clock()

# Fonte do placar
fonte = pygame.font.SysFont(None, 35)

# Carregar imagens
coração_img = pygame.image.load("coracao.png")
coração_img = pygame.transform.scale(coração_img, (30, 30))

fundo_img = pygame.image.load("fundo.png")
fundo_img = pygame.transform.scale(fundo_img, (largura_tela, altura_tela))

# Função para mostrar o placar
def exibir_pontuacao(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)  # Alterado para BRANCO
    tela.blit(texto, [10, 10])

# Função para mostrar as vidas
def exibir_vidas(vidas):
    for i in range(vidas):
        tela.blit(coração_img, [largura_tela - 40 * (i + 1), 10])

# Função para mostrar mensagens
def exibir_mensagem(mensagem):
    texto = fonte.render(mensagem, True, PRETO)
    tela.blit(texto, [largura_tela // 2 - texto.get_width() // 2, altura_tela // 2 - texto.get_height() // 2])

# Classe para o fundo
class Fundo:
    def __init__(self):
        self.x = 0

    def atualizar(self):
        self.x -= 5
        if self.x <= -largura_tela:
            self.x = 0
        tela.blit(fundo_img, (self.x, 0))
        tela.blit(fundo_img, (self.x + largura_tela, 0))

fundo = Fundo()

# Classe para o dinossauro
class Dinossauro:
    def __init__(self):
        # Carregar imagens do dinossauro
        self.imagens = {
            'correndo': [pygame.image.load(f"dino_run_{i}.png") for i in range(2)],
            'pular': pygame.image.load("dino_jump.png")
        }
        self.estado = 'correndo'
        self.imagem = pygame.transform.scale(self.imagens[self.estado][0], (60, 60))
        self.rect = self.imagem.get_rect()
        self.rect.x = 50
        self.rect.y = altura_tela - self.imagem.get_height()
        self.velocidade_y = 0
        self.pulou = False
        self.frame = 0
        self.tempo_frame = 0
        self.delay_frame = 200  # Atraso entre os frames (em milissegundos)

    def pular(self):
        if self.rect.y == altura_tela - self.imagem.get_height():  # Verifica se está no chão
            self.velocidade_y = -altura_salto  # Ajusta a velocidade inicial do pulo
            self.pulou = True
            self.estado = 'pular'
            self.imagem = pygame.transform.scale(self.imagens[self.estado], (60, 60))

    def atualizar(self):
        # Atualiza o tempo para troca de frames
        self.tempo_frame += relogio.get_time()
        
        self.velocidade_y += gravidade  # Aplica a gravidade à velocidade do pulo
        self.rect.y += self.velocidade_y

        if self.rect.y >= altura_tela - self.imagem.get_height():
            self.rect.y = altura_tela - self.imagem.get_height()
            self.velocidade_y = 0
            if self.estado == 'pular':
                self.estado = 'correndo'
                self.imagem = pygame.transform.scale(self.imagens[self.estado][0], (60, 60))
            self.pulou = False

        if self.rect.y < 0:  # Garante que o dinossauro não suba além do topo da tela
            self.rect.y = 0
            self.velocidade_y = 0

        if self.estado == 'correndo':
            if self.tempo_frame >= self.delay_frame:
                self.frame = (self.frame + 1) % len(self.imagens['correndo'])
                self.imagem = pygame.transform.scale(self.imagens[self.estado][self.frame], (60, 60))
                self.tempo_frame = 0  # Reseta o temporizador

        tela.blit(self.imagem, self.rect)

# Classe para os cactos
class Cacto:
    def __init__(self):
        self.imagens = [pygame.image.load(f"cacto_{i}.png") for i in range(2)]
        self.imagem = pygame.transform.scale(self.imagens[0], (40, 80))  # Aumentado o tamanho do cacto
        self.rect = self.imagem.get_rect()
        self.rect.x = largura_tela
        self.rect.y = altura_tela - self.imagem.get_height()
        self.frame = 0
        self.tempo_frame = 0
        self.delay_frame = 300  # Atraso entre os frames (em milissegundos)

    def atualizar(self):
        self.rect.x -= velocidade_jogo
        if self.rect.x < -40:  # Ajustado o tamanho do cacto
            self.rect.x = largura_tela + random.randint(100, 300)

        self.tempo_frame += relogio.get_time()
        if self.tempo_frame >= self.delay_frame:
            self.frame = (self.frame + 1) % len(self.imagens)
            self.imagem = pygame.transform.scale(self.imagens[self.frame], (40, 80))  # Aumentado o tamanho do cacto
            self.tempo_frame = 0  # Reseta o temporizador

        tela.blit(self.imagem, self.rect)

# Função principal do jogo
def jogo():
    global vidas
    fim_de_jogo = False
    pontos = 0

    dinossauro = Dinossauro()
    cacto = Cacto()

    while not fim_de_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    dinossauro.pular()

        fundo.atualizar()
        dinossauro.atualizar()
        cacto.atualizar()

        # Verifica colisão
        if dinossauro.rect.colliderect(cacto.rect):
            vidas -= 1
            if vidas <= 0:
                fim_de_jogo = True
            else:
                cacto.rect.x = largura_tela
                dinossauro.rect.y = altura_tela - dinossauro.imagem.get_height()
                dinossauro.pulou = False

        # Verifica se o dinossauro pulou sobre o cacto
        if dinossauro.rect.right > cacto.rect.left and dinossauro.rect.left < cacto.rect.right:
            if dinossauro.pulou and dinossauro.rect.bottom < cacto.rect.top:
                pontos += 1
                dinossauro.pulou = False

        # Atualiza o placar e as vidas
        exibir_pontuacao(pontos)
        exibir_vidas(vidas)

        pygame.display.update()
        relogio.tick(30)

    exibir_mensagem("Game Over!")
    pygame.display.update()
    pygame.time.wait(2000)  # Espera 2 segundos antes de fechar

    pygame.quit()
    quit()

# Inicia o jogo
jogo()
