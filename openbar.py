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
pref=dict()
def getpreference():
    for k, v in questions.iteritems():
        print v
        inp=raw_input ("Enter yes or y if you like else whatever :").lower()
        if inp == "yes" or inp =="y":
            pref[k]=True
        else: pref[k]=False
    return pref
    
def makedrink():
    import random
    drink=list()
    for k, v in pref.iteritems():
        if v:
            drink.append(random.choice(ingredients[k]))
    if len(drink) > 0:
        print "your drink contains: "
        for x in drink:
            print x
    else: print "Congratulations ! You are sober today day"    
        
if __name__ == "__main__":
    getpreference()
    makedrink()
