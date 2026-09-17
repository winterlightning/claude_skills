"""Football Cleat Shoe.

Right-facing football cleat with four evenly spaced studs and two lace strokes attached to the upper. Centerline extremes (4,10)-(44,38). Lucide sport-shoe informs directional upper and simple sole. Omit a doubled outsole to reserve space for the four studs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f717e85c-ca47-4860-9b6c-ee4105895c9c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/footwear/sneakers_f717e85c-ca47-4860-9b6c-ee4105895c9c.svg'
AUTHOR = 'gpt-6'

class FootballCleatWithFourStuds(Solo48):
    icon_id = 'football-cleat-with-four-studs'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'footwear'
    aliases = ()
    keywords = ('football', 'cleat', 'shoe')

    def build(self):
        # Symbol plan: Right-facing football cleat with four evenly spaced studs and two lace strokes attached to the upper. Centerline extremes (4,10)-(44,38). Lucide sport-shoe informs directional upper and simple sole. Omit a doubled outsole to reserve space for the four studs.

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

        path('shoe',(4,10),[('C',(12,14),(6,14),(9,15)),('L',(20,10)),('L',(26,14)),('L',(34,18)),('C',(44,28),(40,20),(44,22)),('L',(44,30)),('A',(40,34),4,4,True),('L',(36,34)),('L',(26,34)),('L',(16,34)),('L',(6,34)),('L',(4,34)),('L',(4,10))],True)
        for i,x in enumerate((6,16,26,36)):line(f'stud-{i}',(x,34),(x,38));join(f'stud-{i}','shoe')
        for i,(x,y) in enumerate(((26,14),(34,18))):line(f'lace-{i}',(x,y),(x-2,y+4));join(f'lace-{i}','shoe')
