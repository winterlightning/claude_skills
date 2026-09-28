"""Modern High Bar Stool.

Tall modern stool with low rounded back, shallow seat and long splayed legs with footrest. Centerline extremes (10,4)-(38,44). Lucide armchair informs rounded upholstery; no useful exact stool match. Retain low back and seat as separate attached shapes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '036315b4-0ddb-506d-8b61-8592f2a1be3c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/chair bar_036315b4-0ddb-506d-8b61-8592f2a1be3c.svg'
AUTHOR = 'gpt-6'

class ModernBarStoolLowBack(Solo48):
    icon_id = 'modern-bar-stool-low-back'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('modern', 'high', 'bar', 'stool')

    def build(self):
        # Symbol plan: Tall modern stool with low rounded back, shallow seat and long splayed legs with footrest. Centerline extremes (10,4)-(38,44). Lucide armchair informs rounded upholstery; no useful exact stool match. Retain low back and seat as separate attached shapes.

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

        path('back',(14,14),[('L',(16,7)),('C',(20,4),(16,5),(18,4)),('L',(28,4)),('C',(32,7),(30,4),(32,5)),('L',(34,14))])
        path('seat',(14,14),[('L',(34,14)),('A',(38,18),4,4,True),('A',(34,22),4,4,True),('L',(32,22)),('L',(16,22)),('L',(14,22)),('A',(10,18),4,4,True),('A',(14,14),4,4,True)],True);join('back','seat')
        for n,a,m,z in [('left',(16,22),(12,36),(10,44)),('right',(32,22),(36,36),(38,44))]:self.add_polyline(n,a,m,z);join(n,'seat')
        line('footrest',(12,36),(36,36));join('footrest','left');join('footrest','right')
