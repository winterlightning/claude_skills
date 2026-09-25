"""Italic E bars meet a peaked A with an attached crossbar; shared A crossbar nodes preserve the slant; filled ribbons reduced to strokes; extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6a1a6a37-9632-482c-b527-8e1f3bc33bd9'
SOURCE_PATH = 'pictographic-primitives/logos/ea logo_6a1a6a37-9632-482c-b527-8e1f3bc33bd9.svg'
AUTHOR = 'gpt-6'

class EaLogo(Solo48):
    icon_id = 'ea-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('ea', 'electronic-arts', 'gaming', 'logo', 'brand', 'letters', 'publisher')

    def build(self):
        # Plan: Italic E bars meet a peaked A with an attached crossbar; shared A crossbar nodes preserve the slant; filled ribbons reduced to strokes; extremes (4,8)-(44,40).
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

        line('e-top',(10,8),(23,8))
        poly('e-lower',(26,24),(12,24),(4,40),(20,40))
        poly('a',(20,40),(26,24),(32,8),(38,24),(44,40))
        line('a-bar',(26,24),(38,24))
        join('a','a-bar');join('a','e-lower')
