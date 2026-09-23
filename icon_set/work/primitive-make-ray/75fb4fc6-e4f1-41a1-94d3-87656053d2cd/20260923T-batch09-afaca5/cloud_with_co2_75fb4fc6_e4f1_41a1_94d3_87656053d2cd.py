"""cloud with co2: complete reference reconstructed on SOLO48.
Keyshape: VRECT_L, visible bounds (6, 2, 42, 46).
Construction reference: cloud. See build comments for symbols and relationships.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '75fb4fc6-e4f1-41a1-94d3-87656053d2cd'
SOURCE_PATH = 'icon_set/work/todo-references/cloud with co2_75fb4fc6-e4f1-41a1-94d3-87656053d2cd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloud-with-co2'
    keyshape = Keyshape.VRECT_L
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
        # Open cloud canopy; C, O and lowered 2 are independently authored glyphs.
        self.add_arc('cloud-left',(10,29),(14,13),radius_x=9)
        self.add_line('shoulder-left',(14,13),(15,13))
        self.add_arc('cloud-top',(15,13),(35,13),radius_x=10)
        self.add_line('shoulder-right',(35,13),(36,13))
        self.add_arc('cloud-right',(36,13),(42,28),radius_x=8)
        self.add_contour('cloud','cloud-left','shoulder-left','cloud-top','shoulder-right','cloud-right')
        self.add_arc('c-top',(19,28),(11,28),radius_x=4,sweep=False)
        self.add_line('c-stem',(11,28),(11,36))
        self.add_arc('c-bottom',(11,36),(19,36),radius_x=4,sweep=False)
        self.add_contour('c','c-top','c-stem','c-bottom')
        self.rounded_rect('o',25,24,8,16,4)
        self.add_arc('two-top',(38,36),(44,36),radius_x=3)
        self.add_polyline('two-base',(44,36),(38,44),(44,44))
        self.relate('connect','two-top','two-base')

