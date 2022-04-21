import random

class Pendu():
	def __init__(self):
		self.mot = Mot()
		self.mot.mot = self.mot.choisir()
#		print(self.mot.mot)
		self.mot_cache = '_' * len(self.mot.mot)
		self.nb_essais = 0
		self.gagne = False
		self.perdu = False

	def essai(self, lettre):
		if lettre in self.mot.mot:
			for i in range(len(self.mot.mot)):
				if self.mot.mot[i] == lettre:
					self.mot_cache = self.mot_cache[:i] + lettre + self.mot_cache[i+1:]
#					print(self.mot_cache)
			self.trouver(self.mot_cache)
		else:
			print('Erreur de saisie')
			self.nb_essais += 1
			if self.nb_essais == 10:
				self.perdu = True

	def trouver(self, tentative):
		if tentative == self.mot.mot:
			self.gagne = True
		else:
			self.nb_essais += 1
			if self.nb_essais == 10:
				self.perdu = True	

	def jouer(self):
		while not self.gagne and not self.perdu:
			self.afficher()
			lettre = input('Entrez une lettre ou un mot entier: ')
			if len(lettre) == 1:
				self.essai(lettre)
			else:
				self.trouver(lettre)
		self.afficher()

	def afficher(self):
		print(self.mot_cache)
		print('Essais restants:', 10 - self.nb_essais)
		if self.gagne:
			print('Gagné!')
		elif self.perdu:
			print('Perdu!')

class Mot():
	def __init__(self):
		self.mot = ""

	def choisir(self):
		with open('mots.txt', 'r') as f:
			mots = f.readlines()
			self.mot = mots[random.randint(0, len(mots) - 1)].strip()

		return self.mot
