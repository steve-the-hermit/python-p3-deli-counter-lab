def line(deli_line):
    if not deli_line:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently: "
        for i, person in enumerate(deli_line, start=1):
            line_str += f"{i}. {person} "
        print(line_str.strip())

def take_a_number(deli_line, name):
    deli_line.append(name)
    position = len(deli_line)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(deli_line):
    if not deli_line:
        print("There is nobody waiting to be served!")
    else:
        serving = deli_line.pop(0)
        print(f"Currently serving {serving}.")

# Clearing the deli line for each test case
def reset_deli_line():
    TestDeliCounter.KATZ_DELI.clear()
    TestDeliCounter.OTHER_DELI.clear()
    TestDeliCounter.ANOTHER_DELI.clear()

# Uncomment this line to reset the deli line before each test case
# reset_deli_line()
