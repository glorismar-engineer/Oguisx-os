import customtkinter as ctk
import hashlib
from datetime import datetime
import os
import threading
import time

# Garante o motor gráfico profissional para ler as tuas fotos
try:
    from PIL import Image, ImageDraw
except ImportError:
    os.system("pip install pillow")
    from PIL import Image, ImageDraw

ctk.set_appearance_mode("dark")

# =====================================================================
# 🧠 PARTE 1: CÉREBRO COGNITIVO SOBERANO E SUPER DOTADO
# =====================================================================
class OguisxCognitiveBrain:
    def __init__(self):
        self.lema_sistema = "Os sistemas mundiais são treinados, mas a Oguisx tem de ser dotada."
        self.coordenadas_gps = "Lat: -8.8368 | Long: 13.2343 (Luanda, Angola)"
        self.modo_online = True  
        
        self.taxas_mensais = {
            "EMPRESARIAL": "5.000 AKZ/mês", "EDUCAÇÃO": "3.500 AKZ/mês",
            "SAÚDE": "4.000 AKZ/mês", "MININT": "6.000 AKZ/mês"
        }
        
        self.arquitetura_pacotes_nuvem = {
            "EMPRESARIAL": {
                "Pequeno Comércio (Cantina)": "Regra: Stock inicial fixo de 10. Alerta de troco ativo. Venda via BI (Taxa: 0.00 AKZ).",
                "Grandes Armazéns (Armagem)": "Regra: Scanner OCR de faturas de fornecedores em ordem alfabética. PROCV Primavera.",
                "Grandes Indústrias (Sonangol)": "Regra: Auditoria macro de tráfego, balanço geral comercial e liquidação de impostos AGT."
            },
            "MININT": {
                "Delegação do SIC / Polícia": "Regra: Monitor de linguagem corporal e voz. Alerta silencioso para o 113 com coordenadas GPS.",
                "Concurso Público 2026": "Regra: Varredura de histórico escolar, antecedentes criminais do cidadão e botão Contratado ativo."
            }
        }
        
        self.banco_funcionarios = {
            "000123456LA045": {
                "nome": "Glorismar Engenheiro", "salario_base": 250000.0, "faltas_ano": 2, 
                "saldo_bancario": 500000.0, "nif_empresa": "540123456", "empresa_trabalho": "Oguisx Labs",
                "horario": "08:00 - 16:00", "status_contrato": "Efetivo"
            }
        }
        self.stock_cantina = 10

    def verify_hibrid_status(self, online_status) -> str:
        self.modo_online = online_status
        if not self.modo_online:
            return "🌍 [PÉS NO CHÃO] MODO OFF-LINE AUTOMÁTICO RECONHECIDO\n▪️ Regras locais ativas na máquina física. Taxas Ocultas: 0.00 AKZ."
        return "⚡ [CABEÇA NAS NUVENS] MODO ON-LINE ACTIVO\n▪️ Conexão global ativa via X-Road e Aadhaar. Sincronização e Download de pacotes habilitados."

    def descarregar_pacote_dotado(self, nome_pacote: str):
        return self.arquitetura_pacotes_nuvem.get(str(nome_pacote).upper(), {})

    def executar_venda_cantina(self, numero_bi, qtd_texto):
        bi_limpo = str(numero_bi).strip()
        if bi_limpo not in self.banco_funcionarios: return "❌ Erro: BI não cadastrado na carteira digital."
        try: qtd = int(qtd_texto)
        except ValueError: return "❌ Erro: Quantidade inválida."
        if self.stock_cantina < qtd:
            return f"📊 STATUS DO STOCK DA CANTINA:\n• Estado: Vazio / Insuficiente.\n• Disponível: {self.stock_cantina} unidades."
        self.stock_cantina -= qtd
        custo = 1500.0 * qtd
        self.banco_funcionarios[bi_limpo]["saldo_bancario"] -= custo
        return f"🖨️ [COMPROVATIVO TÉRMICO DA CANTINA]\nComprador: {self.banco_funcionarios[bi_limpo]['nome']}\n🛒 Bens Adquiridos | Qtd: {qtd} | Débito: {custo:,.2f} AKZ\n🛡️ Taxa Interbancária: 0.00 AKZ | Stock Restante: {self.stock_cantina}"

    def liquidar_imposto_agt(self, numero_bi, tipo_imposto):
        bi_limpo = str(numero_bi).strip()
        if bi_limpo not in self.banco_funcionarios: return "❌ BI/NIF não cadastrado."
        u = self.banco_funcionarios[bi_limpo]
        u["saldo_bancario"] -= 3000.0
        return f"🖨️ [COMPROVATIVO TÉRMICO AGT]\n▪️ NIF Auditado: {u['nif_empresa']} | Tributo Pago: {tipo_imposto}\n▪️ Quantia Retirada: 3,000.00 AKZ (Taxas Ocultas: 0.00 AKZ)\n📅 Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}"

    def monitor_seguranca_sic(self, dialogo, postura):
        txt = str(dialogo).strip().lower()
        if "assalto" in txt or "passa" in txt or "hostil" in str(postura).lower():
            return f"🚨🚨🚨 [ALERTA SOBERANO: PROTOCOLO SIC ATIVO] 🚨🚨🚨\n📞 Canal aberto com: 113 POLÍCIA & SIC\n📍 GPS Enviado: {self.coordenadas_gps}\n📸 Gravação forense de rostos iniciada."
        return "🛡️ Monitoramento: Diálogo em conformidade moral."

    def processar_voto_cne(self, numero_bi, escolha_partido):
        bi_limpo = str(numero_bi).strip()
        if bi_limpo not in self.banco_funcionarios: return "❌ BI não cadastrado nos cadernos."
        token_voto = hashlib.sha256(f"VOTO-{bi_limpo}".encode()).hexdigest()[:10].upper()
        return f"🗳️ [SISTEMA ELEITORAL CNE]\n▪️ Eleitor Validado: {bi_limpo} | Opção: {escolha_partido}\n🔐 Chave Única Antifraude SHA-256: {token_voto}"


# =====================================================================
# 🖥️ PARTE 2: CAMADA DA INTERFACE GRÁFICA (MOBILE OFFICE HUB)
# =====================================================================
class TelaMestreOguisx(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Oguisx OS - Super Doted Cloud Environment")
        self.geometry("1160x960")
        self.cerebro = OguisxCognitiveBrain()
        self.is_online = True
        self.botoes_classes_dinamicas = []
        
        # 🎨 TESTE SE AS IMAGENS REAIS EXISTEM, SE NÃO, GERA RESERVA PROFISSIONAL
        self.caminho_wallpaper = "oguisx_wallpaper.jpg"
        self.caminho_logo = "oguisx_logo.png"
        
        if not os.path.exists(self.caminho_wallpaper):
            img_w = Image.new("RGB", (1160, 960), color="#040804")
            draw = ImageDraw.Draw(img_w)
            for i in range(0, 1160, 30): draw.line([(i, 0), (i, 960)], fill="#001503", width=1)
            img_w.save(self.caminho_wallpaper)
            
        if not os.path.exists(self.caminho_logo):
            img_l = Image.new("RGBA", (80, 80), color="#00FF66")
            img_l.save(self.caminho_logo)

        # Renderiza o Teu Papel de Parede Real de Fundo
        self.img_fundo_pil = Image.open(self.caminho_wallpaper)
        self.img_fundo_ctk = ctk.CTkImage(light_image=self.img_fundo_pil, dark_image=self.img_fundo_pil, size=(1160, 960))
        self.lbl_background = ctk.CTkLabel(self, image=self.img_fundo_ctk, text="")
        self.lbl_background.place(x=0, y=0, relwidth=1, relheight=1)

        # MENU SUPERIOR OFFICE
        self.frame_menu = ctk.CTkFrame(self, height=40, fg_color="#1e1e1e")
        self.frame_menu.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(self.frame_menu, text=" 📑 Instalação Oguisx    🏠 Início    📊 Multiverso UNESCO    🏢 Gestão AGT & MININT 2026", font=("Arial", 12), text_color="#aaaaaa").pack(side="left", padx=15, pady=8)
        
        self.switch_rede = ctk.CTkSwitch(self.frame_menu, text="Cabeça nas Nuvens (Online)", font=("Arial", 11, "bold"), text_color="white", progress_color="#00FF66", command=self.alternar_modo_rede)
        self.switch_rede.select()
        self.switch_rede.pack(side="right", padx=20, pady=5)

        # 🍁 CONTAINER DA PERGUNTA + CARREGAMENTO DO TEU LOGÓTIPO REAL
        self.frame_desktop = ctk.CTkFrame(self, fg_color="#141414", border_width=1, border_color="#00FF66")
        self.frame_desktop.pack(fill="x", padx=15, pady=4)
        
        # Carrega o Teu Logótipo do Camaleão com cores Google
        self.img_logo_pil = Image.open(self.caminho_logo).resize((60, 60))
        self.img_logo_ctk = ctk.CTkImage(light_image=self.img_logo_pil, dark_image=self.img_logo_pil, size=(60, 60))
        
        self.lbl_logo_img = ctk.CTkLabel(self.frame_desktop, image=self.img_logo_ctk, text="")
        self.lbl_logo_img.pack(side="left", padx=15, pady=5)
        
        self.lbl_pergunta = ctk.CTkLabel(self.frame_desktop, text="❓ COMO PRETENDES USAR A OGUISX?", font=("Arial", 16, "bold"), text_color="#00FF66")
        self.lbl_pergunta.pack(anchor="w", padx=10, pady=15)

        # LISTAGEM DE PACOTES NO TOPO
        self.frame_pacotes_topo = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_pacotes_topo.pack(fill="x", padx=15, pady=4)
        ctk.CTkButton(self.frame_pacotes_topo, text="💼\nActivar Setor\nEmpresarial", font=("Arial", 11, "bold"), fg_color="#1f538d", height=65, width=170, command=lambda: self.iniciar_instalacao_pacote("EMPRESARIAL")).pack(side="left", padx=15, pady=5)
        ctk.CTkButton(self.frame_pacotes_topo, text="🛡️\nActivar Setor\nMININT", font=("Arial", 11, "bold"), fg_color="#ff3333", height=65, width=170, command=lambda: self.iniciar_instalacao_pacote("MININT")).pack(side="left", padx=15, pady=5)

        # PAINEL DINÂMICO DE CLASSES
        self.frame_classes = ctk.CTkFrame(self, fg_color="#181818", border_width=1, border_color="#00FF66")
        self.frame_classes.pack(fill="x", padx=15, pady=4)
        self.lbl_class_titulo = ctk.CTkLabel(self.frame_classes, text="🌿 CONSTITUIÇÃO DO PACOTE INSTALADO (CLASSES E SUB-SETORES):", font=("Arial", 11, "bold"), text_color="#00FF66")
        self.lbl_class_titulo.pack(anchor="w", padx=15, pady=3)
        self.sub_frame_classes = ctk.CTkFrame(self.frame_classes, fg_color="transparent")
        self.sub_frame_classes.pack(fill="x", padx=10, pady=5)

                # INTERAÇÃO DE BALCÃO de faturamento
        self.frame_busca = ctk.CTkFrame(self, fg_color="#141414", border_width=1, border_color="#333333")
        self.frame_busca.pack(fill="x", padx=15, pady=4)
        
        self.e_bi = ctk.CTkEntry(self.frame_busca, width=160, placeholder_text="Número do BI...")
        self.e_bi.pack(side="left", padx=10, pady=8)
        self.e_bi.insert(0, "000123456LA045")
        
        self.e_cmd = ctk.CTkEntry(self.frame_busca, width=150, placeholder_text="Qtd / Comando...")
        self.e_cmd.pack(side="left", padx=5, pady=8)
        self.e_cmd.insert(0, "2")
        
        ctk.CTkButton(self.frame_busca, text="Cantina Venda", fg_color="#00FF66", text_color="black", font=("Arial", 11, "bold"), command=self.testar_venda_cantina).pack(side="left", padx=5, pady=8)
        ctk.CTkButton(self.frame_busca, text="Lançar Falta RH", fg_color="#d9822b", text_color="white", font=("Arial", 11, "bold"), command=self.testar_falta_rh).pack(side="left", padx=5, pady=8)
        ctk.CTkButton(self.frame_busca, text="Pagar IVA AGT", fg_color="#a133ff", text_color="white", font=("Arial", 11, "bold"), command=self.testar_iva_agt).pack(side="left", padx=5, pady=8)
        ctk.CTkButton(self.frame_busca, text="Auditar SIC", fg_color="#ff3333", text_color="white", font=("Arial", 11, "bold"), command=self.testar_sic_defesa).pack(side="left", padx=5, pady=8)
        ctk.CTkButton(self.frame_busca, text="Voto CNE", fg_color="#ffbb00", text_color="black", font=("Arial", 11, "bold"), command=self.testar_voto_cne).pack(side="left", padx=5, pady=8)

        # MONITOR VISUAL PRINCIPAL (A FOLHA VERDE DO WORD)
        self.frame_visual = ctk.CTkFrame(self, border_width=2, border_color="#00FF66", fg_color="#0d140d")
        self.frame_visual.pack(fill="both", expand=True, padx=15, pady=5)
        
        self.txt_ecra_visual = ctk.CTkTextbox(self.frame_visual, font=("Consolas", 12), text_color="#00FF66", fg_color="#101810")
        self.txt_ecra_visual.pack(fill="both", expand=True, padx=15, pady=10)
        self.txt_ecra_visual.insert("end", f"🧠 [OGUISX SOBERANA v1.5] Modo Real de Imagens Activo no monitor.\n✨ LEMA: {self.cerebro.lema_sistema}")

    def iniciar_instalacao_pacote(self, nome_pacote):
        if not self.is_online:
            self.txt_ecra_visual.delete("1.0", "end")
            self.txt_ecra_visual.insert("end", "⚠️ OPERAÇÃO RECUSADA: Modo Online necessário para descarregar novos pacotes!")
            return
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", f"⚡ CONECTANDO SERVIDORES GLOBAIS OGUISX...\n📥 Comando: pip install pacote_{nome_pacote.lower()} --soberano\n💰 Taxa: {self.cerebro.taxas_mensais[nome_pacote]}\n🕒 Estruturando sub-classes da nuvem...")
        threading.Thread(target=self._executar_download_nuvem_thread, args=(nome_pacote,)).start()

    def _executar_download_nuvem_thread(self, nome_pacote):
        time.sleep(1.2)
        mapa_classes = self.cerebro.descarregar_pacote_dotado(nome_pacote)
        self.after(0, lambda: self._atualizar_interface_pos_download(nome_pacote, mapa_classes))

    def _atualizar_interface_pos_download(self, nome_pacote, mapa_classes):
        for btn in self.botoes_classes_dinamicas: 
            btn.destroy()
        self.botoes_classes_dinamicas.clear()
        
        self.lbl_class_titulo.configure(text=f"🌿 FERRAMENTAS ACTIVADAS DA CONSTITUIÇÃO DO PACOTE {nome_pacote}:")
        for classe_nome, diretriz in mapa_classes.items():
            btn = ctk.CTkButton(self.sub_frame_classes, text=classe_nome, font=("Arial", 11, "bold"), fg_color="#2b2b2b", text_color="#aaaaaa", hover_color="#00FF66", height=32, command=lambda n=classe_nome, d=diretriz: self.exibir_diretriz_classe(n, d))
            btn.pack(side="left", padx=8, pady=5)
            self.botoes_classes_dinamicas.append(btn)
        self.txt_ecra_visual.insert("end", f"\n\n✅ INSTALAÇÃO CONCLUÍDA NA NUVEM COM SUCESSO!\nO pacote {nome_pacote} foi totalmente integrado.")

    def exibir_diretriz_classe(self, nome, diretriz):
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", f"==================================================================================\n🏛️ SUB-CLASSE CONSTITUÍDA VIA NUVEM: {nome.upper()}\n==================================================================================\n\n📜 Diretrizes Operacionais:\n{diretriz}\n\n💎 Esta infraestrutura já vive de forma estável localmente nos pés no chão!")

    def testar_venda_cantina(self):
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", self.cerebro.executar_venda_cantina(self.e_bi.get().strip(), self.e_cmd.get().strip()))

    def testar_falta_rh(self):
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", self.cerebro.registrar_falta_rh_e_sms(self.e_bi.get().strip()))

    def testar_iva_agt(self):
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", self.cerebro.liquidar_imposto_agt(self.e_bi.get().strip(), "IVA Comercial"))

    def testar_sic_defesa(self):
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", self.cerebro.monitor_seguranca_sic("Isto é um assalto!", "hostil"))

    def testar_voto_cne(self):
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", self.cerebro.processar_voto_cne(self.e_bi.get().strip(), "PARTIDO CONCORRENTE S"))

    def alternar_modo_rede(self):
        self.is_online = self.switch_rede.get()
        self.txt_ecra_visual.delete("1.0", "end")
        self.txt_ecra_visual.insert("end", f"🔄 CHAVEAMENTO COGNITIVO DETECTADO...\n\n{self.cerebro.verify_hibrid_status(self.is_online)}")

if __name__ == "__main__":
    app = TelaMestreOguisx()
    app.mainloop()
