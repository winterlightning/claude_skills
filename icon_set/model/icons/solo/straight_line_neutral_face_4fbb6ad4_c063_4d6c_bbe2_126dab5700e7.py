'Expressionless Neutral Face Emoji.\nPlan and review: Retained round face, two short horizontal eyes and longer straight mouth.\nKeyshape: CIRCLE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fbb6ad4-c063-4d6c-bbe2-126dab5700e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face expressionless_4fbb6ad4-c063-4d6c-bbe2-126dab5700e7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'straight-line-neutral-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('straight', 'line', 'neutral', 'face')

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
        for name,a,b in [('eye-left',(14,20),(18,20)),('eye-right',(30,20),(34,20)),('mouth',(18,32),(30,32))]:self.add_line(name,a,b)
