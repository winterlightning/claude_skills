SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/side-repair-50-priority-8/batch.json'
AUTHOR='gpt-6'
D={20:('SQUARE','Rounded wallet body, closed right fastening tab and angled protruding bill.','wallet: rounded enclosure and genuinely attached fastening tab',"""
self.add_line('left',(2,27),(2,13));self.add_arc('tl',(2,13),(5,10),radius_x=3)
self.add_line('top',(5,10),(22,10));self.add_arc('tr',(22,10),(25,13),radius_x=3)
self.add_line('right-top',(25,13),(25,16));self.add_contour('upper','left','tl','top','tr','right-top')
self.add_line('right-base',(25,24),(25,27));self.add_arc('br',(25,27),(22,30),radius_x=3)
self.add_line('base',(22,30),(5,30));self.add_arc('bl',(5,30),(2,27),radius_x=3);self.add_contour('lower','right-base','br','base','bl');self.relate('connect','upper','lower')
box(self,'tab',20,16,30,24,4)
self.relate('connect','tab','upper');self.relate('connect','tab','lower')
self.add_line('bill-left',(9,10),(20,2))
self.add_bezier('bill-corner',(20,2),((22,2),(23,4),(24,10)))
self.add_contour('bill','bill-left','bill-corner');self.relate('connect','bill','upper')
""")}
