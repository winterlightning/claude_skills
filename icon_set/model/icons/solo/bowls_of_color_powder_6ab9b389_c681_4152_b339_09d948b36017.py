"""Bowls of Color Powder.

Plan: Two powder mounds in bowls; left bowl is lower. Shared width and mound curvature, raised back bowl. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ab9b389-c681-4152-b339-09d948b36017'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/holi_6ab9b389-c681-4152-b339-09d948b36017.svg'
AUTHOR = 'gpt-6'

class BowlsOfColorPowder(Solo48):
    icon_id = 'bowls-of-color-powder'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/holidays'
    aliases = ()
    keywords = ('bowls', 'of', 'color', 'powder')

    def build(self):
        for i,x,y in [(0,12,32),(1,36,24)]:
         self.add_arc(f'mound-{i}-l',(x-8,y),(x,y-16),radius_x=8,radius_y=16)
         self.add_arc(f'mound-{i}-r',(x,y-16),(x+8,y),radius_x=8,radius_y=16)
         self.add_arc(f'bowl-{i}',(x+8,y),(x-8,y),radius_x=8)
         self.add_contour(f'outline-{i}',f'mound-{i}-l',f'mound-{i}-r',f'bowl-{i}',closed=True)
         self.add_line(f'rim-{i}',(x-8,y),(x+8,y));self.relate('connect',f'outline-{i}',f'rim-{i}')
