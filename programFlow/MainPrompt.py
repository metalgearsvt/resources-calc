class MainPrompt:

	def __init__(self):
		self.test = ""
		self.options = ["Edit Factories", "Edit Utility Buildings", "Item Database", "Transactions", "Exit"]

	def set_test(self, i):
		self.test = i

	def get_test(self):
		return self.test

	def disp_prompt(self):
		print("\n=== MENU ===\n")
		for i in range(len(self.options)):
			print(str(i + 1) + ".) " + self.options[i])
		option = int(input("\nOption: ")) - 1
		self.handle_option(self.options[option])

	def handle_option(self, op):
		print("You chose " + op)
