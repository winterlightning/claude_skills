"""Full Length Standing Mirror.

Full-length standing mirror with splayed support legs, crossbar and diagonal glint. Centerline extremes (10,4)-(38,44). No close local Lucide mirror match. One diagonal glass reflection replaces two crowded marks; support geometry is mirrored.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5c9d70c-5585-5c5c-8cbf-3cae0cbe4655'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/dressing mirror_e5c9d70c-5585-5c5c-8cbf-3cae0cbe4655.svg'
AUTHOR = 'gpt-6'

class StandingMirrorSplayedLegs(Solo48):
    icon_id = 'standing-mirror-splayed-legs'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('full', 'length', 'standing', 'mirror')

    def build(self):
        # Symbol plan: Full-length standing mirror with splayed support legs, crossbar and diagonal glint. Centerline extremes (10,4)-(38,44). No close local Lucide mirror match. One diagonal glass reflection replaces two crowded marks; support geometry is mirrored.

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

        path('mirror',(16,4),[('L',(32,4)),('A',(36,8),4,4,True),('L',(36,28)),('A',(32,32),4,4,True),('L',(16,32)),('A',(12,28),4,4,True),('L',(12,8)),('A',(16,4),4,4,True)],True)
        line('glint',(21,22),(27,16))
        for n,a,m,z in [('left',(16,32),(12,40),(10,44)),('right',(32,32),(36,40),(38,44))]:self.add_polyline(n,a,m,z);join(n,'mirror')
        line('crossbar',(12,40),(36,40));join('crossbar','left');join('crossbar','right')
