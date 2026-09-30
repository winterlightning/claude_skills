"""Rejected scissor handles are tiny and film appears as two brackets. Enlarge handles, keep crossing blades, and close the separated film frames to make the cut readable.
Plan: SQUARE envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='204c5517-7bf1-4d62-a20e-65036d54c49b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__scissors-cutting-film/20260929T130116Z-thuan-mac/reference/video edit cut_204c5517-7bf1-4d62-a20e-65036d54c49b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='scissors-cutting-film'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('video', 'edit', 'cut')
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
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:
                path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        circle('loop-top',11,14,5);circle('loop-bottom',11,34,5)
        self.add_line('blade-down',(14,18),(30,34));join('loop-top','blade-down')
        self.add_line('blade-up',(14,30),(30,14));join('loop-bottom','blade-up');join('blade-up','blade-down')
        box('film-top',30,6,42,18,0);join('blade-up','film-top')
        box('film-bottom',30,30,42,42,0);join('blade-down','film-bottom')
