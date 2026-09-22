'Empty right-facing manual wheelchair with large rear wheel, small caster, push handle and projecting front frame. Omit tiny axle, redundant seat rail and footrest bend.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. Lucide wheelchair search found no match. Reference supplies large wheel and projecting front frame; omit axle and redundant seat rail.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e279196-338d-47df-9c7e-639098b008bb'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_27/motorized wheelchair_5e279196-338d-47df-9c7e-639098b008bb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wheelchair-with-large-rear-wheel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ["Manual Wheelchair Accessibility Icon"]
    keywords = ["wheelchair", "mobility", "wheels", "seat", "footrest", "accessibility", "chair"]
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

        path('wheel',(18,18),[((30,30),12,12,True),((18,42),12,12,True),((6,30),12,12,True),((18,18),12,12,True)],True)
        poly('frame',(8,6),(18,6),(18,18),(34,18),(42,28))
        join('frame','wheel')
        circle('front-wheel',38,40,2)
