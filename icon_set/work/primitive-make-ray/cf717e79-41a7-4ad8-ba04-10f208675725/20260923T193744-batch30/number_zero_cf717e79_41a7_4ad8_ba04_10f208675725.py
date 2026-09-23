"""An outlined oval numeral zero.

Symbol plan: Single vertical ellipse on the shared center (24,24), radii 14 and 20. VRECT_M ink extremes (8,2)-(40,46).
Construction: No useful Lucide numeral match found; a coherent two-arc oval preserves the reference.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'cf717e79-41a7-4ad8-ba04-10f208675725'
SOURCE_PATH = 'icon_set/work/todo-references/number zero_cf717e79-41a7-4ad8-ba04-10f208675725.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'number-zero'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('number', 'zero')

    def build(self):
        self.circle('zero',24,24,14,20)

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-upper', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-lower', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-upper', name+'-lower', closed=True)

    def box(self, name, x, y, right, bottom, r=4):
        # A single radius owns all four tangent corners.
        pts=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),
             (right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i in range(8):
            n=f'{name}-{i}'; a=pts[i]; b=pts[(i+1)%8]
            if a == b:
                continue
            if i%2:
                self.add_arc(n,a,b,radius_x=r)
            else:
                self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def clipboard(self):
        # Clip capsule and open board share the two lateral attachment nodes.
        self.box('clip',16,4,32,12,4)
        self.add_line('board-top-right',(32,8),(36,8))
        self.add_arc('board-tr',(36,8),(40,12),radius_x=4)
        self.add_line('board-right',(40,12),(40,40))
        self.add_arc('board-br',(40,40),(36,44),radius_x=4)
        self.add_line('board-bottom',(36,44),(12,44))
        self.add_arc('board-bl',(12,44),(8,40),radius_x=4)
        self.add_line('board-left',(8,40),(8,12))
        self.add_arc('board-tl',(8,12),(12,8),radius_x=4)
        self.add_line('board-top-left',(12,8),(16,8))
        self.add_contour('board','board-top-right','board-tr','board-right','board-br','board-bottom','board-bl','board-left','board-tl','board-top-left')
        self.relate('connect','board','clip')

