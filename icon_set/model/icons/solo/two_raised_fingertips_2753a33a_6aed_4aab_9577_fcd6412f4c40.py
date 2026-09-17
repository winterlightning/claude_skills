"""Two Raised Fingertips — batch 52."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2753a33a-6aed-4aab-9577-fcd6412f4c40'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/gesture tap two fingers_2753a33a-6aed-4aab-9577-fcd6412f4c40.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-raised-fingertips'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('two', 'raised', 'fingertips')

    def build(self):
        # Plan: two equal arch-topped fingers sharing a central open stem.
        # HRECT_L extremes4,8,44,40. Lucide pointer: tangent rounded fingertips.
        # Nail arcs dropped: two separate interior marks cannot retain MIC here.
        for n,x in [('left',4),('right',24)]:
            self.add_arc(n+'-cap',(x,18),(x+20,18),radius_x=10)
        self.add_line('left-wall',(4,40),(4,18))
        self.add_line('right-wall',(44,18),(44,40))
        self.add_contour('outline','left-wall','left-cap','right-cap','right-wall')
        self.add_line('middle',(24,18),(24,40));self.relate('connect','middle','outline')


    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)

