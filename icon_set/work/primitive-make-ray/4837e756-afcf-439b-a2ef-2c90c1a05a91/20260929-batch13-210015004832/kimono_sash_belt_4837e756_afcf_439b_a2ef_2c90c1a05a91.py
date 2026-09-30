"""Square sharp buckle and thick square hole lose the rounded horizontal belt buckle. Restore rounded buckle corners and wider central slot.
Plan: HRECT_M exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful exact match; source rectangular buckle and strap topology.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4837e756-afcf-439b-a2ef-2c90c1a05a91'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__kimono-sash-belt/20260929T135357Z-thuan-mac/reference/obi_4837e756-afcf-439b-a2ef-2c90c1a05a91.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='kimono-sash-belt'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('kimono', 'sash', 'belt')
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

        box('buckle',11,10,37,38,4)
        box('opening',20,20,28,28)
        poly('left-strap',(11,16),(4,16),(4,32),(11,32));join('left-strap','buckle')
        poly('right-strap',(37,16),(44,16),(44,32),(37,32));join('right-strap','buckle')
