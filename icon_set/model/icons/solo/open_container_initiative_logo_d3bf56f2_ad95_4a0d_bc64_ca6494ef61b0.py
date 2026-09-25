"""A square frame holds a squared letter C beside a lowercase i with a square dot, drawn as thick outlines.

Symbol plan: Square badge with squared C and lowercase i; extremes (6,6)-(42,42).
Review notes: Retains the square, C and i; reduces their outlined forms to single strokes and the square dot to a round dot. Earlier Lucide square informs the frame.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3bf56f2-ad95-4a0d-bc64-ca6494ef61b0'
SOURCE_PATH = 'pictographic-primitives/logos/open container intiative logo_d3bf56f2-ad95-4a0d-bc64-ca6494ef61b0.svg'
AUTHOR = 'gpt-6'

class OpenContainerInitiativeLogo(Solo48):
    icon_id = 'open-container-initiative-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('open-container-initiative', 'oci', 'containers', 'logo', 'brand', 'standard', 'ci')

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
        self.add_polyline('frame',(6,6),(42,6),(42,42),(6,42),closed=True)
        self.add_polyline('c',(24,15),(15,15),(15,33),(24,33))
        self.add_dot('i-dot',(33,15));self.add_line('i-stem',(33,24),(33,33))
