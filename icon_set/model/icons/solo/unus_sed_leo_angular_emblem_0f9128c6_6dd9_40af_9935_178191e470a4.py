"""Unus Sed Leo Cryptocurrency Logo."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f9128c6-6dd9-40af-9935-178191e470a4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/virtual coin crypto unus sed leo_0f9128c6-6dd9-40af-9935-178191e470a4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'unus-sed-leo-angular-emblem'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('unus sed leo', 'cryptocurrency', 'logo', 'emblem', 'angular', 'hexagon', 'finance')

    def build(self):
        # Plan: Three open angular ribbons wind around a central void. Shared step gives broad gaps. Preserve rotational motion; no exact Lucide match. Bounds (6,6)-(42,42).
        self.add_polyline('upper',(24,6),(34,13),(34,25),(22,25))
        self.add_polyline('left',(22,16),(16,10),(6,16),(6,28))
        self.add_polyline('lower',(14,24),(14,36),(24,42),(42,32),(42,20))
