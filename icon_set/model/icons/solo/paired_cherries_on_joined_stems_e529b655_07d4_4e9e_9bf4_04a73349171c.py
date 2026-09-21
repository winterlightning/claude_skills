'Two round cherries overlap slightly beneath long curved stems that meet above them. A single pointed leaf extends to the upper right from the shared stem junction.\nPlan: Two touching round cherries under joined curved stems and a pointed leaf.\nConstruction reference: Lucide cherry original and atomic-debug: round paired fruit and joined curved stems.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e529b655-07d4-4e9e-9bf4-04a73349171c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cherries_e529b655-07d4-4e9e-9bf4-04a73349171c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paired-cherries-on-joined-stems'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('paired', 'cherries', 'on', 'joined', 'stems')

    # Repair: Match cherry radii and exact keyshape; review pair spacing and leaf opening.
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

        circle('left',14,34,8);circle('right',34,34,8)
        path('stem-left',(14,26),[('C',(24,6),(14,16),(20,8))]);join('stem-left','left')
        path('stem-right',(34,26),[('C',(24,6),(28,20),(26,12))]);join('stem-right','right');join('stem-left','stem-right')
        path('leaf',(24,6),[('L',(42,6)),('C',(24,6),(40,18),(32,20))],True);join('leaf','stem-left');join('leaf','stem-right')
