'A dhow floats on a wavy waterline beneath a single tall triangular sail with curved sides. A short central mast joins the sail to a shallow hull with raised pointed ends.\nPlan: Curved lateen sail over low hull; mast joins exact endpoints. Water reduced to hull sweep.\nConstruction reference: Lucide sailboat original and atomic-debug: triangular sail, mast, simple hull.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f2cbf40-337f-41ff-a679-2763c9d67e12'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/dhow_4f2cbf40-337f-41ff-a679-2763c9d67e12.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dhow-with-curved-triangular-sail'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('dhow', 'with', 'curved', 'triangular', 'sail')

    # Repair: Flatten hull rail to create 8-unit sail clearance and hull interior.
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

        path('sail',(18,6),[('C',(38,26),(28,12),(36,20)),('L',(18,26)),('L',(10,26)),('C',(18,6),(16,20),(18,14))],True)
        line('mast',(18,26),(18,34));join('mast','sail')
        path('hull',(6,34),[('L',(18,34)),('L',(42,34)),('L',(36,42)),('L',(12,42)),('L',(6,34))],True);join('mast','hull')
