'Quiet Shushing Face.\nPlan and review: Retained round open lower face, dot eyes and raised index finger with curled hand. Omitted tiny knuckle creases.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44304182-30e8-43fd-bc78-4dcef5ba1b33'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/face shush_44304182-30e8-43fd-bc78-4dcef5ba1b33.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shushing-face-with-raised-finger'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('shushing', 'face', 'with', 'raised', 'finger')

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

        path('head-top',(6,24),[((42,24),18,18,True)])
        curve('cheek-left',(6,24),((6,34),(10,40),(16,40)))
        curve('cheek-right',(42,24),((42,30),(40,34),(38,36)))
        for s in ('cheek-left','cheek-right'):self.relate('connect','head-top',s)
        path('hand',(24,42),[(24,30),((32,30),4,4,True),(32,36),(38,36),(38,42)])
        self.relate('connect','hand','cheek-right')
        self.add_dot('eye-left',(17,18));self.add_dot('eye-right',(31,18))
