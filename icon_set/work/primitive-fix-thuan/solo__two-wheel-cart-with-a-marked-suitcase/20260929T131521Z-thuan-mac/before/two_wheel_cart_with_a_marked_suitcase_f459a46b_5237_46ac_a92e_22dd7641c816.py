'Suitcase rests on the curved luggage trolley above two wheels. Lucide luggage informs rounded case and handle; omit tiny face lines to preserve silhouette.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f459a46b-5237-46ac-a92e-22dd7641c816'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baggage cart 2_f459a46b-5237-46ac-a92e-22dd7641c816.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-wheel-cart-with-a-marked-suitcase'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    def build(self):


        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=4):
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        path('cart',(6,6),[((14,14),8,8,True),(14,25),((18,29),4,4,False),(22,29),(42,29)])
        path('case',(22,29),[(22,18),((26,14),4,4,True),(38,14),((42,18),4,4,True),(42,29)]);join('case','cart')
        poly('handle',(26,14),(26,6),(38,6),(38,14));join('handle','case')
        circle('wheel-left',18,40,2);circle('wheel-right',38,40,2)
