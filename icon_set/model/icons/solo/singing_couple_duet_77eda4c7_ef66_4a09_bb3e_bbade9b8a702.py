"""Two singers stand beside a musical note. HRECT_L accommodates the pair and central note. Both heads have radius 3 at y=15; their torso junctions at y=26 give the exact 8 centerline / 4 ink head gap. Shared mirrored stick figures follow full_body_ref.png. Reduced two notes to one and omitted gender-specific clothing to preserve spacing.

Source rendered and inspected before authoring. Preserve the saved user classification.
Lucide image and ticket-x originals and atomic geometry informed coherent contours
and rounded enclosures; human reference used only for the three human scenes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '77eda4c7-ef66-4a09-bb3e-bbade9b8a702'
SOURCE_PATH = 'pictographic-primitives/entertainment/concert couple duet_77eda4c7-ef66-4a09-bb3e-bbade9b8a702.svg'
AUTHOR = 'gpt-6'

class QueueIcon(Solo48):
    icon_id = 'singing-couple-duet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ('Singing Couple Duet',)
    keywords = ('singing', 'couple', 'duet')
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
        for name,x in [('left',9),('right',39)]:
            circle(name+'-head',x,15,3)
            self.add_line(name+'-torso',(x,26),(x,32))
            self.add_polyline(name+'-arms',(x-5,29),(x,26),(x+5,29))
            self.add_polyline(name+'-legs',(x-4,40),(x,32),(x+4,40))
            self.relate('connect',name+'-torso',name+'-arms')
            self.relate('connect',name+'-torso',name+'-legs')
            self.mark_human_figure(name,head=name+'-head',torso=name+'-torso',torso_junction='start')
        note('music',23,18)
