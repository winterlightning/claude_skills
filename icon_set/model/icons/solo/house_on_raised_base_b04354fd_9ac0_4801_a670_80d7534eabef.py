'Simple House With Door and Window.\nPlan and review: Retained peaked house, upper window, rectangular doorway and broad raised foundation. Simplified upper window to a mark; removed duplicate floor/foundation line.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide house: peaked roof, centered doorway and single upper window; source foundation retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b04354fd-9ac0-4801-a670-80d7534eabef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/inn_b04354fd-9ac0-4801-a670-80d7534eabef.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'house-on-raised-base'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('house', 'on', 'raised', 'base')

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

        path('roof',(8,18),[(24,4),(40,18)])
        path('walls',(12,15),[(12,36)]);path('wall-right',(36,15),[(36,36)])
        for s in ('walls','wall-right'):self.relate('connect','roof',s)
        path('foundation',(8,36),[(40,36),(40,44),(8,44),(8,36)],True)
        for s in ('walls','wall-right'):self.relate('connect','foundation',s)
        self.add_dot('window',(24,18))
        path('door',(20,36),[(20,28),(28,28),(28,36)]);self.relate('connect','door','foundation')
