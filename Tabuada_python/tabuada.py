import flet as ft

def calc_tabuada(numero):
    if 2 <= numero <= 10:
        return [f"{numero} x {i:2} = {numero * i:2}" for i in range(1, 11)]
    else:
        raise ValueError("Número deve estar entre 2 e 10.")
    
def on_click(number_input, result_area):
    # verifica se o campo está vazio
    try:
        if not number_input.value.strip():
            raise ValueError('O campo não funciona vazio')
        
        # entrada do usuario com uma conversão para inteiro
        number = int(number_input.value)
        # chamada da função 
        results = calc_tabuada(number)
        
       # Limpa resultados anteriores
        result_area.controls.clear()

        # Resultados centralizado
        for result in results:
            result_area.controls.append(
                ft.Row(
                    controls=[
                        ft.Text(
                            value=result, 
                            size=20, 
                            color="black", 
                            weight=ft.FontWeight.BOLD,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )
        
        # Torna visível após cálculo
        result_area.visible = True  

        # Atualiza a tela para mostrar as mudanças
        number_input.page.update()

    # captura erros
    except ValueError as ve:
        result_area.controls = [
            ft.Row(
                controls=[
                    ft.Text(
                        value=str(ve), 
                        color="black", 
                        weight=ft.FontWeight.BOLD, 
                        size=25
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]

        # exibição na tela
        result_area.visible = True
        # atualização da página
        number_input.page.update()
    