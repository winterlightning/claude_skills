"""Whole and Sliced Starfruit.

Long whole starfruit behind a five-point cross section. Centerline extremes (6,6)-(42,42). The foreground slice occludes the whole fruit at two shared silhouette endpoints. Preserve the source diagonal arrangement; omit fine radial slice veins. No useful local Lucide subject match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b16280dc-c5f8-496c-99d7-eaecc0358b57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/starfruit_b16280dc-c5f8-496c-99d7-eaecc0358b57.svg'
AUTHOR = 'gpt-6'

class StarfruitWithStarCrossSection(Solo48):
    icon_id = 'starfruit-with-star-cross-section'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('whole', 'and', 'sliced', 'starfruit')

    def build(self):
        # Symbol plan: Long whole starfruit behind a five-point cross section. Centerline extremes (6,6)-(42,42). The foreground slice occludes the whole fruit at two shared silhouette endpoints. Preserve the source diagonal arrangement; omit fine radial slice veins. No useful local Lucide subject match.

        def path(name, start, commands, closed=False):
            members=[]
            for i, command in enumerate(commands):
                kind,end,*args=command
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,start,end)
                elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
                members.append(member)
                start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def bilateral(name, start, right, closed=True):
            # One half owns geometry; mirror and reverse it about the shared axis.
            axis=24
            mirror=lambda p:(2*axis-p[0],p[1])
            segments=[]
            here=start
            for kind,end,*args in right:
                segments.append((kind,here,end,args));here=end
            left=[]
            for kind,begin,end,args in reversed(segments):
                if kind=='C': left.append((kind,mirror(begin),mirror(args[1]),mirror(args[0])))
                elif kind=='A': left.append((kind,mirror(begin),*args))
                else:left.append((kind,mirror(begin)))
            if closed:path(name,start,right+left,True)
            else:path(name,mirror(here),left+right)
        line=self.add_line
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)

        path('whole',(18,26),[('C',(10,30),(15,30),(12,30)),('C',(6,22),(7,28),(6,25)),('C',(24,6),(6,13),(16,6)),('C',(30,16),(30,6),(32,10))])
        self.add_polyline('star',(30,16),(34,25),(42,26),(36,33),(38,42),(30,38),(22,42),(24,33),(18,26),(27,25),closed=True)
        join('whole','star')
