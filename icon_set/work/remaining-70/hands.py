exec(open(__file__.replace('hands.py','repair.py')).read().split('edit(3,')[0])
H='from ._symmetry_curves import path, ellipse, line, poly, contacts\n'
redraw(12,H+'''
for j,cx in enumerate((12,36)):
    path(self,f'hand-{j}',(cx-8,12),('A',4,4,True,(cx,12)),('A',4,4,True,(cx+8,12)),('L',(cx+8,24)),('A',8,8,True,(cx,32)),('A',8,8,True,(cx-8,24)),('L',(cx-8,12)),closed=True)
    line(self,f'finger-{j}',(cx,12),(cx,20))
line(self,'handle-left',(12,32),(32,40))
line(self,'handle-right',(36,32),(16,40))
contacts(self)
self.relate('connect','handle-left','handle-right')
''','Build two broad toy hands from the same rounded shape, with eight-unit spacing and crossed handles.',key='HRECT_L')
redraw(4,H+'''
path(self,'front',(15,33),('L',(15,23)),('A',4,4,True,(19,19)),('A',4,4,True,(23,23)),('L',(23,29)),('L',(34,13)),('A',5,5,True,(42,17)),('L',(34,32)),('A',10,10,True,(24,42)),('A',9,9,True,(15,33)),closed=True)
poly(self,'rear-fingers',(6,25),(16,6),(26,6),(19,19))
path(self,'rear-palm',(6,25),('A',12,12,False,(15,33)))
contacts(self)
''','Replace the rear hand zigzag with one broad raised finger; use exact shared thumb and palm contacts between the clapping hands.')
# Keep the broader little finger from the first repair, rebalance the thumb too.
g=P[51];p=Path(g['target_file']);s=p.read_text().replace('(35, 20)','(31, 20)').replace('(37, 8)','(34, 8)').replace("radius_x=6, radius_y=6", "radius_x=4, radius_y=4");p.write_text(s);CHANGED[51]='Widen both extended fingers; retain the shaka silhouette and rounded central knuckles.'
edit(47,[('rx, ry = (20, 10)','rx, ry = (20, 8)')],'Rebalance all three React orbits together to enlarge the six outer counters without changing the atom topology.')
(W/'hands-changes.json').write_text(json.dumps(CHANGED,indent=2))
