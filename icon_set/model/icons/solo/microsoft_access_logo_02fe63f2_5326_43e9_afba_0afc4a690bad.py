"""A tall slanted panel with a capital A overlaps the left side of a stacked database cylinder with three horizontal rings.

Symbol plan: Capital A beside a three-level cylinder; extremes (4,8)-(44,40).
Review notes: Drops the slanted letter-panel frame to preserve A and the database. Lucide database informs shared elliptical caps and split cylinder walls. Three levels remain; A is drawn with exact crossbar junctions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02fe63f2-5326-43e9-afba-0afc4a690bad'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft access logo_02fe63f2-5326-43e9-afba-0afc4a690bad.svg'
AUTHOR = 'gpt-6'

class MicrosoftAccessLogo(Solo48):
    icon_id = 'microsoft-access-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('microsoft-access', 'microsoft', 'database', 'office', 'logo', 'brand', 'letter-a')

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
        self.add_polyline('a',(4,40),(8,24),(12,8),(16,24),(20,40))
        self.add_line('a-bar',(8,24),(16,24))
        for member in ['a-1','a-2','a-3','a-4']:self.relate('connect','a-bar',member)
        self.add_arc('cap-top',(28,12),(44,12),radius_x=8,radius_y=4)
        self.add_arc('cap-bottom',(44,12),(28,12),radius_x=8,radius_y=4)
        self.add_contour('cap','cap-top','cap-bottom',closed=True)
        for side,x in [('left',28),('right',44)]:
            self.add_line(side+'-upper',(x,12),(x,25))
            self.add_line(side+'-lower',(x,25),(x,36))
            self.add_contour(side,side+'-upper',side+'-lower')
            for cap in ['cap-top','cap-bottom']:self.relate('connect',side+'-upper',cap)
        self.add_arc('middle',(28,25),(44,25),radius_x=8,radius_y=4,sweep=False)
        self.add_arc('bottom',(28,36),(44,36),radius_x=8,radius_y=4,sweep=False)
        for side in ['left','right']:
            for part in ['upper','lower']:self.relate('connect','middle',side+'-'+part)
            self.relate('connect','bottom',side+'-lower')
