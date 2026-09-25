'Three cubes form a compact pyramid, with one centered above two side by side cubes. Diamond shaped top faces and upright dividing edges describe the shared corners and visible sides.\nPlan: Three stacked cubes sharing the central junction; diamond top faces preserve the pyramid stack.\nConstruction reference: cuboid: shared perspective edges, source three-cube structure.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61414d47-3b9c-4221-b6ce-be737ea8d333'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/cubes_61414d47-3b9c-4221-b6ce-be737ea8d333.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-cubes-in-pyramid-stack'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'cubes', 'in', 'pyramid', 'stack')

    # Repair: Deepen lower cube faces to repair parallel-edge separation; envelope will be rechecked.
    # Repair: Rebalance the stack: lower cube walls have ten-unit height and remain inside SQUARE bounds.
    # Repair: Smaller upper cube leaves deeper lower faces while preserving all three connected blocks and their face junctions.
    # Repair: Deepen the top diamond to ten units, with eleven-unit upper walls and ten-unit lower walls.
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

        poly('outline',(24,6),(32,11),(32,22),(42,27),(42,37),(33,42),(24,37),(15,42),(6,37),(6,27),(16,22),(16,11),(24,6))
        poly('upper-top',(16,11),(24,16),(32,11));line('upper-front',(24,16),(24,27))
        poly('mid',(16,22),(24,27),(32,22));poly('lower-top',(6,27),(15,32),(24,27),(33,32),(42,27))
        line('left-vertical',(15,32),(15,42));line('right-vertical',(33,32),(33,42));line('center',(24,27),(24,37))
        for a,b in [('outline','upper-top'),('upper-top','upper-front'),('upper-front','mid'),('mid','outline'),('mid','lower-top'),('upper-front','lower-top'),('lower-top','outline'),('lower-top','left-vertical'),('lower-top','right-vertical'),('outline','left-vertical'),('outline','right-vertical'),('center','lower-top'),('center','mid'),('center','upper-front'),('center','outline')]:join(a,b)
