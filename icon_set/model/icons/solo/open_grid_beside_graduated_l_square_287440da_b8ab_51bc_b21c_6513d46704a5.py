"""Grid with L-Square Ruler.
Plan: L-square beside a regular open grid. Centerline extremes (6,6)-(42,42).
Construction: Lucide ruler; sparse regular drafting marks.
Reduction: Grid reduced to two rows and two columns; graduations omitted because the leg cannot hold them at legal clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '287440da-b8ab-51bc-b21c-6513d46704a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/grid ruler_287440da-b8ab-51bc-b21c-6513d46704a5.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/grid ruler_287440da-b8ab-51bc-b21c-6513d46704a5.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'open-grid-beside-graduated-l-square'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('grid', 'with', 'l-square', 'ruler')

    def build(self):
        self.add_polyline('ruler',(34,6),(42,6),(42,42),(6,42),(6,34),(34,34),(34,6),closed=True)
        # Grid owns two equal rows and columns, sharing their actual intersections.
        for j,y in enumerate((6,18)):
         self.add_polyline(f'row-{j}',(6,y),(18,y),(26,y))
        for j,x in enumerate((6,18)):
         self.add_polyline(f'column-{j}',(x,6),(x,18),(x,26))
         for k in range(2):self.relate('connect',f'column-{j}',f'row-{k}')
