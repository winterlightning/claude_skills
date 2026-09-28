"""The wordmark lyft in heavy rounded lowercase letters, the y descending and the f and t joined.

Symbol plan: Stroke-built l, descending y, and connected f/t crossbar. Extremes (4,8)-(44,40).
Review notes: The thick outline wordmark reduces to readable letter strokes. The descending y and joined f/t preserve its identifying structure. Local Lucide circle supplies tangent quarter/half arcs; no useful local brand original was found.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eed67ed8-1756-4c90-9c2b-b367e0df28f6'
SOURCE_PATH = 'pictographic-primitives/logos/lyft logo_eed67ed8-1756-4c90-9c2b-b367e0df28f6.svg'
AUTHOR = 'gpt-6'

class LyftLogo(Solo48):
    icon_id = 'lyft-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('lyft', 'rideshare', 'taxi', 'wordmark', 'logo', 'brand', 'transport')

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
        self.add_line('l',(4,8),(4,32))
        self.add_line('y-left',(12,16),(12,24))
        self.add_arc('y-bowl',(12,24),(20,24),radius_x=4,sweep=False)
        self.add_contour('y-bowl-path','y-left','y-bowl')
        self.add_line('y-right-top',(20,16),(20,24))
        self.add_line('y-right-bottom',(20,24),(20,32))
        self.add_arc('y-descender',(20,32),(12,40),radius_x=8)
        self.add_contour('y-stem','y-right-top','y-right-bottom','y-descender')
        for member in ['y-right-top','y-right-bottom']:self.relate('connect','y-bowl',member)
        self.add_arc('f-cap',(30,18),(40,8),radius_x=10)
        for name,x in [('f',30),('t',40)]:
            self.add_line(name+'-upper',(x,18),(x,24))
            self.add_line(name+'-lower',(x,24),(x,32))
            self.add_contour(name+'-stem',name+'-upper',name+'-lower')
        self.relate('connect','f-cap','f-upper')
        self.add_arc('t-foot',(40,32),(44,36),radius_x=4,sweep=False)
        self.relate('connect','t-foot','t-lower')
        self.add_polyline('ft-bar',(30,24),(40,24),(44,24))
        for a in ['f-upper','f-lower']:self.relate('connect',a,'ft-bar-1')
        for a in ['t-upper','t-lower']:
            for b in ['ft-bar-1','ft-bar-2']:self.relate('connect',a,b)
