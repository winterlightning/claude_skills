'Eyelashes on Closed Eye.\nPlan and review: Retained closed curved eyelid and fanning lashes. Reduced seven lashes to five. Treated as a standalone eye detail at the user-requested SOLO48 size.\nKeyshape: HRECT_M, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Lucide eye-closed: smooth broad lid with attached lashes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f29b7563-7092-4a2d-a25c-9987c1f09ccf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/lashes_f29b7563-7092-4a2d-a25c-9987c1f09ccf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-eye-curved-lashes'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('closed', 'eye', 'curved', 'lashes')

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

        curve('lid',(4,10),((8,22),(16,28),(24,28)),((32,28),(40,22),(44,10)))
        for j,(a,b) in enumerate((((7,17),(4,26)),((15,26),(12,36)),((24,28),(24,38)),((33,26),(36,36)),((41,17),(44,26)))):
         self.add_line(f'lash-{j}',a,b);self.relate('connect','lid',f'lash-{j}')
