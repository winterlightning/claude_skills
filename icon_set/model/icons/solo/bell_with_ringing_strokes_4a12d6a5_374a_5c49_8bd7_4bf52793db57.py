"""Bell with Ringing Strokes.
Plan: Bell dome, flared sides and clapper share endpoints; paired ringing marks mirror x24. Ink (2,6)-(46,42).
Reference construction: bell-ring.
Reduction: Reduce the knob to a short stem.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4a12d6a5-374a-5c49-8bd7-4bf52793db57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/alarm bell ring_4a12d6a5-374a-5c49-8bd7-4bf52793db57.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'bell-with-ringing-strokes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('bell', 'with', 'ringing', 'strokes')
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

        for x,s in [(4,1),(44,-1)]:
            self.add_line(f'ring-upper-{x}',(x,14),(x+2*s,16))
            self.add_line(f'ring-lower-{x}',(x,24),(x+2*s,24))
