"""circle skull 1: complete reference reconstructed on SOLO48.
Keyshape: CIRCLE, visible bounds (2, 2, 46, 46).
Construction reference: skull. See build comments for symbols and relationships.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0275d46c-9a52-48fb-9993-9a0c2a0a4b89'
SOURCE_PATH = 'icon_set/work/todo-references/circle skull 1_0275d46c-9a52-48fb-9993-9a0c2a0a4b89.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-skull-1'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('circle', 'skull', '1')

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
        self.circle('ring',24,24,20)
        # Symmetric domed skull, open jaw ends, and central mouth stroke.
        self.add_arc('dome',(14,23),(34,23),radius_x=10)
        self.add_arc('cheek-right',(34,23),(30,31),radius_x=10)
        self.add_line('jaw-right',(30,31),(30,35))
        self.add_arc('cheek-left',(18,31),(14,23),radius_x=10)
        self.add_line('jaw-left',(18,35),(18,31))
        self.add_contour('skull','jaw-left','cheek-left','dome','cheek-right','jaw-right')
        self.add_line('mouth',(24,32),(24,35))
        for side in (-1,1):
            self.add_line('eye-'+str(side),(24+side*6,23),(24+side*3,26))

