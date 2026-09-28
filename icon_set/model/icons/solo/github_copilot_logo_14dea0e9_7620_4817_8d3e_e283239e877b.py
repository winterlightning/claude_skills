"""A robot pilot mask with paired upper goggle lobes and two eye slits; merge the ear pieces into the face contour; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '14dea0e9-7620-4817-8d3e-e283239e877b'
SOURCE_PATH = 'pictographic-primitives/logos/github copilot logo_14dea0e9-7620-4817-8d3e-e283239e877b.svg'
AUTHOR = 'gpt-6'

class GithubCopilotLogo(Solo48):
    icon_id = 'github-copilot-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('github-copilot', 'copilot', 'ai', 'logo', 'brand', 'developer', 'assistant')

    def build(self):
        # Plan: A robot pilot mask with paired upper goggle lobes and two eye slits; merge the ear pieces into the face contour; extremes (6,6)-(42,42).
        # Construction reference: Lucide bot original and atomic-debug: rounded robot mask and paired eye slits.

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

        path('goggles',(24,6),[('L',(15,6)),('A',(15,22),8,8,False),('L',(24,22)),('L',(33,22)),('A',(33,6),8,8,False),('L',(24,6)),('L',(24,22))])
        path('face',(15,22),[('C',(6,30),(8,22),(6,24)),('C',(24,42),(6,38),(14,42)),('C',(42,30),(34,42),(42,38)),('C',(33,22),(42,24),(40,22))]);join('face','goggles')
        for i,x in enumerate((18,30)):line(f'eye-{i}',(x,31),(x,33))
