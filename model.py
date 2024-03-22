super_quant_mech_king_great_magnus = """If this card is sent to the GY: You can Special Summon 3 "Super Quantal Mech Beast" Xyz Monsters with different names form your GY. 
This card gains these effects, based on the number of matrials with different names attached to it. ● 2+: Once per turn, during the Main Phase (Quick Effect): You can detach 
1 material from this card; shuffle 1 card on the field into the Deck. ● 4+: It is unaffected by card effects, except "Super Quant" cards. ● 6+: Your opponent cannot add cards 
from the Deck to the hand by card effects."""

the_arrival_cyberse_at_ignister = """You can only control 1 "The Arrival Cyberse @Ignister". The original ATK of this card becomes 1000 x the number of Link Materials used 
for its Link Summon. Unaffected by other cards' effects. Once perturn: You can target 1 other monster on the field; destroy it, and if you do, Special Summon 1 "@Ignister 
Token" (Cyberse/DARK/Level 1/ATK 0/ DEF 0) to your zone this card points to."""

koaki_meiru_maximus = """This card cannot be Normal Summoned or Set. This card can only be Special Summoned by removing from play 1 "Iron Core of Koa'ki Meiru" from your 
hand. During each of your End Phases, destroy this card unless you send 1 "Iron Core of Koa'ki Meiru" or 1 "Koa'ki Meiru" monster from your hand to the Graveyard. Once per turn, 
during your Main Phase, you can select and destroy 1 card your opponent controls."""

miscellaneousaurus = """During either player's Main Phase: You can send this card from your hand to the Graveyard; during this Main Phase, Dinosaur-Type mosnters you control are 
unaffected by your opponent's activated effects. You can banish any number of Dinosaur-Type monsters from your Graveyard, including this card; Special Summon 1 Dinosaur-Type monster 
from your Deck with a Level equal to the total number of monsters banished to activate this effect, but destroy it during the End Phase. You can only use this effect of 
"Miscellaneousaurus" once per turn."""

catapult_turtle = """Once per turn: You can Tribute 1 monster; inflict damage to your opponent equal to half the Tributed monster's ATK on the field."""

#first resource
ps_console_generation = {
    1 : {
        'id' : 1,
        'name' : 'PlayStation',
        'price' : 399,
        'global_release_date' : 1995
    },
    2 : {
        'id' : 2,
        'name' : 'PlayStation 2',
        'price' : 299,
        'global_release_date' : 2000
    },
    3 : {
        'id' : 3,
        'name' : 'PlayStation 3',
        'price' : 499,
        'global_release_date' : 2006
    },
    4 : {
        'id' : 4,
        'name' : 'PlayStation 4',
        'price' : 400,
        'global_release_date' : 2013
    },
    5 : {
        'id' : 5,
        'name' : 'PlayStation 5',
        'price' : 500,
        'global_release_date' : 2020
    }
}

#second resource
fav_ygo_cards = {
    1: {
        'id' : 1,
        'name' : 'Super Quantal Mech King Great Magnus',
        'attribute': 'LIGHT',
        'level/rank/link rating' : 12,
        'type' : 'Machine',
        'card_type' : 'Xyz/Effect',
        'summon requirement' : '3 Level 12 monsters',
        'ATK' : 3600,
        'DEF' : 3200,
        'effect' : super_quant_mech_king_great_magnus
    },
    2: {
        'id' : 2,
        'name': 'The Arrival Cyberse @Ignister',
        'attribute' : 'DARK',
        'level/rank/link rating': 6,
        'type' : 'Cyberse',
        'card_type' : 'Link/Effect',
        'summon requirement' : '3+ monsters with different attributes',
        'ATK' : 0,
        'effect' : the_arrival_cyberse_at_ignister
    },
    3: {
        'id' : 3,
        'name' : 'Koa\'ki Meiru Maximus',
        'attribute' : 'WIND',
        'level/rank/link rating': 8,
        'type' : 'Dragon',
        'card_type' : 'Effect',
        'ATK' : 3000,
        'DEF' : 2500,
        'effect' : koaki_meiru_maximus
    },
    4: {
        'id' : 4,
        'name' : 'Miscellaneousaurus',
        'attribute' : 'FIRE',
        'level/rank/link rating' : 4,
        'type' : 'Dinosaur',
        'card_type' : 'Effect',
        'ATK' : 1800,
        'DEF' : 1000,
        'effect' : miscellaneousaurus
    },
    5: {
        'id' : 5,
        'name' : 'Catapult Turtle',
        'attribute' : 'WATER',
        'level/rank/link rating' : 5,
        'type' : 'Aqua',
        'card_type' : 'Effect',
        'ATK' : 1000,
        'DEF' : 2000,
        'effect' : catapult_turtle
    }
}

