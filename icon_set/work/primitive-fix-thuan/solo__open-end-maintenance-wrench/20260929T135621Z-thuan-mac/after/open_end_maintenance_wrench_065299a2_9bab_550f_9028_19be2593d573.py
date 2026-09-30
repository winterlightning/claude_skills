"""The reference is the current wrench. Its head occupies most of the height and leaves a short handle. Shorten the jaw and lengthen the handle while retaining the U-shaped open end.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct match for this tuning-fork-like wrench.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='065299a2-9bab-550f-9028-19be2593d573'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__open-end-maintenance-wrench/20260929T135621Z-thuan-mac/reference/open-end-maintenance-wrench_065299a2-9bab-550f-9028-19be2593d573.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='open-end-maintenance-wrench'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('open', 'end', 'maintenance', 'wrench')
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

        path('jaw',(8,4),[('L',(18,4)),('L',(18,12)),('A',(30,12),6,6,False),('L',(30,4)),('L',(40,4)),('L',(40,12)),('A',(24,28),16,16,True),('A',(8,12),16,16,True),('L',(8,4))],True)
        line('handle',(24,28),(24,44));join('handle','jaw')
