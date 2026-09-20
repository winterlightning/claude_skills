SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/side-repair-50-priority-7/batch.json'
AUTHOR='gpt-6'
D={}
def plan(n,shape,parts,ref,body):D[n]=(shape,parts,ref,body)
plan(1,'SQUARE','Diagonal aircraft facing upper-right, rounded nose, broad swept wing and notched lower-left tail.','plane: coherent rounded nose and diagonal outer silhouette',"""
points=((2,26),(5,20),(10,22),(16,18),(2,10),(10,2),(22,10),(26,6))
for i,(a,b) in enumerate(zip(points,points[1:])):self.add_line(f'edge-{i}',a,b)
self.add_bezier('nose-top',(26,6),((28,4),(30,4),(30,8)))
self.add_bezier('nose-bottom',(30,8),((30,12),(30,14),(28,16)))
self.add_line('body-bottom',(28,16),(14,28))
self.add_bezier('tail-bottom',(14,28),((13,29),(13,30),(12,30)))
self.add_bezier('tail-round',(12,30),((10,30),(11,29),(8,28)))
self.add_line('tail-close',(8,28),(2,26))
self.add_contour('plane',*[f'edge-{i}' for i in range(7)],'nose-top','nose-bottom','body-bottom','tail-bottom','tail-round','tail-close',closed=True)
""")
plan(4,'SQUARE','Balaclava mask with complete crossing eye loops, rounded skull, two neck notches and flared lower hem.','venetian-mask: coherent enclosing contour and paired curved eye construction',"""
self.add_arc('skull',(2,16),(30,16),radius_x=14)
self.add_line('right',(30,16),(30,20));self.add_bezier('right-neck',(30,20),((30,22),(28,24),(26,25)))
self.add_line('right-flare',(26,25),(30,28))
self.add_bezier('hem-right',(30,28),((30,30),(24,30),(16,30)))
self.add_bezier('hem-left',(16,30),((8,30),(2,30),(2,28)))
self.add_line('left-flare',(2,28),(6,25))
self.add_bezier('left-neck',(6,25),((4,24),(2,22),(2,20)))
self.add_line('left',(2,20),(2,16))
self.add_contour('mask','skull','right','right-neck','right-flare','hem-right','hem-left','left-flare','left-neck','left',closed=True)
self.add_bezier('eye-l-top',(16,16),((12,10),(9,10),(9,16)))
self.add_bezier('eye-l-bottom',(9,16),((9,22),(12,22),(16,16)))
self.add_bezier('eye-r-top',(16,16),((20,10),(23,10),(23,16)))
self.add_bezier('eye-r-bottom',(23,16),((23,22),(20,22),(16,16)))
self.add_contour('eyes','eye-l-top','eye-l-bottom','eye-r-top','eye-r-bottom',closed=True)
""")
