animais = [  
    {"id": 1, "tipo": "Leão", "peso": 190, "altura": 1.2, "idade": 16, "habitat": "Savana", "classe": "Mamífero"},
    {"id": 2, "tipo": "Elefante", "peso": 5000, "altura": 3.3, "idade": 54, "habitat": "Savana", "classe": "Mamífero"},
    {"id": 3, "tipo": "Girafa", "peso": 1200, "altura": 5.5, "idade": 23, "habitat": "Savana", "classe": "Mamífero"},
    {"id": 4, "tipo": "Crocodilo", "peso": 450, "altura": 0.5, "idade": 61, "habitat": "Pântano", "classe": "Réptil"},
    {"id": 5, "tipo": "Águia", "peso": 6.5, "altura": 0.9, "idade": 34, "habitat": "Alasca", "classe": "Ave"},
    {"id": 6, "tipo": "Pato", "peso": 3.5, "altura": 0.8, "idade": 12, "habitat": "Lagos", "classe": "Ave"}
]

def adicionar_animal(tipo, peso, altura, idade, habitat, classe):
    novo_id = max(animal["id"] for animal in animais) + 1
    novo_animal = {"id": novo_id, "tipo": tipo, "peso": peso, "altura": altura, "idade": idade, "habitat": habitat, "classe": classe}
    animais.append(novo_animal)
    print(f"Animal adicionado com sucesso. ID: {novo_id}")

def atualizar_animal(id, tipo=None, peso=None, altura=None, idade=None, habitat=None, classe=None):
    for animal in animais:
        if animal["id"] == id:
            if tipo:
                animal["tipo"] = tipo
            if peso:
                animal["peso"] = peso
            if altura:
                animal["altura"] =  altura
            if idade:
                animal["idade"] = idade
            if habitat:
                animal["habitat"] = habitat
            if classe:
                animal["classe"] = classe
            print(f"Animal com ID {id} atualizado com sucesso.")
            return
    print(f"Animal com ID {id} não encontrado.")

def mostrar_animais():
    for animal in animais:
        print(f"ID: {animal['id']}")
        print(f"Tipo: {animal['tipo']}")
        print(f"Peso: {animal['peso']} Kg")
        print(f"Altura: {animal['altura']} m")
        print(f"Idade: {animal['idade']} anos")
        print(f"Habitat: {animal['habitat']}")
        print(f"Classe: {animal['classe']}")
        print("-" * 30)

def mostrar_animal_por_id(id):
    for animal in animais:
        if animal["id"] == id:
            print(f"ID: {animal['id']}")
            print(f"Tipo: {animal['tipo']}")
            print(f"Peso: {animal['peso']} Kg")
            print(f"Altura: {animal['altura']} m")
            print(f"Idade: {animal['idade']} anos")
            print(f"Habitat: {animal['habitat']}")
            print(f"Classe: {animal['classe']}")
            return
    print(f"Animal com ID {id} não encontrado.")

def deletar_animal(id):
    for animal in animais:
        if animal["id"] == id:
            animais.remove(animal)
            print(f"Animal com ID {id} deletado com sucesso.")
            return
    print(f"Animal com ID {id} não encontrado.")

def buscar_animais(criterio, valor):
    resultados = []
    for animal in animais:
        if criterio in animal and animal[criterio] == valor:
            resultados.append(animal)
    return resultados


print("Lista inicial de animais")
mostrar_animais()

print("\nAdicionando um novo animal: ")    
adicionar_animal("Gato", 4.5, 0.3, 5, "Casa", "Mamífero")

print("\nAtualizando o peso do elefante: ")
atualizar_animal(2, peso=5500)

print("\nMostrando a lista atualizada de animais: ")
mostrar_animais()

print("\nMostrando animal específico (ID 4): ")
mostrar_animal_por_id(4)

print("\nDeletando o leão: ")
deletar_animal(1)

print("\nLista final de animais: ")
mostrar_animais()


resultado_mamiferos = buscar_animais("classe", "Mamífero")
print("\nAnimais da classe 'Mamífero':")
for animal in resultado_mamiferos:
    print(f"ID: {animal['id']}, Tipo: {animal['tipo']}, Peso: {animal['peso']} Kg, Altura: {animal['altura']} m, Idade: {animal['idade']}, Habitat: {animal['habitat']}")
