from author import put,write,ROWS
SOURCE_ICON_ID=tuple(r['source_uuid'] for r in ROWS)
SOURCE_PATH=tuple(r['reference_path'] for r in ROWS)
AUTHOR='gpt-6'
for key in ['counterclockwise-circular-arrow-batch-019-08','counterclockwise-circular-arrow-batch-021-03','counterclockwise-refresh-arrow']:
 put(key,'SQUARE','rotate-ccw','A single smooth near-circular counterclockwise orbit ends in a balanced downward V head; lower-left opening retained.', '''
path('orbit',(27,42),[('A',(42,24),15,18,False),('A',(27,6),15,18,False),('A',(12,24),15,18,False)])
poly('head',(6,18),(12,24),(18,18));join('orbit','head')
''')
for key in ['counterclockwise-circular-refresh-arrows-batch-020-03','counterclockwise-circular-refresh-arrows-solo-b018','counterclockwise-synchronize-arrows']:
 put(key,'SQUARE','refresh-ccw','Two counterclockwise turns and balanced V heads are exact half-turn partners; coherent arcs replace awkward squared hooks.', '''
for name,flip in [('upper',False),('lower',True)]:
    p=lambda x,y:(48-x,48-y) if flip else (x,y)
    path(name,p(36,12),[('C',p(24,6),p(33,8),p(29,6)),('A',p(12,24),12,18,False)])
    poly(name+'-head',p(6,18),p(12,24),p(18,18));join(name,name+'-head')
''')
for key in ['button-syncing','diagonal-circular-refresh-arrows-solo-b018']:
 put(key,'SQUARE','refresh-cw','Two smooth clockwise arcs and diagonal open heads share a 180-degree rotational construction and equal radii.', '''
for name,flip in [('upper',False),('lower',True)]:
    p=lambda x,y:(48-x,48-y) if flip else (x,y)
    path(name,p(6,24),[('A',p(24,6),18,18,True),('C',p(38,14),p(31,6),p(35,10))])
    poly(name+'-head',p(30,14),p(38,14),p(38,6));join(name,name+'-head')
''')
for key in ['chess-rook-batch-013-07','chess-rook-batch-013-15']:
 put(key,'VRECT_L','chess-rook','A symmetric rook has three clean battlement strokes, a tapered upright tower and a rounded pedestal. Equal radii and shared attachment nodes keep the crown and base aligned.', '''
path('crown',(8,4),[('L',(8,12)),('L',(8,16)),('A',(12,20),4,4,False),('L',(16,20)),('L',(32,20)),('L',(36,20)),('A',(40,16),4,4,False),('L',(40,12)),('L',(40,4))])
poly('rim',(8,12),(24,12),(40,12));line('center-tooth',(24,4),(24,12));join('rim','crown');join('center-tooth','rim')
line('tower-left',(16,20),(14,36));line('tower-right',(32,20),(34,36));join('tower-left','crown');join('tower-right','crown')
path('base',(12,36),[('L',(14,36)),('L',(34,36)),('L',(36,36)),('A',(40,40),4,4,True),('L',(40,44)),('L',(8,44)),('L',(8,40)),('A',(12,36),4,4,True)],True)
join('tower-left','base');join('tower-right','base')
''','Battlement edges reduced to three open prongs so the tower keeps its upright proportions.')
put('cog-cbadf384','SQUARE','settings','Six-tooth cog with mirrored curved roots and rounded tooth corners; central circular hole is enlarged and centered.', '''
# One right half is mirrored to form the left half. Each smooth junction shares a tangent.
right=[('L',(26,6)),('C',(29,11),(28,6),(28,9)),('C',(34,13),(30,13),(32,14)),('L',(38,11)),('C',(40,12),(39,10),(40,11)),('L',(42,18)),('C',(40,21),(42,19),(41,20)),('C',(40,27),(38,23),(38,25)),('C',(42,30),(41,28),(42,29)),('L',(40,36)),('C',(38,37),(40,37),(39,38)),('L',(34,35)),('C',(29,37),(32,34),(30,35)),('C',(26,42),(28,39),(28,42)),('L',(24,42))]
# Explicit reverse traversal mirrors endpoints and reverses each cubic's controls.
points=[(24,6)]+[c[1] for c in right]
commands=list(right)
for i in range(len(right)-1,-1,-1):
    kind,end,*args=right[i];target=(48-points[i][0],points[i][1])
    if kind=='L':commands.append(('L',target))
    else:commands.append(('C',target,(48-args[1][0],args[1][1]),(48-args[0][0],args[0][1])))
path('gear',(24,6),commands,True)
oval('hole',24,24,4,4)
''')
put('cricket','HRECT_L','bug','A side-view cricket retains the long wing, curved antenna, two low feet and tall folded jumping leg. Natural directional asymmetry is preserved.', '''
path('body',(12,18),[('L',(20,20)),('L',(40,26)),('C',(28,32),(38,31),(34,32)),('C',(16,30),(22,32),(19,32)),('C',(12,18),(12,28),(10,23))],True)
path('antenna',(12,18),[('C',(4,8),(6,16),(4,14))]);join('antenna','body')
poly('hind-leg',(20,20),(34,8),(44,40));join('hind-leg','body')
poly('front-leg',(16,30),(12,40),(4,40));poly('middle-leg',(28,32),(32,40),(24,40));join('front-leg','body');join('middle-leg','body')
''','Small wing seam and extra antenna omitted for readable separation.')
put('key-shaped-blank-solo-b017','SQUARE','key-round','Toothless key blank with a circular bow and diagonal broad shaft; the bow transitions mirror across the shaft axis and the tiny center dot is retained.', '''
path('key',(21,19),[('L',(34,6)),('L',(42,6)),('L',(42,14)),('L',(29,27)),('C',(30,30),(30,28),(30,29)),('A',(18,42),12,12,True),('A',(6,30),12,12,True),('A',(18,18),12,12,True),('C',(21,19),(19,18),(20,18))],True)
self.add_dot('bow-dot',(18,30))
''')
put('crop-rotate','SQUARE','crop','Two crossing crop corners retain exact right angles; opposite quarter-turn arrows use matched arcs and open chevrons.', '''
poly('crop-left',(20,6),(20,20),(20,28),(28,28),(42,28))
poly('crop-right',(6,20),(20,20),(28,20),(28,28),(28,42));join('crop-left','crop-right')
path('top',(42,18),[('A',(30,10),12,8,False)])
poly('top-head',(34,6),(30,10),(34,14));join('top','top-head')
path('bottom',(6,30),[('A',(18,38),12,8,False)])
poly('bottom-head',(14,34),(18,38),(14,42));join('bottom','bottom-head')
''')
put('check-payment-give','SQUARE','hand','A check above a pointing hand, with rounded check corners and a single coherent hand outline; source hand pose retained. Shared human-reference guidance reviewed; no detached figure.', '''
path('check',(12,26),[('L',(9,26)),('A',(6,23),3,3,True),('L',(6,9)),('A',(9,6),3,3,True),('L',(39,6)),('A',(42,9),3,3,True),('L',(42,23))])
line('writing',(15,15),(22,15));line('amount',(31,15),(33,15))
path('hand',(24,28),[('A',(32,28),4,4,True),('L',(32,34)),('L',(36,34)),('L',(36,36)),('A',(30,42),6,6,True),('L',(22,42)),('A',(16,36),6,6,True),('L',(16,34)),('L',(24,28))],True)
line('finger',(24,28),(24,34));join('finger','hand')
''','Secondary writing lines and small folded fingers simplified; index finger and check retained.')
put('a-with-sync-arrow','SQUARE','refresh-cw','Capital A inside two opposed smooth sync arcs; the A has straight symmetric legs and a horizontal crossbar, with equal paired arrow wings.', '''
path('upper',(6,19),[('A',(42,19),18,13,True)])
poly('upper-head',(39,16),(42,19),(42,13));join('upper','upper-head')
path('lower',(42,29),[('A',(6,29),18,13,True)])
poly('lower-head',(9,32),(6,29),(6,35));join('lower','lower-head')
poly('letter',(17,31),(18,29),(24,17),(30,29),(31,31));line('bar',(18,29),(30,29));join('bar','letter')
''','Arrowhead wings kept compact to preserve the central A.')
if __name__=='__main__':write()
