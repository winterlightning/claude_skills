'Electric Hoverboard.\nPlan and review: Retained two rounded upright wheels and a connected two-edge foot platform. Mirrored wheel dimensions.\nKeyshape: HRECT_M, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb688b45-5638-4a9f-9ef1-245c56470d5a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hoverboard_fb688b45-5638-4a9f-9ef1-245c56470d5a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-wheel-hoverboard'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'wheel', 'hoverboard')

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

        box('wheel-left',4,10,12,38,4);box('wheel-right',36,10,44,38,4)
        self.add_line('deck-top',(12,20),(36,20));self.add_line('deck-bottom',(12,28),(36,28))
        for w in ('wheel-left','wheel-right'):
         for s in ('deck-top','deck-bottom'):self.relate('connect',w,s)
