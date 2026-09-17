"""Dairy Milk Carton.

Plan: Perspective carton with raised ridge, two faces and a wavy left panel. Bounds (8,4)-(40,44); shared roof and spine nodes.
Construction reference: No useful carton match; Lucide glass-water informs the wave.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '114ac68f-5386-5f19-891d-c28c8ec282ff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/soft drinks milk_114ac68f-5386-5f19-891d-c28c8ec282ff.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'gable-top-milk-carton-with-wavy-side-panel'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('dairy', 'milk', 'carton')

    def build(self):
        poly(self,'outline',(8,22),(16,12),(16,4),(32,4),(32,12),(40,22),(40,40),(24,44),(8,40),(8,22))
        poly(self,'roof',(16,12),(24,22),(40,22))
        line(self,'ridge',(16,12),(32,12))
        poly(self,'spine',(24,22),(24,32),(24,44))
        path(self,'wave',(8,32),('A',4,2,True,(16,32)),('A',4,2,False,(24,32)))
        contacts(self)
