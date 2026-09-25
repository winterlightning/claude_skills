'A hooded mantle spreads outward from a round hood with an empty face opening. Two curved front panels hang apart down the body, revealing a narrow central opening and lower connecting hem.\nPlan: Open hood and broad mantle panels surround a tall center opening.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '473d1ae0-220d-41fe-bfdd-95aa0ed5d00e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mantle_473d1ae0-220d-41fe-bfdd-95aa0ed5d00e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-hooded-mantle-with-broad-panels'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('open', 'hooded', 'mantle', 'with', 'broad', 'panels')

    # Repair: Use exact semicircle hood crown at y4.
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

        path('hood',(14,20),[('L',(14,14)),('A',(34,14),10,10,True),('L',(34,20))])
        path('left',(14,20),[('C',(8,40),(10,22),(8,32)),('L',(18,44)),('L',(20,22))]);join('hood','left')
        path('right',(34,20),[('C',(40,40),(38,22),(40,32)),('L',(30,44)),('L',(28,22))]);join('hood','right')
