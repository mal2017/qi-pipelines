#!/ark/home/ml290/miniconda3/envs/py35/bin/python
import snakemake
from optparse import OptionParser
import pipeline_helpers as ph
import sys

## get mode
try:
    MODE = sys.argv[1]
except IndexError:
    print('Please add a mode and options and try again.')
    sys.exit()
if (MODE != "configure") & (MODE != "analyze"):
    print('Please add a valid mode and options and try again.')
    sys.exit()

def configure():

    ## get user options
    parser = OptionParser()
    parser.add_option("-e","--existing-configfile",dest="configfile",help="path to configuration file if it exists",default=None)
    parser.add_option("-d","--datatables",dest="datatables",help="a list of semicolon separated pairs of comma separated pairs. e.g. <assay type 1,dt1>;[assay type 2,dt2]")
    #http://stackoverflow.com/questions/4934806/how-can-i-find-scripts-directory-with-python
    parser.add_option("-s","--snakedir",dest="snakedir",help="enter directories with your workflows, separated by commas",default=sys.path[0])
    options, args = parser.parse_args()
    configfile = options.configfile
    datatables = {x.split(',')[0]:x.split(',')[1] for x in options.datatables.split(';')} 
    snakedir = options.snakedir.split(',')
    ph.yamlize(datatable_dict=datatables,configfile=configfile,snakedir=snakedir)

    
    
def analyze():
    pass
    ## get user options






## steps config mode
# load info
# load yaml
# update yaml config
# reload yaml config

## steps analyze mode
# load yaml
# call indiv analysis
# call group analysis
# call differential analysis of groups




def main():
    if MODE=='configure':
        configure()



main()
