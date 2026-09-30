from author import make
make(14,'SQUARE','The rejected doll omitted the pin and made the head very flat. Restore a visible pin entering the left head edge and a rounder sewn head with two clear cross eyes. Keep an upright layout to retain both eyes at 48px; simplify the original diagonal pose.', '''
path('doll',(6,20),[('C',(10,12),(6,16),(8,14)),('C',(24,8),(14,8),(18,8)),('C',(42,20),(35,8),(42,12)),('C',(34,28),(42,25),(37,28)),('L',(36,28)),('A',(40,32),4,4,True),('A',(36,36),4,4,True),('L',(36,38)),('A',(32,42),4,4,True),('L',(24,34)),('L',(16,42)),('A',(12,38),4,4,True),('L',(12,36)),('A',(8,32),4,4,True),('A',(12,28),4,4,True),('L',(14,28)),('C',(6,20),(11,28),(6,25))],True)
for x in (18,30):
 line(f'eye-{x}-a',(x-2,18),(x+2,20));line(f'eye-{x}-b',(x-2,20),(x+2,18));join(f'eye-{x}-a',f'eye-{x}-b')
line('pin',(6,6),(10,12));join('pin','doll')
''','Original sewn doll and pin; smooth curve construction, upright reduction for readable crossed eyes.')
