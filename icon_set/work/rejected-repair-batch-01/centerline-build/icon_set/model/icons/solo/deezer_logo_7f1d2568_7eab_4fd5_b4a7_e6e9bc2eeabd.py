"""Seven equal short strokes form a four-column stepped equalizer; repeated length 4 and step 12; capsule outlines reduced to strokes; extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7f1d2568-7eab-4fd5-b4a7-e6e9bc2eeabd'
SOURCE_PATH = 'pictographic-primitives/logos/deezer music logo_7f1d2568-7eab-4fd5-b4a7-e6e9bc2eeabd.svg'
AUTHOR = 'gpt-6'

class DeezerLogo(Solo48):
    icon_id = 'deezer-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('deezer', 'music', 'streaming', 'logo', 'brand', 'equalizer', 'audio')

    def build(self):
        # Plan: Seven equal short strokes form a four-column stepped equalizer; repeated length 4 and step 12; capsule outlines reduced to strokes; extremes (4,8)-(44,40).
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

        for row,columns in ((0,(3,)),(1,(2,3)),(2,(0,1,2,3))):
            for col in columns:
                x=4+12*col; y=8+16*row
                line(f'bar-{row}-{col}',(x,y),(x+4,y))
