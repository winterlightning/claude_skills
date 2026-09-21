'An upright apple core has deeply eaten sides, broad ends, a short stem and central seed. VRECT_L supports the tall core, extremes 8,4,40,44. Outline mirrors about x24 including the short straight stem. Lucide apple informs the shallow paired lobes and stem attachment; source supplies concave bitten sides. Retain the central seed as one short stroke.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50bebec4-c860-42c8-a7d2-78ac2ddb5a90'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/apple core_50bebec4-c860-42c8-a7d2-78ac2ddb5a90.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'eaten-apple-core'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Eaten Apple Core',)
    keywords = ('apple', 'core', 'fruit', 'eaten', 'stem', 'food', 'leftover')
    def build(self):
        def path(name,start,steps,closed=False):
            members=[];point=start
            for j,step in enumerate(steps):
                member=f"{name}-{j}"
                if len(step)==2:self.add_line(member,point,step);point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        self.add_bezier('top-left',(8,12),((12,8),(18,8),(24,12)))
        self.add_bezier('top-right',(24,12),((30,8),(36,8),(40,12)))
        self.add_arc('right-bite',(40,12),(40,36),radius_x=6,radius_y=12,sweep=False)
        self.add_bezier('bottom-right',(40,36),((36,44),(30,44),(24,44)))
        self.add_bezier('bottom-left',(24,44),((18,44),(12,44),(8,36)))
        self.add_arc('left-bite',(8,36),(8,12),radius_x=6,radius_y=12,sweep=False)
        self.add_contour('core','top-left','top-right','right-bite','bottom-right','bottom-left','left-bite',closed=True)
        self.add_line('stem',(24,12),(24,4));self.relate('connect','stem','core')
        self.add_line('seed',(24,23),(24,27))
