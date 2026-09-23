"""A six-petal Onam floral emblem inside a circle.

Symbol plan: Mirrored six-petal flower surrounding one circular center, nested in a circle. CIRCLE ink radius22.
Construction: No useful exact Lucide match found; paired leaf curves constructed directly from supplied floral arrangement.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7d27b436-d05f-41d3-b72f-2e31759f48e2'
SOURCE_PATH = 'icon_set/work/todo-references/onam 1_7d27b436-d05f-41d3-b72f-2e31759f48e2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'onam-1'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('onam', '1')

    def build(self):
        self.circle('rim',24,24,20)
        # Six exact radius-5 nodes own both the central circle and the six petal bases.
        nodes=[(21,20),(27,20),(29,24),(27,28),(21,28),(19,24)]
        tips=[(24,8),(40,14),(40,34),(24,40),(8,34),(8,14)]
        controls=[((17,14),(31,14)),((34,14),(38,25)),((38,23),(34,36)),((31,34),(17,34)),((14,36),(10,23)),((10,25),(14,14))]
        for i,a in enumerate(nodes):
            b=nodes[(i+1)%6]
            self.add_arc(f'center-{i}',a,b,radius_x=5)
        self.add_contour('flower-center',*[f'center-{i}' for i in range(6)],closed=True)
        for i,a in enumerate(nodes):
            b=nodes[(i+1)%6]; tip=tips[i]; c1,c2=controls[i]
            self.add_bezier(f'petal-{i}',a,(c1,tip,tip),(tip,c2,b))
            self.relate('connect',f'petal-{i}','flower-center')
            if i: self.relate('connect',f'petal-{i}',f'petal-{i-1}')
        self.relate('connect','petal-0','petal-5')

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

