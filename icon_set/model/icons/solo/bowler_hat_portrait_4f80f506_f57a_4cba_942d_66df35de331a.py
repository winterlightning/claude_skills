'Bowler-hat avatar with circular jaw, domed hat and broad smooth shoulders. human_ref/user.svg informs shoulders; jaw bottom28 / body top32 gives touching ink. Plain face preserved.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f80f506-f57a-4cba-942d-66df35de331a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bowler_4f80f506-f57a-4cba-942d-66df35de331a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bowler-hat-portrait'
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

        self.add_arc('jaw',(14,18),(34,18),radius_x=10,radius_y=10,sweep=False)
        path('hat',(14,18),[(14,16),((34,16),10,10,True),(34,18)])
        line('brim',(8,18),(40,18));join('brim','jaw');join('brim','hat')
        self.add_arc('body-top',(6,42),(42,42),radius_x=18,radius_y=10,sweep=True);join('jaw','body-top')
