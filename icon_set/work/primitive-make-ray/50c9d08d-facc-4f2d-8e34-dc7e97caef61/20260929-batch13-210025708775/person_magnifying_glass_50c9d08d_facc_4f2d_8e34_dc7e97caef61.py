"""Steep handle and narrow shoulders differ from diagonal magnifier and broad bust. Re-angle handle and broaden shoulder contour.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: search plus human_ref/user.svg: circular head, exact detached gap
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='50c9d08d-facc-4f2d-8e34-dc7e97caef61'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-magnifying-glass/20260929T135610Z-thuan-mac/reference/person magnifying glass_50c9d08d-facc-4f2d-8e34-dc7e97caef61.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='person-magnifying-glass'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('person', 'magnifying', 'glass')
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

        # Lens center21,21,r15; integer diagonal handle attachment30,33.
        self.add_arc('lens-main',(30,33),(6,21),radius_x=15,large_arc=True,sweep=False)
        self.add_arc('lens-return',(6,21),(30,33),radius_x=15,sweep=False)
        self.add_contour('lens','lens-main','lens-return',closed=True)
        line('handle',(30,33),(42,42));join('handle','lens')
        oval('head',21,18,4,4)
        path('shoulders',(12,33),[('A',(30,33),9,3,True)]);join('shoulders','lens')
        # Head bottom22; shoulder apex30: exact4-unit ink gap.
