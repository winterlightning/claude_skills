"""A left-facing donkey with one upright ear, a long back and two visible blocky legs; omit hidden legs and facial marks; extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '888dfde6-30d5-43cc-b479-4f75c2f230cd'
SOURCE_PATH = 'pictographic-primitives/logos/election democrat_888dfde6-30d5-43cc-b479-4f75c2f230cd.svg'
AUTHOR = 'gpt-6'

class DemocraticDonkey(Solo48):
    icon_id = 'democratic-donkey'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('donkey', 'democrat', 'election', 'politics', 'party', 'vote', 'animal')

    def build(self):
        # Plan: A left-facing donkey with one upright ear, a long back and two visible blocky legs; omit hidden legs and facial marks; extremes (4,8)-(44,40).
        # Construction reference: No useful subject-specific Lucide match; construction follows the supplied brand render.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i, command in enumerate(commands):
                kind, end, *args=command
                part=f"{name}-{i}"
                if kind=='L': self.add_line(part,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(part,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C': self.add_bezier(part,here,(args[0],args[1],end))
                members.append(part); here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def c_ring(name):
            # Exact radius-20 points on the circle about (24,24).
            self.add_arc(name,(36,8),(36,40),radius_x=20,large_arc=True,sweep=False)
        poly=self.add_polyline
        line=self.add_line
        join=lambda a,b:self.relate('connect',a,b)

        def graph(edges):
            for name,a,b in edges: line(name,a,b)
            for i,(name,a,b) in enumerate(edges):
                for other,c,d in edges[:i]:
                    if {a,b}&{c,d}: join(name,other)

        path('animal',(4,20),[('L',(10,12)),('L',(10,8)),('L',(16,12)),('L',(18,20)),('L',(36,20)),('C',(40,28),(40,20),(40,24)),('L',(40,40)),('L',(32,40)),('L',(30,30)),('L',(22,30)),('L',(20,40)),('L',(12,40)),('L',(12,26)),('L',(4,30)),('L',(4,20))],True)
        line('tail',(40,28),(44,32));join('tail','animal')
