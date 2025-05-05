# Tabela de preços formatada
precos = (
    'Corte ................... R$70\n'
    'Barba ................... R$60\n'
    'Combo (corte + barba) ... R$110\n'
    'Máquina e Barba ......... R$90\n'
    'Máquina 1 pente .......... R$45\n'
    'Pezinho ................. R$25\n'
    'Sobrancelha ............. R$20'
)

def main():
    print("Olá! Bem-vindo à Barbearia Madalena!")

    # Pergunta se deseja ver os preços
    resposta = input("Deseja ver os preços? (sim/não): ").strip().lower()

    if resposta == 'sim':
        print("\nAqui estão nossos serviços:\n")
        print(precos)

        # Pergunta se deseja agendar
        agendar = input("\nGostaria de marcar um horário? (sim/não): ").strip().lower()

        if agendar == 'sim':
            horario = input("Maravilha! Me diga qual horário você prefere: ")
            print(f"✅ Prontinho! Seu horário foi agendado para {horario}.")
        else:
            print("Tudo bem, te esperamos numa próxima visita! ✂️")
    
    else:
        # Se a pessoa não quiser nem ver os preços
        print("Sem problemas! Quando quiser cortar o cabelo, estamos à disposição. 💈")

# Executar a função
main()

