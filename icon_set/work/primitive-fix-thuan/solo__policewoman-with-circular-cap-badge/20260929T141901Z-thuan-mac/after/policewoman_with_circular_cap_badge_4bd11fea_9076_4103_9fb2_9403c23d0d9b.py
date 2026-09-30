"""The rejected circular cap badge is a solid dot. Restore an outlined circular badge on a fuller cap and remove the unrelated central chest stripe.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular jaw and broad shoulders with touching bust ink.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4bd11fea-9076-4103-9fb2-9403c23d0d9b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__policewoman-with-circular-cap-badge/20260929T141901Z-thuan-mac/reference/police woman_4bd11fea-9076-4103-9fb2-9403c23d0d9b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='policewoman-with-circular-cap-badge'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('policewoman', 'with', 'circular', 'cap', 'badge')
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

        path('cap',(8,28),[('A',(24,4),16,24,True),('A',(40,28),16,24,True)])
        poly('brim',(8,28),(16,28),(32,28),(40,28));join('brim','cap')
        path('jaw',(32,28),[('A',(16,28),8,8,True)]);join('jaw','brim')
        oval('badge',24,16,3,3)
        for side,s in [('l',-1),('r',1)]:
         path('hair'+side,(24+s*8,28),[('C',(24+s*16,34),(24+s*10,31),(24+s*12,33))]);join('hair'+side,'jaw');join('hair'+side,'brim')
        path('shoulders',(8,44),[('A',(24,40),16,4,True),('A',(40,44),16,4,True)]);join('jaw','shoulders')
