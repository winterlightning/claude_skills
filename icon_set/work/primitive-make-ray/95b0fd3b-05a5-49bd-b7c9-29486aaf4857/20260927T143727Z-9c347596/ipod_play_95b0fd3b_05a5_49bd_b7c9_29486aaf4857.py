"""Revision of the claimed reference after comparing original and rejected drawing."""
"""Portable player with play triangle and circular control.
Plan: Separate vertical control bands. Play triangle and circular button remain recognizable at 48px.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '95b0fd3b-05a5-49bd-b7c9-29486aaf4857'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ipod-play/20260927T142529Z-thuan-mac-1/reference/ipod play_95b0fd3b-05a5-49bd-b7c9-29486aaf4857.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'ipod-play'
    keyshape = Keyshape.VRECT_L
    # Visible ink extremes: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'music'
    categories = ('primitives', 'music')
    aliases = ()
    keywords = ('ipod', 'play')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):
        # Two content bands restore the line that separates display and control.
        self.rect('body',8,4,32,40)
        self.add_polyline('play',(18,13),(29,16),(18,19),closed=True)
        self.add_line('screen-divider',(8,27),(40,27))
        self.relate('connect','body','screen-divider')
        self.add_dot('control',(24,35))

PLAN = 'Portable player with play triangle and circular control. Separate vertical control bands.'
OMISSIONS = 'Screen separator omitted.'
CONSTRUCTION_REFERENCES = ['icon_set/references/lucide/original/tablet.svg', 'icon_set/references/lucide/atomic-debug/tablet.svg']
PARENT_SOURCE = 'icon_set/model/icons/solo/ipod_play_95b0fd3b_05a5_49bd_b7c9_29486aaf4857.py'
