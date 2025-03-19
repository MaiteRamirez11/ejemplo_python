import random

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

#contador de puntaje
score = 0

# la funcion random.sample() selecciona 3 preguntas aleatorias con sus respuestas correctas y el índice de la respuesta correcta, sin repeticion
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for question, answers_options, correct_index in questions_to_ask:
    #pregunta
    print(question)
    # Se muestran las respuestas posibles
    for i, answer in enumerate(answers_options):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        #se verifica si la respuesta es valida
        if user_answer.isdigit() and int(user_answer) in range(1,5):
            # Se verifica si la respuesta es correcta        
            if int(user_answer) - 1 == correct_index:
                print("¡Correcto!")
                score += 1
                break
            else: score -= 0.5
        else:
            print("Respuesta no válida")
            exit(1)
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers_options[correct_index])

    # Se imprime un blanco al final de la pregunta
    print()

if score > 0: print(f"Puntaje total: {score}")
else: print("Puntaje total: 0")