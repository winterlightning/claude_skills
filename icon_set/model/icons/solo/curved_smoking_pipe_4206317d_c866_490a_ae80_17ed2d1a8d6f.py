'A smoking pipe has a deep rounded bowl on the left with a flat upper rim. The bowl flows into a slender curved stem that rises to a short open mouthpiece on the right.\nPlan: Deep pipe bowl on left, curved stem rising toward right. Continuous silhouette with wide open stem band.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4206317d-c866-490a-ae80-17ed2d1a8d6f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/pipe smoking_4206317d-c866-490a-ae80-17ed2d1a8d6f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-smoking-pipe'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('curved', 'smoking', 'pipe')

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

        path('pipe',(4,12),[('L',(16,12)),('L',(16,24)),('C',(24,24),(16,29),(20,29)),('C',(44,8),(32,12),(36,8)),('L',(44,18)),('C',(30,32),(37,18),(34,27)),('C',(18,40),(26,38),(22,40)),('C',(4,26),(8,40),(4,34)),('L',(4,12))],True)
