"""Horizontal Measuring Ruler Tool.
Plan: Horizontal rounded ruler with centered graduation series. Centerline extremes (4,10)-(44,38).
Construction: Lucide ruler; rounded body and repeating edge graduations.
Reduction: Five ticks reduced to three: five ticks plus end clearance exceed the 40-unit centerline width.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e5cf0f4-16ef-55be-9abb-2b6fd8017da3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/ruler_8e5cf0f4-16ef-55be-9abb-2b6fd8017da3.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/ruler_8e5cf0f4-16ef-55be-9abb-2b6fd8017da3.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'horizontal-ruler-with-five-top-ticks'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('horizontal', 'measuring', 'ruler', 'tool')

    def build(self):
        left,right,top,bottom,r=4,44,10,38,4
        _run(self,'top',(8,top),(16,top),(24,top),(32,top),(40,top))
        self.add_arc('tr',(40,10),(44,14),radius_x=r)
        self.add_line('right',(44,14),(44,34))
        self.add_arc('br',(44,34),(40,38),radius_x=r)
        self.add_line('bottom',(40,38),(8,38))
        self.add_arc('bl',(8,38),(4,34),radius_x=r)
        self.add_line('left',(4,34),(4,14))
        self.add_arc('tl',(4,14),(8,10),radius_x=r)
        self.add_contour('outline',*[f'top-{i}' for i in range(1,5)],'tr','right','br','bottom','bl','left','tl',closed=True)
        for i in range(3):
         x=16+i*8
         self.add_line(f'tick-{i}',(x,10),(x,18))
         self.relate('connect',f'tick-{i}','outline')
