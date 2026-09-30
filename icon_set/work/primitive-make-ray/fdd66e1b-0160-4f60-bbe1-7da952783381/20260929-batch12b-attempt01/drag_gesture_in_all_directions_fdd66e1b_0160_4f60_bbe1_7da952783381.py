"""Rejected arrows are thick isolated chevrons with virtually no shafts. Restore four explicit arrow shafts around the centered fingertip.
Plan: SQUARE; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='fdd66e1b-0160-4f60-bbe1-7da952783381'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__drag-gesture-in-all-directions/20260929T132613Z-thuan-mac/reference/gesture tap all direction_fdd66e1b-0160-4f60-bbe1-7da952783381.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='drag-gesture-in-all-directions'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('gesture', 'tap', 'all', 'direction')
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

        path('finger',(18,28),[('L',(18,25)),('A',(30,25),6,6,True),('L',(30,28))])
        self.add_polyline('up-head',(20,10),(24,6),(28,10));self.add_line('up-shaft',(24,6),(24,11));join('up-head','up-shaft')
        self.add_polyline('down-head',(20,38),(24,42),(28,38));self.add_line('down-shaft',(24,36),(24,42));join('down-head','down-shaft')
        self.add_polyline('left-head',(10,20),(6,24),(10,28));self.add_line('left-shaft',(6,24),(10,24));join('left-head','left-shaft')
        self.add_polyline('right-head',(38,20),(42,24),(38,28));self.add_line('right-shaft',(38,24),(42,24));join('right-head','right-shaft')
