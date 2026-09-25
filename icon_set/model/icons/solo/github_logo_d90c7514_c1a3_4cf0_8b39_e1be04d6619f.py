"""A cat-like Octocat face with pointed ears and two eyes; remove the inner mask outline to preserve clear facial space; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd90c7514-c1a3-4cf0-8b39-e1be04d6619f'
SOURCE_PATH = 'pictographic-primitives/logos/github logo_d90c7514-c1a3-4cf0-8b39-e1be04d6619f.svg'
AUTHOR = 'gpt-6'

class GithubLogo(Solo48):
    icon_id = 'github-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('github', 'octocat', 'git', 'logo', 'brand', 'developer', 'code')

    def build(self):
        # Plan: A cat-like Octocat face with pointed ears and two eyes; remove the inner mask outline to preserve clear facial space; extremes (6,6)-(42,42).
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

        path('head',(8,6),[('L',(17,12)),('C',(31,12),(21,9),(27,9)),('L',(40,6)),('C',(39,19),(42,12),(42,15)),('C',(42,28),(41,22),(42,25)),('C',(24,42),(42,38),(34,42)),('C',(6,28),(14,42),(6,38)),('C',(9,19),(6,25),(7,22)),('C',(8,6),(6,15),(6,12))],True)
        for i,x in enumerate((17,31)):line(f'eye-{i}',(x,25),(x,30))
