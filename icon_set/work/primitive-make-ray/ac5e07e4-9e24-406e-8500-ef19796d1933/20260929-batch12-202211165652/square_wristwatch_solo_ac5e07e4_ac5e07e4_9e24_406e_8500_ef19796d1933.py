"""Blank watch removes the euro symbol; restore its C-shaped curve and crossbar on a larger square face.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: watch: face with centered straps
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ac5e07e4-9e24-406e-8500-ef19796d1933'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__square-wristwatch-solo-ac5e07e4/20260929T131521Z-thuan-mac/reference/smart watch square euro sign_ac5e07e4-9e24-406e-8500-ef19796d1933.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='square-wristwatch-solo-ac5e07e4'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('square', 'wristwatch', 'solo', 'ac5e07e4')
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

        box('face',8,10,40,38,4)
        line('strap-upper',(24,4),(24,10));join('strap-upper','face')
        line('strap-lower',(24,38),(24,44));join('strap-lower','face')
        path('euro',(30,18),[('L',(25,18)),('A',(19,24),6,6,False),('A',(25,30),6,6,False),('L',(30,30))])
        line('euro-bar',(16,24),(25,24));join('euro-bar','euro')
