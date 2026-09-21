'Bag on a platform with a tall right-hand weighing dial. Omit small suitcase bands to make room for the mechanical scale.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '87883707-fdb1-4115-85e4-5211fad9c524'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baggage weight 2_87883707-fdb1-4115-85e4-5211fad9c524.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'banded-suitcase-on-a-raised-dial-scale'
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
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        poly('case',(6,42),(6,34),(22,34),(22,42))
        poly('handle',(8,34),(8,26),(16,26),(16,34));join('handle','case')
        line('base',(6,42),(32,42));join('base','case')
        circle('dial',32,16,10);line('post',(32,26),(32,42));join('post','dial');join('post','base')
        line('pointer',(32,16),(33,15))
