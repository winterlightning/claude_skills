"""Portable player with play triangle and circular control.
Plan: Separate vertical control bands. Play triangle and circular button remain recognizable at 48px.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '95b0fd3b-05a5-49bd-b7c9-29486aaf4857'
SOURCE_PATH = 'pictographic-primitives/music/ipod play_95b0fd3b-05a5-49bd-b7c9-29486aaf4857.svg'
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
        # The body contains a generous play band and the circular control below.
        # Omit the screen separator to allocate clearance to both controls.
        self.rect('body',8,4,32,40)
        self.add_polyline('play',(17,13),(29,19),(17,25),closed=True)
        self.circle('button',24,33,2)

PLAN = 'Portable player with play triangle and circular control. Separate vertical control bands.'
OMISSIONS = 'Screen separator omitted.'
CONSTRUCTION_REFERENCES = ['icon_set/references/lucide/original/tablet.svg', 'icon_set/references/lucide/atomic-debug/tablet.svg']
PARENT_SOURCE = 'icon_set/model/icons/solo/ipod_play_95b0fd3b_05a5_49bd_b7c9_29486aaf4857.py'
