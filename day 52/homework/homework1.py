#Pete, the baker

def cakes(recipe, available):  
    max_cakes = float('inf') 
    for ingredient, amount_required in recipe.items():  
        if ingredient not in available:  
            return 0  
        amount_available = available[ingredient]  
        max_cakes = min(max_cakes, amount_available // amount_required)  
    return max_cakes