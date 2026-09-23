"""A rounded mobile phone showing a pound sterling symbol above a bottom divider.

Symbol plan: Vertical enclosure with split walls at divider; hand-authored pound with hooked top, shared stem/crossbar node and curved foot. Ink extremes (8,2)-(40,46).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a70db137-a446-4f4c-b656-4fea14660981'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone pound sign_a70db137-a446-4f4c-b656-4fea14660981.svg'
AUTHOR = "gpt-6"

def circle(icon, name, cx, cy, r):
    icon.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
    icon.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
    icon.add_contour(name, name+'-top', name+'-bottom', closed=True)

def rounded_rect(icon, name, x0,y0,x1,y1,r):
    points=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
    members=[]
    for j,a in enumerate(points):
        b=points[(j+1)%8]; part=name+'-'+str(j)
        if j%2: icon.add_arc(part,a,b,radius_x=r)
        else: icon.add_line(part,a,b)
        members.append(part)
    icon.add_contour(name,*members,closed=True)

def monitor(icon, x0=6,y0=6,x1=42,y1=34,foot=42):
    # Split bottom wall at the exact stand attachment.
    r=3; cx=24
    icon.add_line('screen-top',(x0+r,y0),(x1-r,y0))
    icon.add_arc('screen-tr',(x1-r,y0),(x1,y0+r),radius_x=r)
    icon.add_line('screen-right',(x1,y0+r),(x1,y1-r))
    icon.add_arc('screen-br',(x1,y1-r),(x1-r,y1),radius_x=r)
    icon.add_line('screen-bottom-r',(x1-r,y1),(cx,y1))
    icon.add_line('screen-bottom-l',(cx,y1),(x0+r,y1))
    icon.add_arc('screen-bl',(x0+r,y1),(x0,y1-r),radius_x=r)
    icon.add_line('screen-left',(x0,y1-r),(x0,y0+r))
    icon.add_arc('screen-tl',(x0,y0+r),(x0+r,y0),radius_x=r)
    icon.add_contour('screen','screen-top','screen-tr','screen-right','screen-br','screen-bottom-r','screen-bottom-l','screen-bl','screen-left','screen-tl',closed=True)
    icon.add_line('stand',(cx,y1),(cx,foot))
    icon.add_line('foot-left',(16,foot),(cx,foot));icon.add_line('foot-right',(cx,foot),(32,foot))
    icon.add_contour('foot','foot-left','foot-right')
    for part in ['screen-bottom-r','screen-bottom-l','foot-left','foot-right']: icon.relate('connect','stand',part)

class AuthoredIcon(Solo48):
    icon_id = 'mobile-phone-pound-sign'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'other'
    aliases = ()
    keywords = ('mobile', 'phone', 'pound', 'sign')

    def build(self):
        self.add_line('phone-top',(14,4),(34,4));self.add_arc('phone-tr',(34,4),(38,8),radius_x=4)
        self.add_line('phone-right-upper',(38,8),(38,36));self.add_line('phone-right-lower',(38,36),(38,40))
        self.add_arc('phone-br',(38,40),(34,44),radius_x=4);self.add_line('phone-bottom',(34,44),(14,44))
        self.add_arc('phone-bl',(14,44),(10,40),radius_x=4)
        self.add_line('phone-left-lower',(10,40),(10,36));self.add_line('phone-left-upper',(10,36),(10,8));self.add_arc('phone-tl',(10,8),(14,4),radius_x=4)
        self.add_contour('phone','phone-top','phone-tr','phone-right-upper','phone-right-lower','phone-br','phone-bottom','phone-bl','phone-left-lower','phone-left-upper','phone-tl',closed=True)
        self.add_line('divider',(10,36),(38,36))
        for edge in ('phone-right-upper','phone-right-lower','phone-left-lower','phone-left-upper'): self.relate('connect','divider',edge)
        self.add_arc('pound-hook',(29,17),(21,17),radius_x=4,sweep=False)
        self.add_line('pound-upper',(21,17),(21,20));self.add_line('pound-lower',(21,20),(21,24))
        self.add_bezier('pound-foot',(21,24),((21,26),(20,28),(19,28)))
        self.add_line('pound-base',(19,28),(29,28))
        self.add_contour('pound','pound-hook','pound-upper','pound-lower','pound-foot','pound-base')
        self.add_line('pound-cross-l',(19,20),(21,20));self.add_line('pound-cross-r',(21,20),(25,20));self.add_contour('pound-cross','pound-cross-l','pound-cross-r')
        for a in ('pound-cross-l','pound-cross-r'):
         for b in ('pound-upper','pound-lower'): self.relate('connect',a,b)
