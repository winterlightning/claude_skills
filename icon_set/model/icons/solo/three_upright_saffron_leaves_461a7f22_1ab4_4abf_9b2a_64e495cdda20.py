'Three long pointed leaf-like forms spread from a short central stem. The middle leaf rises highest, while the outer pair angle outward and curve inward toward their shared narrow base.\nPlan: Three long saffron leaf lobes on a short stem. Continuous cluster outline retains the pointed center and flanking leaves.\nConstruction reference: sprout: shared stem and coherent leaf contours, source upright fan.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '461a7f22-1ab4-4abf-9b2a-64e495cdda20'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/saffron_461a7f22-1ab4-4abf-9b2a-64e495cdda20.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-upright-saffron-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'upright', 'saffron', 'leaves')

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

        path('leaves',(24,4),[('C',(31,23),(30,12),(31,17)),('L',(40,14)),('C',(24,36),(40,27),(31,33)),('C',(8,14),(17,33),(8,27)),('L',(17,23)),('C',(24,4),(17,17),(18,12))],True)
        line('stem',(24,36),(24,44));join('stem','leaves')
