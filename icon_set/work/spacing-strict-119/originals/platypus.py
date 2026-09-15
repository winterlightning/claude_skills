# Review candidate; original preserved.
"""platypus: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd9e4bd26-488d-456c-8a81-23be0e9dd789'
SOURCE_PATH = 'pictographic-primitives/animals/duck bill platypus_d9e4bd26-488d-456c-8a81-23be0e9dd789.svg'
AUTHOR = 'gpt-6'

class Platypus(Solo48):
    icon_id = 'platypus'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('platypus', 'duckbill', 'australia', 'mammal', 'monotreme', 'animal', 'wildlife', 'aquatic')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_arc('tail-1',(18, 20),(16, 14),radius_x=10,radius_y=10,large_arc=False,sweep=True)
        self.add_bezier('tail-2',(16, 14),*(((17.96491735, 8.62844247), (22.99693568, 4.75765914), (29, 4)),))
        self.add_bezier('tail-3',(29, 4),*(((31.72076519, 4), (34.46238974, 4.88392944), (36, 8)),))
        self.add_line('tail-4',(36, 8),(27, 16))
        self.add_line('tail-5',(27, 16),(27, 20))
        self.add_arc('body-1',(18, 20),(12, 29),radius_x=6,radius_y=9,large_arc=False,sweep=False)
        self.add_bezier('body-2',(12, 29),*(((13.10423652, 32.38747008), (15.49919387, 34.47908484), (18, 34)),))
        self.add_line('body-3',(18, 34),(28, 34))
        self.add_bezier('body-4',(28, 34),*(((30.50080613, 34.47908484), (32.89576348, 32.38747008), (34, 29)),))
        self.add_arc('body-5',(34, 29),(27, 20),radius_x=7,radius_y=9,large_arc=False,sweep=False)
        self.add_line('body-6',(27, 20),(18, 20))
        self.add_line('bill-1',(18, 34),(28, 34))
        self.add_bezier('bill-2',(28, 34),*(((30.76142375, 34.0), (33.0, 36.23857625), (33.0, 39.0)), ((33.0, 41.76142375), (30.76142375, 44), (28, 44))))
        self.add_line('bill-3',(28, 44),(18, 44))
        self.add_bezier('bill-4',(18, 44),*(((15.23857625, 44), (13.0, 41.76142375), (13.0, 39.0)), ((13.0, 36.23857625), (15.23857625, 34.0), (18, 34))))
        self.add_line('left-foreleg',(12, 29),(8, 24))
        self.add_line('right-foreleg',(34, 29),(40, 24))
        self.add_line('left-hindleg',(18, 34),(8, 34))
        self.add_line('right-hindleg',(28, 34),(40, 34))
        self.add_contour('tail',*('tail-1', 'tail-2', 'tail-3', 'tail-4', 'tail-5'),closed=False)
        self.add_contour('body',*('body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6'),closed=True)
        self.add_contour('bill',*('bill-1', 'bill-2', 'bill-3', 'bill-4'),closed=True)
        self.relate('connect',*('tail', 'body'))
        self.relate('connect',*('bill', 'body'))
        self.relate('connect',*('left-foreleg', 'body'))
        self.relate('connect',*('right-foreleg', 'body'))
        self.relate('connect',*('left-hindleg', 'body'))
        self.relate('connect',*('left-hindleg', 'bill'))
        self.relate('connect',*('right-hindleg', 'body'))
        self.relate('connect',*('right-hindleg', 'bill'))
