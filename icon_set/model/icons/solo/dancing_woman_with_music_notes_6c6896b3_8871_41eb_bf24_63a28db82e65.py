"""A woman in a short dress dances beside two notes. VRECT_L accommodates the outstretched arm, bent leg and right-hand notes. Human full_body_ref.png supplies circular head and simple dress construction. Head center (18,8), radius 4, torso start (18,20) gives exactly 4 ink clearance. Paired noteheads have radius 2 and a shared 22-unit vertical step. Natural pose asymmetry retained.

Source rendered and inspected before authoring. Preserve the saved user classification.
Lucide image and ticket-x originals and atomic geometry informed coherent contours
and rounded enclosures; human reference used only for the three human scenes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6c6896b3-8871-41eb-bf24-63a28db82e65'
SOURCE_PATH = 'pictographic-primitives/entertainment/party music dance woman_6c6896b3-8871-41eb-bf24-63a28db82e65.svg'
AUTHOR = 'gpt-6'

class QueueIcon(Solo48):
    icon_id = 'dancing-woman-with-music-notes'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ('Dancing Woman with Music Notes',)
    keywords = ('dancing', 'woman', 'with', 'music', 'notes')
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
        circle('head',18,8,4)
        self.add_line('torso',(18,20),(18,28))
        self.add_polyline('arms',(8,20),(18,20),(24,20))
        self.add_polyline('dress',(18,28),(24,37),(22,37),(14,37),(12,37),closed=True)
        self.add_polyline('left-leg',(14,37),(10,44))
        self.add_polyline('right-leg',(22,37),(24,41),(22,44))
        self.relate('connect','torso','arms')
        self.relate('connect','torso','dress')
        self.relate('connect','dress','left-leg')
        self.relate('connect','dress','right-leg')
        self.mark_human_figure('dancer',head='head',torso='torso',torso_junction='start')
        note('upper-note',34,14)
        note('lower-note',34,36)
