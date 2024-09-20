import flet as ft

def calc_tabuada(numero):
    if 2 <= numero <= 10:
        return [f"{numero} x {i} = {numero * i}" for i in range(1, 11)]
    else:
        raise ValueError("Número deve estar entre 2 e 10.")
    
def on_click(number_input, result_area):
    try:
        number = int(number_input.value)
        results = calc_tabuada(number)
        
        # Limpa resultados anteriores
        result_area.controls.clear()
        for result in results:
            result_area.controls.append(ft.Text(value=result, size=20, color="blue"))
        
        result_area.visible = True  # Torna visível após cálculo
    except ValueError as ve:
        result_area.controls = [ft.Text(value=str(ve), color="red", size=20)]
        result_area.visible = True
    except Exception:
        result_area.controls = [ft.Text(value="Por favor, insira um número válido.", color="red", size=20)]
        result_area.visible = True