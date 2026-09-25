"""Takeaway Beverage Cup with Straw.

Plan: Tapered takeaway cup with broad rounded lid, curved straw and liquid wave. Bounds (8,4)-(40,44). Lid merged with upper rim for a clean band.
Construction reference: Lucide cup-soda: bent straw and tapered cup.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '892d89a4-ba9b-57e4-87bd-0842d5f8a25d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee straw_892d89a4-ba9b-57e4-87bd-0842d5f8a25d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'lidded-takeaway-drink-with-curved-straw'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('takeaway', 'beverage', 'cup', 'with', 'straw')

    def build(self):
        box(self,'lid',8,12,40,20,4,xs=(12,24,36))
        path(self,'body',(12,20),('L',(12,31)),('L',(13,40)),('A',4,4,False,(17,44)),('L',(31,44)),('A',4,4,False,(35,40)),('L',(36,31)),('L',(36,20)))
        path(self,'straw',(24,12),('A',8,8,True,(32,4)),('L',(36,4)))
        path(self,'liquid',(12,31),('A',6,3,True,(24,31)),('A',6,3,False,(36,31)))
        contacts(self)
