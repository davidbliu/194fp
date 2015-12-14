from os import listdir
from os.path import isfile, join

def getFnames(mypath):
    fnames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    fnames = ['\"' + mypath + f + '\"' for f in fnames]
    return fnames

jsStr = ''
# mypath = './images/coneFountain/'
for path in ['coneFountain', 'simon', 'both', 'still']:
    mypath = './images/'+path+'/'
    fnames = getFnames(mypath)
    jsStr += 'var '+path + ' = [' + ','.join(fnames) + '];'
    jsStr += '\n\n'

with open('fnames.js', 'wb') as ofile:
    ofile.write(jsStr)
