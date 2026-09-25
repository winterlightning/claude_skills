"""Glass of Beer with Foam.

Plan: Tapered beer tumbler under a separated three-lobe foam crown. Bounds (8,4)-(40,44); shared lobe radii.
Construction reference: Lucide beer and glass-water: foam and tapered bowl.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'c5a14581-0bc1-571d-a81f-39bba4c9c07d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/cake cream_c5a14581-0bc1-571d-a81f-39bba4c9c07d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'tapered-beer-tumbler-beneath-foam-lobes'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('glass', 'of', 'beer', 'with', 'foam')

    def build(self):
        path(self,'glass',(8,23),('L',(40,23)),('L',(36,40)),('A',4,4,True,(32,44)),('L',(16,44)),('A',4,4,True,(12,40)),('L',(8,23)),closed=True)
        path(self,'foam',(8,14),('A',6,6,True,(18,10)),('A',6,6,True,(30,10)),('A',6,6,True,(40,14)))
        contacts(self)
