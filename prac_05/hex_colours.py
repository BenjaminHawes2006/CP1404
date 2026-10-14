"""
CP1404 Practical
hexadecimal colour names in a dictionary
"""

colour_to_hex = {'ABSOLUTE ZERO': '0048ba', 'ALICEBLUE': 'f0f8ff', 'AMBER': 'ffbf00', 'ANTIQUEWHITE': 'faebd7', 'APRICOT': 'fbceb1', 'AQUA': '00ffff', 'ARMY GREEN': '4b5320', 'ASH GREY': 'b2beb5', 'BABY BLUE': '89cff0', 'BARN RED': '7c0a02'}

colour = input("Enter colour name: ")
valid_colour = colour.upper()

while colour != "":
    if valid_colour in colour_to_hex.keys():
        print(f"{colour} is #{colour_to_hex[valid_colour]}")
    else:
        print("Invalid colour")
    colour = input("Enter colour name: ")
    valid_colour = colour.upper()

