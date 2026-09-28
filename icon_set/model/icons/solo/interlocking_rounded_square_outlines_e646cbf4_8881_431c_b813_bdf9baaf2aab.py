'Two rounded square outlines overlap diagonally from upper left to lower right. Their facing edges break around a smaller central square-shaped intersection, making the two larger forms appear interlinked.\nPlan: Two interrupted square surrounds and central overlap cell, with 8-unit breaks.\nConstruction reference: Lucide copy original and atomic-debug: clean separated rounded corners.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e646cbf4-8881-431c-b813-bdf9baaf2aab'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/amazon worklink_e646cbf4-8881-431c-b813-bdf9baaf2aab.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'interlocking-rounded-square-outlines'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('interlocking', 'rounded', 'square', 'outlines')

    # Repair: Reduce the center intersection cell slightly to give curved gap endpoints a certifiable margin.
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

        path('upper',(10,30),[('A',(6,26),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(26,6)),('A',(30,10),4,4,True)])
        path('lower',(38,18),[('A',(42,22),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(22,42)),('A',(18,38),4,4,True)])
        poly('center',(19,19),(29,19),(29,29),(19,29),(19,19))
