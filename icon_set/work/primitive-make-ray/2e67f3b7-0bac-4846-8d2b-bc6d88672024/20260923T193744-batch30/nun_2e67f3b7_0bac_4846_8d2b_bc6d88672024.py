"""A nun wearing a veil and a cross on her habit.

Symbol plan: Mirrored veil, circular face, smooth shoulders and cross. VRECT_L ink extremes (6,2)-(42,46).
Construction: user-round: curved shoulder vocabulary, subject governed by shared human reference.
Human construction: icon_set/references/human_ref/user.svg and human-reference.md: circular face radius6; shoulder top28 minus jaw bottom24 =4 centerline units, zero ink gap under bust construction. Veil proximity and cross crowding require validation review.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2e67f3b7-0bac-4846-8d2b-bc6d88672024'
SOURCE_PATH = 'icon_set/work/todo-references/nun_2e67f3b7-0bac-4846-8d2b-bc6d88672024.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'nun'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('nun',)
    human_construction = "bust"

    def build(self):
        # Circular veil crown and equal straight sides frame a circular face.
        self.add_line('veil-left',(8,36),(8,20))
        self.add_arc('veil-crown',(8,20),(40,20),radius_x=16)
        self.add_line('veil-right',(40,20),(40,36))
        self.add_contour('veil','veil-left','veil-crown','veil-right')
        self.circle('head',24,18,6)
        self.add_line('forehead-band',(18,18),(30,18))
        self.relate('connect','head','forehead-band')
        self.add_line('habit-left',(8,44),(8,36))
        self.add_arc('shoulder-left',(8,36),(24,28),radius_x=16,radius_y=8)
        self.add_arc('shoulder-right',(24,28),(40,36),radius_x=16,radius_y=8)
        self.add_line('habit-right',(40,36),(40,44))
        self.add_line('habit-base',(40,44),(8,44))
        self.add_contour('habit','habit-left','shoulder-left','shoulder-right','habit-right','habit-base',closed=True)
        self.relate('connect','veil','habit')
        self.relate('connect','head','habit')
        self.add_line('cross-top',(24,32),(24,36))
        self.add_line('cross-bottom',(24,36),(24,40))
        self.add_line('cross-left',(20,36),(24,36))
        self.add_line('cross-right',(24,36),(28,36))
        parts=['cross-top','cross-bottom','cross-left','cross-right']
        for i,a in enumerate(parts):
            for b in parts[:i]: self.relate('connect',a,b)

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

