'Dizzy Face with X Eyes.\nPlan and review: Retained circular face, crossed eyes and wavy distressed mouth. Omitted eyebrows; rebuilt mouth as a mirrored repeating wave.\nKeyshape: CIRCLE, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide circular face vocabulary; source crossed eyes and wavy distressed mouth.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c1d6a5d-ade7-4c13-98d0-f93f1952d915'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face confounded_6c1d6a5d-ade7-4c13-98d0-f93f1952d915.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dizzy-face-with-x-eyes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('dizzy', 'face', 'with', 'x', 'eyes')

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        circle('head',24,24,20)
        for j,x in enumerate((16,32)):
         self.add_polyline(f'cross-a-{j}',(x-2,18),(x,20),(x+2,22));self.add_polyline(f'cross-b-{j}',(x-2,22),(x,20),(x+2,18));self.relate('connect',f'cross-a-{j}',f'cross-b-{j}')
        path('mouth',(17,33),[((21,33),2,2,True),((27,33),3,2,False),((31,33),2,2,True)])
