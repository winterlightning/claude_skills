"""A division sign with two equal rings and a long central bar; collapse the outlined bar to one stroke; extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '545cc9fd-afe2-4019-9c23-25c662f3e84b'
SOURCE_PATH = 'pictographic-primitives/logos/feathub logo_545cc9fd-afe2-4019-9c23-25c662f3e84b.svg'
AUTHOR = 'gpt-6'

class FeathubLogo(Solo48):
    icon_id = 'feathub-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('feathub', 'divide', 'division', 'logo', 'brand', 'feedback', 'math')

    def build(self):
        # Plan: A division sign with two equal rings and a long central bar; collapse the outlined bar to one stroke; extremes (4,8)-(44,40).
        # Construction reference: Lucide divide original and atomic-debug: centered repeats and one horizontal bar.

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

        line('bar',(4,24),(44,24))
        for i,y in enumerate((11,37)):circle(f'ring-{i}',24,y,3)
