import json

airport = ""
domestic = []
international = []

if __name__ == "__main__":
	c = 9
	while c != 0:
		print("\n")
		c = int(input("Type an int value from below and hit enter:\n"
									"1 - Enter airport code\n"
									"2 - Enter domestic\n"
									"3 - Enter international\n"
									"4 - Generate json file\n"
									"0 - Exit\n\n"))

		while c < 0 or c > 4:
			print("Invalid number.")
			c = int(input("Type an int value from below and hit enter:\n"
									"1 - Enter airport code\n"
									"2 - Enter domestic\n"
									"3 - Enter international\n"
									"4 - Generate json file\n"
									"0 - Exit\n\n"))

		if c == 1:
			airport = input("Enter airport code:\n")
		elif c == 2:
			
			x = ""
			while x != "quit":
				x = input("Enter domestic:\n")
				if (x != "quit"):
					domestic.append(int(x))
		elif c == 3:
			
			x = ""
			while x != "quit":
				x = input("Enter international:\n")
				if (x != "quit"):
					international.append(int(x))
		elif c == 4:
			final_list = []
			year = 2002
			month = 10
			for i in range(len(domestic)):
				item = {}
				item["airport"] = airport
				item["domestic"] = domestic[i]
				item["international"] = international[i]
				if month > 12:
					year += 1
					month = 1
				item["month"] = str(year) + "-" + str(month)
				month += 1
				final_list.append(item)
		
			with open(airport + "_data.json", 'w') as outfile:
				json.dump(final_list, outfile)
