"""Wrapped Sweet Candy.
Plan: Diagonal wrapped candy is one joined outline; two diagonal seams separate its round center from flared ends. Extrema (6,6)-(42,42).
Reference: Lucide candy: diagonal sweet with two flared wrapper ends.
Reduction: Fine wrapper folds reduced to broad flares.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1a6a3aa-6305-5a69-985b-650ac03c4792'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/halloween candy_e1a6a3aa-6305-5a69-985b-650ac03c4792.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'oval-twist-wrapped-candy'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('wrapped', 'sweet', 'candy')

    def build(self):

        self.add_arc('center-upper',(14,24),(24,14),radius_x=10)
        self.add_polyline('wrap-upper',(24,14),(30,6),(42,6),(42,18),(34,24))
        self.add_arc('center-lower',(34,24),(24,34),radius_x=10)
        self.add_polyline('wrap-lower',(24,34),(18,42),(6,42),(6,30),(14,24))
        for a,b in (('center-upper','wrap-upper'),('wrap-upper','center-lower'),('center-lower','wrap-lower'),('wrap-lower','center-upper')):self.relate('connect',a,b)
        self.add_line('seam-upper',(24,14),(34,24))
        self.add_line('seam-lower',(14,24),(24,34))
        for a,b in (('seam-upper','center-upper'),('seam-upper','wrap-upper'),('seam-upper','center-lower'),('seam-lower','center-upper'),('seam-lower','wrap-lower'),('seam-lower','center-lower')):self.relate('connect',a,b)
