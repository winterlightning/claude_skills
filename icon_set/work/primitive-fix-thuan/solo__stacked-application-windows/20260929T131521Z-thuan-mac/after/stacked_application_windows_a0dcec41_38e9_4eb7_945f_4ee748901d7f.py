"""Rear window disconnected at bottom left and reads as a bracket. Restore a visibly overlapping rounded rear window.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: panels-top-left: rounded frame and header line
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a0dcec41-38e9-4eb7-945f-4ee748901d7f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__stacked-application-windows/20260929T131521Z-thuan-mac/reference/app window two_a0dcec41-38e9-4eb7-945f-4ee748901d7f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='stacked-application-windows'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('stacked', 'application', 'windows')
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

        box('front',6,6,32,32,3)
        line('header',(6,14),(32,14));join('header','front')
        path('rear',(32,14),[('L',(38,14)),('A',(42,18),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(18,42)),('A',(14,38),4,4,True),('L',(14,32))]);join('rear','front')
        line('rear-header',(32,24),(42,24));join('rear-header','rear');join('rear-header','front')
