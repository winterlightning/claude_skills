'Commercial Airplane Top View.\nPlan and review: Retained rounded nose, central fuselage, swept wings and tailplanes; mirrored about x24.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide plane: coherent closed silhouette and swept wing/tail construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a551ee87-c098-4d82-aa6e-b2fd52713a4e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/aircraft_a551ee87-c098-4d82-aa6e-b2fd52713a4e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'commercial-airplane-top-view'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('commercial', 'airplane', 'top', 'view')

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

        path('plane',(20,8),[((28,8),4,4,True),(28,20),(40,28),(40,36),(28,32),(28,36),(34,44),(24,40),(14,44),(20,36),(20,32),(8,36),(8,28),(20,20),(20,8)],True)
