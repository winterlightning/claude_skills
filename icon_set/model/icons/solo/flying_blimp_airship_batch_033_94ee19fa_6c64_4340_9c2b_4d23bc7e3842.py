'Flying Blimp Airship. Blimp envelope, two left fins and hanging gondola retained. Integrated the fins into the outer silhouette to eliminate two undersized enclosed triangles. The asymmetric rounded nose preserves flight direction. HRECT_L fits the wide complete subject. No useful Lucide blimp match found; source reference governs the contour. SOLO48, stroke4, HRECT_L centerline bounds (4,8)-(44,40).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '94ee19fa-6c64-4340-9c2b-4d23bc7e3842'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/airship_94ee19fa-6c64-4340-9c2b-4d23bc7e3842.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'flying-blimp-airship-batch-033'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('flying-blimp-airship',)
    keywords = ('batch-033',)

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

        # Integrate the fins into the envelope silhouette, avoiding tiny enclosed triangles.
        path('envelope',(4,8),[(16,12),(32,12),((44,22),12,10,True),((32,32),12,10,True),(16,32),(4,36),(8,24),(4,22),(8,20),(4,8)],True)
        path('gondola',(20,32),[(22,40),(30,40),(32,32)])
        self.relate('connect','envelope','gondola')
