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
# 🧠 PARTE 1: SUPER CÉREBRO COGNITIVO SOBERANO - UNIVERSO POLIGLOTA
# =====================================================================
class OguisxCognitiveBrain:
    def __init__(self):
        self.lema_sistema = "Os systems mundiais são treinados, mas a Oguisx tem de ser dotada."
        self.coordenadas_gps = "Lat: -8.8368 | Long: 13.2343 (Luanda, Angola)"
        self.modo_online = True  
        
        # 💵 MOTOR DE CÂMBIO DE LICENÇAS INTERNACIONAIS (Proteção em Kwanzas)
        self.taxa_cambio_usd_to_akz = 850.0  # Cotação base: 1 USD = 850 AKZ
        
        # 🗓️ REGRAS DE LICENCIAMENTO DE MARKETING (14 DIAS GRÁTIS + 6.000 AKZ DE ATUALIZAÇÃO)
        self.dias_teste_gratis = 14
        self.taxa_atualizacao_obrigatoria = 6000.0
        
        # 💰 MENSALIDADES POR CATEGORIA COM REGRA DE 95% DE DESCONTO DO MERCADO
        self.taxas_mensais_categorias = {
            "CANTINA": 10000.0,       # Pequeno Comércio Local
            "ARMAGEM": 20000.0,       # Médias Empresas / Armazéns
            "SONANGOL": 50000.0,      # Grandes Indústrias VIP / Portos
            "MININT_CORE": 50000.0,   # Delegações de Estado / SIC / Comarcas / Cadeias
            "BANCO_VIP": 50000.0      # Caixa Social / Ex-Militares / Lar do Beiral
        }
        
        # MATRIZ DE INFRAESTRUTURA DE TODOS OS PACOTES COM COOPERAÇÃO DE IAs (DONNA, CLAUDE, WHISPER)
        self.matriz_infraestrutura_pacotes = {
            "EMPRESARIAL": {
                "ciencias": "Ciências Económicas e Administrativas da UNESCO",
                "ia_aliada": "IA Donna + OpenAI Whisper (Monitorização de Fraudes e Caixa Comercial)",
                "fundo_desc": "🍁 [FUNDO ACTIVO: CAMALEÃO GOOGLE E FOLHA OGUISX]\nInterface de Balcão e Contabilidade Comercial ativa nos pés no chão.",
                "subcetores": ["Pequeno Comércio (Cantina)", "Grandes Armazéns (Armagem)", "Grandes Indústrias (Sonangol)"]
            },
            "EDUCACAO": {
                "ciencias": "Ciências Sociais, Humanas e Pedagógicas da UNESCO",
                "ia_aliada": "OpenAI GPT-4o (Gestão de Matrículas, Notas e Controle Académico)",
                "fundo_desc": "🎓 [FUNDO ACTIVO: REDE ACADÉMICA MULTIVERSO]\nAmbiente de Educação. Domesticação do Microsoft Office Hub para controle estudantil.",
                "subcetores": ["Escolas Primárias / Secundárias", "Faculdades / Universidades", "Orfanatos / Abrigos Infantis"]
            },
            "SAUDE": {
                "ciencias": "Ciências Médicas, Biológicas e da Saúde Pública",
                "ia_aliada": "Google Med-PaLM 2 (Triagem Diagnóstica e Recepção de Receitas OCR)",
                "fundo_desc": "🏥 [FUNDO ACTIVO: TRIAGEM HOSPITALAR INTEGRADA]\nAmbiente de Saúde. Domesticação do X-Road para interligação hospitalar nacional.",
                "subcetores": ["Farmácias de Saúde Pública", "Hospitais Gerais / Clínicas", "Morgues / Necrotérios Provinciais"]
            },
            "MININT": {
                "ciencias": "Ciências Jurídicas, Criminais e de Defesa de Estado",
                "ia_aliada": "IA Donna Audio + Câmaras do Computador (Vigilância, Comarcas e Triagem Forense)",
                "fundo_desc": "🛡️ [FUNDO ACTIVO: SEGURANÇA NACIONAL / SIC 113]\nMonitorização de Postura Corporal e Voz ativada de forma resiliente.",
                "subcetores": ["Delegações do SIC / Esquadras", "Comarcas / Cadeias", "Concurso Público 2026"]
            },
            "BANCO_VIP": {
                "ciencias": "Ciências Políticas, Jurídicas e Assistência Social do Estado",
                "ia_aliada": "Anthropic Claude 3.5 (Leitura OCR e Arquivamento Inteligente PDF/Word)",
                "fundo_desc": "🗄️ [FUNDO ACTIVO: BANCO DE DADOS VIP / CAIXA SOCIAL COMPACTA]\nGestão Assistencial de Ex-Militares, Orfanatos e Lar do Beiral.",
                "subcetores": ["Caixa Social / Ex-Militares", "Lar de Idosos Beiral / Abrigos", "Orfanatos / Comarcas"]
            }
        }
        
        # PÉS NO CHÃO: Armazenamento local imutável contra duplicações de arquivos
        self.banco_usuarios_local = {
            "000123456LA045": {
                "nome": "Glorismar Engenheiro", "saldo_bancario_akz": 500000.0, 
                "dias_uso_sistema": 15, "pacote_ativo": "BANCO_VIP", "subsetor_ativo": "Caixa Social / Ex-Militares",
                "atualizado": False, "nip_militar": "NIP-2026-X", "cotas_pagas": 12, "agregado": "3 Pessoas"
            }
        }
        self.stock_cantina = 10

    def verify_hibrid_status(self, online_status) -> str:
        self.modo_online = online_status
        if not self.modo_online: 
            return "🌍 [PÉS NO CHÃO] OPERANDO EM MODO OFF-LINE LOCAL\n▪️ Dados, fotos de meio corpo e faturamentos guardados com segurança e taxa zero de dados."
        return "⚡ [CABEÇA NAS NUVENS] MODO ON-LINE ACTIVO\n▪️ Buscando suporte técnico de IAs globais (Donna, Claude, Whisper) via X-Road."

    def calcular_cambio_ia_donna(self, custo_usd: float) -> str:
        """Motor de Câmbio: Converte o valor em dólares e remove taxas ocultas"""
        total_akz = custo_usd * self.taxa_cambio_usd_to_akz
        return (
            f"💵 [CONVERSOR DE CÂMBIO OGUISX IA]\n"
            f"▪️ Custo da Licença Internacional (Donna/Google): {custo_usd:,.2f} USD\n"
            f"▪️ Cotação do Dia: 1 USD = {self.taxa_cambio_usd_to_akz} AKZ\n"
            f"📉 TOTAL EM AKZ PARA CARREGAR NO CARTÃO VISA VIRTUAL: {total_akz:,.2f} AKZ\n"
            f"🛡️ Isento de Taxas Ocultas Interbancárias: 0.00 AKZ."
        )

    def espiar_fraude_e_assalto_acustico(self, dialogo_texto: str) -> str:
        """COOPERAÇÃO DONNA/WHISPER: Interpreta letras e áudios em TODOS os pacotes"""
        txt = str(dialogo_texto).strip().lower()
        if "assalto" in txt or "passa" in txt or "arma" in txt:
            return (
                f"🚨🚨🚨 [ALERTA DE EMERGÊNCIA: PROTOCOLO SIC ATIVO] 🚨🚨🚨\n"
                f"📡 CANAL ACIONADO: Chamada silenciosa enviada ao 113 POLÍCIA!\n"
                f"📍 GPS do Computador: {self.coordenadas_gps}\n"
                f"📸 Gravação forense de rostos ativada de forma silenciosa."
            )
        if "troco" in txt and "paguei" in txt and not any(w in txt for w in ["toma", "aqui", "dinheiro"]):
            return "🚨 [ALERTA DE FRAUDE DE TROCO BALCÃO]: Operador detectado em contradição moral.\n🎥 CÂMARA DO COMPUTADOR ATIVADA CONTRA FRAUDES!"
        return "🛡️ Monitorização de Áudio: Diálogo moral em conformidade contábil."

    def executar_PROCV_anti_procriar(self, numero_bi, nip_ou_cmd, subsetor):
        """COOPERAÇÃO CLAUDE: Lê documentos físicos, unifica em Word/PDF e NÃO procria arquivos duplicados"""
        bi_limpo = str(numero_bi).strip()
        u = self.banco_usuarios_local.get(bi_limpo, None)
        if u and ("Caixa Social" in subsetor or "Ex-Militares" in subsetor or "Comarcas" in subsetor or "Cadeias" in subsetor):
            return (
                f"🗄️ [REGRA SOBERANA ANTI-PROCRIAÇÃO - BANCO DE DADOS VIP]\n"
                f"⚠️ Detectado arquivo pré-existente para o BI {bi_limpo} no banco local!\n"
                f"▪️ Beneficiário VIP: {u['nome']} | NIP: {u['nip_militar']} | Cotas Pagas: {u['cotas_pagas']} anuais.\n"
                f"----------------------------------------------------------------------\n"
                f"✅ FLUXO INTEGRADO VIRTUAL: A Oguisx utilizou as capacidades OCR das IAs aliadas, digitalizou e unificou os novos dados das câmeras, scanners e telefones em formato PDF/Word dentro do arquivo único já existente."
            )
        return f"📥 Novo cadastro instanciado para o sub-setor {subsetor}. Fotos de meio corpo salvas."

    def verificar_licenca_e_ambiente_geral(self, numero_bi: str, pacote_nome: str, subsetor_nome: str):
        bi_limpo = str(numero_bi).strip()
        if bi_limpo not in self.banco_usuarios_local: 
            return {"erro": True, "msg": "❌ BI não localizado na base local."}
            
        u = self.banco_usuarios_local[bi_limpo]
        u["pacote_ativo"] = pacote_nome.upper()
        u["subsetor_ativo"] = subsetor_nome
        
        if u["dias_uso_sistema"] > self.dias_teste_gratis and not u["atualizado"]:
            return {
                "erro": True,
                "msg": f"⚠️ [OGUISX SOBERANA: PERÍODO EXPERIMENTAL EXPIRADO]\n"
                       f"▪️ O teu período de graça de {self.dias_teste_gratis} dias terminou e o sistema perdeu as atualizações.\n"
                       f"📦 Pacote Bloqueado: {u['pacote_ativo']} | Sub-setor: {u['subsetor_ativo']}\n"
                       f"💵 TAXA DE ATUALIZAÇÃO REQUERIDA: {self.taxa_atualizacao_obrigatoria:,.2f} AKZ\n"
                       f"Efetue o pagamento de 6.000 AKZ para atualizar o pacote e liberar as diretrizes universais."
            }
            
        chave_taxa = "BANCO_VIP" if "Caixa Social" in subsetor_nome or "Ex-Militares" in subsetor_nome else u["pacote_ativo"]
        if "Cantina" in subsetor_nome: chave_taxa = "CANTINA"
        elif "Armagem" in subsetor_nome: chave_taxa = "ARMAGEM"
        elif "Sonangol" in subsetor_nome: chave_taxa = "SONANGOL"
        
        mensalidade = self.taxas_mensais_categorias.get(chave_taxa, 20000.0)
        dados_infra = self.matriz_infraestrutura_pacotes.get(u["pacote_ativo"], self.matriz_infraestrutura_pacotes["BANCO_VIP"])
        
        return {
            "erro": False,
            "msg": f"✅ Oguisx OS Ativo de Forma Profissional (Modelo de Marketing 95%).\n"
                   f"▪️ Pacote Activo: {u['pacote_ativo']} | Sub-setor: {u['subsetor_ativo']}\n"
                   f"🤝 Cooperação Integrada: {dados_infra['ia_aliada']}\n"
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
        return f"⚡ [PACOTE REATIVADO VIA NUVEM]\n✅ Sucesso: {self.taxa_atualizacao_obrigatoria:,.2f} AKZ deduzidos. O Oguisx OS recuperou a atualização universal!"


# =====================================================================
# 🖥️ PARTE 2: CAMADA DA INTERFACE GRÁFICA MESTRE (OFFICE HOME HUB)
# =====================================================================
class TelaMestreOguisx(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Oguisx OS - Professional Ministerial & Corporate Hub")
        self.geometry("1180x960")
        self.cerebro = OguisxCognitiveBrain()
        self.pacote_selected = "EMPRESARIAL"
        self.botoes_subsetores = []
        
        self.caminho_wallpaper = "oguisx_wallpaper.jpg"
        self.caminho_logo = "oguisx_logo.png"

        if not os.path.exists(self.caminho_wallpaper):
            img_w = Image.new("RGB", (1180, 960), color="#040804")
            img_w.save(self.caminho_wallpaper)
        if not os.path.exists(self.caminho_logo):
            img_l = Image.new("RGBA", (80, 80), color="#00FF66")
            img_l.save(self.caminho_logo)

        # FOTO 3: Carrega a imagem futurista "Welcome to the Future" de fundo no monitor
        self.img_fundo_pil = Image.open(self.caminho_wallpaper)
        self.img_fundo_ctk = ctk.CTkImage(light_image=self.img_fundo_pil, dark_image=self.img_fundo_pil, size=(1180, 960))
        self.lbl_background = ctk.CTkLabel(self, image=self.img_fundo_ctk, text="")
        self.lbl_background.place(x=0, y=0, relwidth=1, relheight=1)

        # MENU SUPERIOR STYLE OFFICE
        self.frame_menu = ctk.CTkFrame(self, height=40, fg_color="#1e1e1e")
        self.frame_menu.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(self.frame_menu, text=" 📑 Instalação Oguisx    🏠 Início    📊 Ciências UNESCO    🗄️ Controle de Custos e Faturamento", font=("Arial", 12), text_color="#aaaaaa").pack(side="left", padx=15, pady=8)
        
        self.switch_rede = ctk.CTkSwitch(self.frame_menu, text="Cabeça nas Nuvens (Online)", font=("Arial", 11, "bold"), text_color="white", progress_color="#00FF66", command=self.alternar_modo_rede)
        self.switch_rede.select()
        self.switch_rede.pack(side="right", padx=20, pady=5)

        # CONTAINER DO ECRÃ DE BOAS-VINDAS (FOTO 3)
        self.frame_desktop = ctk.CTkFrame(self, fg_color="#141414", border_width=1, border_color="#00FF66")
        self.frame_desktop.pack(fill="x", padx=15, pady=4)
        
        self.img_logo_pil = Image.open(self.caminho_logo).resize((60, 60))
        self.img_logo_ctk = ctk.CTkImage(light_image=self.img_logo_pil, dark_image=self.img_logo_pil, size=(60, 60))
        self.lbl_logo_img = ctk.CTkLabel(self.frame_desktop, image=self.img_logo_ctk, text="")
        self.lbl_logo_img.pack(side="left", padx=15, pady=5)
        
        ctk.CTkLabel(self.frame_desktop, text="🖥️ WELCOME TO THE FUTURE - OGUISX COGNITIVA SOBERANA", font=("Arial", 16, "bold"), text_color="#00FF66").pack(anchor="w", padx=10, pady=15)
        
        # 📦 LISTAGEM DE TODOS OS PACOTES MUNDIAIS DESTACADOS NO TOPO (FOTO 2 REORGANIZADA)
        self.frame_pacotes_topo = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_pacotes_topo.pack(fill="x", padx=15, pady=4)
        ctk.CTkButton(self.frame_pacotes_topo, text="💼\nSetor\nEmpresarial", font=("Arial", 11, "bold"), fg_color="#1f538d", height=65, width=145, command=lambda: self.carregar_subsetores_interface("EMPRESARIAL")).pack(side="left", padx=6, pady=5)
        ctk.CTkButton(self.frame_pacotes_topo, text="🎓\nSetor\nEducação", font=("Arial", 11, "bold"), fg_color="#2eb85c", height=65, width=145, command=lambda: self.carregar_subsetores_interface("EDUCACAO")).pack(side="left", padx=6, pady=5)
        ctk.CTkButton(self.frame_pacotes_topo, text="🏥\nSetor\nSaúde Pública", font=("Arial", 11, "bold"), fg_color="#a133ff", height=65, width=145, command=lambda: self.carregar_subsetores_interface("SAUDE")).pack(side="left", padx=6, pady=5)
        ctk.CTkButton(self.frame_pacotes_topo, text="🛡️\nSetor\nMININT / Esquadra", font=("Arial", 11, "bold"), fg_color="#ff3333", height=65, width=145, command=lambda: self.carregar_subsetores_interface("MININT")).pack(side="left", padx=6, pady=5)
        ctk.CTkButton(self.frame_pacotes_topo, text="🗄️\nBanco Dados\nVIP Caixa Social", font=("Arial", 11, "bold"), fg_color="#e67e22", height=65, width=145, command=lambda: self.carregar_subsetores_interface("BANCO_VIP")).pack(side="left", padx=6, pady=5)

        # PAINEL DINÂMICO DE SUB-SETORES E CATEGORIAS (FOTO 4)
        self.frame_classes = ctk.CTkFrame(self, fg_color="#181818", border_width=1, border_color="#00FF66")
        self.frame_classes.pack(fill="x", padx=15, pady=4)
        self.lbl_class_titulo = ctk.CTkLabel(self.frame_classes, text="🌿 CATEGORIAS DO SECTOR SELECIONADO NA NUVEM:", font=("Arial", 11, "bold"), text_color="#00FF66")
        self.lbl_class_titulo.pack(anchor="w", padx=15, pady=3)
        self.sub_frame_classes = ctk.CTkFrame(self.frame_classes, fg_color="transparent")
        self.sub_frame_classes.pack(fill="x", padx=10, pady=5)

        # CAIXA OPERACIONAL DE BALCÃO DE FATURAMENTO
        self.frame_busca = ctk.CTkFrame(self, fg_color="#141414", border_width=1, border_color="#333333")
        self.frame_busca.pack(fill="x", padx=15, pady=4)
        self.e_bi = ctk.CTkEntry(self.frame_busca, width=150, placeholder_text="Número do BI..."); self.e_bi.pack(side="left", padx=10, pady=8); self.e_bi.insert(0, "000123456LA045")
        self.e_cmd = ctk.CTkEntry(self.frame_busca, width=180, placeholder_text="NIP / Custo USD / Voz..."); self.e_cmd.pack(side="left", padx=5, pady=8); self.e_cmd.insert(0, "5.99")
        self.lbl_sub_selecionado = ctk.CTkLabel(self.frame_busca, text="Sub-setor: Nenhum", font=("Arial", 11, "bold"), text_color="#00FF66")
        self.lbl_sub_selecionado.pack(side="left", padx=15, pady=8)
        
        # Botões Executivos de Comando Balcão
        ctk.CTkButton(self.frame_busca, text="Verificar Licença", fg_color="#1f538d", text_color="white", font=("Arial", 11, "bold"), command=self.testar_licenca_geral).pack(side="right", padx=10, pady=8)
        ctk.CTkButton(self.frame_busca, text="Pagar 6.000 AKZ", fg_color="#ff3333", text_color="white", font=("Arial", 11, "bold"), command=self.testar_pagamento_licenca).pack(side="right", padx=5, pady=8)
        ctk.CTkButton(self.frame_busca, text="PROCV VIP", fg_color="#e67e22", text_color="white", font=("Arial", 11, "bold"), command=self.testar_procv_vip).pack(side="right", padx=5, pady=8)
        ctk.CTkButton(self.frame_busca, text="Espião Voz/Letra", fg_color="#2eb85c", text_color="white", font=("Arial", 11, "bold"), command=self.testar_espiao_acustico).pack(side="right", padx=5, pady=8)
        ctk.CTkButton(self.frame_busca, text="Calcular Câmbio", fg_color="#a133ff", text_color="white", font=("Arial", 11, "bold"), command=self.testar_cambio_moeda).pack(side="right", padx=5, pady=8)

        # MONITOR VISUAL PRINCIPAL (A FOLHA VERDE COMPATÍVEL COM IMPRESSÃO OFFICE)
        self.frame_visual = ctk.CTkFrame(self, border_width=2, border_color="#00FF66", fg_color="#0d140d")
        self.frame_visual.pack(fill="both", expand=True, padx=15, pady=5)
        self.txt_ecra_visual = ctk.CTkTextbox(self.frame_visual, font=("Consolas", 12), text_color="#00FF66", fg_color="#101810")
        self.txt_ecra_visual.pack(fill="both", expand=True, padx=15, pady=10)
        
        self.carregar_subsetores_interface("EMPRESARIAL")

    def carregar_subsetores_interface(self, nome_pacote):
        self.pacote_selected = nome_pacote
        for btn in self.botoes_subsetores: btn.destroy()
        self.botoes_subsetores.clear()
        
        self.lbl_class_titulo.configure(text=f"🌿 SUB-SETORES DO PACOTE UNIVERSAL {nome_pacote} DISPONÍVEIS:")
        sub_lista = self.cerebro.matriz_infraestrutura_pacotes[nome_pacote]["subcetores"]
        
        for sub_nome in sub_lista:
            btn = ctk.CTkButton(self.sub_frame_classes, text=sub_nome, font=("Arial", 11, "bold"), fg_color="#2b2b2b", text_color="#aaaaaa", hover_color="#00FF66", height=32, command=lambda s=sub_nome: self.selecionar_subsetor(s))
            btn.pack(side="left", padx=8, pady=5)
            self.botoes_subsetores.append(btn)
            
    def selecionar_subsetor(self, nome_sub):
        self.sub_selecionado = nome_sub
        self.lbl_sub_selecionado.configure(text=f"Sub-setor: {nome_sub}")
        self.testar_licenca_geral()

    def testar_licenca_geral(self):
        if not hasattr(self, 'sub_selecionado'):
            self.txt_ecra_visual.delete("1.0", "end")
            self.txt_ecra_visual.insert("end", "⚠️ Por favor, selecione uma das categorias listadas nos botões acima primeiro!")
            return
        bi = self.e_bi.get().strip()
        res_rede = self.cerebro.verify_hibrid_status(self.switch_rede.get())
        info_lic = self.cerebro.verificar_licenca_e_ambiente_geral(bi, self.pacote_selected, self.sub_selecionado)
        self.txt_ecra_visual.insert("end", f"{res_rede}\n\n")
        self.txt_ecra_visual.insert("end", info_lic["msg"])

    def testar_procv_vip(self):
        if not hasattr(self, 'sub_selecionado'): 
            return
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
        try: 
            valor_usd = float(self.e_cmd.get().strip())
        except ValueError:
            self.txt_ecra_visual.delete("1.0", "end")
            self.txt_ecra_visual.insert("end", "❌ Erro: Insira um valor numérico em USD (Ex: 5.99) na caixa para simular o câmbio!")
            return
        res = self.cerebro.calcular_cambio_ia_donna(valor_usd)
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", res)

    def testar_pagamento_licenca(self):
        bi = self.e_bi.get().strip()
        res = self.cerebro.pagar_atualizacao_sistema(bi)
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", res)

    def alternar_modo_rede(self):
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", f"🔄 CHAVEAMENTO COGNITIVO DETECTADO...\n\n{self.cerebro.verify_hibrid_status(self.switch_rede.get())}")

if __name__ == "__main__":
    app = TelaMestreOguisx()
    app.mainloop()

