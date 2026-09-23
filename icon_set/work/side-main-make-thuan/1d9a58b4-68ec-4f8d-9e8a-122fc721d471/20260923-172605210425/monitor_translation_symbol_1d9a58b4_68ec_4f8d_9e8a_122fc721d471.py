"""A desktop monitor displaying a Chinese translation glyph.

Symbol plan: Square total envelope, centered screen stand; glyph has top tick, shared bar attachments and mirrored crossing curves. Ink extremes (4,4)-(44,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1d9a58b4-68ec-4f8d-9e8a-122fc721d471'
SOURCE_PATH = 'pictographic-primitives/other/monitor language_1d9a58b4-68ec-4f8d-9e8a-122fc721d471.svg'
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
    icon_id = 'monitor-translation-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'other'
    aliases = ()
    keywords = ('monitor', 'translation', 'symbol')

    def build(self):
        monitor(self)
        self.add_line('glyph-bar-l',(15,18),(18,18));self.add_line('glyph-bar-mid-l',(18,18),(24,18));self.add_line('glyph-bar-mid-r',(24,18),(30,18));self.add_line('glyph-bar-r',(30,18),(33,18))
        self.add_contour('glyph-bar','glyph-bar-l','glyph-bar-mid-l','glyph-bar-mid-r','glyph-bar-r')
        self.add_line('glyph-tick',(24,15),(24,18))
        for p in ('glyph-bar-mid-l','glyph-bar-mid-r'):self.relate('connect','glyph-tick',p)
        self.add_bezier('glyph-left-upper',(18,18),((19,20),(21,22),(24,23)))
        self.add_bezier('glyph-left-lower',(24,23),((27,25),(30,25),(32,25)))
        self.add_bezier('glyph-right-upper',(30,18),((29,20),(27,22),(24,23)))
        self.add_bezier('glyph-right-lower',(24,23),((21,25),(18,25),(16,25)))
        self.add_contour('glyph-left','glyph-left-upper','glyph-left-lower');self.add_contour('glyph-right','glyph-right-upper','glyph-right-lower')
        for p in ('glyph-bar-l','glyph-bar-mid-l'):self.relate('connect','glyph-left-upper',p)
        for p in ('glyph-bar-mid-r','glyph-bar-r'):self.relate('connect','glyph-right-upper',p)
        for a in ('glyph-left-upper','glyph-left-lower'):
         for b in ('glyph-right-upper','glyph-right-lower'):self.relate('connect',a,b)
