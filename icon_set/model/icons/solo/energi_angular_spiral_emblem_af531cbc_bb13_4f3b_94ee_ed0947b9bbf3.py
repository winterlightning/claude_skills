"""Energi Cryptocurrency Symbol.
Plan: A continuous tilted angular spiral winds inward. Extrema (6,6)-(42,42).
Reference: Supplied original; no useful exact local Lucide match. Shared axes and simple geometric construction.
Reduction: Rounded corners handled by round joins; one continuous centerline preserves the angular spiral.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af531cbc-bb13-4f3b-94ee-ed0947b9bbf3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/virtual coin crypto energi_af531cbc-bb13-4f3b-94ee-ed0947b9bbf3.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'energi-angular-spiral-emblem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/finance"
    aliases = ()
    keywords = ('energi', 'cryptocurrency', 'symbol')

    def build(self):

        self.add_polyline('spiral',(42,24),(24,42),(6,24),(24,6),(36,18),(24,30),(18,24),(26,16))
