"""Tiny head above triangular shoulders loses the rounded portrait; restore a circular head and smooth shoulders under three inward marks.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular head and smooth bust; source aura
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8c539ea0-c1e4-4239-86da-777c9408c3f4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-with-spiritual-enlightenment-symbols/20260929T135610Z-thuan-mac/reference/asalha puja_8c539ea0-c1e4-4239-86da-777c9408c3f4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='person-with-spiritual-enlightenment-symbols'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('person', 'with', 'spiritual', 'enlightenment', 'symbols')
    human_construction="bust"
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

        path('aura',(8,34),[('C',(6,24),(6,31),(6,27)),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('C',(40,34),(42,27),(42,31))])
        poly('mark-center',(22,15),(24,17),(26,15))
        line('mark-left',(15,22),(16,21));line('mark-right',(33,22),(32,21))
        oval('head',24,30,4,4)
        path('body',(14,42),[('A',(24,38),10,4,True),('A',(34,42),10,4,True)]);join('head','body')
