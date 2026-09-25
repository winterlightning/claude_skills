"""Modern Lounge Chair Profile.

Right-facing lounge chair with sloping back, long seat, short curved arm and two angled legs. Centerline extremes (6,6)-(42,42). Lucide rocking-chair informs a coherent back/seat bend. Simplify doubled shell thickness to one stroke; preserve the arm.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6d7267b-b3b5-5e0b-9e6e-aa9a3007719e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/chair_a6d7267b-b3b5-5e0b-9e6e-aa9a3007719e.svg'
AUTHOR = 'gpt-6'

class LoungeChairSideProfile(Solo48):
    icon_id = 'lounge-chair-side-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('modern', 'lounge', 'chair', 'profile')

    def build(self):
        # Symbol plan: Right-facing lounge chair with sloping back, long seat, short curved arm and two angled legs. Centerline extremes (6,6)-(42,42). Lucide rocking-chair informs a coherent back/seat bend. Simplify doubled shell thickness to one stroke; preserve the arm.

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

        path('shell',(6,6),[('L',(14,24)),('C',(20,30),(15,28),(17,30)),('L',(34,30)),('L',(38,30)),('L',(42,30))])
        for n,a,b in [('rear',(20,30),(14,42)),('front',(34,30),(40,42))]:line(n,a,b);join(n,'shell')
        path('arm',(27,20),[('L',(34,20)),('A',(38,24),4,4,True),('L',(38,30))]);join('arm','shell')
