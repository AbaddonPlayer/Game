
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 64

BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'SPRITES/Pixeltype.ttf'
UI_FONT_SIZE = 18

WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':'../graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'../graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'../graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'../graphics/weapons/sai/full.png'}}

monster_data = {
    'red slime': {'health':40, 'exp':20, 'damage':20, 'attack_type':'slash'},
    'purple slime': {'health':40, 'exp':20, 'damage':20, 'attack_type':'slash'},
    'orange slime': {'health':40, 'exp':20, 'damage':20, 'attack_type':'slash'},
    'blue slime': {'health':40, 'exp':20, 'damage':20, 'attack_type':'slash'}
}