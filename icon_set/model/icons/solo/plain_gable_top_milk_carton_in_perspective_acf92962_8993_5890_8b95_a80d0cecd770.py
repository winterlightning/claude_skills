"""Milk Carton Container.

Plan: Plain perspective milk carton with raised ridge and gable folds. Bounds (8,4)-(40,44); common roof/spine nodes preserve perspective.
Construction reference: Lucide package: coherent perspective seams and shared corners.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'acf92962-8993-5890-8b95-a80d0cecd770'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/milk carton_acf92962-8993-5890-8b95-a80d0cecd770.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'plain-gable-top-milk-carton-in-perspective'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('milk', 'carton', 'container')

    def build(self):
        poly(self,'outline',(8,22),(16,12),(16,4),(32,4),(32,12),(40,22),(40,40),(24,44),(8,40),(8,22))
        poly(self,'roof',(16,12),(24,22),(40,22))
        line(self,'ridge',(16,12),(32,12))
        line(self,'spine',(24,22),(24,44))
        contacts(self)
