'Three tracks and one round knob; Lucide split-track construction.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3e92f67-d196-4def-aa1b-0cd99524983f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/sliders simple_d3e92f67-d196-4def-aa1b-0cd99524983f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-tracks-with-single-slider-knob'
    keyshape = Keyshape.HRECT_L
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
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        line('top',(4,8),(44,8));line('bottom',(4,40),(44,40));circle('knob',32,24,5)
        line('track-left',(4,24),(27,24));line('track-right',(37,24),(44,24));join('knob','track-left');join('knob','track-right')
