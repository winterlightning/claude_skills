"""A rounded square with a capital S overlaps the left side of a cluster of three overlapping circles.

Symbol plan: Large S beside a triangular cluster of three equal small rings. Extremes (4,8)-(44,40).
Review notes: Removes the letter tile and separates/reduces the circle cluster to preserve S plus three circles with legal spacing. Lucide circle informs the repeated rings and smooth S turns. The source cluster arrangement remains asymmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97a396e6-fc7c-4d50-a89d-8ba649e47acb'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft sharepoint logo_97a396e6-fc7c-4d50-a89d-8ba649e47acb.svg'
AUTHOR = 'gpt-6'

class MicrosoftSharepointLogo(Solo48):
    icon_id = 'microsoft-sharepoint-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('sharepoint', 'microsoft', 'collaboration', 'office', 'logo', 'brand', 'letter-s')

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
        self.add_arc('s-top',(20,16),(4,16),radius_x=8,sweep=False)
        self.add_arc('s-upper-turn',(4,16),(12,24),radius_x=8,sweep=False)
        self.add_arc('s-lower-turn',(12,24),(20,32),radius_x=8)
        self.add_arc('s-bottom',(20,32),(4,32),radius_x=8)
        self.add_contour('s','s-top','s-upper-turn','s-lower-turn','s-bottom')
        for name,x,y in [('top',33,11),('right',41,24),('bottom',33,37)]:ring(name,x,y,3)
