"""Rejected visor is too tall and narrow, with a blob-like X and angular nose cut. Broaden the visor, soften the nose recess and enlarge the central cross.
Plan: HRECT_M; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a58cb8f2-5a25-594d-a031-72828d14122f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__game-immersive-vr/20260929T132937Z-thuan-mac/reference/game immersive vr_a58cb8f2-5a25-594d-a031-72828d14122f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='game-immersive-vr'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('game', 'immersive', 'vr')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                kind,end,*args=step; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end; members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b): self.relate('connect',a,b)

        def box(name,l,t,r,b,rad=0):
            if not rad:self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('visor',(16,10),[('L',(32,10)),('A',(40,18),8,8,True),('L',(40,24)),('L',(40,30)),('A',(32,38),8,8,True),('C',(24,34),(28,38),(28,34)),('C',(16,38),(20,34),(20,38)),('A',(8,30),8,8,True),('L',(8,24)),('L',(8,18)),('A',(16,10),8,8,True)],True)
        self.add_line('strap-left',(4,24),(8,24));join('strap-left','visor')
        self.add_line('strap-right',(40,24),(44,24));join('strap-right','visor')
        self.add_line('cross-a',(20,19),(28,25));self.add_line('cross-b',(20,25),(28,19));join('cross-a','cross-b')
