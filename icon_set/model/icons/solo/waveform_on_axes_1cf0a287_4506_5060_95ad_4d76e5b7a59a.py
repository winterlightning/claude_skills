"""An upward-pointing vertical axis meets a horizontal baseline. A smooth wave dips below the baseline on the left, rises to a rounded crest on the right, and curves downward toward the baseline.

SQUARE visible bounds (4,4)-(44,44); full upward arrow, horizontal axis, smooth trough and crest. No useful exact Lucide match. Left trough and right crest retain their directional arrangement.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cf0a287-4506-5060-95ad-4d76e5b7a59a'
SOURCE_PATH = 'pictographic-primitives/science/graph_1cf0a287-4506-5060-95ad-4d76e5b7a59a.svg'
AUTHOR = 'gpt-6'

class WaveformOnAxes(Solo48):
    icon_id = 'waveform-on-axes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('graph', 'waveform', 'axis', 'curve', 'plot', 'science')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_polyline('axis-y',(14,42),(14,26),(14,6))
        self.add_polyline('arrow',(6,14),(14,6),(22,14))
        self.relate('connect','arrow','axis-y')
        self.add_line('axis-x',(14,26),(30,26))
        self.add_line('axis-x-right',(30,26),(42,26))
        self.relate('connect','axis-x','axis-y');self.relate('connect','axis-x','axis-x-right')
        self.add_arc('trough-left',(22,30),(26,38),radius_x=4,radius_y=8,sweep=False)
        self.add_arc('trough-rise',(26,38),(30,26),radius_x=4,radius_y=12,sweep=False)
        self.add_arc('crest-rise',(30,26),(36,14),radius_x=6,radius_y=12)
        self.add_arc('crest-fall',(36,14),(42,26),radius_x=6,radius_y=12)
        self.add_contour('wave','trough-left','trough-rise','crest-rise','crest-fall')
        self.relate('connect','wave','axis-x');self.relate('connect','wave','axis-x-right')
