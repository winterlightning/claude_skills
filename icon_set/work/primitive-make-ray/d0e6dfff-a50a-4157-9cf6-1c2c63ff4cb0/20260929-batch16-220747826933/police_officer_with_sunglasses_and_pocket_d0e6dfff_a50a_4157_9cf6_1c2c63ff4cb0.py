"""The rejected glasses collapse into thick eye slits, the hat has sharp corners, and the pocket is a stray lower line. Restore a rounded hat, paired sunglass lenses and a real pocket.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg for circular jaw; Lucide user for rounded shoulder construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d0e6dfff-a50a-4157-9cf6-1c2c63ff4cb0'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__police-officer-with-sunglasses-and-pocket/20260929T145934Z-thuan-mac/reference/police man_d0e6dfff-a50a-4157-9cf6-1c2c63ff4cb0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='police-officer-with-sunglasses-and-pocket'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('police', 'officer', 'with', 'sunglasses', 'and', 'pocket')
    human_construction = "bust"
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

        path('hat',(12,16),[('L',(14,8)),('A',(18,4),4,4,True),('L',(30,4)),('A',(34,8),4,4,True),('L',(36,16))])
        poly('brim',(8,16),(12,16),(24,16),(36,16),(40,16));join('hat','brim')
        path('jaw',(36,16),[('A',(12,16),12,12,True)]);join('jaw','hat');join('jaw','brim')
        for n,l,r in [('left',12,24),('right',24,36)]:
         path(n+'lens',(l,16),[('A',(r,16),6,6,False)]);join(n+'lens','brim');join(n+'lens','jaw');join(n+'lens','hat')
        join('leftlens','rightlens')
        path('body',(8,44),[('A',(24,32),16,12,True),('A',(40,44),16,12,True)]);join('jaw','body')
