"""A desktop monitor displaying a paint palette beside a pointed brush.

Symbol plan: Horizontal screen with centered foot; bean-shaped palette on the left, separate slanted brush on the right. Ink extremes (2,6)-(46,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '69067a56-4a6a-4f02-bdcf-fc3b45bb66ac'
SOURCE_PATH = 'pictographic-primitives/other/monitor painting_69067a56-4a6a-4f02-bdcf-fc3b45bb66ac.svg'
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
    icon_id = 'monitor-art-palette-brush'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'other'
    aliases = ()
    keywords = ('monitor', 'art', 'palette', 'brush')

    def build(self):
        monitor(self,4,8,44,32,40)
        self.add_bezier('palette',(18,16),((12,16),(12,20),(12,22)),((12,25),(17,26),(21,24)),((23,23),(20,21),(22,19)),((24,17),(21,16),(18,16)))
        self.add_contour('palette-outline','palette',closed=True)
        self.add_bezier('brush-head-right',(35,16),((35,18),(36,20),(36,21)),((36,23),(35,24),(33,24)))
        self.add_bezier('brush-head-left',(33,24),((31,24),(30,23),(30,21)),((30,19),(33,18),(35,16)))
        self.add_contour('brush-outline','brush-head-right','brush-head-left',closed=True)
        self.add_line('brush-handle',(33,24),(29,28))
        self.relate('connect','brush-handle','brush-head-right')
        self.relate('connect','brush-handle','brush-head-left')
