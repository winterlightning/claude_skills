'Sad Crying Face.\nPlan and review: Retained two closed-eye curves, frown and separate left tear. Simplified droplet to a small round bulb and short tip; shifted frown right for spacing. Uses the existing complete-circle diameter4 hole exception.\nKeyshape: CIRCLE, exact SOLO48 envelope.\nConstruction reference: Source face and tear; Lucide circular-face vocabulary.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb57b7db-4e36-492c-979b-5c7f2457c852'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/face sad cry_cb57b7db-4e36-492c-979b-5c7f2457c852.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crying-face-with-single-tear'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('crying', 'face', 'with', 'single', 'tear')

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
        self.add_arc('eye-left',(16,17),(20,17),radius_x=2,radius_y=1,sweep=False)
        self.add_arc('eye-right',(28,17),(32,17),radius_x=2,radius_y=1,sweep=False)
        self.add_arc('frown',(27,33),(31,33),radius_x=2,radius_y=2,sweep=True)
        path('tear',(17,27),[((17,31),2,2,True),((17,27),2,2,True)],True)
        self.add_line('tear-tip',(17,26),(17,27));self.relate('connect','tear-tip','tear')
