"""circle upload: complete reference reconstructed on SOLO48.
Keyshape: CIRCLE, visible bounds (2, 2, 46, 46).
Construction reference: upload. See build comments for symbols and relationships.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3b83fd38-db3b-4974-b39c-fe72f9fbd03d'
SOURCE_PATH = 'icon_set/work/todo-references/circle upload_3b83fd38-db3b-4974-b39c-fe72f9fbd03d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-upload'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('circle', 'upload')

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
        # Tray and upward shaft are independent; arrowhead shares its tip.
        self.add_line('shaft',(24,14),(24,24))
        self.add_polyline('arrow',(18,20),(24,14),(30,20))
        self.relate('connect','shaft','arrow')
        self.add_polyline('tray',(16,28),(16,32),(32,32),(32,28))

