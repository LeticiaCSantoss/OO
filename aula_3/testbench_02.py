from package.maths.terms import Circle

# Exemplo de uso da classe Circle
circulo = Circle(5, 3, 4)  # Cria um círculo com raio 5 e centro (3, 4)
print("Equação Reduzida:", circulo.equacao_reduzida(1, 2))
print("Circunferência:", circulo.circunferencia())
print("Área:", circulo.area())
circulo.model()

