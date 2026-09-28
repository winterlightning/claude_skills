'A horizontal sash extends to both sides of a broad rounded central fastening. A small rectangular opening sits inside the fastening, while the two straight belt ends remain aligned behind it.\nPlan: Broad sash with rounded central fastening and single spacious opening. Box4,10–44,38.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4837e756-afcf-439b-a2ef-2c90c1a05a91'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/obi_4837e756-afcf-439b-a2ef-2c90c1a05a91.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kimono-sash-belt'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('kimono', 'sash', 'belt')

    # Repair: Widen central fastening to retain a true rectangular opening instead of a stroke.
    # Repair: Reduce short sash tails to strokes and enlarge the central fastening for a readable square opening.
    # Repair: Restore broad sash tails and use straight fastening walls so the exact 8-unit opening clearance is certifiable.
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

        poly('knot',(12,10),(36,10),(36,14),(36,34),(36,38),(12,38),(12,34),(12,14),(12,10))
        poly('left',(12,14),(4,14),(4,34),(12,34));poly('right',(36,14),(44,14),(44,34),(36,34));join('left','knot');join('right','knot')
        poly('opening',(20,20),(28,20),(28,28),(20,28),(20,20))
