'A tall rectangular hat crown rests on a straight brim extending beyond both sides. Beneath the brim, a plain oval-ended face descends smoothly with no additional facial details.\nPlan: Flat tall crown over circular lower face; the brim shares crown endpoints.\nConstruction reference: human_ref/user.svg circular face construction; Lucide hat-glasses for projecting straight brim.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '957499ed-8404-48f7-85f3-5f1cd00bc8c1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/avatar korean man_957499ed-8404-48f7-85f3-5f1cd00bc8c1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'head-wearing-a-tall-flat-topped-hat'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('head', 'wearing', 'a', 'tall', 'flat', 'topped', 'hat')

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

        poly('hat',(12,24),(12,4),(36,4),(36,24))
        poly('brim',(8,24),(12,24),(36,24),(40,24));join('hat','brim')
        path('face',(12,24),[('L',(12,32)),('A',(36,32),12,12,False),('L',(36,24))]);join('face','brim');join('face','hat')
