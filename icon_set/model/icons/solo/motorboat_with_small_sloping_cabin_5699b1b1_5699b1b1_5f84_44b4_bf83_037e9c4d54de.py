"""Level the hull and restore rising bow with smoothly rounded stern; cabin endpoints meet split gunwale.
Construction: No useful exact Lucide match; supplied reference controls the silhouette.
Omissions: None
Keyshape HRECT_M: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5699b1b1-5f84-44b4-bf83-037e9c4d54de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/motorboat_5699b1b1-5f84-44b4-bf83-037e9c4d54de.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'motorboat-with-small-sloping-cabin-5699b1b1'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('motorboat', 'with', 'small', 'sloping', 'cabin', '5699b1b1')
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

        path('hull',(4,24),[('L',(16,24)),('L',(34,24)),('L',(44,24)),('C',(30,38),(40,32),(37,38)),('L',(12,38)),('A',(8,34),4,4,True),('L',(4,24))],True)
        path('cabin',(16,24),[('L',(16,10)),('L',(26,10)),('A',(30,14),4,4,True),('L',(34,24))])
        join('hull','cabin')
