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

        path('loop',(6,34),[('C',(20,16),(6,28),(12,21)),('C',(34,6),(26,11),(30,6)),('A',(42,14),8,8,True),('C',(28,32),(42,20),(34,27)),('C',(14,42),(22,37),(18,42)),('A',(6,34),8,8,True)],True)
        path('rear-top',(6,14),[('A',(14,6),8,8,True),('L',(18,6))])
        path('rear-bottom',(42,34),[('A',(34,42),8,8,True),('L',(30,42))])
