"""Vector Path with Anchor Points.

Symbol plan: Two equal diamond anchor handles on a rising diagonal. Shared diamond dimensions and edge-midpoint attachments; rounded stroke joins. No useful exact Lucide match.
Keyshape SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '759dc232-d099-4fb8-af2b-e6958589890c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/vectors line path_759dc232-d099-4fb8-af2b-e6958589890c.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'diagonal-vector-line-with-rounded-diamond-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('vector', 'path', 'with', 'anchor', 'points')

    def build(self):
        for i,(cx,cy) in enumerate([(14,34),(34,14)]):
            if i==0:pts=[(cx-8,cy),(cx,cy-8),(cx+4,cy-4),(cx+8,cy),(cx,cy+8)]
            else:pts=[(cx-8,cy),(cx,cy-8),(cx+8,cy),(cx,cy+8),(cx-4,cy+4)]
            self.add_polyline(f'anchor-{i}',*pts,closed=True)
        self.add_line('path',(18,30),(30,18))
        for i in range(2):self.relate('connect','path',f'anchor-{i}')
