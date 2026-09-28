"""Geothermal Heat Extraction.
Symbol plan: Geothermal diagram: down arrow over ground, two horizontal strata and two heat strokes.
Reference construction: wind.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'efeebfbe-5d0b-5c8b-b995-0fa4e7ad550c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/geothermal energy ground_efeebfbe-5d0b-5c8b-b995-0fa4e7ad550c.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'ground-line-with-downward-arrow-and-heat-curves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    categories = ("primitives", "ecology")
    aliases = ()
    keywords = ('geothermal', 'heat', 'ground', 'arrow', 'strata', 'energy', 'extraction', 'diagram')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def contour(n,*parts,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members) & set(parts)]
            self.add_contour(n,*parts,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
        def rect(n,x,y,w,h,r=0):
            if not r:
                poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2: arc(n+str(i),a,b,r)
                else: line(n+str(i),a,b)
            contour(n,*(n+str(i) for i in range(8)),closed=True)
        line('arrow',(24,6),(24,18))
        poly('arrowhead',(18,12),(24,18),(30,12))
        line('ground',(6,26),(42,26))
        for y in (34,42):
         line('strata-left'+str(y),(6,y),(14,y))
         line('strata-right'+str(y),(34,y),(42,y))
        arc('heat',(24,35),(24,42),5,5)
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
