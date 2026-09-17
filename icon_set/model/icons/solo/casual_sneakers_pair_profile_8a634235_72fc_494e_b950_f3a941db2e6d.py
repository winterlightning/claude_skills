"""Pair of Casual Sneakers.

Two stacked right-facing casual sneakers, each with raised heel, sloping upper and rounded toe. Centerline extremes (6,6)-(42,42). Repeat one shoe definition at y offsets 0 and 22. Lucide sport-shoe informs the unified outline. Remove doubled soles and tiny laces for pair clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a634235-72fc-494e-b950-f3a941db2e6d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/footwear/sneakers_8a634235-72fc-494e-b950-f3a941db2e6d.svg'
AUTHOR = 'gpt-6'

class CasualSneakersPairProfile(Solo48):
    icon_id = 'casual-sneakers-pair-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'footwear'
    aliases = ()
    keywords = ('pair', 'of', 'casual', 'sneakers')

    def build(self):
        # Symbol plan: Two stacked right-facing casual sneakers, each with raised heel, sloping upper and rounded toe. Centerline extremes (6,6)-(42,42). Repeat one shoe definition at y offsets 0 and 22. Lucide sport-shoe informs the unified outline. Remove doubled soles and tiny laces for pair clearance.

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

        for i,y in enumerate((6,28)):
            path(f'shoe-{i}',(6,y),[('C',(14,y+4),(8,y+5),(11,y+5)),('L',(20,y)),('L',(36,y+6)),('C',(42,y+10),(40,y+7),(42,y+7)),('A',(38,y+14),4,4,True),('L',(10,y+14)),('A',(6,y+10),4,4,True),('L',(6,y))],True)
