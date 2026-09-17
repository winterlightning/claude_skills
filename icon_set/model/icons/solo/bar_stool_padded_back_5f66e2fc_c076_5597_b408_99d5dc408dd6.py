"""High Bar Stool with Backrest.

Tall bar stool with padded back, narrow seat, long slanted legs and footrest. Centerline extremes (8,4)-(40,44). Lucide armchair-style shared supports inform contact topology; no close stool match. Keep one seat edge instead of a doubled cushion.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f66e2fc-c076-5597-b408-99d5dc408dd6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/chair bar_5f66e2fc-c076-5597-b408-99d5dc408dd6.svg'
AUTHOR = 'gpt-6'

class BarStoolPaddedBack(Solo48):
    icon_id = 'bar-stool-padded-back'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('high', 'bar', 'stool', 'with', 'backrest')

    def build(self):
        # Symbol plan: Tall bar stool with padded back, narrow seat, long slanted legs and footrest. Centerline extremes (8,4)-(40,44). Lucide armchair-style shared supports inform contact topology; no close stool match. Keep one seat edge instead of a doubled cushion.

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

        path('back',(16,4),[('L',(32,4)),('A',(36,8),4,4,True),('L',(36,12)),('L',(30,12)),('L',(18,12)),('L',(12,12)),('L',(12,8)),('A',(16,4),4,4,True)],True)
        for x in (18,30):line(f'support-{x}',(x,12),(x,22));join(f'support-{x}','back')
        self.add_polyline('seat',(8,22),(18,22),(30,22),(40,22))
        for x in (18,30):join(f'support-{x}','seat')
        for n,a,m,z in [('left',(18,22),(14,36),(12,44)),('right',(30,22),(34,36),(36,44))]:self.add_polyline(n,a,m,z);join(n,'seat')
        line('footrest',(14,36),(34,36));join('footrest','left');join('footrest','right')
