'Three bent line arrows follow one another around an open triangular center. Each shaft curves around one corner before ending in an open arrowhead, with clear gaps between the separate arrows.\nPlan: Three open round-ended arrows cycle around triangle; no solid arrowheads.\nConstruction reference: Lucide recycle original and atomic-debug: three separated cyclic arrow paths.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eba86955-13f5-4b0a-a78e-55e6a9fb7a6a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/recycling symbol_eba86955-13f5-4b0a-a78e-55e6a9fb7a6a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-open-recycling-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('three', 'open', 'recycling', 'arrows')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)

        path('top',(14,14),[('L',(19,6)),('L',(25,6)),('L',(34,18))]);poly('head-top',(24,16),(34,18),(38,8));join('top','head-top')
        path('right',(42,28),[('L',(42,38)),('A',(38,42),4,4,True),('L',(26,42))]);poly('head-right',(32,34),(26,42),(34,42));join('right','head-right')
        path('left',(16,42),[('L',(10,42)),('A',(6,38),4,4,True),('L',(6,24))]);poly('head-left',(6,32),(6,24),(14,28));join('left','head-left')
