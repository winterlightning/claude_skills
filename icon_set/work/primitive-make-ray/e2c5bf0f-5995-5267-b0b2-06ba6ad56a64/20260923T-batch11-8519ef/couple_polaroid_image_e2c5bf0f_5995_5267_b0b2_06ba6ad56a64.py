"""couple polaroid image. Reconstructed whole reference on SOLO48.
Plan: VRECT_L visible bounds (6, 2, 42, 46).
Construction: human_ref/user.svg, users and heart. Shared dimensions and relationships are recorded in build.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e2c5bf0f-5995-5267-b0b2-06ba6ad56a64'
SOURCE_PATH = 'icon_set/work/todo-references/couple polaroid image_e2c5bf0f-5995-5267-b0b2-06ba6ad56a64.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'couple-polaroid-image'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('couple', 'polaroid', 'image')

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
        # Two equal busts and a heart inside a Polaroid frame.
        # Human construction: icon_set/references/human_ref/user.svg.
        self.add_polyline('frame',(8,4),(40,4),(40,44),(8,44),closed=True)
        self.add_line('photo-bottom',(8,36),(40,36))
        self.relate('connect','frame','photo-bottom')
        for i,cx in enumerate((17,31)):
            self.circle(f'head-{i}',cx,20,4)
            # Head bottom24 -> shoulders top32 =8 centreline /4 ink clearance.
            self.add_arc(f'shoulders-{i}',(cx-6,36),(cx+6,36),radius_x=6,radius_y=4)
            self.relate('connect',f'shoulders-{i}','photo-bottom')
        self.add_bezier('heart-left',(24,9),((18,3),(15,10),(24,15)))
        self.add_bezier('heart-right',(24,15),((33,10),(30,3),(24,9)))
        self.add_contour('heart','heart-left','heart-right',closed=True)

