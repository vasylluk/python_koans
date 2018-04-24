#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import re

class AboutMyOwnClass(Koan):

	def test_my_car_class_name(self):
	    self.assertEqual('Car', "Car")

	class Car(object):
		
		"I'm a car"

		def __init__(self):
			#ініціалізація параметрів за замовчуванням
			self._name = 'Base'
			self.price = 100

		def set_name(self, a_name):
			self._name = a_name

		def is_premium(self):
			#перевірка автомобіля на його належність до преміум-класу
			if(self.price>=1000000):
				return True
			else:
				return False

	def test_set_sort(self)
		#маніпуляції з множиною
		car_set=["audi",'bmw',"rover","cadillac"]
		self.assertEqual(["audi","bmw","cadillac","rover"], sorted(car_set))

	def test_cap_set(self):
		#поелементна маніпуляція у множині
		car_set=["audi",'bmw',"rover","cadillac"]
		cap_set=[car.capitalize() for car in car_set]
		self.assertEqual(["Audi","Bmw","Rover","Cadillac"],cap_set)

	
	def test_list_comprehensions(self):
		#операції над списками
		sentence = "the quick chick fox goes over the lazy dog"
		words = sentence.split()
		word_lengths = [len(word) for word in words if word != "the"]
		word_lengths.pop(1)
		s = sum(word_lengths)
		self.assertEqual(s,23)

	def test_car_is_premium(self):
		#перезапис параметру класу
		UAZ = self.Car()
		UAZ.price = 12000
		self.assertFalse(UAZ.is_premium())

	def test_email(self):
		#перевірка валідності адреси електронної пошти
		pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
		pattern = re.compile(pattern)
		not_passed=0
		passed=0
		emails = ["i@u.com", "p@p.org", "s.t`1?ug{}ly@email.com"]
		for email in emails:
			if not re.match(pattern, email):
				not_passed+=1
			elif not pattern:
				not_passed+=1
			else:
				passed+=1
		self.assertEqual(passed,3)
		self.assertEqual(not_passed,0)

			
	def test_dict_manipulations(self):
		#додавання та видалення елементів зі словника
		result=0
		car_dict = {
			"BMW" : 10000,
			"Mercedes" : 15000,
			"Audi" : 10000,
			"Saab" : 12000
		}
		del car_dict["Audi"]
		car_dict["Renault"] = 15000
		if "Audi" not in car_dict:
			result=-1
		if "Renault" in car_dict:
			result=1
		self.assertEqual(result,1)



	def test_init_method(self):
		#виклик параметрів за замовчуванням
		saab = self.Car()
		self.assertEqual('Base', saab._name)

	def test_init_method_customize(self):
		#перезапис параметру за замовчуванням
		saab = self.Car()
		saab.set_name("MySaab")
		self.assertEqual('MySaab', saab._name)

	def test_class_inheritance(self):
		#виклик назви класу об’єкта
		bmw = self.Car()
		self.assertEqual('Car', bmw.__class__.__name__)

	def test_docstrings(self):
		#виклик документації класу
		self.assertRegex(self.Car.__doc__, "I'm a car")

	def test_speeds(self):
		speed = 100
		self.assertEqual(speed,100)
