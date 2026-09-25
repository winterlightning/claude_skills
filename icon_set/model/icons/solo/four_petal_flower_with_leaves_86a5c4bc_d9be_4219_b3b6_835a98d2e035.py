'Simple Four Petal Flower.\nPlan and review: Retained four rounded petals, stem and both pointed leaves. Omitted petal division seams and moved leaves lower to keep clear openings.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide flower and sprout: repeated petals and leaves attached to stem.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86a5c4bc-d9be-4219-b3b6-835a98d2e035'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flax_86a5c4bc-d9be-4219-b3b6-835a98d2e035.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-petal-flower-with-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('four', 'petal', 'flower', 'with', 'leaves')

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

        path('flower',(18,10),[((30,10),6,6,True),((30,22),6,6,True),((18,22),6,6,True),((18,10),6,6,True)],True)
        self.add_line('stem',(24,28),(24,44));self.relate('connect','stem','flower')
        curve('leaf-left',(8,34),((18,34),(22,40),(24,44)),((14,44),(8,40),(8,34)))
        curve('leaf-right',(40,34),((30,34),(26,40),(24,44)),((34,44),(40,40),(40,34)))
        for s in ('leaf-left','leaf-right'):self.relate('connect','stem',s)
        self.relate('connect','leaf-left','leaf-right')
