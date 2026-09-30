"""Narrow halo opening and angular shoulders make the bust mechanical. Open halo ellipse and replace polygon shoulders with a smooth symmetric arc.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular head and broad shoulders
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='26417ba5-2631-48ff-a294-d0bcf4e7a13e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-with-halo/20260929T135610Z-thuan-mac/reference/god_26417ba5-2631-48ff-a294-d0bcf4e7a13e.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='person-with-halo'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('person', 'with', 'halo')
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

        oval('halo',24,8,12,4)
        oval('head',24,26,6,6)
        path('shoulders',(8,44),[('A',(40,44),16,4,True)])
        # Head bottom32; shoulder apex40: exactly8 centerline /4 ink.
