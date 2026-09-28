"""Bell with Sound Arcs.
Plan: Bell dome, flared sides and clapper share endpoints; paired ringing marks mirror x24. Ink (2,6)-(46,42).
Reference construction: bell-ring.
Reduction: Reduce the knob to a short stem. Keep one sound arc on each side instead of two nested arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a6f84a63-2813-514f-b20f-b689003dbecf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/alarm bell ring_a6f84a63-2813-514f-b20f-b689003dbecf.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'bell-with-sound-arcs'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('bell', 'with', 'sound', 'arcs')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_arc('dome-left',(16,20),(24,12),radius_x=8)
        self.add_arc('dome-right',(24,12),(32,20),radius_x=8)
        self.add_bezier('right-flare',(32,20),((32,24),(33,26),(36,30)))
        self.add_line('rim-right',(36,30),(34,30))
        self.add_line('rim',(34,30),(14,30))
        self.add_line('rim-left',(14,30),(12,30))
        self.add_bezier('left-flare',(12,30),((15,26),(16,24),(16,20)))
        self.add_contour('bell','dome-left','dome-right','right-flare','rim-right','rim','rim-left','left-flare',closed=True)
        self.add_line('knob',(24,8),(24,12))
        self.relate('connect','knob','bell')
        self.add_arc('clapper',(14,30),(34,30),radius_x=10,sweep=False)
        self.relate('connect','clapper','bell')

        self.add_arc('ring-left',(4,22),(10,8),radius_x=6,radius_y=14)
        self.add_arc('ring-right',(38,8),(44,22),radius_x=6,radius_y=14)
