'A window blind hangs beneath a wide rectangular top rail. Four horizontal divisions mark its lowered slats, and a long cord descends at the right to a round pull.\nPlan: Blind with top rail, three lowered slat divisions and right pull cord. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: No useful direct Lucide match; coherent contours reconstructed from the inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9ecc5e0-2922-46a1-938f-bfa8272a4d14'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blinds_d9ecc5e0-2922-46a1-938f-bfa8272a4d14.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'window-blind-with-pull-cord'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('window', 'blind', 'with', 'pull', 'cord')

    # Repair: Move the pull cord and round pull two units outward to clear the last slat.
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
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

        poly('rail',(6,6),(42,6),(42,14),(40,14),(30,14),(6,14),(6,6))
        poly('blind',(6,14),(6,22),(6,30),(6,38),(30,38),(30,30),(30,22),(30,14));join('blind','rail')
        for y in (22,30):line('slat'+str(y),(6,y),(30,y));join('slat'+str(y),'blind')
        line('cord',(40,14),(40,38));circle('pull',40,40,2);join('cord','rail');join('cord','pull')
