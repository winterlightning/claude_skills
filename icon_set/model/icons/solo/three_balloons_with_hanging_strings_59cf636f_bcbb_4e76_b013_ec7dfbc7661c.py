'Three teardrop-shaped balloons overlap, with the center balloon raised above the side pair. A straight central string and two gently curling side strings hang from their pointed lower knots.\nPlan: Three round balloons at differing heights; long strings terminate independently.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59cf636f-bcbb-4e76-b013-ec7dfbc7661c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/balloons_59cf636f-bcbb-4e76-b013-ec7dfbc7661c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-balloons-with-hanging-strings'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('three', 'balloons', 'with', 'hanging', 'strings')

    # Repair: Smaller side balloons give the central string proper clearance.
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

        circle('middle',24,12,6);circle('left',10,26,4);circle('right',38,26,4)
        line('string-middle',(24,18),(24,42));line('string-left',(10,30),(10,42));line('string-right',(38,30),(38,42))
        join('middle','string-middle');join('left','string-left');join('right','string-right')
