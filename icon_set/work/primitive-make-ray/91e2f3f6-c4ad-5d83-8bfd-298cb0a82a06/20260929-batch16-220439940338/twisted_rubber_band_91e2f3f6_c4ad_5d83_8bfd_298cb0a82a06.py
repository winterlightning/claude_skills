"""The rejected elastic is two separate loops meeting at one point. Restore one elongated diagonal loop crossing an interrupted opposing loop.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct Lucide match; preserve the source crossing and occlusion.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='91e2f3f6-c4ad-5d83-8bfd-298cb0a82a06'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__twisted-rubber-band/20260929T145934Z-thuan-mac/reference/elastic band_91e2f3f6-c4ad-5d83-8bfd-298cb0a82a06.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='twisted-rubber-band'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('twisted', 'rubber', 'band')
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

        path('front',(8,40),[('C',(16,16),(2,34),(10,22)),('C',(40,8),(24,8),(36,2)),('C',(32,32),(46,14),(38,26)),('C',(8,40),(24,40),(12,46))],True)
        path('rear-top',(6,26),[('C',(8,8),(3,18),(3,10)),('C',(24,6),(12,3),(18,3))])
        path('rear-bottom',(24,42),[('C',(40,40),(30,45),(36,45)),('C',(42,24),(45,36),(45,30))])
