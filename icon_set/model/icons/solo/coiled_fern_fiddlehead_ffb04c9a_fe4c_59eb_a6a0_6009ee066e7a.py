"""Young Coiled Fern Sprout.

Fern fiddlehead with one coherent open spiral and a long stalk. Centerline extremes (8,4)-(40,44). No close Lucide match; use sprout coherent stem attachment. The spiral continues into the stem, and the second stalk edge is omitted to keep the coil legible.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffb04c9a-fe4c-59eb-a6a0-6009ee066e7a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/fiddlehead_ffb04c9a-fe4c-59eb-a6a0-6009ee066e7a.svg'
AUTHOR = 'gpt-6'

class CoiledFernFiddlehead(Solo48):
    icon_id = 'coiled-fern-fiddlehead'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('young', 'coiled', 'fern', 'sprout')

    def build(self):
        # Symbol plan: Fern fiddlehead with one coherent open spiral and a long stalk. Centerline extremes (8,4)-(40,44). No close Lucide match; use sprout coherent stem attachment. The spiral continues into the stem, and the second stalk edge is omitted to keep the coil legible.

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

        path('fern',(8,44),[('L',(8,20)),('C',(24,4),(8,11),(15,4)),('C',(40,20),(33,4),(40,11)),('C',(26,34),(40,28),(34,34)),('C',(17,24),(20,34),(17,30)),('C',(25,14),(17,18),(20,14)),('C',(31,22),(29,14),(31,17))])
