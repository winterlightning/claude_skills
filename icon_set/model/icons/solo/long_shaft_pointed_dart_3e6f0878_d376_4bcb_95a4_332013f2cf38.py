"""Restore horizontal long shaft, broad curved point and bent tail. Point owns shared shaft attachment at (28,24).
Construction: No useful exact Lucide match; supplied reference controls the silhouette.
Omissions: None
Keyshape HRECT_M: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3e6f0878-d376-4bcb-95a4-332013f2cf38'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blowgun_3e6f0878-d376-4bcb-95a4-332013f2cf38.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'long-shaft-pointed-dart'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('long', 'shaft', 'pointed', 'dart')
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

        poly('shaft',(4,28),(4,24),(28,24))
        path('point',(28,24),[('L',(28,10)),('C',(44,24),(34,10),(40,18)),('C',(28,38),(40,30),(34,38)),('L',(28,24))],True)
        join('shaft','point')
