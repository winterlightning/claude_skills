"""Handheld Bottle Opener.

Plan: Broad opener head and flared separate grip, with rounded trapezoid aperture. Bounds (8,4)-(40,44); enlarged head protects aperture clearance.
Construction reference: No useful local opener match; shared-axis head and grip.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7bb85302-0b29-5cf0-a28b-f3dad5fd7fa7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/beer opener_7bb85302-0b29-5cf0-a28b-f3dad5fd7fa7.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'bottle-opener-with-rounded-trapezoid-opening'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('handheld', 'bottle', 'opener')

    def build(self):
        path(self,'outline',(24,4),('A',16,12,True,(40,16)),('L',(40,24)),('L',(30,32)),('L',(32,38)),('A',8,6,True,(16,38)),('L',(18,32)),('L',(8,24)),('L',(8,16)),('A',16,12,True,(24,4)),closed=True)
        poly(self,'aperture',(19,14),(29,14),(28,22),(20,22),(19,14))
        line(self,'grip-seam',(18,32),(30,32))
        contacts(self)
