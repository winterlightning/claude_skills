"""A rounded square frame holds a cursive lowercase in with a dotted i and a looping n.

Plan: Rounded tile contains dotted i and open n, retaining clear nine-unit gaps.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected file-text and bot: sparse details in an enclosure.
Simplification: Cursive flourish becomes clear monoline in.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6742b2e4-0a48-4b9c-a3b9-fddbfa96da87'
SOURCE_PATH = 'pictographic-primitives/logos/invision logo_6742b2e4-0a48-4b9c-a3b9-fddbfa96da87.svg'
AUTHOR = 'gpt-6'


class InvisionLogo(Solo48):
    icon_id = 'invision-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('invision', 'design', 'prototype', 'in', 'logo', 'brand', 'collaboration')

    def build(self):
        self.add_polyline('frame',(6,6),(42,6),(42,42),(6,42),closed=True)
        self.add_dot('idot',(15,15))
        self.add_line('i',(15,25),(15,33))
        self.add_line('nl',(24,25),(24,33))
        self.add_arc('na',(24,25),(32,25),radius_x=4)
        self.add_line('nr',(32,25),(32,33))
        self.add_contour('narch','na','nr')
        self.relate('connect','nl','narch')
