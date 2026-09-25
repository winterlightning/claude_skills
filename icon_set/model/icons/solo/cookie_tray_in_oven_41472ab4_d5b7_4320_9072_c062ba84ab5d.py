"""Baking Tray with Fresh Cookies."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41472ab4-d5b7-4320-9072-c062ba84ab5d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/cooking baking tray oven_41472ab4-d5b7-4320-9072-c062ba84ab5d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cookie-tray-in-oven'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('baking', 'oven', 'cookie', 'tray', 'kitchen', 'heat', 'food')

    def build(self):
        # Plan: Open oven casing above a shallow tray, with two round cookies reduced from four. Shared oven/tray corners. No exact local Lucide tray match. Bounds (6,6)-(42,42).
        # Perspective tray stays separate from the two upper oven brackets.
        self.add_polyline('oven-left',(6,14),(6,6),(10,6))
        self.add_polyline('oven-right',(38,6),(42,6),(42,14))
        for side in (-1,1):
            x=24+side*5
            self.add_bezier(f'heat-{side}',(x,6),((x+side*2,8),(x-side*2,11),(x,13)))
        self.add_polyline('tray',(14,22),(34,22),(42,42),(6,42),closed=True)
        for i,x in enumerate((19,29)):
            self.add_dot(f'cookie-{i}',(x,32))
