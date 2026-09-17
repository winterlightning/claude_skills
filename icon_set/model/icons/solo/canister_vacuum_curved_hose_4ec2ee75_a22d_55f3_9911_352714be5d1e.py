"""Canister Vacuum Cleaner.

Canister vacuum with low wheeled body, curved hose, diagonal wand and floor nozzle. Centerline extremes (4,8)-(44,40). No useful local Lucide vacuum match. Single-stroke hose preserves its curve; omit doubled wand and nozzle borders.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ec2ee75-a22d-55f3-9911-352714be5d1e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/cleaning vacuum_4ec2ee75-a22d-55f3-9911-352714be5d1e.svg'
AUTHOR = 'gpt-6'

class CanisterVacuumCurvedHose(Solo48):
    icon_id = 'canister-vacuum-curved-hose'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('canister', 'vacuum', 'cleaner')

    def build(self):
        # Symbol plan: Canister vacuum with low wheeled body, curved hose, diagonal wand and floor nozzle. Centerline extremes (4,8)-(44,40). No useful local Lucide vacuum match. Single-stroke hose preserves its curve; omit doubled wand and nozzle borders.

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

        path('body',(8,32),[('L',(8,28)),('C',(12,24),(8,25),(10,24)),('C',(22,36),(17,24),(22,30)),('C',(18,40),(22,39),(20,40)),('L',(8,40))])
        path('hose',(12,24),[('C',(12,18),(14,22),(14,20)),('C',(10,8),(7,14),(7,8)),('C',(22,8),(14,8),(18,8)),('L',(38,34))]);join('hose','body')
        self.add_polyline('nozzle',(30,40),(30,34),(38,34),(44,34),(44,40));join('nozzle','hose')
        oval('wheel',8,36,4,4);join('wheel','body')
