# birthstone = {
#         "january": "Garnet",       
#         "february": "Amethyst",
#         "march": "Aquamarine",
#         "april": "Diamond",
#         "may": "Emerald",
#         "june": "Pearl",
#         "july": "Ruby",
#         "august": "Peridot",
#         "september": "Sapphire",
#         "october": "Opal",
#         "november": "Topaz",
#         "december": "Turquoise",
#     }

def get_birthmonth(birth):    
    for month in birthstone.keys(): 
        if birth == "january":
            return "Garnet"
        elif birth == "february":
            return "Amethyst"
        elif birth == "march":
            return "Aquamarine"
        elif birth == "april":
            return "Diamond"
        elif birth ==  "may":
            return  "Emerald"
        elif birth == "june":
            return "Pearl"
        elif birth == "july":
            return "Ruby"
        elif birth == "august"
            return "Peridot"
        elif birth == "september":
            return "Sapphire" 
        elif birth == "october":
            return "Opal"
        elif birth == "november":
            return "Topaz"
        elif birth == "december"
            return "Turquoise"
        else:
            return "N/A"