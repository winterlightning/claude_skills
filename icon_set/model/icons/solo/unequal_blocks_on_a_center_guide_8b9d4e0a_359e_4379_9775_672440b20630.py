'Two upright rounded blocks of unequal height sit side by side with their centers on one horizontal line. The taller block is on the left and the shorter block on the right.\nPlan: Unequal vertical blocks centered on horizontal guide; guide occluded inside each block.\nConstruction reference: Lucide align-vertical-justify-center original and atomic-debug: deliberate central alignment of different block heights.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b9d4e0a-359e-4379-9775-672440b20630'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/align middle_8b9d4e0a-359e-4379-9775-672440b20630.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'unequal-blocks-on-a-center-guide'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('unequal', 'blocks', 'on', 'a', 'center', 'guide')

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

        poly('tall',(8,8),(20,8),(20,24),(20,40),(8,40),(8,24),(8,8))
        poly('short',(28,16),(40,16),(40,24),(40,32),(28,32),(28,24),(28,16))
        line('left',(4,24),(8,24));line('middle',(20,24),(28,24));line('right',(40,24),(44,24))
        join('left','tall');join('middle','tall');join('middle','short');join('right','short')
