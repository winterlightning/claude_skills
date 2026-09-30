"""The rejected horseshoe is a rigid U with parallel uprights. Restore subtly flared tips and bowed outer sides.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='707aefe4-5cb6-4a10-8642-455a8f4143eb'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__open-horseshoe/20260929T135609Z-thuan-mac/reference/hoof_707aefe4-5cb6-4a10-8642-455a8f4143eb.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='open-horseshoe'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('open', 'horseshoe')
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

        path('shoe',(10,4),[('L',(18,4)),('C',(17,27),(18,12),(17,20)),('A',(31,27),7,7,False),('C',(30,4),(31,20),(30,12)),('L',(38,4)),('C',(40,28),(38,12),(40,20)),('A',(8,28),16,16,True),('C',(10,4),(8,20),(10,12))],True)
