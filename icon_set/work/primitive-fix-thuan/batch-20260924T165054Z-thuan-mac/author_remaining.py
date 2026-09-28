from author import put,write,DESIGNS,ROWS
SOURCE_ICON_ID = tuple(row['source_uuid'] for row in ROWS)
SOURCE_PATH = tuple(row['reference_path'] for row in ROWS)
AUTHOR = 'gpt-6'
put('fire-flame-curved','VRECT_L','flame','An asymmetric flame tip flows into one rounded bowl, with a deliberate inward notch on the left.', '''
path('flame',(24,4),[('C',(40,28),(34,12),(40,20)),('A',(24,44),16,16,True),('A',(8,28),16,16,True),('C',(14,16),(8,23),(10,19)),('C',(19,22),(15,19),(17,21)),('C',(24,4),(25,17),(27,10))],True)
''')
put('fire-flower-batch-086','VRECT_L','flower-2','Symmetric oval flower head with two eyes, a central stem, and mirrored rounded leaves.', '''
oval('head',24,15,16,11)
line('eye-left',(20,13),(20,17));line('eye-right',(28,13),(28,17))
line('stem',(24,26),(24,44));join('stem','head')
path('leaves',(24,44),[('C',(8,34),(14,44),(8,40)),('L',(16,34))])
path('leaves-right',(24,44),[('C',(40,34),(34,44),(40,40)),('L',(32,34))])
join('stem','leaves');join('stem','leaves-right');join('leaves','leaves-right')
''','Inner face oval omitted to retain eye clearance. Leaves are open at their inner tips.')
put('fish-bowl','SQUARE','fish','Symmetric glass bowl with a flat rim and waterline; a small smooth fish faces right inside.', '''
path('bowl',(10,6),[('L',(38,6)),('C',(42,14),(40,8),(42,10)),('L',(42,24)),('A',(24,42),18,18,True),('A',(6,24),18,18,True),('L',(6,14)),('C',(10,6),(6,10),(8,8))],True)
line('water',(6,14),(42,14));join('water','bowl')
path('fish',(20,26),[('C',(26,22),(22,23),(24,22)),('C',(32,26),(28,22),(30,23)),('C',(26,30),(30,29),(28,30)),('C',(20,26),(24,30),(22,29))],True)
poly('tail',(17,22),(20,26),(17,30));join('tail','fish')
''','Tiny eye omitted.')
put('fish-facing-left','HRECT_M','fish','Horizontally swimming fish with mirrored upper and lower contours, a curved gill seam, and crescent tail.', '''
path('body',(4,24),[('C',(16,10),(8,16),(11,10)),('C',(34,20),(23,10),(29,14)),('L',(44,10)),('C',(40,24),(43,16),(40,21)),('C',(44,38),(40,27),(43,32)),('L',(34,28)),('C',(16,38),(29,34),(23,38)),('C',(4,24),(11,38),(8,32))],True)
path('gill',(16,10),[('C',(16,38),(25,18),(25,30))]);join('gill','body')
''','Tiny eye omitted as in the original reference.')
put('flatboat-with-deck-cabin','HRECT_M','ship','Symmetric shallow hull with tangent rounded bilge corners and a plain rectangular deck cabin.', '''
path('hull',(4,26),[('L',(14,26)),('L',(34,26)),('L',(44,26)),('L',(41,34)),('C',(35,38),(40,37),(38,38)),('L',(13,38)),('C',(7,34),(10,38),(8,37)),('L',(4,26))],True)
poly('cabin',(14,26),(14,10),(34,10),(34,26));join('cabin','hull')
''')
put('left-facing-swordfish','HRECT_L','fish','Long left-pointing bill, smooth swimming body, small swept fins and a crescent tail. Organic asymmetry preserves the reference.', '''
path('body',(12,24),[('C',(20,19),(15,21),(17,19)),('C',(26,8),(20,14),(23,10)),('C',(26,18),(25,12),(25,15)),('C',(36,21),(30,18),(33,20)),('C',(44,14),(38,17),(41,15)),('C',(44,36),(39,21),(39,29)),('C',(36,28),(41,34),(38,31)),('C',(24,30),(32,29),(28,30)),('C',(26,40),(24,34),(24,37)),('C',(19,30),(21,37),(19,34)),('C',(12,24),(16,29),(14,26))],True)
line('bill',(4,24),(12,24));join('bill','body')
''','Eye and fin seams omitted; bill, two fins and crescent tail retained.')
put('liquid-drop-07da1c02','VRECT_L','droplet','Symmetric pointed drop with tangent shoulders flowing into a circular lower bowl; short reflection retained.', '''
path('drop',(24,4),[('C',(40,28),(30,13),(40,21)),('A',(24,44),16,16,True),('A',(8,28),16,16,True),('C',(24,4),(8,21),(18,13))],True)
line('reflection',(29,32),(26,35))
''')
put('long-legged-ostrich','SQUARE','bird','Broad feathered body, long curved neck, small round head and two long angular legs; natural side-view asymmetry.', '''
path('body',(6,29),[('C',(18,20),(9,23),(13,20)),('C',(30,25),(23,20),(27,22)),('C',(32,32),(33,28),(35,32)),('L',(26,32)),('L',(18,32)),('C',(12,30),(15,32),(14,29)),('L',(6,29))],True)
path('neck',(30,25),[('C',(36,12),(39,25),(36,18))]);join('neck','body')
oval('head',36,9,3,3);join('head','neck')
line('beak',(39,9),(42,10));join('head','beak')
poly('leg-left',(18,32),(16,42),(21,42));poly('leg-right',(26,32),(30,42),(35,42));join('leg-left','body');join('leg-right','body')
''','Internal feather marks and eye omitted.')
put('looped-swan','SQUARE','bird','A curved-neck swan with a long low hull and curled wing; continuous neck and body curves replace short kinks.', '''
path('outline',(24,16),[('C',(33,6),(24,10),(28,6)),('C',(42,16),(39,6),(42,10)),('L',(34,16)),('C',(38,27),(31,20),(34,23)),('C',(42,34),(40,29),(42,31)),('C',(24,42),(42,40),(32,42)),('C',(6,32),(14,42),(6,38)),('C',(15,24),(6,28),(10,24)),('C',(24,26),(19,24),(22,25)),('C',(24,16),(25,23),(24,20))],True)
path('wing',(24,26),[('C',(16,32),(27,30),(22,32))]);join('wing','outline')
''')
put('love-compatibility','HRECT_L','heart','Two overlapping hearts with matched lobe curves; rear heart disappears only at shared front-heart endpoints.', '''
path('front',(31,22),[('C',(38,18),(33,19),(35,18)),('C',(44,25),(42,18),(44,21)),('C',(31,40),(44,31),(37,36)),('C',(21,32),(27,37),(23,35)),('C',(18,25),(19,29),(18,27)),('C',(24,18),(18,21),(20,18)),('C',(31,22),(27,18),(29,19))],True)
path('rear',(21,32),[('L',(16,40)),('C',(4,20),(10,34),(4,27)),('C',(12,8),(4,12),(7,8)),('C',(21,12),(16,8),(19,10)),('C',(29,8),(23,10),(25,8)),('C',(38,18),(34,8),(38,12))]);join('rear','front')
''')
if __name__=='__main__':write()
