'A front-facing woman wears her hair in a rounded bun above a center-parted fringe. Broad shoulders sit beneath a high neck, and two diagonal collar bands overlap across the chest.\nPlan: Circular face at24,20 r8; hair bun above; round shoulders touch jaw ink at y30; open cross collar.\nConstruction reference: Shared human_ref/user.svg: circular face and broad curved shoulders; current zero ink-gap avatar rule.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce74e80f-cc0b-4726-b153-1d360f619e1a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/avatar chinese woman 1_ce74e80f-cc0b-4726-b153-1d360f619e1a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'woman-with-a-hair-bun-and-crossed-collar'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('woman', 'with', 'a', 'hair', 'bun', 'and', 'crossed', 'collar')

    # Repair: Use circular shoulders with exact vertical extrema, head bottom24 and shoulder top28, giving zero ink gap.
    # Repair: Centered circular bun and face meet at y10. Face bottom26 and shoulder apex30 give zero painted gap. Two crossing collar strokes stay inside the shoulder opening.
    # Repair: A single diagonal wrap seam reads as clothing more clearly than a tiny X; omit the second collar layer at native size.
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

        circle('bun',24,7,3);circle('head',24,18,8);join('bun','head')
        path('body',(10,44),[('A',(24,30),14,14,True),('A',(38,44),14,14,True)]);join('head','body')
        line('wrap-collar',(20,44),(28,40))
