"""Replace angular vane with a flowing curved feather; preserve a broad notch and diagonal quill.
Construction: Lucide feather: diagonal shaft within coherent vane; source notch and organic silhouette retained.
Omissions: Upper fine notch omitted to keep clear shaft spacing.
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '93e084e6-277a-40cc-ae9f-d30ce99eb92e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/feather_93e084e6-277a-40cc-ae9f-d30ce99eb92e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'notched-feather'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('notched', 'feather')
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

        path('vane',(12,36),[('C',(28,10),(12,23),(19,15)),('C',(38,6),(32,8),(35,6)),('A',(42,10),4,4,True),('C',(38,22),(42,15),(40,20)),('L',(32,24)),('L',(37,28)),('C',(12,36),(27,34),(20,36))],True)
        poly('shaft',(6,42),(12,36),(24,24));join('shaft','vane')
