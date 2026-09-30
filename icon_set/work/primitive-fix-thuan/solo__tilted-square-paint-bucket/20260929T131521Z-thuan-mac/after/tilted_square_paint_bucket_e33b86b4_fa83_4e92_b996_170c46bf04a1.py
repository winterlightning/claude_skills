"""Tiny diamond body and squat drop lose the large pouring bucket. Enlarge and soften bucket silhouette.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: paint-bucket: diagonal vessel and separate droplet
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e33b86b4-fa83-4e92-b996-170c46bf04a1'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__tilted-square-paint-bucket/20260929T131521Z-thuan-mac/reference/color bucket 1_e33b86b4-fa83-4e92-b996-170c46bf04a1.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tilted-square-paint-bucket'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('tilted', 'square', 'paint', 'bucket')
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

        poly('bucket',(6,26),(22,10),(34,22),(18,38),closed=True)
        path('handle',(10,22),[('L',(10,12)),('A',(22,12),6,6,True)]);join('handle','bucket')
        path('drop',(38,31),[('C',(42,38),(40,34),(42,36)),('A',(34,38),4,4,True),('C',(38,31),(34,36),(36,34))],True)
