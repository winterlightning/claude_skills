"""A circle divided by a diagonal exclusion cross.

Symbol plan: Four arcs share exact integer 3:4:5 circle points with four spokes. CIRCLE ink radius22.
Construction: No useful exact Lucide match inspected; coherent circle arcs and shared cross junctions.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b4787f31-7286-435f-a9e4-6114f60b64e5'
SOURCE_PATH = 'icon_set/work/todo-references/object exclude_b4787f31-7286-435f-a9e4-6114f60b64e5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'object-exclude'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('object', 'exclude')

    def build(self):
        points=[(12,8),(36,8),(36,40),(12,40)]
        for i,p in enumerate(points):
            self.add_arc(f'rim-{i}',p,points[(i+1)%4],radius_x=20)
        self.add_contour('rim',*[f'rim-{i}' for i in range(4)],closed=True)
        for i,p in enumerate(points):
            self.add_line(f'spoke-{i}',p,(24,24))
            self.relate('connect',f'spoke-{i}','rim')
            for j in range(i):
                self.relate('connect',f'spoke-{i}',f'spoke-{j}')

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

