'A front-facing head is framed by a smooth bob haircut with outward-curving ends and a central part. A mask covers the lower face, with its upper edge rising over the nose.\nPlan: Bob hairstyle around circular head and broad mask dividing face. Extrema6,6,42,42; omit minor mask folds.\nConstruction reference: human_ref/user.svg circular face; supplied head-only mask reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1f5e900-261d-4886-9c63-8beef0eb6820'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/air purifier 5_e1f5e900-261d-4886-9c63-8beef0eb6820.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'woman-wearing-a-face-mask'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('woman', 'wearing', 'a', 'face', 'mask')

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

        path('hair',(4,40),[('C',(4,28),(8,36),(4,34)),('A',(24,8),20,20,True),('A',(44,28),20,20,True),('C',(44,40),(44,34),(40,36))])
        circle('face',24,28,10)
        path('mask-top',(14,28),[('C',(24,26),(18,28),(21,26)),('C',(34,28),(27,26),(30,28))]);join('face','mask-top')
        line('part',(24,8),(24,18));join('hair','part');join('face','part')
