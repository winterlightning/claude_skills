"""Geisha bust with radius-8 circular jaw, round bun, symmetric hairpins, and a curved kimono with diagonal lapel. Shared human-reference user.svg informs circular jaw and shoulders; explicit bust contact is zero ink gap (jaw bottom 26, shoulder top 30).
Omissions: Small hairline and secondary kimono lapel omitted.
Construction references: no useful direct Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8294bb7e-b135-54c0-9464-4ea256245719'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/geisha_8294bb7e-b135-54c0-9464-4ea256245719.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    human_construction="bust"
    icon_id='geisha-bust'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "culture"
    aliases=()
    keywords=('geisha',)

    def path(self, name, start, commands, closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            eid=f'{name}-{i}'; ids.append(eid)
            if c[0]=='L': self.add_line(eid,here,c[1])
            elif c[0]=='A': self.add_arc(eid,here,c[1],radius_x=c[2],radius_y=c[3],sweep=c[4],large_arc=c[5] if len(c)>5 else False)
            elif c[0]=='C': self.add_bezier(eid,here,(c[2],c[3],c[1]))
            here=c[1]
        self.add_contour(name,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,x,y,w,h,r):
        self.path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)

    def build(self):
        # Circular jaw touching curved shoulders: extrema are exactly 4 apart.
        self.path('head',(24,10),[('A',(32,18),8,8,True),('A',(24,26),8,8,True),('A',(16,18),8,8,True),('A',(24,10),8,8,True)],True)
        self.path('bun',(24,10),[('A',(24,4),3,3,True),('A',(24,10),3,3,True)],True)
        self.add_line('pin-left',(8,4),(16,18));self.add_line('pin-right',(40,4),(32,18))
        for a,b in [('head','bun'),('head','pin-left'),('head','pin-right')]:self.relate('connect',a,b)
        self.path('kimono',(8,44),[('A',(24,30),16,14,True),('A',(40,44),16,14,True),('L',(16,44)),('L',(8,44))],True)
        self.relate('connect','head','kimono')
        self.add_line('lapel',(24,30),(16,44));self.relate('connect','lapel','kimono')
