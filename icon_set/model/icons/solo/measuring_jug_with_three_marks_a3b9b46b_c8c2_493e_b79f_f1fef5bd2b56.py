'Measuring jug with pointed upper-left spout, right loop handle and exactly three front marks.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3b9b46b-c8c2-493e-b79f-f1fef5bd2b56'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/quart_a3b9b46b-c8c2-493e-b79f-f1fef5bd2b56.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'measuring-jug-with-three-marks'
    keyshape = Keyshape.SQUARE
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

        path('jug',(6,6),[(32,6),(30,38),((26,42),4,4,True),(14,42),((10,38),4,4,True),(10,14),(6,6)],True)
        poly('handle',(32,14),(42,14),(42,30),(31,30));join('jug','handle')
        for y in (17,25,33):line(f'mark{y}',(19,y),(21,y))
