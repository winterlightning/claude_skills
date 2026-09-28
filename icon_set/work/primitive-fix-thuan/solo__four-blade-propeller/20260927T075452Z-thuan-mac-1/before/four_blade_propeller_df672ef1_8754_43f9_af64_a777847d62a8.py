"""Four Bladed Fan Propeller.

Four curved fan blades rotating around a round center hub. Centerline extremes (6,6)-(42,42). Lucide fan informs one coherent fourfold blade silhouette. Rotate one blade definition through four quarter turns; simplify outlined hub to a round dot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df672ef1-8754-43f9-af64-a777847d62a8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/fanblades_df672ef1-8754-43f9-af64-a777847d62a8.svg'
AUTHOR = 'gpt-6'

class FourBladePropeller(Solo48):
    icon_id = 'four-blade-propeller'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('four', 'bladed', 'fan', 'propeller')

    def build(self):
        # Symbol plan: Four curved fan blades rotating around a round center hub. Centerline extremes (6,6)-(42,42). Lucide fan informs one coherent fourfold blade silhouette. Rotate one blade definition through four quarter turns; simplify outlined hub to a round dot.

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
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
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

        def turn(p,i):
            x,y=p
            for _ in range(i):x,y=48-y,x
            return x,y
        segment=[('C',(18,6),(13,10),(13,6)),('C',(32,10),(24,6),(32,6)),('L',(30,16))]
        commands=[]
        for i in range(4):
            for kind,end,*args in segment:commands.append((kind,turn(end,i),*[turn(p,i) for p in args]))
        path('blades',(16,18),commands,True)
        dot('hub',(24,24))
