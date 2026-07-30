import os
from PIL import Image, ImageDraw

def criar_identidade_visual_oguisx():
    print("🎨 [OGUISX ART ENGINE] A renderizar o Logótipo e o Papel de Parede do Dossiê...")

    # =====================================================================
    # 💎 1. GERAR O LOGÓTIPO OFICIAL (O Camaleão em forma de "O" com cores Google)
    # =====================================================================
    logo = Image.new("RGBA", (400, 400), (0, 0, 0, 0)) # Fundo transparente profissional
    draw_logo = ImageDraw.Draw(logo)
    
    # Desenha a base: A Folha Mística em tom verde-bordo/bronze
    draw_logo.polygon([(200, 50), (280, 150), (350, 180), (280, 230), (200, 350), (120, 230), (50, 180), (120, 150)], fill="#1b3a1e", outline="#00FF66", width=3)
    
    # Desenha o Camaleão enrolado formando a letra "O", usando os 4 quadrantes da Google
    # Arco 1: Azul Google (Topo-Esquerda)
    draw_logo.arc([110, 110, 290, 290], start=180, end=270, fill="#4285F4", width=22)
    # Arco 2: Vermelho Google (Topo-Direita)
    draw_logo.arc([110, 110, 290, 290], start=270, end=360, fill="#EA4335", width=22)
    # Arco 3: Amarelo Google (Baixo-Direita)
    draw_logo.arc([110, 110, 290, 290], start=0, end=90, fill="#FBBC05", width=22)
    # Arco 4: Verde Google (Baixo-Esquerda)
    draw_logo.arc([110, 110, 290, 290], start=90, end=180, fill="#34A853", width=22)
    
    # Desenha a cauda em espiral do Camaleão no centro e o olho inteligente
    draw_logo.arc([160, 160, 240, 240], start=0, end=270, fill="#34A853", width=10)
    draw_logo.ellipse([260, 180, 270, 190], fill="#FFFFFF") # Olho focado
    draw_logo.ellipse([263, 183, 267, 187], fill="#000000") # Pupila dotada
    
    logo.save("oguisx_logo.png")
    print("✅ Logótipo 'oguisx_logo.png' gerado com sucesso!")

    # =====================================================================
    # 🦅 2. GERAR O PAPEL DE PAREDE (A Metáfora da Águia e da Folha)
    # =====================================================================
    wallpaper = Image.new("RGB", (1160, 960), color="#030804") # Escuro corporativo
    draw_wall = ImageDraw.Draw(wallpaper)
    
    # Desenha as linhas de código da Matrix e Grelha do Office Hub
    for i in range(0, 1160, 40):
        draw_wall.line([(i, 0), (i, 960)], fill="#001a05", width=1)
        draw_wall.line([(0, i), (1160, i)], fill="#001a05", width=1)
        
    # Desenha formas abstratas que representam as asas da Águia Soberana 🦅 nas laterais
    draw_wall.polygon([(0, 200), (300, 480), (0, 700)], fill="#05240c")
    draw_wall.polygon([(1160, 200), (860, 480), (1160, 700)], fill="#05240c")
    
    # Desenha o reflexo da água no fundo com ondulações lineares
    for y in range(800, 960, 15):
        draw_wall.line([(0, y), (1160, y)], fill="#0a3c17", width=2)
        
    # Desenha a silhueta da Folha 🍁 a flutuar no centro da tela
    draw_wall.polygon([(580, 400), (640, 480), (700, 500), (640, 540), (580, 620), (520, 540), (460, 500), (520, 480)], fill="#0d4214", outline="#00FF66", width=2)
    
    wallpaper.save("oguisx_wallpaper.jpg")
    print("✅ Papel de Parede 'oguisx_wallpaper.jpg' renderizado com sucesso!")
    print("\n🚀 PROTOCOLO CONCLUÍDO: As imagens profissionais já estão na pasta do teu projeto!")

if __name__ == "__main__":
    criar_identidade_visual_oguisx()
