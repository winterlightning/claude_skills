"""The rejected phone was wide and squat, and its arrow dwarfed the device. Restore a taller phone with a long outgoing shaft.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No additional useful Lucide match; inspected source defines device.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='26f6456e-efc4-4a01-b0a3-43ae69125204'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__mobile-phone-long-outgoing-arrow/20260929T135549Z-thuan-mac/reference/mobile phone call forwarding outgoing 3_26f6456e-efc4-4a01-b0a3-43ae69125204.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='mobile-phone-long-outgoing-arrow'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('mobile', 'phone', 'long', 'outgoing', 'arrow')
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

        path('phone',(28,11),[('L',(28,8)),('A',(24,4),4,4,False),('L',(12,4)),('A',(8,8),4,4,False),('L',(8,35)),('L',(8,40)),('A',(12,44),4,4,False),('L',(24,44)),('A',(28,40),4,4,False),('L',(28,35))])
        line('bezel',(8,35),(28,35));join('bezel','phone')
        line('shaft',(17,23),(40,23));poly('arrow',(34,17),(40,23),(34,29));join('shaft','arrow')
