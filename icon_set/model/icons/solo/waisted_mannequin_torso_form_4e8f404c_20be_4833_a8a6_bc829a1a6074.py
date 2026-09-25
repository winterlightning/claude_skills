'Headless dress-form torso with neck stump, sloped shoulders, narrow waist and broad rounded base. Preserve body shape without adding a stand.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e8f404c-20be-4833-a8a6-bc829a1a6074'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/dummy_4e8f404c-20be-4833-a8a6-bc829a1a6074.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'waisted-mannequin-torso-form'
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

        path('neck',(18,12),[(18,8),((22,4),4,4,True),(26,4),((30,8),4,4,True),(30,12)])
        bez('body',(18,12),((18,14),(8,14),(8,20)),((8,26),(14,29),(14,32)),((14,36),(8,44),(14,44)),((20,44),(28,44),(34,44)),((40,44),(34,36),(34,32)),((34,29),(40,26),(40,20)),((40,14),(30,14),(30,12)));join('neck','body')
