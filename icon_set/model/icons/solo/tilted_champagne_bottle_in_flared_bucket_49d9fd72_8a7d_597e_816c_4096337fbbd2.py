"""Champagne Bottle in Ice Bucket.

Plan: Tilted bottle rising from flared bucket, a natural physical group; bounds (6,6)-(42,42). Secondary lip seams omitted.
Construction reference: Lucide bottle-wine: narrow neck widening into shoulder; natural diagonal retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '49d9fd72-8a7d-597e-816c-4096337fbbd2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/champagne cooler_49d9fd72-8a7d-597e-816c-4096337fbbd2.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'tilted-champagne-bottle-in-flared-bucket'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'drinks'
    aliases = ()
    keywords = ('champagne', 'bottle', 'in', 'ice', 'bucket')

    def build(self):
        poly(self,'bucket',(6,22),(12,42),(36,42),(42,22),(32,22),(16,22),(6,22))
        path(self,'bottle',(16,22),('A',18,18,True,(27,12)),('L',(33,6)),('L',(41,12)),('L',(35,18)),('L',(32,22)))
        contacts(self)
