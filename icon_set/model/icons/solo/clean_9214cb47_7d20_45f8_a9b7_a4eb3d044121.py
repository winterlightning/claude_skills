"""clean: complete reference reconstructed on SOLO48.
Keyshape: VRECT_M, visible bounds (8, 2, 40, 46).
Construction reference: No close subject match; coherent tangent arcs. See build comments for symbols and relationships.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9214cb47-7d20-45f8-a9b7-a4eb3d044121'
SOURCE_PATH = 'icon_set/work/todo-references/clean_9214cb47-7d20-45f8-a9b7-a4eb3d044121.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clean'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('clean',)

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
        # Continuous upper semicircle rolls into the inset S waist and lower panel.
        self.add_arc('upper',(10,18),(38,18),radius_x=14)
        self.add_arc('waist-right',(38,18),(24,30),radius_x=14,radius_y=12)
        self.add_arc('waist-left',(24,30),(10,42),radius_x=14,radius_y=12,sweep=False)
        self.add_line('bottom-left',(10,42),(10,44))
        self.add_line('bottom',(10,44),(38,44))
        self.add_line('right',(38,44),(38,18))
        self.add_contour('roll','upper','waist-right','waist-left','bottom-left','bottom','right')

