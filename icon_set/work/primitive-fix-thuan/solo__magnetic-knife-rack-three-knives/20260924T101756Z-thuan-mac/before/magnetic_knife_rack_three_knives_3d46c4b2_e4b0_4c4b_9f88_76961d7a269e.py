"""Magnetic Kitchen Knife Rack.

Three broad tapered knives mounted on a horizontal magnetic rail. Centerline extremes (4,8)-(44,40). No close local Lucide rack match. Three translated knife definitions keep spacing equal; simplify the rail and handles to single strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d46c4b2-e4b0-4c4b-9f88-76961d7a269e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/kitchen knife set_3d46c4b2-e4b0-4c4b-9f88-76961d7a269e.svg'
AUTHOR = 'gpt-6'

class MagneticKnifeRackThreeKnives(Solo48):
    icon_id = 'magnetic-knife-rack-three-knives'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('magnetic', 'kitchen', 'knife', 'rack')

    def build(self):
        # Symbol plan: Three broad tapered knives mounted on a horizontal magnetic rail. Centerline extremes (4,8)-(44,40). No close local Lucide rack match. Three translated knife definitions keep spacing equal; simplify the rail and handles to single strokes.

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

        self.add_polyline('rail',(4,20),(12,20),(20,20),(28,20),(36,20),(44,20))
        for i,x in enumerate((12,28,44)):
            line(f'handle-{i}',(x,8),(x,20));join(f'handle-{i}','rail')
            path(f'blade-{i}',(x,20),[('L',(x,28)),('L',(x-8,40)),('L',(x-8,20))]);join(f'blade-{i}','rail')
