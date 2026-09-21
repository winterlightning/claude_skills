"A sombrero has a tall tapering crown with a rounded top above a very broad brim. The brim's upper edge is straight, while its ends curve down into a shallow rounded base.\nPlan: Tall rounded sombrero crown and broad shallow curved brim.\nConstruction reference: Lucide hat-glasses original and atomic-debug: clear crown and projecting brim."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e5c1ae0-8307-49ef-8b54-53bcabd5374c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/sombrero_3e5c1ae0-8307-49ef-8b54-53bcabd5374c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tall-sombrero-with-wide-curved-brim'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('tall', 'sombrero', 'with', 'wide', 'curved', 'brim')

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

        path('crown',(14,28),[('L',(18,16)),('C',(30,16),(20,8),(28,8)),('L',(34,28))])
        path('brim',(4,28),[('L',(14,28)),('L',(34,28)),('L',(44,28)),('C',(34,38),(44,34),(40,38)),('L',(14,38)),('C',(4,28),(8,38),(4,34))],True);join('crown','brim')
