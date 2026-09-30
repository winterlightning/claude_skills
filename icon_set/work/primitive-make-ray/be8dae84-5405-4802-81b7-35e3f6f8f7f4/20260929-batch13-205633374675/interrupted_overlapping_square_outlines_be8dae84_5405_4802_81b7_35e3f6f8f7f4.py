"""Broken square fragment shrank into a dot-like hook and broad corner radii distort the interlocked outlines. Restore straight equal-size square edges and clear interruptions.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: messages-square: overlapping frames; source interruption pattern
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='be8dae84-5405-4802-81b7-35e3f6f8f7f4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__interrupted-overlapping-square-outlines/20260929T135357Z-thuan-mac/reference/pathfinder outline_be8dae84-5405-4802-81b7-35e3f6f8f7f4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='interrupted-overlapping-square-outlines'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('interrupted', 'overlapping', 'square', 'outlines')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('upper',(30,18),[('L',(30,9)),('A',(27,6),3,3,False),('L',(9,6)),('A',(6,9),3,3,False),('L',(6,27)),('A',(9,30),3,3,False),('L',(18,30)),('L',(18,21)),('A',(21,18),3,3,True),('L',(30,18))])
        path('lower',(38,18),[('L',(39,18)),('A',(42,21),3,3,True),('L',(42,39)),('A',(39,42),3,3,True),('L',(21,42)),('A',(18,39),3,3,True)])
        poly('overlap',(30,26),(30,30),(26,30))
