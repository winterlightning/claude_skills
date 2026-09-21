# Final repair: Broaden bells and separate open bow by9 centerline units; remove tiny ribbon holes.
'Paired Christmas Bells with Bow\nPlan: Two outward flared bells share top bow knot; paired geometry derives from center axis.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Remove ribbon tails; retain matched bells and top bow.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71902e74-498c-4f90-9102-f4805b93d83d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/christmas bells_71902e74-498c-4f90-9102-f4805b93d83d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paired-christmas-bells-with-bow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('paired', 'christmas', 'bells', 'with', 'bow')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        for sign in (-1,1):
            def p(x,y):return (24+sign*x,y)
            path(f'bell-{sign}',p(8,29),[(p(16,29),4,4,sign==1),p(20,36),p(4,36),p(8,29)],True)
            self.add_line(f'clapper-{sign}',p(12,36),p(12,40));self.relate('connect',f'clapper-{sign}',f'bell-{sign}')
        self.add_polyline('bow',(12,8),(24,16),(36,8))
