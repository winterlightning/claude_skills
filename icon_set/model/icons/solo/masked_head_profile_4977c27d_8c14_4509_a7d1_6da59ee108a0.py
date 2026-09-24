"""Round skull, mask bottom and neck transitions; restore two sides of the mask strap as one loop.
Construction: Human reference user.svg: smooth head and shoulder vocabulary; continuous-neck profile from source.
Omissions: Fine mask folds omitted.
Keyshape VRECT_L: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4977c27d-8c14-4509-a7d1-6da59ee108a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/head side mask_4977c27d-8c14-4509-a7d1-6da59ee108a0.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'masked-head-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('masked', 'head', 'profile')
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

        path('head',(20,44),[('C',(17,36),(20,40),(19,38)),('L',(10,32)),('L',(8,24)),('L',(13,18)),('C',(26,4),(13,10),(18,4)),('C',(40,18),(34,4),(40,10)),('C',(35,32),(40,24),(37,28)),('C',(34,44),(33,36),(33,39))])
        path('mask',(8,24),[('L',(21,24)),('A',(25,28),4,4,True),('L',(25,32)),('A',(21,36),4,4,True),('L',(17,36))])
        path('strap',(21,24),[('L',(30,19)),('C',(29,25),(31,18),(31,22)),('L',(25,32))])
        join('head','mask');join('mask','strap')
