"""Side-view cricket with long antenna, curved abdomen and a tall folded jumping leg. Short legs form two coherent jointed strokes; no useful exact Lucide match."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f676f8b4-b6a7-4e6b-ab0e-87feab8269f5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__cricket/20260924T083211Z-thuan-mac/reference/insect cricket body_f676f8b4-b6a7-4e6b-ab0e-87feab8269f5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='cricket'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def build(self):
        # Symbol plan: Side-view cricket with long antenna, curved abdomen and a tall folded jumping leg. Short legs form two coherent jointed strokes; no useful exact Lucide match.

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

        path('body',(4,18),[('L',(16,18)),('C',(36,27),(23,20),(30,23)),('C',(24,34),(34,33),(29,34)),('C',(12,32),(20,34),(16,34)),('C',(4,18),(6,29),(4,24))],True)
        path('antenna',(4,18),[('L',(4,8))]);join('antenna','body')
        self.add_polyline('hind',(16,18),(34,8),(44,40));join('hind','body')
        self.add_polyline('leg1',(12,32),(10,40),(4,40));join('leg1','body')
        self.add_polyline('leg2',(24,34),(26,40),(22,40));join('leg2','body')
