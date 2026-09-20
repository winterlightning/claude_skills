'Facial Tissue Box.\nPlan and review: Retained rounded box and emerging tissue with wavy upper edge. Omitted duplicate box seam and small tissue fold. Tissue sides share the box top without a retraced bottom edge.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc1a9bfc-4deb-4455-bae6-4fce9144a2b7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tissue_bc1a9bfc-4deb-4455-bae6-4fce9144a2b7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tissue-box'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('tissue', 'box')

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

        box('box',4,24,44,40,4)
        curve('tissue-top',(12,8),((18,16),(26,8),(36,8)))
        self.add_line('tissue-left',(12,8),(18,24));self.add_line('tissue-right',(36,8),(30,24))
        for s in ('tissue-left','tissue-right'):self.relate('connect','tissue-top',s);self.relate('connect','box',s)
