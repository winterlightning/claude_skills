"""Crawdad with closed leaf-shaped claws, paired legs and a tail fan.
Plan: VRECT_L retains an upright body and raised claws.
Reduction: Fine antennae, extra leg rows, eyes and separate tail lobes omitted; body and tail enlarged and simplified.
Construction: shrimp: coherent curved body and clear segmentation; no exact claw match. Paired appendages mirror about x=24.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f4812ef0-fce6-4380-9124-384916ee103d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_13/crawdad_f4812ef0-fce6-4380-9124-384916ee103d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crawdad'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('crawdad',)

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def rounded_rect(self, name, x, y, w, h, r):
        nodes=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=nodes[i],nodes[(i+1)%8];eid=f'{name}-{i}';members.append(eid)
            if i%2:self.add_arc(eid,a,b,radius_x=r)
            else:self.add_line(eid,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Mirrored elongated claws, enlarged body and a broad tail fan; fine antennae and extra legs omitted.
        self.add_arc('body-tl',(18,30),(24,24),radius_x=6)
        self.add_arc('body-tr',(24,24),(30,30),radius_x=6)
        nodes=[(30,30),(28,36),(32,44),(16,44),(20,36),(18,30)]
        for k,(a,z) in enumerate(zip(nodes,nodes[1:]),1):self.add_line(f'body-bottom-{k}',a,z)
        self.add_contour('body','body-tl','body-tr',*[f'body-bottom-{i}' for i in range(1,6)],closed=True)
        self.add_line('tail-band',(20,36),(28,36));self.relate('connect','body','tail-band')
        for side in (-1,1):
            def P(x,y):return 24+side*x,y
            n='left' if side==-1 else 'right'
            self.add_line(n+'-arm',P(6,30),P(12,16));self.relate('connect','body',n+'-arm')
            self.add_arc(n+'-claw-a',P(12,4),P(12,16),radius_x=4,radius_y=6)
            self.add_arc(n+'-claw-b',P(12,16),P(12,4),radius_x=4,radius_y=6)
            self.add_contour(n+'-claw',n+'-claw-a',n+'-claw-b',closed=True)
            self.relate('connect',n+'-arm',n+'-claw')
            self.add_polyline(n+'-leg',P(6,30),P(12,30),P(16,34));self.relate('connect','body',n+'-leg');self.relate('connect',n+'-arm',n+'-leg')
