"""An Indian rupee sign centered in a circular coin.

Symbol plan: Circle centered (24,24), centerline radius20. Rupee owns two bars, split curved bowl and a diagonal leg. Retain directional glyph asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '54a12c47-2b42-4009-a41b-1b8ab3a9ef93'
SOURCE_PATH = 'pictographic-primitives/other/circle rupee_54a12c47-2b42-4009-a41b-1b8ab3a9ef93.svg'
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
    icon_id = 'indian-rupee-coin'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'other'
    aliases = ()
    keywords = ('indian', 'rupee', 'coin')

    def build(self):
        circle(self,'coin',24,24,20)
        self.add_line('header-l',(18,14),(24,14));self.add_line('header-r',(24,14),(30,14));self.add_contour('header','header-l','header-r')
        self.add_arc('bowl-upper',(24,14),(30,22),radius_x=6,radius_y=8)
        self.add_arc('bowl-lower',(30,22),(22,30),radius_x=8)
        self.add_line('bowl-return',(22,30),(18,30));self.add_line('leg',(18,30),(28,35))
        self.add_contour('rupee-body','bowl-upper','bowl-lower','bowl-return','leg')
        self.add_line('cross-l',(17,22),(30,22));self.add_line('cross-r',(30,22),(31,22));self.add_contour('crossbar','cross-l','cross-r')
        for a in ('header-l','header-r'): self.relate('connect',a,'bowl-upper')
        for a in ('cross-l','cross-r'):
         for b in ('bowl-upper','bowl-lower'): self.relate('connect',a,b)
