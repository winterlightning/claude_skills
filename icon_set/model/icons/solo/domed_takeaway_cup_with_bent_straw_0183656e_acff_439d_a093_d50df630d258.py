"""Disposable Drink Cup with Straw.

Plan: Domed takeaway cup and bent straw, bounds (8,4)-(40,44). Secondary base mark omitted to preserve straw clearance.
Construction reference: Lucide cup-soda: tapered cup, projecting rim and bent straw.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '0183656e-acff-439d-a093-d50df630d258'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/bubble tea 1_0183656e-acff-439d-a093-d50df630d258.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'domed-takeaway-cup-with-bent-straw'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('disposable', 'drink', 'cup', 'with', 'straw')

    def build(self):
        path(self,'cup',(10,24),('L',(14,40)),('A',4,4,False,(18,44)),('L',(30,44)),('A',4,4,False,(34,40)),('L',(38,24)))
        poly(self,'rim',(8,24),(10,24),(24,24),(38,24),(40,24))
        path(self,'dome',(10,24),('A',14,12,True,(24,12)),('A',14,12,True,(38,24)))
        poly(self,'straw',(24,32),(24,24),(24,12),(26,4),(38,4))
        contacts(self)
