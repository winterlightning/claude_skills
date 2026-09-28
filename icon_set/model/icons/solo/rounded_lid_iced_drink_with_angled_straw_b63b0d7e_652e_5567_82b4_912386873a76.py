"""Takeaway Iced Drink with Straw.

Plan: Iced drink with softly raised lid and right-bent straw, above a liquid wave. Bounds (8,4)-(40,44).
Construction reference: Lucide cup-soda: tapered cup, straw; rounded lid from source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'b63b0d7e-652e-5567-82b4-912386873a76'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee cold_b63b0d7e-652e-5567-82b4-912386873a76.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'rounded-lid-iced-drink-with-angled-straw'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('takeaway', 'iced', 'drink', 'with', 'straw')

    def build(self):
        path(self,'dome',(10,20),('L',(10,16)),('A',4,4,True,(14,12)),('L',(34,12)),('A',4,4,True,(38,16)),('L',(38,20)))
        line(self,'rim',(8,20),(40,20))
        path(self,'cup',(10,20),('L',(12,31)),('L',(13,40)),('A',4,4,False,(17,44)),('L',(31,44)),('A',4,4,False,(35,40)),('L',(36,31)),('L',(38,20)))
        poly(self,'straw',(24,12),(28,4),(36,4))
        path(self,'level',(12,31),('A',6,3,True,(24,31)),('A',6,3,False,(36,31)))
        contacts(self)
