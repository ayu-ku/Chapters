
class IllegalCarError(Exception):
	pass


class Car:
	person_weight = 70

	def __init__(self, pax_count, car_mass, gear_count) -> None:
		self.pax_count = pax_count
		self.car_mass = car_mass
		self.gear_count = gear_count
		self.incorrect_parameters = {}
		try:
			self.check_class_parameters()
		except IllegalCarError as ex:
			print(ex)

	def check_class_parameters(self) -> None:
		self.check_if_pax_count_is_correct()
		self.check_if_car_mass_is_correct()
		self.check_if_gear_count_is_correct()
		if self.incorrect_parameters:
			raise IllegalCarError(
				{"message": "Incerrect parameters provided", "data": self.incorrect_parameters}
			)

	def check_if_pax_count_is_correct(self) -> None:
		if self.pax_count not in range(1, 5):
			self.incorrect_parameters["pax_count"] = self.pax_count

	def check_if_car_mass_is_correct(self) -> None:
		if not (type(self.car_mass) in (int, float) and self.car_mass <= 2000):
			self.incorrect_parameters["car_mass"] = self.car_mass

	def check_if_gear_count_is_correct(self) -> None:
		if not isinstance(self.gear_count, int):
			self.incorrect_parameters["gear_count"] = self.gear_count

	def total_mass(self) -> float:
		total_car_mass = self.pax_count * self.person_weight + self.car_mass
		return total_car_mass


class Workshop:
	def accept(self, vehicle):
		vehicle.repair()


class Vehicle:
	def __init__(self, vehicle_type):
		self.vehicle_type = vehicle_type

	def repair(self):
		print(self.vehicle_type)


