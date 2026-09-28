'Two tilted cards protrude from a banded top hat. Omit tiny suit marks; preserve both cards and the hat opening.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8edaf21c-d4da-4295-81c0-25a068c7fb25'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/show hat cards_8edaf21c-d4da-4295-81c0-25a068c7fb25.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'playing-cards-protruding-from-top-hat'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
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

        poly('card-left',(10,22),(6,8),(22,6),(26,22));poly('card-right',(26,22),(30,8),(42,12),(38,22))
        line('brim',(6,22),(42,22));join('brim','card-left');join('brim','card-right')
        path('hat',(10,22),[(10,36),((16,42),6,6,False),(32,42),((38,36),6,6,False),(38,22)]);join('hat','brim')
        line('band',(10,30),(38,30));join('band','hat')
