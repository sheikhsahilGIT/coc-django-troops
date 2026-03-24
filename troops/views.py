from collections import OrderedDict

from django.shortcuts import render


def _img(slug: str) -> str:
    """Troop/hero/pet artwork pulled from coc.guide (game-ripped icons)."""
    return f"https://coc.guide/images/troops/{slug}.png"


# category -> display order (main village focus + heroes/pets/siege + extras)
_UNITS = [
    # —— Elixir troops (Home Village) ——
    {"name": "Barbarian", "category": "Elixir Troops", "housing": 1, "cost": 50, "resource": "Elixir", "detail": "Fearless melee fighter; cheap and fast to train.", "image": _img("barbarian")},
    {"name": "Archer", "category": "Elixir Troops", "housing": 1, "cost": 100, "resource": "Elixir", "detail": "Ranged damage behind tanks and walls.", "image": _img("archer")},
    {"name": "Goblin", "category": "Elixir Troops", "housing": 1, "cost": 160, "resource": "Elixir", "detail": "Fast resource hunter that targets storages and mines.", "image": _img("goblin")},
    {"name": "Giant", "category": "Elixir Troops", "housing": 5, "cost": 2_000, "resource": "Elixir", "detail": "Tank that heads for defenses first.", "image": _img("giant")},
    {"name": "Wall Breaker", "category": "Elixir Troops", "housing": 2, "cost": 5_000, "resource": "Elixir", "detail": "Blasts through walls to open the base.", "image": _img("wall-breaker")},
    {"name": "Balloon", "category": "Elixir Troops", "housing": 5, "cost": 7_600, "resource": "Elixir", "detail": "Flying splash damage that targets defenses.", "image": _img("balloon")},
    {"name": "Wizard", "category": "Elixir Troops", "housing": 4, "cost": 4_000, "resource": "Elixir", "detail": "Glass cannon with strong splash damage.", "image": _img("wizard")},
    {"name": "Healer", "category": "Elixir Troops", "housing": 14, "cost": 12_000, "resource": "Elixir", "detail": "Air unit that heals ground troops under her.", "image": _img("healer")},
    {"name": "Dragon", "category": "Elixir Troops", "housing": 20, "cost": 36_000, "resource": "Elixir", "detail": "Durable flying unit with splash breath.", "image": _img("dragon")},
    {"name": "P.E.K.K.A", "category": "Elixir Troops", "housing": 25, "cost": 46_000, "resource": "Elixir", "detail": "Slow heavy hitter with huge single-target damage.", "image": _img("pekka")},
    {"name": "Baby Dragon", "category": "Elixir Troops", "housing": 10, "cost": 15_000, "resource": "Elixir", "detail": "Flying splasher; tantrum boosts fire rate when alone.", "image": _img("baby-dragon")},
    {"name": "Miner", "category": "Elixir Troops", "housing": 6, "cost": 5_600, "resource": "Elixir", "detail": "Burrows underground, avoids defenses while moving.", "image": _img("miner")},
    {"name": "Electro Dragon", "category": "Elixir Troops", "housing": 30, "cost": 42_000, "resource": "Elixir", "detail": "Chain lightning that jumps across multiple targets.", "image": _img("electro-dragon")},
    {"name": "Yeti", "category": "Elixir Troops", "housing": 18, "cost": 19_000, "resource": "Elixir", "detail": "Splits Yetimites on destruction; strong behind a tank line.", "image": _img("yeti")},
    {"name": "Dragon Rider", "category": "Elixir Troops", "housing": 25, "cost": 26_000, "resource": "Elixir", "detail": "Flying unit that drops fire bombs while circling.", "image": _img("dragon-rider")},
    {"name": "Electro Titan", "category": "Elixir Troops", "housing": 32, "cost": 33_000, "resource": "Elixir", "detail": "Huge tank that radiates lightning to nearby buildings.", "image": _img("electro-titan")},
    {"name": "Apprentice Warden", "category": "Elixir Troops", "housing": 20, "cost": 20_000, "resource": "Elixir", "detail": "Support avatar of the Grand Warden with his own aura pattern.", "image": _img("apprentice-warden")},
    {"name": "Root Rider", "category": "Elixir Troops", "housing": 18, "cost": 18_000, "resource": "Elixir", "detail": "Rider on a root beast that smashes walls and defenses.", "image": _img("root-rider")},
    # —— Dark Elixir troops ——
    {"name": "Minion", "category": "Dark Elixir Troops", "housing": 2, "cost": 6, "resource": "Dark", "detail": "Cheap fast flyer; good for cleanup.", "image": _img("minion")},
    {"name": "Hog Rider", "category": "Dark Elixir Troops", "housing": 5, "cost": 56, "resource": "Dark", "detail": "Jumps walls and hammers defenses.", "image": _img("hog-rider")},
    {"name": "Valkyrie", "category": "Dark Elixir Troops", "housing": 8, "cost": 70, "resource": "Dark", "detail": "Spin attack cleaves clustered buildings.", "image": _img("valkyrie")},
    {"name": "Golem", "category": "Dark Elixir Troops", "housing": 30, "cost": 205, "resource": "Dark", "detail": "Splits into Golemites; soaks huge damage.", "image": _img("golem")},
    {"name": "Witch", "category": "Dark Elixir Troops", "housing": 12, "cost": 205, "resource": "Dark", "detail": "Spawns skeletons continuously behind the front line.", "image": _img("witch")},
    {"name": "Lava Hound", "category": "Dark Elixir Troops", "housing": 30, "cost": 190, "resource": "Dark", "detail": "Air tank that pops into Lava Pups.", "image": _img("lava-hound")},
    {"name": "Bowler", "category": "Dark Elixir Troops", "housing": 6, "cost": 100, "resource": "Dark", "detail": "Rolling boulder hits a line of buildings.", "image": _img("bowler")},
    {"name": "Ice Golem", "category": "Dark Elixir Troops", "housing": 15, "cost": 120, "resource": "Dark", "detail": "Shatters with a freeze when destroyed.", "image": _img("ice-golem")},
    {"name": "Headhunter", "category": "Dark Elixir Troops", "housing": 6, "cost": 115, "resource": "Dark", "detail": "Bonus damage vs heroes; throws poison vials.", "image": _img("headhunter")},
    {"name": "Druid", "category": "Dark Elixir Troops", "housing": 16, "cost": 200, "resource": "Dark", "detail": "Can shapeshift to bear form for extra melee pressure.", "image": _img("druid")},
    # —— Super Troops ——
    {"name": "Super Barbarian", "category": "Super Troops", "housing": 5, "cost": 1_500, "resource": "Elixir", "detail": "Barbarian with rage boost and extra HP.", "image": _img("super-barbarian")},
    {"name": "Sneaky Goblin", "category": "Super Troops", "housing": 3, "cost": 3_600, "resource": "Elixir", "detail": "Invisible to defenses until it attacks.", "image": _img("sneaky-goblin")},
    {"name": "Super Giant", "category": "Super Troops", "housing": 5, "cost": 6_000, "resource": "Elixir", "detail": "Doorbuster Giant that targets walls first.", "image": _img("super-giant")},
    {"name": "Rocket Balloon", "category": "Super Troops", "housing": 8, "cost": 5_600, "resource": "Elixir", "detail": "First hit is a fast rocket charge on defenses.", "image": _img("rocket-balloon")},
    {"name": "Super Wall Breaker", "category": "Super Troops", "housing": 4, "cost": 10_000, "resource": "Elixir", "detail": "Leaves a small bomb after blowing a lane.", "image": _img("super-wall-breaker")},
    {"name": "Super Wizard", "category": "Super Troops", "housing": 10, "cost": 8_000, "resource": "Elixir", "detail": "Power beam that ramps up the longer he fires.", "image": _img("super-wizard")},
    {"name": "Inferno Dragon", "category": "Super Troops", "housing": 15, "cost": 18_000, "resource": "Elixir", "detail": "Beam ramps to single-target inferno damage.", "image": _img("inferno-dragon")},
    {"name": "Super Dragon", "category": "Super Troops", "housing": 40, "cost": 45_000, "resource": "Elixir", "detail": "Larger dragon with stronger breath.", "image": _img("super-dragon")},
    {"name": "Super Minion", "category": "Super Troops", "housing": 12, "cost": 18, "resource": "Dark", "detail": "First shots are long-range blind spots to air defenses.", "image": _img("super-minion")},
    {"name": "Super Valkyrie", "category": "Super Troops", "housing": 20, "cost": 200, "resource": "Dark", "detail": "Spin leaves a rage trail after moving.", "image": _img("super-valkyrie")},
    {"name": "Super Witch", "category": "Super Troops", "housing": 40, "cost": 360, "resource": "Dark", "detail": "Summons a Big Boy instead of many skeletons.", "image": _img("super-witch")},
    {"name": "Ice Hound", "category": "Super Troops", "housing": 40, "cost": 300, "resource": "Dark", "detail": "Frozen variant that freezes on death.", "image": _img("ice-hound")},
    {"name": "Super Bowler", "category": "Super Troops", "housing": 30, "cost": 280, "resource": "Dark", "detail": "Boulder leaves a damaging trail.", "image": _img("super-bowler")},
    {"name": "Super Archer", "category": "Super Troops", "housing": 12, "cost": 4_000, "resource": "Elixir", "detail": "Cross-map opening shot before entering normal range.", "image": _img("super-archer")},
    {"name": "Super Miner", "category": "Super Troops", "housing": 24, "cost": 6_000, "resource": "Elixir", "detail": "Heals briefly after surfacing from underground.", "image": _img("super-miner")},
    {"name": "Super Hog Rider", "category": "Super Troops", "housing": 12, "cost": 170, "resource": "Dark", "detail": "Faster hog with a burst heal when ability triggers.", "image": _img("super-hog-rider")},
    # —— Siege machines ——
    {"name": "Wall Wrecker", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Plows toward Town Hall slamming through segments.", "image": _img("wall-wrecker")},
    {"name": "Battle Blimp", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Flying delivery to core; drops CC troops overhead.", "image": _img("battle-blimp")},
    {"name": "Stone Slammer", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Air siege that splashes defenses from above.", "image": _img("stone-slammer")},
    {"name": "Siege Barracks", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Spawns a P.E.K.K.A and many Wizards on the map edge.", "image": _img("siege-barracks")},
    {"name": "Log Launcher", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Rolls logs through bases for line damage.", "image": _img("log-launcher")},
    {"name": "Flame Flinger", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Long-range incendiary shots from the perimeter.", "image": _img("flame-flinger")},
    {"name": "Battle Drill", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Underground drill that erupts under key targets.", "image": _img("battle-drill")},
    # —— Heroes ——
    {"name": "Barbarian King", "category": "Heroes", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Melee hero; Iron Fist boosts him and nearby barbarians.", "image": _img("barbarian-king")},
    {"name": "Archer Queen", "category": "Heroes", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Ranged hero; Royal Cloak grants invisibility and DPS.", "image": _img("archer-queen")},
    {"name": "Grand Warden", "category": "Heroes", "housing": "—", "cost": "—", "resource": "Elixir", "detail": "Support hero with Life Aura / Eternal Tome modes.", "image": _img("grand-warden")},
    {"name": "Royal Champion", "category": "Heroes", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Throws spear; Seeking Shield jumps to priority defenses.", "image": _img("royal-champion")},
    # —— Hero Pets ——
    {"name": "L.A.S.S.I", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Fast pet that chases and pins targets for the hero.", "image": _img("lassi")},
    {"name": "Electro Owl", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Calls lightning strikes on a periodic charge.", "image": _img("electro-owl")},
    {"name": "Mighty Yak", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Charges walls for bonus structure damage.", "image": _img("mighty-yak")},
    {"name": "Unicorn", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Heals the paired hero during combat.", "image": _img("unicorn")},
    {"name": "Frosty", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Pet polar bear that slows enemies with frost.", "image": _img("frosty")},
    {"name": "Poison Lizard", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Applies poison stacks that ramp damage over time.", "image": _img("poison-lizard")},
    {"name": "Diggy", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Burrows and stuns targets when emerging.", "image": _img("diggy")},
    {"name": "Phoenix", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Leaves a revival flame when the hero would fall.", "image": _img("phoenix")},
    {"name": "Spirit Fox", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Grants brief invisibility windows to the hero.", "image": _img("spirit-fox")},
    {"name": "Angry Jelly", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Spawns angry jellies that distract and chip damage.", "image": _img("angry-jelly")},
    # —— Builder Base troops (extra roster) ——
    {"name": "Raged Barbarian", "category": "Builder Base Troops", "housing": 4, "cost": 600, "resource": "BH", "detail": "Builder Barracks melee that rages when ability is used.", "image": _img("raged-barbarian")},
    {"name": "Sneaky Archer", "category": "Builder Base Troops", "housing": 5, "cost": 900, "resource": "BH", "detail": "Archer with temporary invisibility cloak.", "image": _img("sneaky-archer")},
    {"name": "Beta Minion", "category": "Builder Base Troops", "housing": 4, "cost": 600, "resource": "BH", "detail": "Flying unit with extra-long shot while ability is active.", "image": _img("beta-minion")},
    {"name": "Boxer Giant", "category": "Builder Base Troops", "housing": 12, "cost": 2_500, "resource": "BH", "detail": "Knockback punches vs defenses while tanking.", "image": _img("boxer-giant")},
    {"name": "Bomber", "category": "Builder Base Troops", "housing": 5, "cost": 1_500, "resource": "BH", "detail": "Throws bombs along grouped walls.", "image": _img("bomber")},
    {"name": "Cannon Cart", "category": "Builder Base Troops", "housing": 8, "cost": 6_000, "resource": "BH", "detail": "Becomes a stationary turret if the cart is destroyed.", "image": _img("cannon-cart")},
    {"name": "Baby Dragon (BH)", "category": "Builder Base Troops", "housing": 10, "cost": 6_000, "resource": "BH", "detail": "Builder version with tantrum tied to ability timing.", "image": _img("baby-dragon")},
    {"name": "Hog Glider", "category": "Builder Base Troops", "housing": 12, "cost": 7_000, "resource": "BH", "detail": "Glides to stun a defense on landing.", "image": _img("hog-glider")},
    {"name": "Electrofire Wizard", "category": "Builder Base Troops", "housing": 16, "cost": 12_000, "resource": "BH", "detail": "Alternates lightning and fire bolts for mixed damage.", "image": _img("electrofire-wizard")},
    {"name": "Power P.E.K.K.A", "category": "Builder Base Troops", "housing": 28, "cost": 31_000, "resource": "BH", "detail": "Heavy electric swings; overload pulse when charged.", "image": _img("power-pekka")},
    {"name": "Battle Copter", "category": "Builder Base Troops", "housing": 20, "cost": 25_000, "resource": "BH", "detail": "Flying hero-style unit for Builder Base attacks.", "image": _img("battle-copter")},
    {"name": "Battle Machine", "category": "Builder Base Troops", "housing": "—", "cost": "—", "resource": "BH", "detail": "Builder Base hero; hammer slam ability.", "image": _img("battle-machine")},
]

_CATEGORY_ORDER = [
    "Elixir Troops",
    "Dark Elixir Troops",
    "Super Troops",
    "Siege Machines",
    "Heroes",
    "Hero Pets",
    "Builder Base Troops",
]


def home(request):
    grouped = OrderedDict((c, []) for c in _CATEGORY_ORDER)
    for u in _UNITS:
        cat = u["category"]
        grouped.setdefault(cat, []).append(u)
    return render(
        request,
        "index.html",
        {
            "grouped_units": grouped,
            "unit_count": len(_UNITS),
        },
    )
