'Three round offset knobs with split tracks; reference positions preserved, Lucide construction inspected.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5dda3140-00d3-446d-9e76-7b666c139fcb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/sliders_5dda3140-00d3-446d-9e76-7b666c139fcb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-horizontal-sliders-with-offset-knobs'
    keyshape = Keyshape.HRECT_L
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

        for j,(y,x) in enumerate(((12,20),(24,32),(36,12))):
            circle(f'knob{j}',x,y,4);line(f'left{j}',(4,y),(x-4,y));line(f'right{j}',(x+4,y),(44,y));join(f'knob{j}',f'left{j}');join(f'knob{j}',f'right{j}')
