'Simple Tulip Flower Bud.\nPlan and review: Retained pointed central petal, two crossing outer petals and short stem. Rebuilt outer extrema exactly on keyshape.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide flower: joined petals and stem; source crossing outer petals preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a802dced-4ea6-4a11-b513-f57a804337af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/vegetable banana flower_a802dced-4ea6-4a11-b513-f57a804337af.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tulip-bud'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('tulip', 'bud')

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        curve('left-petal',(8,10),((8,22),(8,38),(24,38)),((34,30),(24,10),(8,10)))
        curve('right-petal',(40,10),((40,22),(40,38),(24,38)),((14,30),(24,10),(40,10)))
        self.relate('connect','left-petal','right-petal')
        path('center',(16,12),[(24,4),(32,12)])
        for s in ('left-petal','right-petal'):self.relate('connect','center',s)
        self.add_line('stem',(24,38),(24,44))
        for s in ('left-petal','right-petal'):self.relate('connect','stem',s)
