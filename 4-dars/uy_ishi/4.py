set1={'olma', 'anor', 'youtube', 'instagram', 'gilos'}
set2={'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
set3={'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}
set1=set1.intersection(set2)
set3=set1.difference(set3)
print(set3)