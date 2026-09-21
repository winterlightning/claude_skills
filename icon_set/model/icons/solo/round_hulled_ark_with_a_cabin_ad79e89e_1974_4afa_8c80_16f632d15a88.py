"A deep curved boat hull has pointed ends and a low rounded bottom. A small rectangular cabin with a shallow trapezoidal roof rises centrally behind the hull's upper edge.\nPlan: Deep round hull with cabin and pitched low roof; shared hull top at cabin corners.\nConstruction reference: Lucide sailboat original and atomic-debug: low connected boat structure."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad79e89e-1974-4afa-8c80-16f632d15a88'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/ark_ad79e89e-1974-4afa-8c80-16f632d15a88.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-hulled-ark-with-a-cabin'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('round', 'hulled', 'ark', 'with', 'a', 'cabin')

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

        path('hull',(4,24),[('L',(14,24)),('L',(34,24)),('L',(44,24)),('C',(24,40),(44,36),(34,40)),('C',(4,24),(14,40),(4,36))],True)
        poly('cabin',(14,24),(14,8),(34,8),(34,24));join('cabin','hull')
