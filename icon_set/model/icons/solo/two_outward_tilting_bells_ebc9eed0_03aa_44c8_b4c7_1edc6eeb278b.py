'Two domed bells lean away from each other with their inner edges overlapping. Their flared lower rims slope outward, with rounded clappers projecting below each bell.\nPlan: Paired outward bell silhouettes with simple clapper strokes; no tiny overlap pocket.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ebc9eed0-03aa-44c8-b4c7-1edc6eeb278b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/christmas bells 1_ebc9eed0-03aa-44c8-b4c7-1edc6eeb278b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-outward-tilting-bells'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'outward', 'tilting', 'bells')

    # Repair: Use explicit domed bell arcs at y8 and exact clapper attachment nodes.
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

        path('left',(4,32),[('C',(8,16),(8,28),(8,20)),('A',(20,16),6,8,True),('L',(24,32)),('L',(12,32)),('L',(4,32))],True)
        path('right',(24,32),[('L',(28,16)),('A',(40,16),6,8,True),('C',(44,32),(40,20),(40,28)),('L',(36,32)),('L',(24,32))],True);join('left','right')
        line('clapper-left',(12,32),(12,40));line('clapper-right',(36,32),(36,40));join('clapper-left','left');join('clapper-right','right')
