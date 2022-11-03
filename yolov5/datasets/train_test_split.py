import numpy as np


##TODO Split train and test image

train_ratio = 0.9
val_ratio  = 0.1

def write_to_file(f, ls):
    with open(f, 'w') as fp:
        for t in ls:
        # write each item on a new line
            fp.write("%s\n" % t)
    print(f'Done wrting {f}')   

allFileNames = []
# read all files
f = open('all.txt')
for line in f:
    allFileNames.append(line)
f.close()
#shuffle names
np.random.shuffle(allFileNames)
train_FileNames, val_FileNames = np.split(np.array(allFileNames), int(train_ratio * len(allFileNames)))

write_to_file('train.txt', train_FileNames)
write_to_file('val.txt', val_FileNames)
