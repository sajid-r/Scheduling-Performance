# allow access to os.system and os.remove
# run lab_7.py with the required overheads and quanta
# combine the output files into summary.txt
# remove the files created by line two
import os
[os.system('python /home/sajid/Documents/HackerRank/project/simulator.py  %s %s /home/sajid/Documents/HackerRank/project/data.txt > results_%s_%s.txt'
           % (overhead, quanta, overhead, quanta))
 for overhead in range(0, 30, 5) for quanta in (50, 100, 250, 500)]
file('summary.txt', 'w').write('=========================\n'.join(
    [''] + [file('results_%s_%s.txt' % (overhead, quanta)).read()
            for overhead in range(0, 30, 5) for quanta in (50, 100, 250, 500)]
    + [''])[:-1])
[os.remove('results_%s_%s.txt' % (overhead, quanta))
 for overhead in range(0, 30, 5) for quanta in (50, 100, 250, 500)]
