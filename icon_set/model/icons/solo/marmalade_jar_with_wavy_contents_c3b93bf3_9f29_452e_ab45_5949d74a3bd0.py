'Jam jar with rounded lid and shoulders, upper band and wavy contents surface. Omit lower secondary band to preserve clear contents wave.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3b93bf3-9f29-452e-ab45-5949d74a3bd0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/marmalade_c3b93bf3-9f29-452e-ab45-5949d74a3bd0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'marmalade-jar-with-wavy-contents'
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

        box('lid',8,4,40,12,4)
        path('jar',(12,12),[(12,16),((8,20),4,4,False),(8,38),((14,44),6,6,False),(34,44),((40,38),6,6,False),(40,20),((36,16),4,4,False),(36,12)]);join('jar','lid')
        line('top-band',(8,24),(40,24));join('top-band','jar')
        bez('contents',(8,34),((13,31),(19,37),(24,34)),((29,31),(35,37),(40,34)));join('contents','jar')
