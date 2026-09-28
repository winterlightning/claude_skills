"""A large rounded location pin outline holds a smaller pin with a dot at its centre.

Symbol plan: Nested pin silhouettes mirrored about x24; outer extremes (8,4)-(40,44).
Review notes: Lucide map-pin informs rounded caps and converging tips. The central dot is removed to preserve clear space between the two identifying nested pins; paired geometry remains mirrored.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc4f4e2d-9360-439d-976c-a2da5e0ae8c4'
SOURCE_PATH = 'pictographic-primitives/logos/mapbox logo_dc4f4e2d-9360-439d-976c-a2da5e0ae8c4.svg'
AUTHOR = 'gpt-6'

class MapboxLogo(Solo48):
    icon_id = 'mapbox-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('mapbox', 'maps', 'location', 'pin', 'logo', 'brand', 'navigation')

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
        self.add_arc('outer-cap',(8,20),(40,20),radius_x=16)
        self.add_arc('outer-right',(40,20),(36,32),radius_x=20)
        chain('outer-tip',(36,32),(24,44),(12,32))
        self.add_arc('outer-left',(12,32),(8,20),radius_x=20)
        self.add_contour('outer','outer-cap','outer-right','outer-tip-1','outer-tip-2','outer-left',closed=True)
        self.add_arc('inner-cap',(17,20),(31,20),radius_x=7)
        self.add_arc('inner-right',(31,20),(29,26),radius_x=10)
        chain('inner-tip',(29,26),(24,32),(19,26))
        self.add_arc('inner-left',(19,26),(17,20),radius_x=10)
        self.add_contour('inner','inner-cap','inner-right','inner-tip-1','inner-tip-2','inner-left',closed=True)
