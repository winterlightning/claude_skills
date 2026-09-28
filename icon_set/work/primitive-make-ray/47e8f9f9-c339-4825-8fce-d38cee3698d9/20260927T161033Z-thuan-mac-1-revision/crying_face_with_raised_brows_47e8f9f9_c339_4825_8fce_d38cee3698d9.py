'Sad Crying Face.\nPlan and review: Retained raised inner brows, short closed eyes, frown and left tear. Simplified droplet to a small round bulb with attached tear track from the eye, and shifted the small frown right. Uses the existing complete-circle diameter4 hole exception; no new exception.\nKeyshape: CIRCLE, exact SOLO48 envelope.\nConstruction reference: Source face and tear; Lucide circular-face vocabulary.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '47e8f9f9-c339-4825-8fce-d38cee3698d9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crying-face-with-raised-brows/20260927T160834Z-thuan-mac-1/reference/face sad tear_47e8f9f9-c339-4825-8fce-d38cee3698d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crying-face-with-raised-brows'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('crying', 'face', 'with', 'raised', 'brows')

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

        circle('head',24,24,20)
        self.add_line('brow-left',(18,15),(20,14));self.add_line('brow-right',(28,14),(30,15))
        self.add_line('eye-left',(18,23),(20,23));self.add_line('eye-right',(28,23),(30,23))
        self.add_arc('frown',(23,34),(29,34),radius_x=3,radius_y=2,sweep=True)
        self.add_dot('tear',(15,31))
