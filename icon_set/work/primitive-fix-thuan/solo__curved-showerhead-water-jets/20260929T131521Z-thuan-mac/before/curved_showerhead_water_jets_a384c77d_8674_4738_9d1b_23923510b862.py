"""Bathroom Shower Head.

Curved shower pipe supporting a diagonal head spraying three separate jets down-left. Centerline extremes (6,6)-(42,42). Lucide shower-head informs half-round spray face and discrete jets; retain long curved feed pipe from the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a384c77d-8674-4738-9d1b-23923510b862'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/light rain sensor_a384c77d-8674-4738-9d1b-23923510b862.svg'
AUTHOR = 'gpt-6'

class CurvedShowerheadWaterJets(Solo48):
    icon_id = 'curved-showerhead-water-jets'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('bathroom', 'shower', 'head')

    def build(self):
        # Symbol plan: Curved shower pipe supporting a diagonal head spraying three separate jets down-left. Centerline extremes (6,6)-(42,42). Lucide shower-head informs half-round spray face and discrete jets; retain long curved feed pipe from the source.

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

        path('pipe',(42,42),[('L',(42,18)),('C',(30,6),(42,10),(38,6)),('C',(22,8),(26,6),(24,6))])
        path('head',(12,12),[('C',(22,8),(15,9),(18,8)),('C',(30,12),(25,8),(28,9)),('C',(30,30),(35,17),(35,25)),('L',(12,12))],True);join('pipe','head')
        for i,(a,b) in enumerate([((12,27),(6,33)),((18,33),(10,41)),((24,39),(21,42))]):line(f'jet-{i}',a,b)
