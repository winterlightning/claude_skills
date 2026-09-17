"""Whole Fresh Cucumber.

Curved diagonal cucumber with a short stem and two surface marks. Centerline extremes (6,6)-(42,42). Preserve intentional organic asymmetry and the source diagonal. Lucide apple informs attached stem construction; no useful closer cucumber match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8351c9b9-d0a2-4f04-96ed-5a04322724b1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/cucumber whole_8351c9b9-d0a2-4f04-96ed-5a04322724b1.svg'
AUTHOR = 'gpt-6'

class CurvedCucumberStem(Solo48):
    icon_id = 'curved-cucumber-stem'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('whole', 'fresh', 'cucumber')

    def build(self):
        # Symbol plan: Curved diagonal cucumber with a short stem and two surface marks. Centerline extremes (6,6)-(42,42). Preserve intentional organic asymmetry and the source diagonal. Lucide apple informs attached stem construction; no useful closer cucumber match.

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

        path('cucumber',(36,12),[('C',(42,20),(40,12),(42,15)),('C',(32,35),(42,25),(37,31)),('C',(14,42),(26,39),(19,42)),('C',(6,34),(9,42),(6,39)),('C',(18,21),(6,27),(14,26)),('C',(28,12),(22,17),(23,12)),('C',(36,12),(31,12),(33,12))],True)
        line('stem',(36,12),(40,6));join('stem','cucumber')
        line('mark-0',(16,33),(18,33));line('mark-1',(29,22),(31,21))
