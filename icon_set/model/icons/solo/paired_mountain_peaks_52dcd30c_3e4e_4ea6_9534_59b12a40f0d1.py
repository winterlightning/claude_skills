'Two triangular mountain peaks share a flat baseline, with the taller mountain on the left. A zigzag snow boundary crosses its upper slope, and a diagonal ridge descends toward the foreground.\nPlan: Two mountain peaks with shared ridge and single snow boundary.\nConstruction reference: Lucide mountain original and atomic-debug: angular peak silhouette and fewer internal facets.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52dcd30c-3e4e-4ea6-9534-59b12a40f0d1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mountains_52dcd30c-3e4e-4ea6-9534-59b12a40f0d1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paired-mountain-peaks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('paired', 'mountain', 'peaks')

    # Repair: Widen the right mountain facet by moving the shared ridge foot left; retain both complete peaks.
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

        poly('mountains',(4,40),(18,8),(30,26),(36,18),(44,40),(34,40),(4,40))
        line('ridge',(30,26),(34,40));join('ridge','mountains')
