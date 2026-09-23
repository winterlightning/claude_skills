"""A head profile containing two checked items and one empty box.

Symbol plan: One head silhouette containing a three-row checklist. VRECT_L ink extremes (6,2)-(42,46).
Construction: No useful exact Lucide match found; supplied profile silhouette owns composition.
Human construction: Human-reference.md inspected; this is a continuous head-and-neck profile, so detached-head gap does not apply.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9bf327e4-22cd-4f46-a740-34545d603a6f'
SOURCE_PATH = 'icon_set/work/todo-references/ocd disorder symptoms 2_9bf327e4-22cd-4f46-a740-34545d603a6f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ocd-disorder-symptoms-2'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('ocd', 'disorder', 'symptoms', '2')

    def build(self):
        self.add_bezier('skull',(14,19),((14,9),(20,4),(28,4)),((36,4),(40,10),(40,19)),((40,28),(36,30),(36,35)))
        self.add_line('neck-1',(36,35),(36,44))
        self.add_line('neck-2',(36,44),(22,44))
        self.add_line('neck-3',(22,44),(22,36))
        self.add_line('neck-4',(22,36),(16,36))
        self.add_arc('chin',(16,36),(12,32),radius_x=4)
        self.add_line('nose-1',(12,32),(12,28))
        self.add_line('nose-2',(12,28),(8,27))
        self.add_line('nose-3',(8,27),(14,19))
        self.add_contour('head','skull','neck-1','neck-2','neck-3','neck-4','chin','nose-1','nose-2','nose-3',closed=True)
        for i,y in enumerate((14,23)):
            self.add_polyline(f'check-{i}',(19,y),(21,y+2),(24,y-2))
            self.add_line(f'text-{i}',(31,y),(33,y))
        self.add_polyline('empty-box',(20,30),(24,30),(24,34),(20,34),closed=True)
        self.add_line('text-2',(31,32),(33,32))

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

