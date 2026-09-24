"""Restore a larger companion circle and a narrow diagonal capsule with smoothly rounded ends.
Construction: Lucide pill: tangent capsule shoulders; source descending orientation and companion circle retained.
Omissions: None
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aa3d7e5e-8e13-49ef-b4c2-760561eff3ec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/analogue logo_aa3d7e5e-8e13-49ef-b4c2-760561eff3ec.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'circle-and-diagonal-capsule-mark'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('circle', 'and', 'diagonal', 'capsule', 'mark')
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

        path('capsule',(23,6),[('C',(28,10),(25,6),(27,8)),('L',(40,30)),('C',(42,36),(41,32),(42,34)),('A',(36,42),6,6,True),('C',(31,38),(34,42),(32,40)),('L',(19,18)),('C',(17,12),(18,16),(17,14)),('A',(23,6),6,6,True)],True)
        circle('companion',12,36,6)
