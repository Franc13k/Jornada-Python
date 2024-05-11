import flet as ft

def main(pagina):
    titulo = ft.Text("ChatZap")
    
    titulo_popup = ft.Text("Bem vindo ao ChatZap")
    camp_nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    
    chat = ft.Column()
    
    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)    
    
    def enviar_mensagem(evento):
        texto_mensagem = camp_mensagem.value
        nome_usuario = camp_nome_usuario.value
        mensagem = f"{nome_usuario}: {texto_mensagem}"
        pagina.pubsub.send_all(mensagem)
        camp_mensagem.value = ""
        pagina.update()
    
    camp_mensagem = ft.TextField(label="Digite sua mensagem...", on_submit=enviar_mensagem) 
    bot_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    linha_mensagem = ft.Row([camp_mensagem, bot_enviar_mensagem])
    
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        popup.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f"{camp_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()
        
    bot_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat) 
    popup = ft.AlertDialog(
        title=titulo_popup,   
        content=camp_nome_usuario, 
        actions=[bot_entrar])
    
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)
    
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    
    
ft.app(main, view=ft.WEB_BROWSER)