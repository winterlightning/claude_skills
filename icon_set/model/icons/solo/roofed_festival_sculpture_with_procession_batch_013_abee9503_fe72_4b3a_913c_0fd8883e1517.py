"""Roofed Honensai sculpture over three equal procession busts. Open eaves and a central ceremonial body keep the roof opening clear; omit side projections and tiny facial/band details. Heads use radius3 at x9,24,39 / y29; shoulders top40, yielding exactly (40-(29+3))-4 = 4 ink units. Broad central sculpture and all three people retained.
Shared human user.svg: circular heads and smooth shoulders; source supplies roofed procession.
Keyshape SQUARE on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'abee9503-fe72-4b3a-913c-0fd8883e1517'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/honensai with persons_abee9503-fe72-4b3a-913c-0fd8883e1517.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/honensai with persons_abee9503-fe72-4b3a-913c-0fd8883e1517.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/honensai with persons_abee9503-fe72-4b3a-913c-0fd8883e1517.svg'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_RADIUS = 3
HEAD_CENTER_Y = 29
SHOULDER_TOP = 40
# Exact emitted nearest gap: 40 - (29 + 3) - 4 = 4 ink units.

class BatchIcon(Solo48):
    icon_id = 'roofed-festival-sculpture-with-procession-batch-013'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('roofed', 'festival', 'sculpture', 'with', 'procession')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_polyline('roof',(14,16),(19,11),(24,6),(29,11),(34,16))
        self.add_polyline('body',(19,11),(19,18),(29,18),(29,11))
        self.relate('connect','roof','body')
        for i,x in enumerate((9,24,39)):
         circle('head-'+str(i),x,29,3)
         self.add_bezier('shoulders-'+str(i),(x-3,42),((x-3,40),(x-2,40),(x,40)),((x+2,40),(x+3,40),(x+3,42)))
