'Flock of Flying Birds.\nPlan and review: Retained four flying birds in staggered formation. Each uses paired mirrored wing curves; the overall group remains intentionally staggered.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ebdb027-a9e7-473b-a0c3-ef3187255295'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flock_1ebdb027-a9e7-473b-a0c3-ef3187255295.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flock-of-four-birds'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('flock', 'of', 'four', 'birds')

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

        for j,(x,y) in enumerate(((6,8),(26,16),(4,26),(24,34))):
         curve(f'bird-{j}',(x,y),((x+5,y),(x+7,y+2),(x+9,y+6)),((x+11,y+2),(x+13,y),(x+18,y)))
