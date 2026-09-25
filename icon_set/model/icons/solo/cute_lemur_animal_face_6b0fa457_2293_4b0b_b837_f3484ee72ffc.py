'Cute Lemur Animal Face.\nPlan and review: Retained rounded ears, paired round eye patches and centered nose; omitted pupils and chin seam. Integrated ears in the silhouette to avoid overlapping closed loops.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide cat: paired ears and sparse animal face; source round lemur eye patches retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b0fa457-2293-4b0b-b837-f3484ee72ffc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/lemur_6b0fa457-2293-4b0b-b837-f3484ee72ffc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cute-lemur-animal-face'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cute', 'lemur', 'animal', 'face')

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

        curve('upper',(4,24),((4,20),(4,18),(4,16)),((4,11),(4,8),(10,8)),((14,8),(16,9),(16,9)),((20,8),(28,8),(32,9)),((32,9),(34,8),(38,8)),((44,8),(44,11),(44,16)),((44,18),(44,20),(44,24)))
        self.add_arc('lower-right',(44,24),(28,40),radius_x=16,sweep=True)
        self.add_line('chin',(28,40),(20,40))
        self.add_arc('lower-left',(20,40),(4,24),radius_x=16,sweep=True)
        self.add_contour('face','upper','lower-right','chin','lower-left',closed=True)
        circle('eye-left',16,22,3);circle('eye-right',32,22,3)
        self.add_dot('nose',(24,31))
