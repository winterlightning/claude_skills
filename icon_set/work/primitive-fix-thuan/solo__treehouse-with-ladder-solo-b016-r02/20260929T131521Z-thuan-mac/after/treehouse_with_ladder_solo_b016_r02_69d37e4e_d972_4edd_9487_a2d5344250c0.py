"""Tree reduced to a pole with one hook; restore a leafy canopy around the left trunk.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: tree-deciduous and house: canopy, roof and ladder
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='69d37e4e-d972-4edd-9487-a2d5344250c0'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__treehouse-with-ladder-solo-b016-r02/20260929T131521Z-thuan-mac/reference/family outdoors tree house_69d37e4e-d972-4edd-9487-a2d5344250c0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='treehouse-with-ladder-solo-b016-r02'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('treehouse', 'with', 'ladder', 'solo', 'b016', 'r02')
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

        path('canopy',(6,28),[('L',(6,20)),('C',(12,12),(6,15),(8,12)),('C',(24,6),(12,8),(17,6))])
        line('trunk',(15,21),(15,42))
        poly('house',(26,18),(34,10),(42,18),(42,26),(26,26),closed=True)
        for x in (28,40):line(f'rail{x}',(x,26),(x,42));join(f'rail{x}','house')
        line('rung',(28,34),(40,34));join('rung','rail28');join('rung','rail40')
