"""Front Loading Cargo Bicycle.

Plan: Cargo bike with rear wheel, frame and deep front box. Bounds4,8,44,40. Simplify pedals and spokes.
Construction reference: bike.
Final review: Simplified spokes and pedals; retained two wheels, bike frame and cargo box.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fc5a524-8dd7-410b-ad10-85c63c42bf5c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bike cargo_0fc5a524-8dd7-410b-ad10-85c63c42bf5c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cargo-bicycle-with-a-deep-front-box'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cargo', 'bicycle', 'with', 'a', 'deep', 'front', 'box')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        circle('rear-wheel',11,33,7);circle('front-wheel',38,34,6)
        poly('frame',(11,26),(18,18),(24,23),(38,28))
        poly('box',(28,8),(44,8),(42,16),(30,16),closed=True)
        line('seat',(10,8),(20,8))
        join('frame','rear-wheel');join('frame','front-wheel')
