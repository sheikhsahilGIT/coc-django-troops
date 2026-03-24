from collections import OrderedDict

from django.shortcuts import render

# Statscell game icons via jsDelivr (reliable). The old coc.guide /troop-slug.png URLs return 404.
_SC_BASE = "https://cdn.jsdelivr.net/gh/Statscell/clash-assets@main/troops/icons/"


def sc(filename: str) -> str:
    return _SC_BASE + filename


# Troops / pets not in the Statscell icon pack — wiki thumbnails (same art style as in-game portraits).
_WIKI_IMG = {
    "Apprentice Warden": "https://static.wikia.nocookie.net/clashofclans/images/8/8b/Avatar_Apprentice_Warden.png/revision/latest?cb=20230613002759",
    "Root Rider": "https://static.wikia.nocookie.net/clashofclans/images/0/0b/Avatar_Root_Rider.png/revision/latest?cb=20231213214829",
    "Druid": "https://static.wikia.nocookie.net/clashofclans/images/9/9a/Druid_info.png/revision/latest/scale-to-width-down/256?cb=20240617132723",
    "Super Miner": "https://static.wikia.nocookie.net/clashofclans/images/f/f5/Super_Miner_info_2.png/revision/latest/scale-to-width-down/256?cb=20221212121930",
    "Super Hog Rider": "https://static.wikia.nocookie.net/clashofclans/images/c/c4/Avatar_Super_Hog_Rider.png/revision/latest/scale-to-width-down/256?cb=20230613002801",
    "L.A.S.S.I": "https://static.wikia.nocookie.net/clashofclans/images/a/ae/LASSI_with_the_butterfly.png/revision/latest/scale-to-width-down/256?cb=20260217131126",
    "Electro Owl": "https://static.wikia.nocookie.net/clashofclans/images/b/bb/Electro_Owl_info_2.png/revision/latest/scale-to-width-down/256?cb=20251122011158",
    "Mighty Yak": "https://static.wikia.nocookie.net/clashofclans/images/e/e0/Mighty_Yak_info_2.png/revision/latest/scale-to-width-down/256?cb=20210821052546",
    "Unicorn": "https://static.wikia.nocookie.net/clashofclans/images/9/93/Unicorn_info_2.png/revision/latest/scale-to-width-down/256?cb=20210821050927",
    "Frosty": "https://static.wikia.nocookie.net/clashofclans/images/3/32/Frosty_info_2.png/revision/latest/scale-to-width-down/256?cb=20221012064337",
    "Poison Lizard": "https://static.wikia.nocookie.net/clashofclans/images/1/1b/Poison_Lizard_info_2.png/revision/latest/scale-to-width-down/256?cb=20221012064351",
    "Diggy": "https://static.wikia.nocookie.net/clashofclans/images/7/7e/Diggy_info_2.png/revision/latest/scale-to-width-down/256?cb=20221012064335",
    "Phoenix": "https://static.wikia.nocookie.net/clashofclans/images/4/47/Phoenix_info_2.png/revision/latest/scale-to-width-down/256?cb=20221012064346",
    "Spirit Fox": "https://static.wikia.nocookie.net/clashofclans/images/d/db/SpiritFox_Concept_Art.jpg/revision/latest/scale-to-width-down/256?cb=20260218104847",
    "Angry Jelly": "https://static.wikia.nocookie.net/clashofclans/images/3/3a/Avatar_Angry_Jelly.png/revision/latest/scale-to-width-down/256?cb=20240418095718",
    "Battle Copter": "https://static.wikia.nocookie.net/clashofclans/images/a/a8/Battle_Copter_info.png/revision/latest/scale-to-width-down/256?cb=20240103221029",
    "Electrofire Wizard": "https://static.wikia.nocookie.net/clashofclans/images/2/2e/Electrofire_Wizard_info.png/revision/latest/scale-to-width-down/256?cb=20230515202816",
}


def _icon(unit_name: str, pack_file: str) -> str:
    return _WIKI_IMG.get(unit_name, sc(pack_file))


# category -> display order (main village focus + heroes/pets/siege + extras)
_UNITS = [
    # —— Elixir troops (Home Village) ——
    {"name": "Barbarian", "category": "Elixir Troops", "housing": 1, "cost": 50, "resource": "Elixir", "detail": "Fearless melee fighter; cheap and fast to train.", "image": _icon("Barbarian", "Barbarian.png")},
    {"name": "Archer", "category": "Elixir Troops", "housing": 1, "cost": 100, "resource": "Elixir", "detail": "Ranged damage behind tanks and walls.", "image": _icon("Archer", "Archer.png")},
    {"name": "Goblin", "category": "Elixir Troops", "housing": 1, "cost": 160, "resource": "Elixir", "detail": "Fast resource hunter that targets storages and mines.", "image": _icon("Goblin", "Goblin.png")},
    {"name": "Giant", "category": "Elixir Troops", "housing": 5, "cost": 2_000, "resource": "Elixir", "detail": "Tank that heads for defenses first.", "image": _icon("Giant", "Giant.png")},
    {"name": "Wall Breaker", "category": "Elixir Troops", "housing": 2, "cost": 5_000, "resource": "Elixir", "detail": "Blasts through walls to open the base.", "image": _icon("Wall Breaker", "Wall_Breaker.png")},
    {"name": "Balloon", "category": "Elixir Troops", "housing": 5, "cost": 7_600, "resource": "Elixir", "detail": "Flying splash damage that targets defenses.", "image": _icon("Balloon", "Balloon.png")},
    {"name": "Wizard", "category": "Elixir Troops", "housing": 4, "cost": 4_000, "resource": "Elixir", "detail": "Glass cannon with strong splash damage.", "image": _icon("Wizard", "Wizard.png")},
    {"name": "Healer", "category": "Elixir Troops", "housing": 14, "cost": 12_000, "resource": "Elixir", "detail": "Air unit that heals ground troops under her.", "image": _icon("Healer", "Healer.png")},
    {"name": "Dragon", "category": "Elixir Troops", "housing": 20, "cost": 36_000, "resource": "Elixir", "detail": "Durable flying unit with splash breath.", "image": _icon("Dragon", "Dragon.png")},
    {"name": "P.E.K.K.A", "category": "Elixir Troops", "housing": 25, "cost": 46_000, "resource": "Elixir", "detail": "Slow heavy hitter with huge single-target damage.", "image": _icon("P.E.K.K.A", "P.E.K.K.A.png")},
    {"name": "Baby Dragon", "category": "Elixir Troops", "housing": 10, "cost": 15_000, "resource": "Elixir", "detail": "Flying splasher; tantrum boosts fire rate when alone.", "image": _icon("Baby Dragon", "Baby_Dragon.png")},
    {"name": "Miner", "category": "Elixir Troops", "housing": 6, "cost": 5_600, "resource": "Elixir", "detail": "Burrows underground, avoids defenses while moving.", "image": _icon("Miner", "Miner.png")},
    {"name": "Electro Dragon", "category": "Elixir Troops", "housing": 30, "cost": 42_000, "resource": "Elixir", "detail": "Chain lightning that jumps across multiple targets.", "image": _icon("Electro Dragon", "Electro_Dragon.png")},
    {"name": "Yeti", "category": "Elixir Troops", "housing": 18, "cost": 19_000, "resource": "Elixir", "detail": "Splits Yetimites on destruction; strong behind a tank line.", "image": _icon("Yeti", "Yeti.png")},
    {"name": "Dragon Rider", "category": "Elixir Troops", "housing": 25, "cost": 26_000, "resource": "Elixir", "detail": "Flying unit that drops fire bombs while circling.", "image": _icon("Dragon Rider", "Dragon_Rider.png")},
    {"name": "Electro Titan", "category": "Elixir Troops", "housing": 32, "cost": 33_000, "resource": "Elixir", "detail": "Huge tank that radiates lightning to nearby buildings.", "image": _icon("Electro Titan", "Electro_Titan.png")},
    {"name": "Apprentice Warden", "category": "Elixir Troops", "housing": 20, "cost": 20_000, "resource": "Elixir", "detail": "Support avatar of the Grand Warden with his own aura pattern.", "image": _icon("Apprentice Warden", "Avatar_Apprentice_Warden.png")},
    {"name": "Root Rider", "category": "Elixir Troops", "housing": 18, "cost": 18_000, "resource": "Elixir", "detail": "Rider on a root beast that smashes walls and defenses.", "image": _icon("Root Rider", "Avatar_Root_Rider.png")},
    # —— Dark Elixir troops ——
    {"name": "Minion", "category": "Dark Elixir Troops", "housing": 2, "cost": 6, "resource": "Dark", "detail": "Cheap fast flyer; good for cleanup.", "image": _icon("Minion", "Minion.png")},
    {"name": "Hog Rider", "category": "Dark Elixir Troops", "housing": 5, "cost": 56, "resource": "Dark", "detail": "Jumps walls and hammers defenses.", "image": _icon("Hog Rider", "Hog_Rider.png")},
    {"name": "Valkyrie", "category": "Dark Elixir Troops", "housing": 8, "cost": 70, "resource": "Dark", "detail": "Spin attack cleaves clustered buildings.", "image": _icon("Valkyrie", "Valkyrie.png")},
    {"name": "Golem", "category": "Dark Elixir Troops", "housing": 30, "cost": 205, "resource": "Dark", "detail": "Splits into Golemites; soaks huge damage.", "image": _icon("Golem", "Golem.png")},
    {"name": "Witch", "category": "Dark Elixir Troops", "housing": 12, "cost": 205, "resource": "Dark", "detail": "Spawns skeletons continuously behind the front line.", "image": _icon("Witch", "Witch.png")},
    {"name": "Lava Hound", "category": "Dark Elixir Troops", "housing": 30, "cost": 190, "resource": "Dark", "detail": "Air tank that pops into Lava Pups.", "image": _icon("Lava Hound", "Lava_Hound.png")},
    {"name": "Bowler", "category": "Dark Elixir Troops", "housing": 6, "cost": 100, "resource": "Dark", "detail": "Rolling boulder hits a line of buildings.", "image": _icon("Bowler", "Bowler.png")},
    {"name": "Ice Golem", "category": "Dark Elixir Troops", "housing": 15, "cost": 120, "resource": "Dark", "detail": "Shatters with a freeze when destroyed.", "image": _icon("Ice Golem", "Ice_Golem.png")},
    {"name": "Headhunter", "category": "Dark Elixir Troops", "housing": 6, "cost": 115, "resource": "Dark", "detail": "Bonus damage vs heroes; throws poison vials.", "image": _icon("Headhunter", "Headhunter.png")},
    {"name": "Druid", "category": "Dark Elixir Troops", "housing": 16, "cost": 200, "resource": "Dark", "detail": "Can shapeshift to bear form for extra melee pressure.", "image": _icon("Druid", "Druid.png")},
    # —— Super Troops ——
    {"name": "Super Barbarian", "category": "Super Troops", "housing": 5, "cost": 1_500, "resource": "Elixir", "detail": "Barbarian with rage boost and extra HP.", "image": _icon("Super Barbarian", "Super_Barbarian.png")},
    {"name": "Sneaky Goblin", "category": "Super Troops", "housing": 3, "cost": 3_600, "resource": "Elixir", "detail": "Invisible to defenses until it attacks.", "image": _icon("Sneaky Goblin", "Sneaky_Goblin.png")},
    {"name": "Super Giant", "category": "Super Troops", "housing": 5, "cost": 6_000, "resource": "Elixir", "detail": "Doorbuster Giant that targets walls first.", "image": _icon("Super Giant", "Super_Giant.png")},
    {"name": "Rocket Balloon", "category": "Super Troops", "housing": 8, "cost": 5_600, "resource": "Elixir", "detail": "First hit is a fast rocket charge on defenses.", "image": _icon("Rocket Balloon", "Rocket_Balloon.png")},
    {"name": "Super Wall Breaker", "category": "Super Troops", "housing": 4, "cost": 10_000, "resource": "Elixir", "detail": "Leaves a small bomb after blowing a lane.", "image": _icon("Super Wall Breaker", "Super_Wall_Breaker.png")},
    {"name": "Super Wizard", "category": "Super Troops", "housing": 10, "cost": 8_000, "resource": "Elixir", "detail": "Power beam that ramps up the longer he fires.", "image": _icon("Super Wizard", "Super_Wizard.png")},
    {"name": "Inferno Dragon", "category": "Super Troops", "housing": 15, "cost": 18_000, "resource": "Elixir", "detail": "Beam ramps to single-target inferno damage.", "image": _icon("Inferno Dragon", "Inferno_Dragon.png")},
    {"name": "Super Dragon", "category": "Super Troops", "housing": 40, "cost": 45_000, "resource": "Elixir", "detail": "Larger dragon with stronger breath.", "image": _icon("Super Dragon", "Super_Dragon.png")},
    {"name": "Super Minion", "category": "Super Troops", "housing": 12, "cost": 18, "resource": "Dark", "detail": "First shots are long-range blind spots to air defenses.", "image": _icon("Super Minion", "Super_Minion.png")},
    {"name": "Super Valkyrie", "category": "Super Troops", "housing": 20, "cost": 200, "resource": "Dark", "detail": "Spin leaves a rage trail after moving.", "image": _icon("Super Valkyrie", "Super_Valkyrie.png")},
    {"name": "Super Witch", "category": "Super Troops", "housing": 40, "cost": 360, "resource": "Dark", "detail": "Summons a Big Boy instead of many skeletons.", "image": _icon("Super Witch", "Super_Witch.png")},
    {"name": "Ice Hound", "category": "Super Troops", "housing": 40, "cost": 300, "resource": "Dark", "detail": "Frozen variant that freezes on death.", "image": _icon("Ice Hound", "Ice_Hound.png")},
    {"name": "Super Bowler", "category": "Super Troops", "housing": 30, "cost": 280, "resource": "Dark", "detail": "Boulder leaves a damaging trail.", "image": _icon("Super Bowler", "Super_Bowler.png")},
    {"name": "Super Archer", "category": "Super Troops", "housing": 12, "cost": 4_000, "resource": "Elixir", "detail": "Cross-map opening shot before entering normal range.", "image": _icon("Super Archer", "Super_Archer.png")},
    {"name": "Super Miner", "category": "Super Troops", "housing": 24, "cost": 6_000, "resource": "Elixir", "detail": "Heals briefly after surfacing from underground.", "image": _icon("Super Miner", "Super_Miner.png")},
    {"name": "Super Hog Rider", "category": "Super Troops", "housing": 12, "cost": 170, "resource": "Dark", "detail": "Faster hog with a burst heal when ability triggers.", "image": _icon("Super Hog Rider", "Avatar_Super_Hog_Rider.png")},
    # —— Siege machines ——
    {"name": "Wall Wrecker", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Plows toward Town Hall slamming through segments.", "image": _icon("Wall Wrecker", "Wall_Wrecker.png")},
    {"name": "Battle Blimp", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Flying delivery to core; drops CC troops overhead.", "image": _icon("Battle Blimp", "Battle_Blimp.png")},
    {"name": "Stone Slammer", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Air siege that splashes defenses from above.", "image": _icon("Stone Slammer", "Stone_Slammer.png")},
    {"name": "Siege Barracks", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Spawns a P.E.K.K.A and many Wizards on the map edge.", "image": _icon("Siege Barracks", "Siege_Barracks.png")},
    {"name": "Log Launcher", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Rolls logs through bases for line damage.", "image": _icon("Log Launcher", "Log_Launcher.png")},
    {"name": "Flame Flinger", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Long-range incendiary shots from the perimeter.", "image": _icon("Flame Flinger", "Flame_Flinger.png")},
    {"name": "Battle Drill", "category": "Siege Machines", "housing": 1, "cost": 100_000, "resource": "Gold", "detail": "Underground drill that erupts under key targets.", "image": _icon("Battle Drill", "Battle_Drill.png")},
    # —— Heroes ——
    {"name": "Barbarian King", "category": "Heroes", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Melee hero; Iron Fist boosts him and nearby barbarians.", "image": _icon("Barbarian King", "Barbarian_King.png")},
    {"name": "Archer Queen", "category": "Heroes", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Ranged hero; Royal Cloak grants invisibility and DPS.", "image": _icon("Archer Queen", "Archer_Queen.png")},
    {"name": "Grand Warden", "category": "Heroes", "housing": "—", "cost": "—", "resource": "Elixir", "detail": "Support hero with Life Aura / Eternal Tome modes.", "image": _icon("Grand Warden", "Grand_Warden.png")},
    {"name": "Royal Champion", "category": "Heroes", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Throws spear; Seeking Shield jumps to priority defenses.", "image": _icon("Royal Champion", "Royal_Champion.png")},
    # —— Hero Pets ——
    {"name": "L.A.S.S.I", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Fast pet that chases and pins targets for the hero.", "image": _icon("L.A.S.S.I", "LASSI.png")},
    {"name": "Electro Owl", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Calls lightning strikes on a periodic charge.", "image": _icon("Electro Owl", "Electro_Owl.png")},
    {"name": "Mighty Yak", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Charges walls for bonus structure damage.", "image": _icon("Mighty Yak", "Mighty_Yak.png")},
    {"name": "Unicorn", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Heals the paired hero during combat.", "image": _icon("Unicorn", "Unicorn.png")},
    {"name": "Frosty", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Pet polar bear that slows enemies with frost.", "image": _icon("Frosty", "Frosty.png")},
    {"name": "Poison Lizard", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Applies poison stacks that ramp damage over time.", "image": _icon("Poison Lizard", "Poison_Lizard.png")},
    {"name": "Diggy", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Burrows and stuns targets when emerging.", "image": _icon("Diggy", "Diggy.png")},
    {"name": "Phoenix", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Leaves a revival flame when the hero would fall.", "image": _icon("Phoenix", "Phoenix.png")},
    {"name": "Spirit Fox", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Grants brief invisibility windows to the hero.", "image": _icon("Spirit Fox", "Spirit_Fox.png")},
    {"name": "Angry Jelly", "category": "Hero Pets", "housing": "—", "cost": "—", "resource": "Dark", "detail": "Spawns angry jellies that distract and chip damage.", "image": _icon("Angry Jelly", "Angry_Jelly.png")},
    # —— Builder Base troops (extra roster) ——
    {"name": "Raged Barbarian", "category": "Builder Base Troops", "housing": 4, "cost": 600, "resource": "BH", "detail": "Builder Barracks melee that rages when ability is used.", "image": _icon("Raged Barbarian", "Raged_Barbarian.png")},
    {"name": "Sneaky Archer", "category": "Builder Base Troops", "housing": 5, "cost": 900, "resource": "BH", "detail": "Archer with temporary invisibility cloak.", "image": _icon("Sneaky Archer", "Sneaky_Archer.png")},
    {"name": "Beta Minion", "category": "Builder Base Troops", "housing": 4, "cost": 600, "resource": "BH", "detail": "Flying unit with extra-long shot while ability is active.", "image": _icon("Beta Minion", "Beta_Minion.png")},
    {"name": "Boxer Giant", "category": "Builder Base Troops", "housing": 12, "cost": 2_500, "resource": "BH", "detail": "Knockback punches vs defenses while tanking.", "image": _icon("Boxer Giant", "Boxer_Giant.png")},
    {"name": "Bomber", "category": "Builder Base Troops", "housing": 5, "cost": 1_500, "resource": "BH", "detail": "Throws bombs along grouped walls.", "image": _icon("Bomber", "Bomber.png")},
    {"name": "Cannon Cart", "category": "Builder Base Troops", "housing": 8, "cost": 6_000, "resource": "BH", "detail": "Becomes a stationary turret if the cart is destroyed.", "image": _icon("Cannon Cart", "Cannon_Cart.png")},
    {"name": "Baby Dragon (BH)", "category": "Builder Base Troops", "housing": 10, "cost": 6_000, "resource": "BH", "detail": "Builder version with tantrum tied to ability timing.", "image": _icon("Baby Dragon (BH)", "Baby_Dragon.png")},
    {"name": "Hog Glider", "category": "Builder Base Troops", "housing": 12, "cost": 7_000, "resource": "BH", "detail": "Glides to stun a defense on landing.", "image": _icon("Hog Glider", "Hog_Glider.png")},
    {"name": "Electrofire Wizard", "category": "Builder Base Troops", "housing": 16, "cost": 12_000, "resource": "BH", "detail": "Alternates lightning and fire bolts for mixed damage.", "image": _icon("Electrofire Wizard", "Electrofire_Wizard.png")},
    {"name": "Power P.E.K.K.A", "category": "Builder Base Troops", "housing": 28, "cost": 31_000, "resource": "BH", "detail": "Heavy electric swings; overload pulse when charged.", "image": _icon("Power P.E.K.K.A", "Super_P.E.K.K.A.png")},
    {"name": "Battle Copter", "category": "Builder Base Troops", "housing": 20, "cost": 25_000, "resource": "BH", "detail": "Flying hero-style unit for Builder Base attacks.", "image": _icon("Battle Copter", "Battle_Copter.png")},
    {"name": "Battle Machine", "category": "Builder Base Troops", "housing": "—", "cost": "—", "resource": "BH", "detail": "Builder Base hero; hammer slam ability.", "image": _icon("Battle Machine", "Battle_Machine.png")},
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
