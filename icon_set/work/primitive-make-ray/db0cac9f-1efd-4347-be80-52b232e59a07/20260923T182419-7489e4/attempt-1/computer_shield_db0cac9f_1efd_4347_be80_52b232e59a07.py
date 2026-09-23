"""A computer display and stand enclosed by a protective shield.
Plan: Lower screen bezel separator omitted and tapered stand reduced to one neck stroke to preserve the nested monitor and shield.
Lucide construction references: shield, monitor.
Keyshape VRECT_L: (6,2)-(42,46) ink.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape

SOURCE_ICON_ID = 'db0cac9f-1efd-4347-be80-52b232e59a07'
SOURCE_PATH = 'icon_set/work/todo-references/computer shield_db0cac9f-1efd-4347-be80-52b232e59a07.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'computer-shield'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('computer', 'shield')

    def circle(self, name, cx, cy, radius):
        self.add_arc(name+'-top',(cx-radius,cy),(cx+radius,cy),radius_x=radius)
        self.add_arc(name+'-bottom',(cx+radius,cy),(cx-radius,cy),radius_x=radius)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, left, top, right, bottom, radius):
        # Shared corner radius and a bottom-centre attachment node.
        mid=(left+right)//2
        pts=[(left+radius,top),(right-radius,top),(right,top+radius),
             (right,bottom-radius),(right-radius,bottom),(mid,bottom),
             (left+radius,bottom),(left,bottom-radius),(left,top+radius),(left+radius,top)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            key=f'{name}-{i}';members.append(key)
            if i in (1,3,6,8): self.add_arc(key,a,b,radius_x=radius)
            else: self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Symmetric shield: sloped roof, vertical flanks, elliptical lower quarters.
        self.add_polyline('roof',(8,24),(8,8),(24,4),(40,8),(40,24))
        self.add_arc('lower-right',(40,24),(24,44),radius_x=16,radius_y=20)
        self.add_arc('lower-left',(24,44),(8,24),radius_x=16,radius_y=20)
        self.add_contour('shield','roof-1','roof-2','roof-3','roof-4','lower-right','lower-left',closed=True)
        self.box('screen',17,16,31,26,2)
        self.add_line('neck',(24,26),(24,34))
        self.add_polyline('foot',(20,34),(24,34),(28,34))
        self.relate('connect','screen','neck')
        self.relate('connect','neck','foot')

