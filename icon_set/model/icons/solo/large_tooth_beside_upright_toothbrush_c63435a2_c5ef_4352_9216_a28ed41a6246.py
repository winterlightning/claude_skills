'A large molar has a shallow dip across its crown and two long rounded roots. An upright toothbrush stands to the right, with short horizontal bristle lines projecting toward the tooth.\nPlan: Molar contour at left, upright brush at right; two broad roots and two bristle branches. Box 6,6–42,42.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c63435a2-c5ef-4352-9216-a28ed41a6246'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/dentist_c63435a2-c5ef-4352-9216-a28ed41a6246.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'large-tooth-beside-upright-toothbrush'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('large', 'tooth', 'beside', 'upright', 'toothbrush')

    # Repair: Widen two root interiors and move short brush right; reference brush is lower than the crown.
    # Repair: Use explicit y6 crown nodes and wide root turns to hold exact extrema.
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

        path('tooth',(6,14),[('C',(14,6),(6,6),(10,6)),('C',(22,6),(18,10),(18,10)),('C',(30,14),(26,6),(30,6)),('L',(28,36)),('C',(20,36),(28,44),(24,44)),('L',(18,28)),('L',(16,36)),('C',(8,36),(12,44),(8,44)),('L',(6,14))],True)
        poly('brush',(42,42),(42,30),(42,22),(38,22))
        line('bristle',(38,30),(42,30));join('brush','bristle')
