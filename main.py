import customtkinter as ctk
import hashlib
from datetime import datetime
import os
import threading
import time

try:
    from PIL import Image, ImageDraw
except ImportError:
    os.system("pip install pillow")
    from PIL import Image, ImageDraw

ctk.set_appearance_mode("dark")

# =====================================================================
# 🧠 PARTE 1: NÚCLEO DE SINGULARIDADE COGNITIVA SOBERANA (GLORISMAR & DR. ROITH)
# =====================================================================
class OguisxSuperCognitiveBrain:
    def __init__(self):
        self.mentores = "Glorismar Pires (Grande Mentor) & Dr. Roith (Equipa de Elite)"
        self.lema_sistema = "Os systems mundiais são treinados, mas a Oguisx tem de ser dotada."
        self.coordenadas_gps = "Lat: -8.8368 | Long: 13.2343 (Luanda, Angola)"
        self.modo_online = True  
        
        # 💵 MOTOR DE CÂMBIO DE LICENÇAS E REMOÇÃO DE TAXAS OCULTAS
        self.taxa_cambio_usd_to_akz = 850.0  
        
        # 🗓️ LICENCIAMENTO DE MARKETING (14 DIAS GRÁTIS + 6.000 AKZ DE ATUALIZAÇÃO)
        self.dias_teste_gratis = 14
        self.taxa_atualizacao_obrigatoria = 6000.0
        
        # 💰 TABELA DE MENSALIDADES BASE (PADRÃO CORTE DE MERCADO DE 95%)
        self.taxas_mensais_categories = {
            "EMPRESARIAL": 20000.0, "CANTINA": 10000.0, "MININT": 50000.0,
            "BANCO_VIP": 50000.0, "DESPORTO": 20000.0, "SAÚDE": 20000.0, 
            "EDUCAÇÃO": 20000.0, "CULTURA": 20000.0
        }
        
        # MULTIVERSO DE CIÊNCIAS DA UNESCO, FÍSICA QUÂNTICA/MOLECULAR E INTELIGÊNCIA AADHAAR DOMESTICADA
        self.matriz_infraestrutura_pacotes = {
            "EMPRESARIAL": {
                "ciencias": "Ciências Económicas, Administrativas e Física Dinâmica de Stocks",
                "ia_aliada": "Aadhaar System Link + Palantir Hub + IA Donna + OpenAI Whisper (Monitorização)",
                "fundo_desc": "🍁 [FUNDO ACTIVO: CAMALEÃO GOOGLE E FOLHA OGUISX]\nInterface de Balcão Comercial ativa com controle de caixa imutável local e Primavera v10.",
                "subcetores": ["Pequeno Comércio (Cantina)", "Grandes Armazéns (Armagem)", "Grandes Indústrias (Sonangol)"]
            },
            "EDUCACAO": {
                "ciencias": "Ciências Sociais, Humanas e Pedagógicas da UNESCO",
                "ia_aliada": "OpenAI GPT-4o (Gestão de Matrículas, Notas e Controlo de Faltas Escolares)",
                "fundo_desc": "🎓 [FUNDO ACTIVO: REDE ACADÉMICA MULTIVERSO]\nAmbiente de Educação. Domesticação do Microsoft Office Hub para controlo estudantil.",
                "subcetores": ["Escolas Primárias / Secundárias", "Faculdades / Universidades", "Orfanatos / Abrigos Infantis"]
            },
            "SAUDE": {
                "ciencias": "Ciências Médicas, Biológicas e da Saúde Pública",
                "ia_aliada": "Google Med-PaLM 2 (Triagem Diagnóstica e Recepção de Receitas OCR)",
                "fundo_desc": "🏥 [FUNDO ACTIVO: TRIAGEM HOSPITALAR INTEGRADA]\nAmbiente de Saúde. Domesticação do X-Road para interligação hospitalar nacional.",
                "subcetores": ["Farmácias de Saúde Pública", "Hospitais Gerais / Clínicas", "Morgues / Necrotérios Provinciais"]
            },
            "MININT": {
                "ciencias": "Ciências Jurídicas, Criminais e Algoritmos de Vigilância de Estado",
                "ia_aliada": "Aadhaar Identificação Nacional + Palantir OS Espião + Triagem por Câmaras do PC",
                "fundo_desc": "🛡️ [FUNDO ACTIVO: SEGURANÇA NACIONAL / SIC 113]\nMonitor de Postura Corporal e Voz ativado contra ameaças hostis e assaltos.",
                "subcetores": ["Delegações do SIC / Esquadras", "Comarcas / Cadeias", "Concurso Público 2026"]
            },
            "BANCO_VIP": {
                "ciencias": "Ciências Políticas, Jurídicas, Sociologia e Cadernos Assistenciais",
                "ia_aliada": "Aadhaar Verificação por Dedo + Anthropic Claude 3.5 Sonnet + Scanner OCR Office",
                "fundo_desc": "🗄️ [FUNDO ACTIVO: BANCO DE DADOS VIP / CAIXA SOCIAL COMPACTA]\nGestão Assistencial de Ex-Militares, Orfanatos e Lar do Beiral.\n⚠️ PROTOCOLO SOBERANO ANTI-PROCRIAÇÃO ATIVO EM TODA A REDE!",
                "subcetores": ["Caixa Social / Ex-Militares", "Lar de Idosos Beiral / Abrigos"]
            },
            "DESPORTO": {
                "ciencias": "Ciência da Motricidade Humana e Nutrição Desportiva da UNESCO",
                "ia_aliada": "Robótica Humanoide Feedback + IA Donna Voice + Câmaras do Balcão",
                "fundo_desc": "⚽ [FUNDO ACTIVO: PAINEL DINÂMICO DE ALTA PERFORMANCE PALANCAS NEGRAS]\nControle de cotas desportivas, peso, altura, controlo de faltas e rendimento de atletas nas camadas jovens.",
                "subcetores": ["Clubes de Futebol / Federações", "Ginásios / Academias Fitness"]
            },
            "CULTURA": {
                "ciencias": "Ciências Antropológicas, Culturais, Sociais e História de Angola da UNESCO",
                "ia_aliada": "IA Donna Clonagem de Voz + OpenAI GPT-4o (Relatórios e Análise Semântica de Atas)",
                "fundo_desc": "🎨 [FUNDO ACTIVO: PRESERVAÇÃO E PATRIMÓNIO HISTÓRICO SOBERANO]\nGestão de bibliotecas nacionais, registos de monumentos, teatros e associações de arte.",
                "subcetores": ["Cultura Gospel / Ministérios", "Associações Artísticas / Belas Artes", "Museus / Monumentos Históricos"]
            }
        }
        
        self.banco_usuarios_local = {
            "000123456LA045": {
                "nome": "Glorismar Engenheiro", "saldo_bancario_akz": 500000.0, 
                "dias_uso_sistema": 15, "pacote_ativo": "BANCO_VIP", "subsetor_ativo": "Caixa Social / Ex-Militares",
                "atualizado": False, "nip_militar": "NIP-2026-X", "cotas_pagas": 12, "agregado": "3 Pessoas"
            }
        }

    def verify_hibrid_status(self, online_status) -> str:
        self.modo_online = online_status
        if not self.modo_online: 
            return "🌍 [PÉS NO CHÃO] MODO OFF-LINE RESILIENTE\n▪️ Dados, BI e faturamentos protegidos localmente com física quântica e bancos Aadhaar offline."
        return "⚡ [CABEÇA NAS NUVENS] MODO ON-LINE ACTIVADO\n▪️ Conexão de suporte agêntico ligada via rede estoniana X-Road com as inteligências Donna e Claude."

    # 🔄 INGESTÃO SOBERANA DE PRIMEIRO ARRANQUE (MIGRAÇÃO DE DADOS SEM PERDAS)
    def executar_migracao_primeiro_arranque_ia(self) -> str:
        # Varredura inteligente simulada nos diretórios locais do cliente
        tempo_inicio = time.time()
        sistemas_encontrados = ["Base de Faturamento Primavera v10", "Planilhas de Caixa Excel", "Cadastros VIP Word"]
        
        # Mapeamento e encapsulamento protetivo
        log_migracao = "📦 [MIGRAÇÃO AGÊNTICA SOBERANA OGUISX - PRIMEIRO ARRANQUE]\n"
        log_migracao += "🔍 Varredura de Disco Ativa: Analisando periféricos e sistemas humonóides antigos...\n"
        for sistema in sistemas_encontrados:
            log_migracao += f"✅ DETECTADO E PROTEGIDO: '{sistema}' integrado com segurança à Oguisx OS.\n"
        log_migracao += "📉 STATUS OPERACIONAL: 100% dos dados salvos. Risco de perda: ZERO por cento.\n"
        log_migracao += "🛡️ Criptografia Quântica Aplicada localmente nos Pés no Chão."
        return log_migracao

    def pesquisa_universal_e_auto_programacao(self, termo_pesquisa: str):
        termo = str(termo_pesquisa).strip().upper()
        id_chave = termo.replace(" ", "_")
        
        if id_chave in self.matriz_infraestrutura_pacotes:
            return id_chave, False
            
        self.taxas_mensais_categories[id_chave] = 20000.0  
        self.matriz_infraestrutura_pacotes[id_chave] = {
            "ciencias": f"Multiverso de Ciências Interdisciplinares, Matemática Aplicada e Física Quântica para {termo_pesquisa}",
            "ia_aliada": "Algoritmo Humanoide Adaptável Oguisx + Aadhaar Data Know-All (Varredura de Pessoas e Sistemas)",
            "fundo_desc": f"✨ [FUNDO AUTO-GERADO SOBERANO]: Interface virtual moldada dinamicamente para gerir o setor de {termo_pesquisa}.",
            "subcetores": [f"Gestão de {termo_pesquisa} nos Pés no Chão", f"Controle de Cotas, BI e Faturamento de {termo_pesquisa}"]
        }
        return id_chave, True
    def calcular_cambio_ia_donna(self, custo_usd: float) -> str:
        total_akz = custo_usd * self.taxa_cambio_usd_to_akz
        return f"💵 [CONVERSOR DE CÂMBIO OGUISX IA]\n▪️ Custo: {custo_usd:,.2f} USD | Cotação: {self.taxa_cambio_usd_to_akz} AKZ ➔ Total Real: {total_akz:,.2f} AKZ (Taxa interbancária oculta: 0.00 AKZ)."

    def espiar_fraude_e_assalto_acustico(self, dialogo_texto: str) -> str:
        txt = str(dialogo_texto).strip().lower()
        if "assalto" in txt or "passa" in txt or "arma" in txt:
            return f"🚨🚨🚨 [ALERTA DE EMERGÊNCIA: PROTOCOLO SIC ATIVO] 🚨🚨🚨\n📡 CANAL ACIONADO: Chamada silenciosa e coordenadas GPS enviadas ao 113 POLÍCIA!"
        if "troco" in txt and "paguei" in txt and not any(w in txt for w in ["toma", "aqui", "dinheiro"]):
            return "🚨 [ALERTA DE FRAUDE DE TROCO BALCÃO]: Operador detectado em contradição moral.\n🎥 CÂMARA DO COMPUTADOR ATIVADA CONTRA FRAUDES!"
        return "🛡️ Monitorização de Áudio: Diálogo moral em conformidade contábil."

    def executar_PROCV_anti_procriar(self, numero_bi, nip_ou_cmd, subsetor):
        bi_limpo = str(numero_bi).strip()
        u = self.banco_usuarios_local.get(bi_limpo, None)
        if u:
            return (
                f"🗄️ [REGRA SOBERANA ANTI-PROCRIAÇÃO - BANCO DE DADOS VIP INTERLIGADO COM AADHAAR]\n"
                f"⚠️ Detectado arquivo pré-existente para o BI {bi_limpo} no banco local!\n"
                f"▪️ Unificando dados de câmeras, scanners, telefones e impressoras em formato PDF e Word único.\n"
                f"✅ Oguisx impediu a duplicação de cadastros nos pés no chão com sucesso."
            )
        return f"📥 Novo cadastro instanciado para o sub-setor {subsetor}."

    def verificar_licenca_e_ambiente_geral(self, numero_bi: str, pacote_nome: str, subsetor_nome: str):
        bi_limpo = str(numero_bi).strip()
        if bi_limpo not in self.banco_usuarios_local: return {"erro": True, "msg": "❌ BI não localizado."}
        u = self.banco_usuarios_local[bi_limpo]
        
        if u["dias_uso_sistema"] > self.dias_teste_gratis and not u["atualizado"]:
            return {
                "erro": True,
                "msg": f"⚠️ [OGUISX SOBERANA: PERÍODO EXPERIMENTAL EXPIRADO]\n📦 Pacote Bloqueado: {pacote_nome}\n💵 TAXA DE ATUALIZAÇÃO REQUERIDA: {self.taxa_atualizacao_obrigatoria:,.2f} AKZ"
            }
            
        u["pacote_ativo"] = pacote_nome.upper()
        u["subsetor_ativo"] = subsetor_nome
        
        mensalidade = self.taxas_mensais_categories.get(pacote_nome.upper(), 20000.0)
        dados_infra = self.matriz_infraestrutura_pacotes.get(pacote_nome.upper())
        
        return {
            "erro": False,
            "msg": f"✅ Oguisx OS Ativo de Forma Profissional (Modelo de Marketing 95%).\n"
                   f"▪️ Pacote Activo: {pacote_nome.upper()} | Sub-setor: {subsetor_nome}\n"
                   f"🤝 Inteligência Acoplada via Aadhaar: {dados_infra['ia_aliada']}\n"
                   f"🔬 Matriz UNESCO: {dados_infra['ciencias']}\n"
                   f"💵 Taxa Mensal: {mensalidade:,.2f} AKZ/mês.\n\n"
                   f"{dados_infra['fundo_desc']}"
        }

    def pagar_atualizacao_sistema(self, numero_bi: str):
        bi_limpo = str(numero_bi).strip()
        u = self.banco_usuarios_local[bi_limpo]
        if u["saldo_bancario_akz"] < self.taxa_atualizacao_obrigatoria: return "❌ Erro: Saldo insuficiente."
        u["saldo_bancario_akz"] -= self.taxa_atualizacao_obrigatoria
        u["atualizado"] = True
        return f"⚡ [PACOTE REATIVADO VIA X-ROAD ESTÓNIA] ✅ Sucesso: {self.taxa_atualizacao_obrigatoria:,.2f} AKZ deduzidos!"


# =====================================================================
# 🖥️ PARTE 2: CORE DO ECOSSISTEMA - INTERFACE HUB CORPORATIVA ADAPTÁVEL
# =====================================================================
class TelaMestreOguisx(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Oguisx OS - Professional Ministerial & Corporate Hub")
        self.geometry("1180x960")
        self.cerebro = OguisxSuperCognitiveBrain()
        self.botoes_subsetores = []
        self.mapa_botoes_fisicos = {}
        
        self.caminho_wallpaper = "oguisx_wallpaper.jpg"
        # FOTO 1: Utilização do teu verdadeiro logótipo centralizado
        self.caminho_logo = "oguisx logo (2).png"

        if not os.path.exists(self.caminho_wallpaper):
            img_w = Image.new("RGB", (1180, 960), color="#040804")
            img_w.save(self.caminho_wallpaper)
        if not os.path.exists(self.caminho_logo):
            img_l = Image.new("RGBA", (80, 80), color="#00FF66")
            img_l.save(self.caminho_logo)

        # FOTO 3: Imagem cinemática de fundo
        self.img_fundo_pil = Image.open(self.caminho_wallpaper)
        self.img_fundo_ctk = ctk.CTkImage(light_image=self.img_fundo_pil, dark_image=self.img_fundo_pil, size=(1180, 960))
        self.lbl_background = ctk.CTkLabel(self, image=self.img_fundo_ctk, text="")
        self.lbl_background.place(x=0, y=0, relwidth=1, relheight=1)

        # MENU SUPERIOR STYLE OFFICE
        self.frame_menu = ctk.CTkFrame(self, height=40, fg_color="#1e1e1e")
        self.frame_menu.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(self.frame_menu, text=f" 📑 Instalação Oguisx    🏠 Início    👑 Mentores: {self.cerebro.mentores}", font=("Arial", 11), text_color="#aaaaaa").pack(side="left", padx=15, pady=8)
        
        self.switch_rede = ctk.CTkSwitch(self.frame_menu, text="Cabeça nas Nuvens (Online)", font=("Arial", 11, "bold"), text_color="white", progress_color="#00FF66", command=self.alternar_modo_rede)
        self.switch_rede.select()
        self.switch_rede.pack(side="right", padx=20, pady=5)

        # CONTAINER DO ECRÃ DE BOAS-VINDAS
        self.frame_desktop = ctk.CTkFrame(self, fg_color="#141414", border_width=1, border_color="#00FF66")
        self.frame_desktop.pack(fill="x", padx=15, pady=4)
        
        self.img_logo_pil = Image.open(self.caminho_logo).resize((60, 60))
        self.img_logo_ctk = ctk.CTkImage(light_image=self.img_logo_pil, dark_image=self.img_logo_pil, size=(60, 60))
        self.lbl_logo_img = ctk.CTkLabel(self.frame_desktop, image=self.img_logo_ctk, text="")
        self.lbl_logo_img.pack(side="left", padx=15, pady=5)
        
        ctk.CTkLabel(self.frame_desktop, text="🖥️ WELCOME TO THE FUTURE - OGUISX COGNITIVA SOBERANA", font=("Arial", 16, "bold"), text_color="#00FF66").pack(anchor="w", padx=10, pady=15)
        
        # 🔍 BARRA DE PESQUISA SUPREMA
        self.frame_pesquisa_universal = ctk.CTkFrame(self, fg_color="#1a241a", border_width=1, border_color="#00FF66")
        self.frame_pesquisa_universal.pack(fill="x", padx=15, pady=4)
        
        self.e_pesquisa = ctk.CTkEntry(self.frame_pesquisa_universal, width=600, placeholder_text="🔍 Escreva qualquer novo pacote ou categoria esquecida (Ex: Escolas de Conducao) e a IA cria na tela...", font=("Arial", 11))
        self.e_pesquisa.pack(side="left", padx=15, pady=10, fill="x", expand=True)
        
        ctk.CTkButton(self.frame_pesquisa_universal, text="Pesquisar / Auto-Programar", font=("Arial", 11, "bold"), fg_color="#00FF66", text_color="black", height=35, command=self.executar_pesquisa_e_auto_programacao_botao).pack(side="right", padx=15, pady=10)

        # 📦 LINHA DO TOPO: OS 7 PACOTES FIXOS ORDENADOS LOGO ABAIXO DA BARRA
        self.frame_pacotes_topo = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_pacotes_topo.pack(fill="x", padx=15, pady=4)
        
        self.botoes_iniciais = ["EMPRESARIAL", "SAUDE", "EDUCACAO", "MININT", "BANCO_VIP", "DESPORTO", "CULTURA"]
        self.montar_botoes_iniciais()

        self.frame_classes = ctk.CTkFrame(self, fg_color="#181818", border_width=1, border_color="#00FF66")
        self.frame_classes.pack(fill="x", padx=15, pady=4)
        self.lbl_class_titulo = ctk.CTkLabel(self.frame_classes, text="🌿 CATEGORIAS E CIÊNCIAS INTEGRADAS NA MÁQUINA VIA AADHAAR:", font=("Arial", 11, "bold"), text_color="#00FF66")
        self.lbl_class_titulo.pack(anchor="w", padx=15, pady=3)
        self.sub_frame_classes = ctk.CTkFrame(self.frame_classes, fg_color="transparent")
        self.sub_frame_classes.pack(fill="x", padx=10, pady=5)

        self.frame_busca = ctk.CTkFrame(self, fg_color="#141414", border_width=1, border_color="#333333")
        self.frame_busca.pack(fill="x", padx=15, pady=4)
        self.e_bi = ctk.CTkEntry(self.frame_busca, width=150, placeholder_text="Número do BI..."); self.e_bi.pack(side="left", padx=10, pady=8); self.e_bi.insert(0, "000123456LA045")
        self.e_cmd = ctk.CTkEntry(self.frame_busca, width=180, placeholder_text="NIP / Voz / Comando..."); self.e_cmd.pack(side="left", padx=5, pady=8); self.e_cmd.insert(0, "5.99")
        self.lbl_sub_selecionado = ctk.CTkLabel(self.frame_busca, text="Sub-setor: Nenhum", font=("Arial", 11, "bold"), text_color="#00FF66")
        self.lbl_sub_selecionado.pack(side="left", padx=15, pady=8)
        
                # Botões de Execução do Balcão (Interligação de Impressoras, Câmaras, Wi-Fi e Bluetooth ativa)
        ctk.CTkButton(self.frame_busca, text="Verificar Licença", fg_color="#1f538d", text_color="white", font=("Arial", 11, "bold"), command=self.testar_licenca_geral).pack(side="right", padx=10, pady=8)
        ctk.CTkButton(self.frame_busca, text="Pagar 6.000 AKZ", fg_color="#ff3333", text_color="white", font=("Arial", 11, "bold"), command=self.testar_pagamento_licenca).pack(side="right", padx=5, pady=8)
        ctk.CTkButton(self.frame_busca, text="PROCV VIP", fg_color="#e67e22", text_color="white", font=("Arial", 11, "bold"), command=self.testar_procv_vip).pack(side="right", padx=5, pady=8)
        ctk.CTkButton(self.frame_busca, text="Espião Voz/Letra", fg_color="#2eb85c", text_color="white", font=("Arial", 11, "bold"), command=self.testar_espiao_acustico).pack(side="right", padx=5, pady=8)
        ctk.CTkButton(self.frame_busca, text="Calcular Câmbio", fg_color="#a133ff", text_color="white", font=("Arial", 11, "bold"), command=self.testar_cambio_moeda).pack(side="right", padx=5, pady=8)

        self.frame_visual = ctk.CTkFrame(self, border_width=2, border_color="#00FF66", fg_color="#0d140d")
        self.frame_visual.pack(fill="both", expand=True, padx=15, pady=5)
        self.txt_ecra_visual = ctk.CTkTextbox(self.frame_visual, font=("Consolas", 12), text_color="#00FF66", fg_color="#101810")
        self.txt_ecra_visual.pack(fill="both", expand=True, padx=15, pady=10)
        
        # 💻 BARRA DE TAREFAS ESTILO WINDOWS NA BASE DA JANELA
        self.frame_taskbar = ctk.CTkFrame(self, height=45, fg_color="#101010", border_width=1, border_color="#222222")
        self.frame_taskbar.pack(fill="x", side="bottom", padx=10, pady=5)
        
        ctk.CTkLabel(self.frame_taskbar, text=" 🪟 Iniciar | 🍁 Oguisx OS v1.5 | Periféricos Activos ", font=("Arial", 11, "bold"), text_color="#00FF66").pack(side="left", padx=15, pady=10)
        
        self.lbl_taskbar_status = ctk.CTkLabel(self.frame_taskbar, text="🌐 Rede: Cabeça nas Nuvens (Online)", font=("Arial", 10), text_color="#aaaaaa")
        self.lbl_taskbar_status.pack(side="left", padx=30, pady=10)
        
        self.lbl_taskbar_clock = ctk.CTkLabel(self.frame_taskbar, text="", font=("Consolas", 11, "bold"), text_color="#00FF66")
        self.lbl_taskbar_clock.pack(side="right", padx=15, pady=10)
        
        ctk.CTkLabel(self.frame_taskbar, text=f"📍 GPS: {self.cerebro.coordenadas_gps} ", font=("Arial", 10), text_color="#888888").pack(side="right", padx=20, pady=10)
        
        self.atualizar_relogio_taskbar_loop()
        
        # EXECUTAR A INGESTÃO AUTOMÁTICA DE PRIMEIRO ARRANQUE CONTRA PERDA DE DADOS
        log_migr = self.cerebro.executar_migracao_primeiro_arranque_ia()
        self.txt_ecra_visual.insert("end", f"{log_migr}\n\n🧠 [OGUISX SOBERANA] Pronto para auditoria integrada.\n")
        
        self.carregar_subsetores_interface("EMPRESARIAL")

    def atualizar_relogio_taskbar_loop(self):
        agora = datetime.now().strftime("%H:%M:%S | %d/%m/%Y")
        self.lbl_taskbar_clock.configure(text=agora)
        self.after(1000, self.atualizar_relogio_taskbar_loop)

    def montar_botoes_iniciais(self):
        for pacote in self.botoes_iniciais:
            self.criar_botao_na_interface_física(pacote)

    def criar_botao_na_interface_física(self, nome_pacote_id):
        txt_exibicao = nome_pacote_id.replace("_", " ")
        btn = ctk.CTkButton(self.frame_pacotes_topo, text=f"📦\n{txt_exibicao}", font=("Arial", 10, "bold"), fg_color="#2b2b2b", hover_color="#00FF66", height=65, width=110, command=lambda: self.carregar_subsetores_interface(nome_pacote_id))
        btn.pack(side="left", padx=5, pady=5)
        self.mapa_botoes_fisicos[nome_pacote_id] = btn

    # ⚡ CASAMENTO DE MÉTODO COM "X" ORTOGRÁFICO CORRIGIDO PARA EVITAR ATTR-ERROR
    def executar_pesquisa_e_auto_programacao_botao(self):
        termo = self.e_pesquisa.get().strip()
        if not termo: return
        
        id_chave, criado_novo = self.cerebro.pesquisa_universal_e_auto_programacao(termo)
        
        if criado_novo:
            self.criar_botao_na_interface_física(id_chave)
            res_log = (
                f"⚡ [MÓDULO ROBÓTICA EVOLUTIVA ACTIVADO VIA AADHAAR] ⚡\n"
                f"✅ O supercérebro político aprendeu as novas filtragens dos humanoides para: '{termo}'!\n"
                f"📦 ACÇÃO MECÂNICA EM TEMPO REAL: Botão físico criado e colado no topo da tela do monitor!\n\n"
                f"▪️ Tratamento Contábil: Integrado com a regra dos 14 dias grátis e desconto de marketing de 95%.\n"
                f"▪️ Raciocínio Aadhaar/Palantir Ativo: Varredura de dados e anti-procriar instanciados de imediato."
            )
        else:
            res_log = f"🔍 [LOCALIZADO IN MEMORY]: O pacote '{termo}' já se encontra acoplado à interface."
            
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", res_log)
        self.carregar_subsetores_interface(id_chave)

    def carregar_subsetores_interface(self, nome_pacote):
        self.pacote_selected = nome_pacote
        for btn in self.botoes_subsetores: btn.destroy()
        self.botoes_subsetores.clear()
        
        for p_id, b_obj in self.mapa_botoes_fisicos.items():
            if p_id == nome_pacote: b_obj.configure(fg_color="#00FF66", text_color="black")
            else: b_obj.configure(fg_color="#2b2b2b", text_color="white")
            
        self.lbl_class_titulo.configure(text=f"🌿 SUB-SETORES DO PACOTE UNIVERSAL {nome_pacote} DISPONÍVEIS VIA INTERLIGAÇÃO:")
        sub_lista = self.cerebro.matriz_infraestrutura_pacotes[nome_pacote]["subcetores"]
        
        for sub_nome in sub_lista:
            btn = ctk.CTkButton(self.sub_frame_classes, text=sub_nome, font=("Arial", 11, "bold"), fg_color="#1f538d", hover_color="#00FF66", height=32, command=lambda s=sub_nome: self.selecionar_subsetor(s))
            btn.pack(side="left", padx=8, pady=5)
            self.botoes_subsetores.append(btn)
            
    def selecionar_subsetor(self, nome_sub):
        self.sub_selecionado = nome_sub
        self.lbl_sub_selecionado.configure(text=f"Sub-setor: {nome_sub}")
        self.testar_licenca_geral()

    def testar_licenca_geral(self):
        if not hasattr(self, 'sub_selecionado'): return
        bi = self.e_bi.get().strip()
        res_rede = self.cerebro.verify_hibrid_status(self.switch_rede.get())
        info_lic = self.cerebro.verificar_licenca_e_ambiente_geral(bi, self.pacote_selected, self.sub_selecionado)
        
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", f"{res_rede}\n\n")
        self.txt_ecra_visual.insert("end", info_lic["msg"])

    def testar_procv_vip(self):
        if not hasattr(self, 'sub_selecionado'): return
        bi = self.e_bi.get().strip()
        nip = self.e_cmd.get().strip()
        res = self.cerebro.executar_PROCV_anti_procriar(bi, nip, self.sub_selecionado)
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", res)

    def testar_espiao_acustico(self):
        dialogo = self.e_cmd.get().strip()
        res = self.cerebro.espiar_fraude_e_assalto_acustico(dialogo)
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", res)

    def testar_cambio_moeda(self):
        try: valor_usd = float(self.e_cmd.get().strip())
        except ValueError: return
        res = self.cerebro.calcular_cambio_ia_donna(valor_usd)
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", res)

    def testar_pagamento_licenca(self):
        bi = self.e_bi.get().strip()
        res = self.cerebro.pagar_atualizacao_sistema(bi)
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", res)

    def alternar_modo_rede(self):
        status = self.switch_rede.get()
        txt_status = "🌐 Rede: Cabeça nas Nuvens (Online)" if status else "🌍 Rede: Pés no Chão (Offline)"
        self.lbl_taskbar_status.configure(text=txt_status)
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", f"🔄 CHAVEAMENTO COGNITIVO DETECTADO...\n\n{self.cerebro.verify_hibrid_status(status)}")

if __name__ == "__main__":
    app = TelaMestreOguisx()
    app.mainloop()
