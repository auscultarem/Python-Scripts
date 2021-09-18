from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_container = []

for question in question_data:
	question_text = question['question']
	question_answer = question['correct_answer']
	new_question_object = Question(question_text, question_answer) # Creo un objeto con dos argumentos
	question_container.append(new_question_object) # Agrego el objeto creado a una lista llamada contenedor

quiz = QuizBrain(question_container) # Creo un objeto quiz y le envio una lista de objetos que tienen dos argumentos

while quiz.still_has_questions():
	quiz.next_question()