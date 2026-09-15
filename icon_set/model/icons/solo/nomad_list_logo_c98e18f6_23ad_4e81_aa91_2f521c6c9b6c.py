"""A large circle holds a folded map with three vertical panels and zigzag top and bottom edges.

Symbol plan: Three equal-width folded map panels; extremes (6,6)-(42,42).
Review notes: Lucide map informs shared folds and alternating edges. Removes the enclosing circle so all three map panels retain broad, readable spaces; preserves alternating fold directions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c98e18f6-23ad-4e81-aa91-2f521c6c9b6c'
SOURCE_PATH = 'pictographic-primitives/logos/nomad list logo_c98e18f6-23ad-4e81-aa91-2f521c6c9b6c.svg'
AUTHOR = 'gpt-6'

class NomadListLogo(Solo48):
    icon_id = 'nomad-list-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('nomad-list', 'travel', 'map', 'remote-work', 'logo', 'brand', 'circle')

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
        self.add_polyline('outline',(6,14),(18,6),(30,14),(42,6),(42,34),(30,42),(18,34),(6,42),closed=True)
        for name,a,b,edges in [('fold-left',(18,6),(18,34),['outline-1','outline-2','outline-6','outline-7']),('fold-right',(30,14),(30,42),['outline-2','outline-3','outline-5','outline-6'])]:
         self.add_line(name,a,b)
         for e in edges:self.relate('connect',name,e)
