"""Modern Side View Armchair.

Left-facing armchair in profile, with high back on the right, short arm and splayed legs. Centerline extremes (6,6)-(42,42). Lucide rocking-chair informs the back/seat bend. Deliberate opposite facing preserves the source; omit doubled upholstery.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6056fc5-c043-545c-98cd-e53b7e9dbee5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/armchair modern_b6056fc5-c043-545c-98cd-e53b7e9dbee5.svg'
AUTHOR = 'gpt-6'

class ArmchairSideViewHighBack(Solo48):
    icon_id = 'armchair-side-view-high-back'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('modern', 'side', 'view', 'armchair')

    def build(self):
        # Symbol plan: Left-facing armchair in profile, with high back on the right, short arm and splayed legs. Centerline extremes (6,6)-(42,42). Lucide rocking-chair informs the back/seat bend. Deliberate opposite facing preserves the source; omit doubled upholstery.

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

        path('shell',(42,6),[('L',(36,24)),('C',(30,30),(35,28),(33,30)),('L',(14,30)),('L',(6,30))])
        for n,a,b in [('front',(14,30),(8,42)),('rear',(30,30),(36,42))]:line(n,a,b);join(n,'shell')
        path('arm',(14,30),[('L',(14,26)),('A',(18,22),4,4,True),('L',(24,22))]);join('arm','shell');join('arm','front')
