'Two wide open chevrons face one another along a vertical axis. The upper chevron points downward and the lower one upward, with a clear gap between their tips and no shafts.\nPlan: Two open inward chevrons with8-unit tip separation; shared24 axis.\nConstruction reference: Lucide arrow-up original and atomic-debug: open diagonal arms; no added shafts.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a44a1df3-4ccd-4137-a15d-3cccc3022c7a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/move shrink vertical_a44a1df3-4ccd-4137-a15d-3cccc3022c7a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chevron-inward-vertical'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('chevron', 'inward', 'vertical')

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

        poly('down',(4,8),(24,20),(44,8));poly('up',(4,40),(24,28),(44,40))
