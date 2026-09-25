"""A fan of curved pages sweeps out from a point at the lower right, the pages spreading to the left and up like an opening book.

Symbol plan: Fan of curved pages with common lower-right binding node (34,44). Extremes (8,4)-(40,44).
Review notes: Preserves the curved page fan and shared binding point, reduced to two broad pages to keep the folds readable at 48 pixels. No local Lucide construction matched this curved fan closely.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b8e0c50-e69b-4665-982c-a203159ee378'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft academic logo_7b8e0c50-e69b-4665-982c-a203159ee378.svg'
AUTHOR = 'gpt-6'

class MicrosoftAcademicLogo(Solo48):
    icon_id = 'microsoft-academic-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('microsoft-academic', 'microsoft', 'research', 'book', 'logo', 'brand', 'papers')

    def build(self):

        def chain(name, *points):
            for i,(start,end) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{i}',start,end)
        def ring(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def rounded(name, left, top, right, bottom, r):
            points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for i,start in enumerate(points):
                end=points[(i+1)%8]; ident=f'{name}-{i}'
                if start==end: continue
                if i%2:self.add_arc(ident,start,end,radius_x=r)
                else:self.add_line(ident,start,end)
                members.append(ident)
            self.add_contour(name,*members,closed=True)
        root=(34,44)
        self.add_bezier('front-edge',(30,4),((38,9),(40,16),(40,26)))
        chain('perimeter',(40,26),root,(8,36),(14,26),(8,20),(30,4))
        self.add_contour('outline','front-edge',*[f'perimeter-{i}' for i in range(1,6)],closed=True)
        self.add_bezier('page',(8,20),((24,20),(32,34),root))
        for member in ['perimeter-1','perimeter-2','perimeter-4','perimeter-5']:self.relate('connect','page',member)
