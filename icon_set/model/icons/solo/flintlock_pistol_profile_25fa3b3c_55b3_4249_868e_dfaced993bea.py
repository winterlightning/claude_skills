'Flintlock Pistol.\nPlan and review: Retained long left-facing barrel, hammer, trigger-guard curve and descending grip. Omitted separate trigger hook; integrated the guard into the silhouette.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25fa3b3c-55b3-4249-868e-dfaced993bea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flintlock_25fa3b3c-55b3-4249-868e-dfaced993bea.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flintlock-pistol-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('flintlock', 'pistol', 'profile')

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

        path('outline',(4,12),[(32,12),((40,24),8,12,True),(44,40),(32,40),(32,30),(24,30),((16,22),8,8,True),(8,22),((4,18),4,4,True),(4,12)],True)
        self.add_line('hammer',(32,12),(40,8));self.relate('connect','hammer','outline')
        self.add_line('barrel-seam',(16,22),(32,22));self.relate('connect','barrel-seam','outline')
