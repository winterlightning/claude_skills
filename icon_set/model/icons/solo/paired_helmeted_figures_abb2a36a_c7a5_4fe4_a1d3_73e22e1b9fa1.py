'Two broad shouldered figures stand close together with the right figure in front. Horizontal bands cross their rounded heads, and two short horizontal marks cross the front torso.\nPlan: Paired helmeted people with head bands and overlapping shoulders.\nConstruction reference: human_ref/user.svg: round heads and curved shoulders; circular helmet bands.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'abb2a36a-c7a5-4fe4-a1d3-73e22e1b9fa1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bounty hunter 1_abb2a36a-c7a5-4fe4-a1d3-73e22e1b9fa1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paired-helmeted-figures'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitive', 'primitives')
    aliases = ()
    keywords = ('paired', 'helmeted', 'figures')

    # Repair: Separate helmeted figures horizontally; each head bottom24 to shoulder top32 yields4 ink gap. Omit torso stripes that cannot fit the short body.
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

        for name,cx in [('left',12),('right',36)]:
         circle('head-'+name,cx,16,8)
         line('band-'+name,(cx-8,16),(cx+8,16));join('band-'+name,'head-'+name)
         path('body-'+name,(cx-8,40),[('A',(cx,32),8,8,True),('A',(cx+8,40),8,8,True)])
