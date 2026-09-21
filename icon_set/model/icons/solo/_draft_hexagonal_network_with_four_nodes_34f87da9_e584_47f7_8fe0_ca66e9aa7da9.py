'Four nodes and central hexagonal hub; geometric network.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34f87da9-e584-47f7-8fe0-ca66e9aa7da9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon eventbridge_34f87da9-e584-47f7-8fe0-ca66e9aa7da9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hexagonal-network-with-four-nodes'
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

        for name,x,y in [('a',14,12),('b',40,24),('c',34,36),('d',8,24)]:circle(name,x,y,4)
        poly('ab',(18,12),(34,12),(40,20));join('a','ab');join('b','ab')
        poly('bc',(40,28),(38,36));join('b','bc');join('c','bc')
        poly('cd',(30,36),(14,36),(8,28));join('c','cd');join('d','cd')
        poly('da',(8,20),(10,12));join('d','da');join('a','da')
        poly('hub',(22,20),(26,20),(28,24),(26,28),(22,28),(20,24),(22,20))
