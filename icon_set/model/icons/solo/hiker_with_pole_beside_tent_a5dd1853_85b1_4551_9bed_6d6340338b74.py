'Full-body reference informs hiker; exact 4-unit head-to-neck ink gap. Preserve tent and pole.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5dd1853-85b1-4551-9bed-6d6340338b74'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/camping trekking 2_a5dd1853-85b1-4551-9bed-6d6340338b74.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hiker-with-pole-beside-tent'
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

        circle('head',12,10,4);line('torso',(12,22),(12,32));self.mark_human_figure('hiker',head='head',torso='torso',torso_junction='start')
        poly('legs',(6,42),(12,32),(18,42));join('legs','torso');poly('arm',(12,22),(18,26),(24,26));join('arm','torso')
        line('pole',(24,26),(24,42));join('pole','arm');poly('tent',(32,42),(42,42),(36,24),(33,34))
