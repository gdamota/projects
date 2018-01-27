questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def answers():
    resp['yes', 'y']
    pref[]
    for key in questions:
        ans = input(questions[key]+' ')
        ans.lower()
        if ans in resp:
           return pref[ans]

def mixer(value):
    drink[]
    for key in value.items():
        if value = True:
            drink.append(ingredients[key])
    return drink
    
def main():
    results = answers()
    for drink in mixer(results):
        print(drink)
            