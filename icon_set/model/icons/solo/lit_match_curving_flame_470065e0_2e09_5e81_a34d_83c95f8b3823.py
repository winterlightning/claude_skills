"""Matchstick With Burning Flame."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '470065e0-2e09-5e81-a34d-83c95f8b3823'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/match fire_470065e0-2e09-5e81-a34d-83c95f8b3823.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lit-match-curving-flame'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/fire'
    aliases = ()
    keywords = ('match', 'matchstick', 'flame', 'fire', 'burning', 'light', 'wood')

    def build(self):
        # Plan: Diagonal matchstick enters the open bottom of a curling flame. Head reduced to a rounded endpoint. Lucide flame bowl; diagonal direction deliberately preserved. Bounds (8,4)-(40,44).
        self.add_bezier('fire',(8,27),((8,25),(8,24),(8,22)),((8,13),(17,7),(26,4)),((23,11),(24,17),(30,19)),((33,21),(35,20),(35,17)),((38,22),(40,25),(40,29)),((40,35),(38,37),(35,39)))
        self.add_line('match',(10,44),(26,28))
