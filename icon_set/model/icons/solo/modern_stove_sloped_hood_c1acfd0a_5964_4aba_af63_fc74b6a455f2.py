"""Modern Kitchen Cooking Stove.

Freestanding stove with broad sloped upper panel, three vertical front panels and projecting base. Centerline extremes (4,8)-(44,40). No close local Lucide match; preserve the unusual supplied silhouette with smooth corners. Omit no defining panel.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1acfd0a-5964-4aba-af63-fc74b6a455f2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/stove_c1acfd0a-5964-4aba-af63-fc74b6a455f2.svg'
AUTHOR = 'gpt-6'

class ModernStoveSlopedHood(Solo48):
    icon_id = 'modern-stove-sloped-hood'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('modern', 'kitchen', 'cooking', 'stove')

    def build(self):
        # Symbol plan: Freestanding stove with broad sloped upper panel, three vertical front panels and projecting base. Centerline extremes (4,8)-(44,40). No close local Lucide match; preserve the unusual supplied silhouette with smooth corners. Omit no defining panel.

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

        path('stove',(12,8),[('L',(36,8)),('C',(40,12),(39,8),(40,9)),('L',(44,22)),('L',(44,28)),('A',(40,32),4,4,True),('L',(40,36)),('A',(36,40),4,4,True),('L',(12,40)),('A',(8,36),4,4,True),('L',(8,32)),('A',(4,28),4,4,True),('L',(4,22)),('L',(8,12)),('C',(12,8),(8,9),(9,8))],True)
        self.add_polyline('upper-panel',(4,22),(16,22),(32,22),(44,22));self.add_polyline('base',(8,32),(16,32),(32,32),(40,32))
        for n in ('upper-panel','base'):join(n,'stove')
        for x in (16,32):line(f'front-{x}',(x,22),(x,32));join(f'front-{x}','upper-panel');join(f'front-{x}','base')
