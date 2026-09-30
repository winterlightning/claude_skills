"""The rejected boots have square toes and an open rear sole. Restore rounded projecting toes, curved insteps and a rear sole meeting the foreground boot.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='25025168-8453-41bc-837d-12c11e280d6c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pair-of-rubber-boots-batch-051/20260929T135630Z-thuan-mac/reference/galoshes_25025168-8453-41bc-837d-12c11e280d6c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pair-of-rubber-boots-batch-051'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('pair', 'of', 'rubber', 'boots', 'batch', '051')
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

        path('front',(6,16),[('L',(18,16)),('L',(18,24)),('C',(30,34),(18,32),(24,31)),('A',(34,38),4,4,True),('L',(34,42)),('L',(6,42)),('L',(6,16))],True)
        path('rear',(14,6),[('L',(28,6)),('L',(28,18)),('C',(38,26),(28,24),(33,24)),('A',(42,30),4,4,True),('L',(42,34)),('L',(30,34))]);join('rear','front')
