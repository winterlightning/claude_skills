"""cloud with co2: complete reference reconstructed on SOLO48.
Keyshape: SQUARE, visible bounds (4, 4, 44, 44).
Construction reference: cloud. See build comments for symbols and relationships.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '75fb4fc6-e4f1-41a1-94d3-87656053d2cd'
SOURCE_PATH = 'icon_set/work/todo-references/cloud with co2_75fb4fc6-e4f1-41a1-94d3-87656053d2cd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloud-with-co2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('cloud', 'with', 'co2')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def rounded_rect(self, name, x, y, w, h, r):
        nodes=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=nodes[i],nodes[(i+1)%8]; eid=f'{name}-{i}';members.append(eid)
            if i%2:self.add_arc(eid,a,b,radius_x=r)
            else:self.add_line(eid,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
         # Symmetric open cloud canopy above individually drawn C, O, and lowered 2.
        self.add_arc('cloud-left',(12,28),(12,16),radius_x=6)
        self.add_line('shoulder-left',(12,16),(14,16))
        self.add_arc('cloud-top',(14,16),(34,16),radius_x=10)
        self.add_line('shoulder-right',(34,16),(36,16))
        self.add_arc('cloud-right',(36,16),(36,28),radius_x=6)
        self.add_contour('cloud','cloud-left','shoulder-left','cloud-top','shoulder-right','cloud-right')
        self.add_arc('c-top',(20,30),(12,30),radius_x=4,sweep=False)
        self.add_line('c-stem',(12,30),(12,34))
        self.add_arc('c-bottom',(12,34),(20,34),radius_x=4,sweep=False)
        self.add_contour('c','c-top','c-stem','c-bottom')
        self.rounded_rect('o',25,26,8,12,4)
        self.add_arc('two-top',(36,35),(42,35),radius_x=3)
        self.add_polyline('two-base',(42,35),(36,42),(42,42))
        self.relate('connect','two-top','two-base')
