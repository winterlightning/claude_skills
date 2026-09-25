"""Traditional Farm Barn.
Plan: Gambrel roof floats above shortened side walls and wide braced doors. Extrema (6,6)-(42,42).
Reference: Lucide warehouse: broad building silhouette and inset door frame.
Reduction: Loft window omitted; genuine detached eaves and braced doors retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1d94f74-e4c5-5f29-a7d8-e4607c03e4e3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/farming barn_b1d94f74-e4c5-5f29-a7d8-e4607c03e4e3.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'barn-detached-roof-eaves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    categories = ("farming", "primitives")
    aliases = ()
    keywords = ('traditional', 'farm', 'barn')

    def build(self):

        self.add_polyline('roof',(6,22),(12,12),(24,6),(36,12),(42,22))
        self.add_polyline('walls',(6,30),(6,42),(14,42),(34,42),(42,42),(42,30))
        self.add_polyline('door',(14,42),(14,26),(34,26),(34,42));self.relate('connect','door','walls')
        self.add_polyline('brace-a',(14,26),(24,34),(34,42))
        self.add_polyline('brace-b',(34,26),(24,34),(14,42))
        for n in ('brace-a','brace-b'):
            self.relate('connect',n,'door');self.relate('connect',n,'walls')
        self.relate('connect','brace-a','brace-b')
