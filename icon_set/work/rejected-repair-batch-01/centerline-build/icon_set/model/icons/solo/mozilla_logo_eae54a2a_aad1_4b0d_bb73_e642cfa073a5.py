"""A square frame holds a heavy slab-serif lowercase m.

Symbol plan: Framed lowercase m with two equal arches; extremes (6,6)-(42,42).
Review notes: Keeps square and lowercase m, removes slab-serif outlines to enlarge counters. Lucide square informs the enclosure; arches share radius4 and an exact center-stem junction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eae54a2a-aad1-4b0d-bb73-e642cfa073a5'
SOURCE_PATH = 'pictographic-primitives/logos/mozilla logo_eae54a2a-aad1-4b0d-bb73-e642cfa073a5.svg'
AUTHOR = 'gpt-6'

class MozillaLogo(Solo48):
    icon_id = 'mozilla-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('mozilla', 'firefox', 'letter-m', 'logo', 'brand', 'open-source', 'web')

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
        self.add_line('left',(16,33),(16,24))
        self.add_arc('arch-left',(16,24),(24,24),radius_x=4)
        self.add_arc('arch-right',(24,24),(32,24),radius_x=4)
        self.add_line('middle',(24,24),(24,33));self.add_line('right',(32,24),(32,33))
        self.add_contour('m','left','arch-left','arch-right','right')
        for a in ['arch-left','arch-right']:self.relate('connect','middle',a)
