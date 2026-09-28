'A tall upright rounded block crosses a horizontal guide. A downward arrow above the guide at left and an upward arrow beneath the block point toward its middle.\nPlan: Vertical block centered on guide with opposed offset arrows.\nConstruction reference: Lucide align-vertical-justify-center and arrow-up original/atomic-debug: centered block and opposed arrows.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '29e16b26-9907-4b01-8d8d-32e83b655134'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/align middle move vertical_29e16b26-9907-4b01-8d8d-32e83b655134.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vertical-object-centering'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('vertical', 'object', 'centering')

    # Repair: Shorten the centered block and place the lower arrow8 units below it; retain both arrows and the guide.
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

        poly('block',(26,16),(34,16),(34,24),(34,32),(26,32),(26,24),(26,16))
        line('guide-left',(8,24),(26,24));line('guide-right',(34,24),(40,24));join('guide-left','block');join('guide-right','block')
        poly('down',(8,12),(12,16),(16,12));line('down-shaft',(12,4),(12,16));join('down','down-shaft')
        poly('up',(26,44),(30,40),(34,44));line('up-shaft',(30,40),(30,44));join('up','up-shaft')
