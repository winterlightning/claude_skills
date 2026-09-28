"""tracker-smartwatch: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c47953f-1034-5ce5-9f6c-89467580488b'
SOURCE_PATH = 'pictographic-primitives/health/tracker smartwatch_2c47953f-1034-5ce5-9f6c-89467580488b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class TrackerSmartwatch(Solo48):
    icon_id = 'tracker-smartwatch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('tracker', 'smartwatch', 'health')

    def build(self):
        # Plan: VRECT_L; one symmetric case, identical strap ends, waveform exactly attached to the case.
        # Reference: Geometric rounded rectangle and repeated straps.
        def box(name,l,t,r,b,corner):
            points=[(l+corner,t),(r-corner,t),(r,t+corner),(r,b-corner),(r-corner,b),(l+corner,b),(l,b-corner),(l,t+corner)]
            members=[]
            for i,a in enumerate(points):
                z=points[(i+1)%8];eid=f'{name}-{i}';members.append(eid)
                if i%2:self.add_arc(eid,a,z,radius_x=corner)
                else:self.add_line(eid,a,z)
            self.add_contour(name,*members,closed=True)

        box('face',8,13,40,35,4)
        for name,mirror in [('top',False),('bottom',True)]:
            def p(x,y):return (x,48-y) if mirror else (x,y)
            self.add_line(name+'-left',p(14,13),p(14,8))
            self.add_arc(name+'-corner-left',p(14,8),p(18,4),radius_x=4,sweep=not mirror)
            self.add_line(name+'-end',p(18,4),p(30,4))
            self.add_arc(name+'-corner-right',p(30,4),p(34,8),radius_x=4,sweep=not mirror)
            self.add_line(name+'-right',p(34,8),p(34,13))
            self.add_contour(name,name+'-left',name+'-corner-left',name+'-end',name+'-corner-right',name+'-right')
            self.relate('connect',name,'face')
        self.add_polyline('pulse',(8,24),(17,24),(22,19),(28,29),(33,24),(40,24))
        self.relate('connect','pulse','face')
