"""Teacup on Saucer.

Plan: Deep teacup with attached right handle seated on shallow saucer. Bounds (4,8)-(44,40); shared bottom contact and broad saucer rim.
Construction reference: Lucide coffee: rounded cup and handle; saucer from source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a7ff22d8-c5c0-5eab-abaa-0578b5a5b994'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/tea cup_a7ff22d8-c5c0-5eab-abaa-0578b5a5b994.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'deep-teacup-resting-on-shallow-saucer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('teacup', 'on', 'saucer')

    def build(self):
        path(self,'cup',(8,8),('L',(34,8)),('L',(34,18)),('A',13,14,True,(21,32)),('A',13,14,True,(8,18)),('L',(8,8)),closed=True)
        path(self,'handle',(34,8),('A',10,7,True,(34,22)))
        path(self,'saucer',(4,32),('L',(21,32)),('L',(44,32)),('A',8,8,True,(36,40)),('L',(12,40)),('A',8,8,True,(4,32)),closed=True)
        contacts(self)
