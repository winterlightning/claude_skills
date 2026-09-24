"""Chateau Frontenac with a tall mansard roof behind lower pointed turrets and a right wing. Roof seams and tower walls share explicit attachment points; small facade details omitted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8ba45a21-4375-538a-afb6-e6d71151d5e5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__chateau-frontenac/20260924T083211Z-thuan-mac/reference/chateau frontenac canada_8ba45a21-4375-538a-afb6-e6d71151d5e5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='chateau-frontenac'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def build(self):
        # Symbol plan: Chateau Frontenac with a tall mansard roof behind lower pointed turrets and a right wing. Roof seams and tower walls share explicit attachment points; small facade details omitted.

        def path(n,start,commands,closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                m=f'{n}-{i}'
                if kind=='L': self.add_line(m,start,end)
                elif kind=='A': self.add_arc(m,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,start,(args[0],args[1],end))
                members.append(m);start=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry=None):
            ry=rx if ry is None else ry
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        join=lambda a,b:self.relate('connect',a,b)

        self.add_polyline('back',(18,28),(18,14),(22,6),(34,6),(38,14),(38,30));line('roof',(18,14),(38,14));join('roof','back')
        self.add_polyline('front',(6,42),(6,28),(12,18),(18,28),(24,18),(30,28),(36,28),(38,30),(42,34),(42,42),closed=True)
        line('tower',(18,28),(18,42));join('tower','front')
        line('wing',(30,28),(30,42));join('wing','front')
        join('back','front')
