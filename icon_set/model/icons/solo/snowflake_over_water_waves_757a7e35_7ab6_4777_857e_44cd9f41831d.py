"""Snowflake over water as one scene. Mirrored ray construction and repeated wave contours; smaller branches and one wave row omitted for native legibility. SQUARE spatial composition.
Redraw authorized 2026-09-22. Source interpretation follows visible composition.
Earlier draft, if any, is preserved. Shared parameters own repeated geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '757a7e35-7ab6-4777-857e-44cd9f41831d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_23/ice water_757a7e35-7ab6-4777-857e-44cd9f41831d.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'snowflake-over-water-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('Snowflake and Water Waves',)
    keywords = ('snowflake', 'over', 'water', 'waves')
    def build(self):
        def curve(n,start,*segments): self.add_bezier(n,start,*segments)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def join(*n): self.relate('connect',*n)
        for n,a,b in [('vertical',(24,6),(24,20)),('diagonal-left',(17,9),(31,17)),('diagonal-right',(17,17),(31,9))]:
            line(n+'-a',a,(24,13));line(n+'-b',(24,13),b)
        join('vertical-a','vertical-b','diagonal-left-a','diagonal-left-b','diagonal-right-a','diagonal-right-b')
        for i,y in enumerate((32,42)):
            curve('wave-'+str(i),(6,y),((9,y-2),(12,y-2),(15,y)),((18,y),(21,y),(24,y-2)),((27,y-4),(30,y-4),(33,y-2)),((36,y),(39,y),(42,y-2)))
