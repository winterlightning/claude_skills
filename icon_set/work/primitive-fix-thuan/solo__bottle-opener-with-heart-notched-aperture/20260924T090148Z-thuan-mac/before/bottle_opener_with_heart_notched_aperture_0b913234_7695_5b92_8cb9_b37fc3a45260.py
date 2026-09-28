"""Handheld Bottle Opener.

Plan: Bottle opener with broad head, notched flat-bottomed aperture, and narrow rounded handle. Bounds (8,4)-(40,44). The head is enlarged and the handle shortened to keep the notched aperture clear.
Construction reference: No useful local bottle-opener match; paired elliptical head and shared-axis aperture.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '0b913234-7695-5b92-8cb9-b37fc3a45260'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/beer opener_0b913234-7695-5b92-8cb9-b37fc3a45260.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'bottle-opener-with-heart-notched-aperture'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('handheld', 'bottle', 'opener')

    def build(self):
        path(self,'outline',(24,4),('A',16,12,True,(40,16)),('L',(40,24)),('L',(30,34)),('L',(30,38)),('A',6,6,True,(18,38)),('L',(18,34)),('L',(8,24)),('L',(8,16)),('A',16,12,True,(24,4)),closed=True)
        poly(self,'opening',(20,14),(24,16),(28,14),(28,24),(20,24),(20,14))
        contacts(self)
