#Завдання
#string
#З кожного речення заданого тексту видалити підрядок найбільшої довжини, що починається та закінчується заданими літерами.

import re

class Main(object):

	def __init__(self, text):
		"""Головні змінні"""
		self.text = Text(text)
		# print(self.text)
		self.start_letter = None
		self.end_letter = None
		self.mod_text = []

	def modification_text(self, start_letter, end_letter):
		"""Метод модифікує текст за завданням"""
		self.start_letter = start_letter
		self.end_letter = end_letter
		#Змінні які будуть приймати індекси слів, які я буду находити в кожному реченні
		start_word = None
		end_word = None
		#Я буду діяти так: Спочатку шукаю початок підрядка, тобто слово, що починається на першу введену букву.
		#Як тільки знаходжу, тоді починаю шукати слово, що закінчується на другу введену букву.
		#Як тільки знаходжу таке слово, пошук не припиняється, адже може бути інше слово, що теж підходить. Відповідно я знаходжу найвіддаленіше.
		#В кінці я перевіряю, якщо знайшло початок та кінець, тоді обрізаю та виводжу, якщо нічого не знайшло, або знайшло щось одне - просто виводжу.
		for sentence in self.text.text:
			for word in sentence.sentence:
				if start_word == None:
					if isinstance(word, Word) and word.word[0].lower() == self.start_letter:
						start_word = sentence.sentence.index(word)
				else:
					if isinstance(word, Word) and word.word[-1].lower() == self.end_letter:
						end_word = sentence.sentence.index(word)
			if start_word != None and end_word != None:
				self.mod_text.append(sentence.sentence[0:int(start_word)]+sentence.sentence[int(end_word)+1:-1])
				print("-{0} sentence: slice from {1}({3} word) to {2}({4} word).".format(int(self.text.text.index(sentence))+1, str(sentence.sentence[int(start_word)]), str(sentence.sentence[int(end_word)]), start_word, end_word))
			else:
				self.mod_text.append(sentence.sentence)
				print("-{} sentence: slice is impossible.".format(int(self.text.text.index(sentence))+1))
			#Також обнуляю змінні, щоб почати все спочатку
			start_word = None
			end_word = None
		#Вивід зробив простенький, так як не було зазначено якийсь конкретний. 
		print("\nEdited text:\n")
		for sentence in self.mod_text:
			print(sentence, "\n")


class Word:
	"""Слова"""
	def __init__(self, word):
		self.word = list(word)

	def __repr__(self):
		return f"{[''.join(self.word)]}"


class Sentence:
	"""Речення"""
	def __init__(self, sentence):
		sentence = re.findall(r"[\w']+|[.,!?;]", sentence)
		self.sentence = []
		for word in sentence:
			if word not in ".,!?;":
				word = Word(word)
			self.sentence.append(word)
	
	def __repr__(self):
		return f"{[self.sentence]}"


class Text:
	"""Текст"""
	def __init__(self, text):
    	#Роблю деякі поправки, щоб не уторбвалися пусті списки при split().
		text.replace("..", ".")
		text.replace("...", ".")
    	#Якщо раптом буде щось типу ........ яке не повинно бути в нормальному тексті - ловлю та міняю.
		for i in range(len(text)):
			try:
				if text[i] == "." and text[i+1] ==".":
					text = text[0:i] + text [i+1:]
			except IndexError: pass
    	#Позбуваюсь точки в кінці, якщо є, щоб не утворився зайвий список, а також написав, щоб не було й спереді, а вдруг буде.
		if text[-1] == ".": text = text[:-2] 
		if text[0] == ".": text = text[1:] 
		text = text.split('.')
		self.text = []
		for sentence in text:
			self.text.append(Sentence(sentence))

	def __repr__(self):
		text = "["
		for sentence in self.text:
			text += f"{sentence}\n"
		text += "]"
		return text


if __name__ == "__main__":

    main_text = ".The Chestnuts Long Barrow is a chambered tomb located near the village of Addington in the south-eastern English county of Kent. Constructed during Britain's Early Neolithic period, it belongs to a regional style of barrows produced in the vicinity of the River Medway. The long barrows built in this area are now known as the Medway Megaliths. Chestnuts Long Barrow lies near both Addington Long Barrow and Coldrum Long Barrow on the western side of the river, and was built on land previously inhabited in the Mesolithic period. It consisted of an earthen mound, estimated to have been 15 metres in length, with a chamber built from sarsen megaliths on its eastern end. Human remains placed within this chamber during the Neolithic period were found alongside pottery sherds, stone arrow heads, and a clay pendant. The mound gradually eroded away and was gone by the twentieth century, leaving only the ruined stone chamber..."

    start = input("Enter the 1st letter: ")
 #    try:
 #    	start = int(start)
 #    except ValueError: pass
	# else:
	# 	print("I need a letter...\n") 
	# 	start = input("Enter the 1st letter: ")

    end = input("Enter the last letter: ")
    obj = Main(main_text)
    obj.modification_text(start_letter=start, end_letter=end)



# Chestnuts Long Barrow is a chambered tomb located near the village of Addington in the south-eastern English county of Kent. 
# Constructed during Britain's Early Neolithic period, it belongs to a regional style of barrows produced in the vicinity of the River Medway. 
# The long barrows built in this area are now known as the Medway Megaliths. 
# Chestnuts Long Barrow lies near both Addington Long Barrow and Coldrum Long Barrow on the western side of the river, and was built on land previously inhabited in the Mesolithic period. 
# It consisted of an earthen mound, estimated to have been 15 metres in length, with a chamber built from sarsen megaliths on its eastern end. 
# Human remains placed within this chamber during the Neolithic period were found alongside pottery sherds, stone arrow heads, and a clay pendant. 
# The mound gradually eroded away and was gone by the twentieth century, leaving only the ruined stone chamber.