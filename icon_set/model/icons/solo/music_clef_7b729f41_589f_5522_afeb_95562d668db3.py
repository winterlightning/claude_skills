"""Restore a tall treble clef with narrow upper loop, rounded lower spiral and smoothly hooked stem.
Construction: No useful exact Lucide match; supplied reference controls the silhouette.
Omissions: None; source upper loop, central curl and bottom hook retained.
Keyshape VRECT_M: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7b729f41-589f-5522-afeb-95562d668db3'
SOURCE_PATH = 'pictographic-primitives/music/music clef_7b729f41-589f-5522-afeb-95562d668db3.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'music-clef'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'music'
    aliases = ()
    keywords = ('music', 'clef')
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

        path('clef',(18,38),[('C',(25,44),(18,42),(20,44)),('C',(30,38),(29,44),(31,42)),('L',(22,10)),('C',(27,4),(21,6),(23,4)),('C',(32,11),(31,4),(34,7)),('C',(20,23),(30,16),(24,20)),('C',(10,31),(14,26),(10,27)),('C',(23,36),(10,35),(17,36)),('C',(38,28),(33,36),(38,33)),('C',(27,22),(38,24),(33,22)),('C',(21,28),(22,22),(20,24))])
