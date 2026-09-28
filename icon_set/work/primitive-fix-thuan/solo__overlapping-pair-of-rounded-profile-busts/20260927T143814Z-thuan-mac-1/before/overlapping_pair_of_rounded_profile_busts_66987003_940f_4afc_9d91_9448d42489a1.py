"""Broaden the foreground shoulders and stagger rear body height to restore overlap and foreground hierarchy. Circular heads keep exact 4-unit detached gap.
Construction: human_ref/user.svg: circular heads, broad rounded shoulders; Lucide users: overlapping foreground hierarchy.
Omissions: No defining features omitted.
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '66987003-940f-4afc-9d91-9448d42489a1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/cousin_66987003-940f-4afc-9d91-9448d42489a1.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'overlapping-pair-of-rounded-profile-busts'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('overlapping', 'pair', 'of', 'rounded', 'profile', 'busts')
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

        circle('front-head',14,12,6);circle('rear-head',34,13,5)
        path('front-body',(6,42),[('L',(6,34)),('A',(14,26),8,8,True),('L',(18,26)),('A',(26,34),8,8,True),('L',(26,38)),('L',(26,42)),('L',(6,42))],True)
        path('rear-body',(26,34),[('C',(34,26),(26,29),(29,26)),('A',(42,34),8,8,True),('L',(42,38)),('L',(26,38))])
        join('front-body','rear-body')
