"""Bunch of Redcurrant Berries."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3140c51b-4429-435b-b406-02a14b04e361'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/redcurrant_3140c51b-4429-435b-b406-02a14b04e361.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'redcurrant-branch'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('redcurrant', 'currant', 'berry', 'branch', 'fruit', 'produce', 'food')

    def build(self):
        # Plan: Four berries alternating along diagonal branch. Lucide grape round fruit construction. Shared attachment cardinal nodes. Envelope (6,6)-(42,42).
        centers=((38,14),(10,24),(18,38),(38,38))
        for i,(x,y) in enumerate(centers):
         pts=((x-4,y),(x,y-4),(x+4,y),(x,y+4),(x-4,y))
         for j in range(4):self.add_arc(f'berry-{i}-{j}',pts[j],pts[j+1],radius_x=4)
         self.add_contour(f'berry-{i}',*[f'berry-{i}-{j}' for j in range(4)],closed=True)
        self.add_polyline('branch',(14,6),(20,16),(28,26))
        for i,(start,end) in enumerate((((20,16),(34,14)),((20,16),(14,24)),((28,26),(18,34)),((28,26),(34,38)))):
         self.add_line(f'stalk-{i}',start,end);self.relate('connect',f'stalk-{i}','branch');self.relate('connect',f'stalk-{i}',f'berry-{i}')
        self.relate('connect','stalk-0','stalk-1')
