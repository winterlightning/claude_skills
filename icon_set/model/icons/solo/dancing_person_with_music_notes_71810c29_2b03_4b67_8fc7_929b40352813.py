"""A dancer holds an energetic wide pose beside two musical notes. SQUARE fits the raised hand, bent legs and left notes. Human full_body_ref.png supplies circular head and round-ended limbs. Head center (30,10), radius 4, torso start (30,22) gives exactly 4 ink clearance. Paired noteheads have radius 2 and a shared 22-unit vertical step. Pose asymmetry retained.

Source rendered and inspected before authoring. Preserve the saved user classification.
Lucide image and ticket-x originals and atomic geometry informed coherent contours
and rounded enclosures; human reference used only for the three human scenes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '71810c29-2b03-4b67-8fc7-929b40352813'
SOURCE_PATH = 'pictographic-primitives/entertainment/party music dance_71810c29-2b03-4b67-8fc7-929b40352813.svg'
AUTHOR = 'gpt-6'

class QueueIcon(Solo48):
    icon_id = 'dancing-person-with-music-notes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ('Dancing Person with Music Notes',)
    keywords = ('dancing', 'person', 'with', 'music', 'notes')
    def build(self):

        def circle(name,x,y,r):
            self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        def rounded(name,l,t,r,b,rad):
            points=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
            ids=[]
            for j,p in enumerate(points):
                q=points[(j+1)%8]; part=f'{name}-{j}'; ids.append(part)
                if j%2: self.add_arc(part,p,q,radius_x=rad)
                else: self.add_line(part,p,q)
            self.add_contour(name,*ids,closed=True)
        def note(name,x,y):
            circle(name+'-head',x,y,2)
            self.add_polyline(name+'-stem',(x+2,y),(x+2,y-10),(x+6,y-9))
            self.relate('connect',name+'-head',name+'-stem')
        circle('head',30,10,4)
        self.add_line('torso',(30,22),(30,32))
        self.add_polyline('arms',(21,22),(30,22),(38,22),(42,18))
        self.add_polyline('legs',(22,42),(22,37),(30,32),(36,42),(42,42))
        self.relate('connect','torso','arms')
        self.relate('connect','torso','legs')
        self.mark_human_figure('dancer',head='head',torso='torso',torso_junction='start')
        note('upper-note',8,16)
        note('lower-note',8,38)
