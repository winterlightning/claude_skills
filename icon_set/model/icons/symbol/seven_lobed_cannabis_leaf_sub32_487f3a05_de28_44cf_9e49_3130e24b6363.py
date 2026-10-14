"""Independent 32px profile of seven-lobed-cannabis-leaf.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '487f3a05-de28-44cf-9e49-3130e24b6363'
SOURCE_PATH = 'pictographic-primitives/cannabis/cannabis_487f3a05-de28-44cf-9e49-3130e24b6363.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('487f3a05-de28-44cf-9e49-3130e24b6363', 'pictographic-primitives/cannabis/cannabis_487f3a05-de28-44cf-9e49-3130e24b6363.svg'), ('8a80ee4f-5c0f-47e3-8f69-d4a34318a6b1', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/cannabis/cannabis_8a80ee4f-5c0f-47e3-8f69-d4a34318a6b1.svg'))
PROFILE_SOURCE_KEYS = ('solo/seven-lobed-cannabis-leaf',)
SOLO_SOURCE_ICON_IDS = ('seven-lobed-cannabis-leaf',)
REFERENCE_EXPORT_SHA256 = 'c0ab8426035055cba698a29a2eb98b6141b6d9b6ff7640a3d0db352b7737ce7b'

class Drawing(Sub32):
    icon_id = 'seven-lobed-cannabis-leaf-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'cannabis'
    categories = ('primitives', 'cannabis')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Leaf as leaflet strokes fanning from one base, with a stem.
        self.add_line('leaflet-0', (16, 22), (2, 20))
        self.add_line('leaflet-1', (16, 22), (3, 10))
        self.add_line('leaflet-2', (16, 22), (8, 3))
        self.add_line('leaflet-3', (16, 22), (16, 2))
        self.add_line('leaflet-4', (16, 22), (24, 3))
        self.add_line('leaflet-5', (16, 22), (29, 10))
        self.add_line('leaflet-6', (16, 22), (30, 20))
        self.add_line('stem', (16, 22), (16, 30))
        self.relate('connect', 'leaflet-0', 'leaflet-1')
        self.relate('connect', 'leaflet-0', 'leaflet-2')
        self.relate('connect', 'leaflet-0', 'leaflet-3')
        self.relate('connect', 'leaflet-0', 'leaflet-4')
        self.relate('connect', 'leaflet-0', 'leaflet-5')
        self.relate('connect', 'leaflet-0', 'leaflet-6')
        self.relate('connect', 'leaflet-0', 'stem')
        self.relate('connect', 'leaflet-1', 'leaflet-2')
        self.relate('connect', 'leaflet-1', 'leaflet-3')
        self.relate('connect', 'leaflet-1', 'leaflet-4')
        self.relate('connect', 'leaflet-1', 'leaflet-5')
        self.relate('connect', 'leaflet-1', 'leaflet-6')
        self.relate('connect', 'leaflet-1', 'stem')
        self.relate('connect', 'leaflet-2', 'leaflet-3')
        self.relate('connect', 'leaflet-2', 'leaflet-4')
        self.relate('connect', 'leaflet-2', 'leaflet-5')
        self.relate('connect', 'leaflet-2', 'leaflet-6')
        self.relate('connect', 'leaflet-2', 'stem')
        self.relate('connect', 'leaflet-3', 'leaflet-4')
        self.relate('connect', 'leaflet-3', 'leaflet-5')
        self.relate('connect', 'leaflet-3', 'leaflet-6')
        self.relate('connect', 'leaflet-3', 'stem')
        self.relate('connect', 'leaflet-4', 'leaflet-5')
        self.relate('connect', 'leaflet-4', 'leaflet-6')
        self.relate('connect', 'leaflet-4', 'stem')
        self.relate('connect', 'leaflet-5', 'leaflet-6')
        self.relate('connect', 'leaflet-5', 'stem')
        self.relate('connect', 'leaflet-6', 'stem')
