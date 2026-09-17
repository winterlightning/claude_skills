"""Steel Beer Keg.

Plan: Cylindrical keg with curved bands and central recessed top grip. Bounds (8,4)-(40,44). Tiny additional slot removed; recess remains the top identity feature.
Construction reference: Lucide database: elliptical rim and repeated curved tiers.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'dd6e18a8-d986-5d49-85ee-38132f81ed02'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/food processing beer fermantation keg steel_dd6e18a8-d986-5d49-85ee-38132f81ed02.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'cylindrical-beer-keg-with-top-grip-recess'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('steel', 'beer', 'keg')

    def build(self):
        path(self,'body',(8,10),('A',16,6,True,(24,4)),('A',16,6,True,(40,10)),('L',(40,38)),('A',16,6,True,(24,44)),('A',16,6,True,(8,38)),('L',(8,10)),closed=True)
        path(self,'top-recess',(8,10),('L',(16,10)),('L',(16,16)),('L',(32,16)),('L',(32,10)),('L',(40,10)))
        path(self,'band',(8,28),('A',16,5,False,(24,33)),('A',16,5,False,(40,28)))
        contacts(self)
