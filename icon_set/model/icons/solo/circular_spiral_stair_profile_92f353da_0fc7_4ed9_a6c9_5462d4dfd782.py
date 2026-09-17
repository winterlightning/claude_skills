"""Circular Winding Stairs Symbol.

Winding stair silhouette with two broad rounded treads over a curved lower base and a vertical landing edge. Centerline extremes (4,8)-(44,40). No close Lucide match. Reduce four small source treads to two readable winding steps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92f353da-0fc7-4ed9-a6c9-5462d4dfd782'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/stairs circular_92f353da-0fc7-4ed9-a6c9-5462d4dfd782.svg'
AUTHOR = 'gpt-6'

class CircularSpiralStairProfile(Solo48):
    icon_id = 'circular-spiral-stair-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('circular', 'winding', 'stairs', 'symbol')

    def build(self):
        # Symbol plan: Winding stair silhouette with two broad rounded treads over a curved lower base and a vertical landing edge. Centerline extremes (4,8)-(44,40). No close Lucide match. Reduce four small source treads to two readable winding steps.

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

        path('stairs',(20,8),[('L',(44,8)),('L',(44,12)),('A',(40,16),4,4,True),('L',(36,16)),('L',(36,20)),('A',(32,24),4,4,True),('L',(28,24)),('L',(28,40)),('L',(20,40)),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,28)),('C',(20,16),(4,21),(12,16)),('L',(20,8))],True)
        self.add_polyline('landing',(20,16),(20,28),(20,40));join('landing','stairs')
        line('lower-step',(4,28),(20,28));join('lower-step','stairs');join('lower-step','landing')
