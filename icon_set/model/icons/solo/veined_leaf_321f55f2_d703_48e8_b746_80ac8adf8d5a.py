'Simple Nature Tree Leaf.\nPlan and review: Retained upright leaf, central midrib, short stem and one side vein. Reduced three side veins to one for spacing.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide leaf: coherent pointed outline and integrated midrib; source upright orientation.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '321f55f2-d703-48e8-b746-80ac8adf8d5a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/wasabi_321f55f2-d703-48e8-b746-80ac8adf8d5a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'veined-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('veined', 'leaf')

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

        curve('leaf',(24,4),((18,10),(8,16),(8,24)),((8,34),(18,38),(24,38)),((30,38),(40,34),(40,24)),((40,16),(30,10),(24,4)))
        self.add_polyline('vein',(24,16),(24,28),(24,38),(24,44));self.relate('connect','vein','leaf')

        self.add_line('side-vein',(16,22),(24,28));self.relate('connect','side-vein','vein')
