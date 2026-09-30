"""The rejected top masks merge into one arch and lose their eye openings. Restore three mask silhouettes with distinct horizontal eye bands in the triangular arrangement.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: equal rounded heads; original supplies masks and arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b87e413a-6c06-4509-b808-28f85d67c2a6'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__three-balaclava-wearers/20260929T145934Z-thuan-mac/reference/terrorists 1_b87e413a-6c06-4509-b808-28f85d67c2a6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='three-balaclava-wearers'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('three', 'balaclava', 'wearers')
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

        for n,cx in [('left',12),('right',36)]:
         path(n,(cx-8,28) if n=='left' else (cx+8,28), [('L',(cx-8,16) if n=='left' else (cx+8,16)),('A',(cx+8,16) if n=='left' else (cx-8,16),8,8,n=='left')])
         line(n+'band',(cx-8,16),(cx+8,16));join(n,n+'band')
        path('front',(16,40),[('L',(16,32)),('A',(32,32),8,8,True),('L',(32,40))])
        line('front-band',(16,32),(32,32));join('front','front-band')
