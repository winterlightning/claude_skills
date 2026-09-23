"""crayfish. Reconstructed whole reference on SOLO48.
Plan: VRECT_L visible bounds (6, 2, 42, 46).
Construction: shrimp (segmented body only). Shared dimensions and relationships are recorded in build.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '813ecb4a-07a5-40d2-a4dc-2d3842c2a9f0'
SOURCE_PATH = 'icon_set/work/todo-references/crayfish_813ecb4a-07a5-40d2-a4dc-2d3842c2a9f0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crayfish'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('crayfish',)

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
        # Shared vertical body, mirrored appendages, and segmented tapered tail.
        axis=24
        self.add_arc('body-tl',(18,20),(24,14),radius_x=6)
        self.add_arc('body-tr',(24,14),(30,20),radius_x=6)
        self.add_line('body-right',(30,20),(30,26))
        self.add_arc('body-br',(30,26),(24,32),radius_x=6)
        self.add_arc('body-bl',(24,32),(18,26),radius_x=6)
        self.add_line('body-left',(18,26),(18,20))
        self.add_contour('body','body-tl','body-tr','body-right','body-br','body-bl','body-left',closed=True)
        self.add_polyline('tail',(20,32),(20,37),(24,40),(28,37),(28,32),closed=True)
        self.relate('connect','body','tail')
        # Narrow extra tail rule omitted; abdomen and fan remain separate segments.
        for side in (-1,1):
            def P(x,y):return axis+side*x,y
            prefix='left' if side==-1 else 'right'
            self.add_bezier(prefix+'-antenna',(24,14),(P(3,8),P(5,5),P(10,4)))
            self.relate('connect','body',prefix+'-antenna')
            self.add_bezier(prefix+'-arm',P(6,20),(P(8,20),P(11,19),P(12,17)))
            self.relate('connect','body',prefix+'-arm')
            for row,(base,outer,end) in enumerate(((26,28,32),)):
                self.add_polyline(f'{prefix}-leg-{row}',P(6,base),P(13,outer),P(16,end))
                self.relate('connect','body',f'{prefix}-leg-{row}')
            self.add_polyline(prefix+'-hindleg',P(4,35),P(10,37),P(12,40))
            self.relate('connect','tail',prefix+'-hindleg')
            # Broad crayfish pincers carry a visible inward slit.
            self.add_bezier(prefix+'-pincer-outer',P(12,17),(P(16,14),P(16,7),P(14,4)))
            self.add_line(prefix+'-pincer-notch-1',P(14,4),P(13,12))
            self.add_line(prefix+'-pincer-notch-2',P(13,12),P(10,14))
            self.add_bezier(prefix+'-pincer-inner',P(10,14),(P(8,13),P(8,10),P(9,8)))
            self.add_contour(prefix+'-pincer',prefix+'-pincer-outer',prefix+'-pincer-notch-1',prefix+'-pincer-notch-2',prefix+'-pincer-inner')
            self.relate('connect',prefix+'-arm',prefix+'-pincer')
        # Three connected lobes distinguish this tail fan from the crawdad's two.
        self.add_bezier('fin-left',(24,40),((18,40),(17,44),(21,44)),((23,44),(24,42),(24,40)))
        self.add_bezier('fin-right',(24,40),((24,42),(25,44),(27,44)),((31,44),(30,40),(24,40)))
        self.add_contour('fin-l','fin-left',closed=True)
        self.add_contour('fin-r','fin-right',closed=True)
        self.add_line('fin-mid',(24,40),(24,44))
        self.relate('connect','tail','fin-l','fin-r','fin-mid')

