'Eye with Eyelashes.\nPlan and review: Retained almond eye, circular iris and three upper lashes. Reduced iris diameter for clearance.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Lucide eye: coherent almond curves and round iris; source upper lashes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c39822f2-87fc-4ba9-b29b-97efb6931546'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/eyelash_c39822f2-87fc-4ba9-b29b-97efb6931546.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'eye-with-three-upper-lashes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('eye', 'with', 'three', 'upper', 'lashes')

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

        curve('eye',(4,28),((14,10),(34,10),(44,28)),((34,44),(14,44),(4,28)))
        circle('iris',24,28,3)
        self.add_line('lash-middle',(24,14),(24,8));self.add_line('lash-left',(12,19),(8,12));self.add_line('lash-right',(36,19),(40,12))
        for s in ('middle','left','right'):self.relate('connect','eye','lash-'+s)
