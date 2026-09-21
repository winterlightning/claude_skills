'Two rounded bust silhouettes overlap, with the larger figure in front on the right. Each has a circular head flowing into sloping shoulders and a broad curved lower edge without facial marks.\nPlan: Paired full bust silhouettes with larger foreground figure and separate circular heads.\nConstruction reference: human_ref/user.svg and Lucide users original/atomic-debug: circular heads, smooth shoulder outlines.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88a00853-ba79-4560-9bd5-bdf8d82dd95b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/msn messenger logo_88a00853-ba79-4560-9bd5-bdf8d82dd95b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'overlapping-user-busts'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('overlapping', 'user', 'busts')

    # Repair: Keep larger person in the foreground on the right, with detached4 ink head gaps per shared group construction.
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

        circle('head-left',14,13,5);circle('head-right',34,12,6)
        path('body-front',(26,42),[('L',(26,34)),('A',(34,26),8,8,True),('A',(42,34),8,8,True),('L',(42,42)),('L',(26,42))],True)
        path('body-back',(6,42),[('L',(6,34)),('A',(14,26),8,8,True),('C',(26,34),(20,26),(24,28))]);line('base',(6,42),(26,42));join('body-back','body-front');join('base','body-back');join('base','body-front')
