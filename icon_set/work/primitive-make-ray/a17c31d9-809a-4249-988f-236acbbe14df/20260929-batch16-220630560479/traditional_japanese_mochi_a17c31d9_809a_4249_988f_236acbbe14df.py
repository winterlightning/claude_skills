"""The rejected mochi becomes a nearly closed circular loop with an inner horseshoe. Restore the rounded dumpling silhouette with two open lower tips and a broad oval inset.
Plan: CIRCLE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct Lucide match; source supplies nested rounded dumpling contours.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a17c31d9-809a-4249-988f-236acbbe14df'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__traditional-japanese-mochi/20260929T145934Z-thuan-mac/reference/mochi_a17c31d9-809a-4249-988f-236acbbe14df.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='traditional-japanese-mochi'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('traditional', 'japanese', 'mochi')
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

        path('dumpling',(12,40),[('A',(4,24),20,20,True),('A',(44,24),20,20,True),('A',(36,40),20,20,True)])
        path('inset',(20,35),[('A',(14,28),10,7,True),('A',(34,28),10,7,True),('A',(28,35),10,7,True)])
