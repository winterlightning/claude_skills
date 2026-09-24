"""Rebuild two smooth diagonal oblong rings; shared crossing nodes make overlapping contours intentional.
Construction: Lucide link: rounded diagonal ring ends; closed overlap retained from source.
Omissions: None
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f3554d59-4ee9-5ba8-bc14-5b1324691503'
SOURCE_PATH = 'pictographic-primitives/interface-essential/attachment_f3554d59-4ee9-5ba8-bc14-5b1324691503.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'overlapping-chain-rings'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('overlapping', 'chain', 'rings')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*pts,closed=False):self.add_polyline(name,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)

        a=(17,17);b=(31,31)
        path('lower',a,[('C',(27,21),(21,17),(24,18)),('C',b,(29,24),(31,27)),('L',(23,39)),('C',(16,42),(21,41),(19,42)),('C',(6,32),(10,42),(6,38)),('C',(9,25),(6,29),(7,27)),('L',a)],True)
        path('upper',a,[('L',(25,9)),('C',(32,6),(27,7),(29,6)),('C',(42,16),(38,6),(42,10)),('C',(39,23),(42,19),(41,21)),('L',b),('C',(21,27),(27,31),(24,30)),('C',a,(19,24),(17,21))],True)
        join('upper','lower')
