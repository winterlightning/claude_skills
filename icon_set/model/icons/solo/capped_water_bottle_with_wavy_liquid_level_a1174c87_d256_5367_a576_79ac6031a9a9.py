"""Water Bottle with Liquid.

Plan: Capped water bottle with rounded shoulders and a wavy liquid level. Bounds (10,4)-(38,44). Tiny cap break removed to keep closure clear.
Construction reference: Lucide bottle-wine and milk: neck, mirrored shoulders and rounded base.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a1174c87-d256-5367-a576-79ac6031a9a9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/water bottle glass_a1174c87-d256-5367-a576-79ac6031a9a9.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'capped-water-bottle-with-wavy-liquid-level'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('water', 'bottle', 'with', 'liquid')

    def build(self):
        path(self,'body',(18,12),('L',(18,4)),('L',(30,4)),('L',(30,12)),('A',8,8,False,(38,20)),('L',(38,38)),('A',6,6,True,(32,44)),('L',(16,44)),('A',6,6,True,(10,38)),('L',(10,20)),('A',8,8,False,(18,12)),closed=True)
        line(self,'cap',(18,12),(30,12))
        path(self,'water',(10,31),('A',7,2,True,(24,31)),('A',7,2,False,(38,31)))
        contacts(self)
