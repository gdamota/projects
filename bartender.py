questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}


ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def responses()
    resps['y','yes']
    prefs = []
    for keys in questions:
        ans = input(questions[keys] + ' ')
        ans = ans.lower()
        if ans in resps:
            prefs[ans]

def mixer(value)
    drink[]
    for key in value:
        if value is True:
            drink.append(ingredients[key])
        return drink
    
# main 

def main():
    yourDrink = responses()
    for drink in mixer(yourDrink):
        print(drink)
