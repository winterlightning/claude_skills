"""Turkish Coffee Pot and Cup.

Plan: Turkish coffee service: waisted long-handled pot and small cup. Bounds (4,8)-(44,40). Steam and cup resting line removed to keep two distinct vessels readable.
Construction reference: Lucide coffee: small cup and handle. Natural two-vessel scene retained with asymmetric scale.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '5c9a7e59-ea50-4884-8c42-b6f78345635a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee turkish_5c9a7e59-ea50-4884-8c42-b6f78345635a.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'long-handled-turkish-coffee-pot-beside-cup'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('turkish', 'coffee', 'pot', 'and', 'cup')

    def build(self):
        path(self,'pot',(4,18),('L',(20,18)),('A',4,8,False,(16,26)),('A',4,8,True,(20,34)),('L',(20,36)),('A',4,4,True,(16,40)),('L',(8,40)),('A',4,4,True,(4,36)),('L',(4,34)),('A',4,8,True,(8,26)),('A',4,8,False,(4,18)),closed=True)
        line(self,'pot-handle',(20,18),(38,8))
        path(self,'cup',(29,28),('L',(37,28)),('L',(37,36)),('A',4,4,True,(33,40)),('A',4,4,True,(29,36)),('L',(29,28)),closed=True)
        path(self,'cup-handle',(37,28),('A',7,4,True,(37,36)))
        contacts(self)
