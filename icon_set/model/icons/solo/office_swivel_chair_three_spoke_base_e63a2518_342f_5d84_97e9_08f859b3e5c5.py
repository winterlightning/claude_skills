"""Office Swivel Chair.

Office swivel chair with tall rounded back, shallow seat and three-spoke base. Centerline extremes (8,4)-(40,44). Lucide armchair informs rounded upholstery; a shared central support owns all base spokes. Omit tiny castor outlines.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e63a2518-342f-5d84-97e9-08f859b3e5c5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/chair_e63a2518-342f-5d84-97e9-08f859b3e5c5.svg'
AUTHOR = 'gpt-6'

class OfficeSwivelChairThreeSpokeBase(Solo48):
    icon_id = 'office-swivel-chair-three-spoke-base'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('office', 'swivel', 'chair')

    def build(self):
        # Symbol plan: Office swivel chair with tall rounded back, shallow seat and three-spoke base. Centerline extremes (8,4)-(40,44). Lucide armchair informs rounded upholstery; a shared central support owns all base spokes. Omit tiny castor outlines.

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

        path('back',(14,26),[('L',(14,14)),('A',(24,4),10,10,True),('A',(34,14),10,10,True),('L',(34,26))])
        self.add_polyline('seat',(8,26),(14,26),(24,26),(34,26),(40,26));join('back','seat')
        self.add_polyline('stem',(24,26),(24,36),(24,44));join('stem','seat')
        for n,x in [('left',10),('right',38)]:path(n,(24,36),[('C',(x,44),(x,39),(x,39))]);join(n,'stem')
        join('left','right')
