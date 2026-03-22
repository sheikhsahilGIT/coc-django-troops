from django.shortcuts import render

troops = [
    {"name": "Barbarian", "desc": "Tough melee warrior.", "housing": 1, "elixir": 40, "image": "https://picsum.photos/id/1015/400/300", "detail": "Fast and cheap."},
    {"name": "Archer", "desc": "Ranged attacker.", "housing": 1, "elixir": 50, "image": "https://picsum.photos/id/201/400/300", "detail": "Shoots from behind."},
    # ... add the other 6 troops the same way as before ...
    {"name": "Dragon", "desc": "Legendary flying beast.", "housing": 20, "elixir": 500, "image": "https://picsum.photos/id/1016/400/300", "detail": "Very strong!"}
]

def home(request):
    return render(request, 'index.html', {'troops': troops})