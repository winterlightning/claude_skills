"""Three rounded diamond slabs stack on top of each other, the top one fully visible and the lower two showing only their front edges.

Symbol plan: Three stacked diamonds with a common axis and step10; extremes (6,6)-(42,42).
Review notes: Lucide layers informs a closed top diamond and two open lower fronts. Keeps all three layers, with ten-unit vertical spacing and rounded stroke joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e702f221-342a-4aad-b017-71faeb9a7f59'
SOURCE_PATH = 'pictographic-primitives/logos/openlayers logo_e702f221-342a-4aad-b017-71faeb9a7f59.svg'
AUTHOR = 'gpt-6'

class OpenlayersLogo(Solo48):
    icon_id = 'openlayers-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('openlayers', 'maps', 'layers', 'stack', 'logo', 'brand', 'gis')

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
        self.add_polyline('top',(24,6),(42,14),(24,22),(6,14),closed=True)
        for i,y in enumerate((24,34)):self.add_polyline(f'layer-{i}',(6,y),(24,y+8),(42,y))
