"""Restore a broad rounded cargo body with a level base and full-sized equal wheels.
Construction: Lucide caravan: rounded cargo roof and separate circular wheels.
Omissions: None
Keyshape HRECT_L: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4e3da0fe-15bd-4ec1-862f-98dbf14eed50'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/transporter 7_4e3da0fe-15bd-4ec1-862f-98dbf14eed50.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'cargo-trailer'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cargo', 'trailer')
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

        path('body',(7,35),[('L',(4,35)),('L',(4,20)),('A',(16,8),12,12,True),('L',(32,8)),('A',(44,20),12,12,True),('L',(44,35)),('L',(41,35))])
        for x in (12,36):circle(f'wheel-{x}',x,35,5);join('body',f'wheel-{x}')
        line('sill',(17,35),(31,35));join('sill','wheel-12');join('sill','wheel-36')
