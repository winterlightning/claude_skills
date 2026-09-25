'Shared human_ref/full_body_ref.png: outlined circular head, simple rounded limbs. Head bottom16, torso/shoulders24 gives exactly8 centerline/4 ink gap. Rounded silhouette translated to human stick vocabulary.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2c89f0b-18a3-4a63-a2bd-e7b45faee034'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/omnivore_c2c89f0b-18a3-4a63-a2bd-e7b45faee034.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-person-rounded-limbs'
    keyshape = Keyshape.VRECT_L
    category = "primitives-generate"
    def build(self):

        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=4):
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        circle('head',24,10,6)
        line('torso',(24,24),(24,32))
        poly('arms',(8,30),(12,24),(36,24),(40,30))
        poly('legs',(14,44),(24,32),(34,44));join('arms','torso');join('legs','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
