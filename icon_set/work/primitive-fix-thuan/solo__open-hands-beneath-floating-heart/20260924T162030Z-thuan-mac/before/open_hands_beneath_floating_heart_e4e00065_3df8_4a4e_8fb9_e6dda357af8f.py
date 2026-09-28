'Mirrored heart and cupped hands; separate fingers simplified to gesture strokes.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4e00065-3df8-4a4e-8fb9-e6dda357af8f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/donation charity hand care heart_e4e00065-3df8-4a4e-8fb9-e6dda357af8f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-hands-beneath-floating-heart'
    keyshape = Keyshape.SQUARE
    category = "objects"
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
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        for side in (-1,1):
            x=lambda a:24+side*a
            self.add_bezier(f'hand{side}',(x(7),42),((x(7),39),(x(18),40),(x(18),34)),((x(18),31),(x(18),28),(x(18),24)))
            line(f'thumb{side}',(x(18),34),(x(10),32))
            join(f'hand{side}',f'thumb{side}')
        self.add_arc('heart-left',(24,11),(14,11),radius_x=5,sweep=False)
        self.add_bezier('heart-tip',(14,11),((14,16),(20,21),(24,23)),((28,21),(34,16),(34,11)))
        self.add_arc('heart-right',(34,11),(24,11),radius_x=5,sweep=False)
        self.add_contour('heart','heart-left','heart-tip','heart-right',closed=True)

