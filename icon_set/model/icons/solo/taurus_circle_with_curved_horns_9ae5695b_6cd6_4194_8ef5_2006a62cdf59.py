'A large plain circle supports a broad upward-opening horn curve. The horns meet the circle at its crown and sweep outward on both sides in a symmetrical arrangement.\nPlan: Taurus ring with symmetrical curved horns joining its crown. A single open horn contour and split circular outline.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ae5695b-6cd6-4194-8ef5-2006a62cdf59'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astrology taurus_9ae5695b-6cd6-4194-8ef5-2006a62cdf59.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'taurus-circle-with-curved-horns'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('taurus', 'circle', 'with', 'curved', 'horns')

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

        path('ring',(24,20),[('A',(36,32),12,12,True),('A',(24,44),12,12,True),('A',(12,32),12,12,True),('A',(24,20),12,12,True)],True)
        path('horns',(8,4),[('A',(24,20),16,16,False),('A',(40,4),16,16,False)])
        join('ring','horns')
