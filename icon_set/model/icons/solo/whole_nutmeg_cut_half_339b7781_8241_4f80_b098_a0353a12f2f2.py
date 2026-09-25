'A large oval nutmeg leans diagonally behind a smaller cut half at the lower right. Curved grooves mark the whole nut, while an irregular central kernel appears inside the thick cut rim.\nPlan: Whole nutmeg and smaller cut half; one main groove and broad cut rim. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: No useful direct Lucide match; coherent contours reconstructed from the inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '339b7781-8241-4f80-b098-a0353a12f2f2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nutmeg_339b7781-8241-4f80-b098-a0353a12f2f2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'whole-nutmeg-cut-half'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('whole', 'nutmeg', 'cut', 'half')

    # Repair: Trim whole nut outline at exact front-shell endpoints instead of leaving it visible through the kernel.
    # Repair: Shorten the retained whole-nut groove to clear the cut shell.
    # Repair: Keep a short diagonal groove in the remaining clear whole-nut region.
    # Repair: Move the retained groove1 unit inward to clear the curved shell with margin.
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

        path('whole',(20,31),[('C',(6,22),(10,34),(6,30)),('C',(24,6),(6,10),(16,6)),('C',(31,20),(32,6),(34,12))]);circle('half',31,31,11);circle('kernel',31,31,2);join('whole','half')
        line('groove',(15,20),(17,16))
