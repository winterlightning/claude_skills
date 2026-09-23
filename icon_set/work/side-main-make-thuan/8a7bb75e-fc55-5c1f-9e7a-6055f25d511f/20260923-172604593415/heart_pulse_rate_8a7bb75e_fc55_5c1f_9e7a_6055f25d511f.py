"""A heart outline crossed by an ECG pulse.

Symbol plan: Mirrored lobes and lower silhouette around x=24; asymmetric continuous pulse joins the silhouette at (8,22) and (40,22). Ink extremes (4,4)-(44,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8a7bb75e-fc55-5c1f-9e7a-6055f25d511f'
SOURCE_PATH = 'pictographic-primitives/health/heart rate_8a7bb75e-fc55-5c1f-9e7a-6055f25d511f.svg'
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
    icon_id = 'heart-pulse-rate'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'health'
    aliases = ()
    keywords = ('heart', 'pulse', 'rate')

    def build(self):
        self.add_arc('left-lobe',(24,14),(6,14),radius_x=9,radius_y=8,sweep=False)
        self.add_bezier('left-shoulder',(6,14),((6,18),(6,20),(8,22)))
        self.add_line('left-lower',(8,22),(24,42))
        self.add_line('right-lower',(24,42),(40,22))
        self.add_bezier('right-shoulder',(40,22),((42,20),(42,18),(42,14)))
        self.add_arc('right-lobe',(42,14),(24,14),radius_x=9,radius_y=8,sweep=False)
        self.add_contour('heart','left-lobe','left-shoulder','left-lower','right-lower','right-shoulder','right-lobe',closed=True)
        self.add_polyline('pulse',(8,22),(16,22),(20,16),(27,31),(33,22),(40,22))
        for edge in ('left-shoulder','left-lower'): self.relate('connect','pulse-1',edge)
        for edge in ('right-shoulder','right-lower'): self.relate('connect','pulse-5',edge)
