# importando a interface gráfica - flet
import flet as ft

# importando a tabuada.py
import tabuada as tab


def main(page: ft.Page):
    # titulo
    page.title = 'TABUADA - PYTHON'

    # titulo principal
    message = ft.Text(
                    value='Bem vindo a tabuada no python', 
                    color='DodgerBlue', 
                    size=60, 
                    weight=ft.FontWeight.BOLD
    )

    # icone
    icon = ft.Icon(name='calculate', size=60)

    # menu
    menu = ft.Text(
        value='Informe uma opção de 2 a 10: ',
        weight=ft.FontWeight.BOLD,
        size=40,
    )

    # caixa de input
    caixa_text = ft.TextField(label='Informe a opção', width=400)
    # resultado
    result_area = ft.Column(controls=[], spacing=10, visible=False)

    # botão
    button = ft.ElevatedButton(
        text=('Clique para executar'),
        on_click=lambda e: tab.on_click(caixa_text, result_area)
    )

    # centralizads - mensagem e icone
    row = ft.Row (
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[icon, message]
    )

    # menu
    row_menu = ft.Row(
        controls=[menu],
        spacing=30,
        alignment=ft.MainAxisAlignment.CENTER
    )

    # input
    input = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[caixa_text, button]
    )


    container = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[row, row_menu, input, result_area],
        spacing=20
    )

    page.add(container)

ft.app(target=main)