# Repair: Replace the pinched vomit puddle zigzags with one smooth widening stream and broad bottom opening.
"""Vomiting Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '062992ad-f866-48c1-b3db-7b22afb71752'
SOURCE_PATH = 'pictographic-primitives/smileys/throw up_062992ad-f866-48c1-b3db-7b22afb71752.svg'
AUTHOR = 'gpt-6'


class VomitingFace(Solo48):
    icon_id = 'vomiting-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('vomiting', 'sick', 'nausea', 'throw up', 'face', 'emoji')

    def build(self):
        from ._symmetry_curves import path, ellipse, line, poly, contacts

        path(self,'head',(6,24),('A',18,18,True,(42,24)))
        poly(self,'eye-left',(18,17),(20,19),(18,21))
        poly(self,'eye-right',(30,17),(28,19),(30,21))
        path(self,'flow',(16,30),('L',(32,30)),('L',(32,34)),('C',(32,38),(39,39),(40,42)),('L',(8,42)),('C',(9,39),(16,38),(16,34)),('L',(16,30)),closed=True)
