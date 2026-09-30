"""Only the rejected drawing is available. Its roots are sharp spikes and the floss hugs the tooth. Round the molar roots and give the hooked floss tail a wider open bend.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct Lucide match; current reference supplies tooth and attached floss.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1c66776d-3576-52e5-a69d-e747648f9c71'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__tooth-with-dental-floss-upload-79ce34090d76e090/20260929T145934Z-thuan-mac/reference/tooth-with-dental-floss-upload-79ce34090d76e090_1c66776d-3576-52e5-a69d-e747648f9c71.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tooth-with-dental-floss-upload-79ce34090d76e090'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('tooth', 'with', 'dental', 'floss', 'upload', '79ce34090d76e090')
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

        path('tooth',(18,10),[('C',(8,8),(14,10),(10,8)),('C',(4,18),(5,8),(4,13)),('L',(6,26)),('L',(8,36)),('A',(14,36),3,3,False),('L',(17,28)),('A',(23,28),3,3,True),('L',(26,36)),('A',(32,36),3,3,False),('L',(34,24)),('L',(34,18)),('C',(30,8),(34,13),(33,8)),('C',(18,10),(28,8),(23,10))],True)
        path('floss',(34,18),[('A',(42,26),8,8,True),('L',(42,36)),('A',(44,40),4,4,False)]);join('tooth','floss')
