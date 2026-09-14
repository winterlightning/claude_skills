"""Nested code brackets have mirrored outer half-hexagons. The slash is omitted to keep all four brackets readable; no useful exact Lucide construction match.
Fresh SOLO48 geometry. Keyshape HRECT_L; bounds are resolved from the live contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ea5186c-163b-532a-b4f6-46d231d39d76'
SOURCE_PATH = 'pictographic-primitives/programing/amazon api gateway code_1ea5186c-163b-532a-b4f6-46d231d39d76.svg'
AUTHOR = 'gpt-6'

class ApiCodeBrackets(Solo48):
    icon_id = 'api-code-brackets'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/programming"
    aliases = ()
    keywords = ('api', 'code', 'brackets', 'gateway', 'developer', 'programming', 'endpoint', 'html')

    def build(self) -> None:
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def oval(name, x, y, rx, ry):
            self.add_arc(name+'-top', (x-rx,y), (x+rx,y), radius_x=rx,radius_y=ry)
            self.add_arc(name+'-bottom', (x+rx,y), (x-rx,y), radius_x=rx,radius_y=ry)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        for side, mirror in (('left',False),('right',True)):
            def point(x,y): return (48-x if mirror else x,y)
            self.add_polyline(side+'-outer',*[point(x,y) for x,y in ((10,8),(4,14),(4,34),(10,40))])
            self.add_polyline(side+'-code',*[point(x,y) for x,y in ((20,18),(14,24),(20,30))])
