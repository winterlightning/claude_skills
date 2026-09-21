'Masked thief avatar with circular head and broad smooth shoulders from human_ref/user.svg. Head bottom30 and shoulder apex34 give touching ink; mask and frown are identity cues.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '230bd616-a9d1-488d-bc7f-3d0a1ac2e6bd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/man thief 1_230bd616-a9d1-488d-bc7f-3d0a1ac2e6bd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'masked-bust-with-crossed-eye-band'
    keyshape = Keyshape.SQUARE
    category = "avatars"
    human_construction = "bust"
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

        circle('head',24,18,12)
        path('shoulders',(6,42),[(((42,42)),18,8,True)]);join('head','shoulders')
        path('mask',(12,18),[((24,18),6,5,False),((36,18),6,5,False)]);join('head','mask')
