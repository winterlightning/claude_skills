'Closed Eye with Eyelashes.\nPlan and review: Two lashes remain on the left half. The eyelid is deeper to fill HRECT_M. Shared attachment nodes avoid floating lashes.\nKeyshape: HRECT_M, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide eye-closed: one continuous eyelid with attached lashes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'afb69f40-6aff-40c4-aa6f-3646708bd0d2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/eyelid_afb69f40-6aff-40c4-aa6f-3646708bd0d2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-eye-with-eyelashes'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('closed', 'eye', 'with', 'eyelashes')

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

        curve('lid',(4,10),((6,16),(8,20),(12,22)),((16,26),(20,28),(24,28)),((34,28),(39,22),(44,10)))
        self.add_line('lash-outer',(12,22),(6,30));self.add_line('lash-inner',(24,28),(20,38))
        self.relate('connect','lid','lash-outer');self.relate('connect','lid','lash-inner')
