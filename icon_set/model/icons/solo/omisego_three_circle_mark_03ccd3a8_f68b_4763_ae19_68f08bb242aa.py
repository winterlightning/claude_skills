"""OmiseGO Cryptocurrency Symbol.
Plan: Three equal circles at upper-left, upper-right and lower-left. Extrema (6,6)-(42,42).
Reference: Supplied original; no useful exact local Lucide match. Shared axes and simple geometric construction.
Reduction: No details removed; equal radius7 circles and eight-unit separations preserve the mark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03ccd3a8-f68b-4763-ae19-68f08bb242aa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/virtual coin crypto omisego_03ccd3a8-f68b-4763-ae19-68f08bb242aa.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'omisego-three-circle-mark'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/finance"
    aliases = ()
    keywords = ('omisego', 'cryptocurrency', 'symbol')

    def build(self):

        self.add_arc('upper-left-a',(13,6),(13,20),radius_x=7)
        self.add_arc('upper-left-b',(13,20),(13,6),radius_x=7)
        self.add_contour('upper-left','upper-left-a','upper-left-b',closed=True)

        self.add_arc('upper-right-a',(35,6),(35,20),radius_x=7)
        self.add_arc('upper-right-b',(35,20),(35,6),radius_x=7)
        self.add_contour('upper-right','upper-right-a','upper-right-b',closed=True)

        self.add_arc('lower-left-a',(13,28),(13,42),radius_x=7)
        self.add_arc('lower-left-b',(13,42),(13,28),radius_x=7)
        self.add_contour('lower-left','lower-left-a','lower-left-b',closed=True)
