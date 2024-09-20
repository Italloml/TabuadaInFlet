import flet as ft

# import pageTabe02

def main(page: ft.Page):
    # nome 
    page.Text = 'TABUADA - PYTHON'

    message = ft.Text(
                    value='Bem vindo a tabuada no python', 
                    color='red', 
                    size=60, weight=ft.FontWeight.BOLD
    )

    # icone
    icon = ft.Icon(name='calculate', size=60)

    # criação de uma linha centralizada - mensagem e icone
    row = ft.Row (
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[icon, message]
    )

    container = ft.Container (
        content=row,
        alignment=ft.alignment.center,
        width=page.width
    )

    page.add(container)

ft.app(target=main)