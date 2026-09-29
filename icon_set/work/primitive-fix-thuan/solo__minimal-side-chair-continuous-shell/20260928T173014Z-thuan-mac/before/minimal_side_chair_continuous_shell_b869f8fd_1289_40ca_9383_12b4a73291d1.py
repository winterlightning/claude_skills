"""Modern Minimalist Side Chair.

Right-facing minimalist chair with one rounded continuous shell and two slim angled legs. Centerline extremes (6,6)-(42,42). Lucide rocking-chair informs the continuous bend; source shell retains its thickness and rounded front lip. Omit the small crossbar.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b869f8fd-1289-40ca-9383-12b4a73291d1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/chair modern_b869f8fd-1289-40ca-9383-12b4a73291d1.svg'
AUTHOR = 'gpt-6'

class MinimalSideChairContinuousShell(Solo48):
    icon_id = 'minimal-side-chair-continuous-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('modern', 'minimalist', 'side', 'chair')

    def build(self):
        # Symbol plan: Right-facing minimalist chair with one rounded continuous shell and two slim angled legs. Centerline extremes (6,6)-(42,42). Lucide rocking-chair informs the continuous bend; source shell retains its thickness and rounded front lip. Omit the small crossbar.

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

        path('shell',(10,6),[('C',(18,10),(15,6),(18,6)),('L',(20,20)),('C',(28,26),(21,24),(24,26)),('L',(38,26)),('A',(42,30),4,4,True),('A',(38,34),4,4,True),('L',(36,34)),('L',(20,34)),('C',(12,26),(15,34),(12,31)),('L',(6,10)),('C',(10,6),(6,7),(7,6))],True)
        for n,a,b in [('rear',(20,34),(16,42)),('front',(36,34),(40,42))]:line(n,a,b);join(n,'shell')
