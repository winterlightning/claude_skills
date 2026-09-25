"""Restore the source crescent with smooth outer arc and open concave bowl; keep asymmetric pointed ends.
Construction: Lucide moon: one convex-to-concave closed contour.
Omissions: None
Keyshape VRECT_L: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '94cff4f3-9ead-4c16-b86f-2d0f51348b40'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crescent moon_94cff4f3-9ead-4c16-b86f-2d0f51348b40.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'open-crescent-moon-with-sharp-tips'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('open', 'crescent', 'moon', 'with', 'sharp', 'tips')
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

        path('moon',(30,4),[('A',(8,24),22,20,False),('A',(28,44),20,20,False),('C',(40,36),(34,44),(39,40)),('C',(20,20),(27,38),(20,32)),('C',(30,4),(20,14),(24,8))],True)
