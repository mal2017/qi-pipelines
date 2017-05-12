#; -*-python3-*- 
#!/ark/home/ml290/miniconda3/envs/py35/bin/python
import yaml
import readline
import glob
import sys
def get_sample_info(datatable,assay):
        with open(datatable,'r') as dt:
                samples=[x.strip().split() for x in dt.readlines()[1:]]
        datadict={}
        for samp in samples:
                datadict[samp[3]]={}
                datadict[samp[3]]['bam']=samp[0]+samp[1]+'_'+samp[2]+'.sorted.bam'
                fastqs = samp[7].split('::')
                if len(fastqs)>1:
                        datadict[samp[3]]['fastq']=fastqs[0]
                        datadict[samp[3]]['fastqpair']=fastqs[1]
                else:
                        datadict[samp[3]]['fastq']=samp[7]
                        datadict[samp[3]]['fastqpair']=None  
                datadict[samp[3]]['genome']=samp[2]
                datadict[samp[3]]['input']=samp[4]
                datadict[samp[3]]['linked_bam']=samp[3]+'.sorted.bam'
                datadict[samp[3]]['linked_fastq']='R1_'+samp[3]+'.fastq.gz'
                datadict[samp[3]]['rx_bam']=None
                if datadict[samp[3]]['fastqpair']:
                        datadict[samp[3]]['linked_fastqpair']='R2_'+samp[3]+'.fastq.gz'
                else:
                        datadict[samp[3]]['linked_fastqpair']=None
        return datadict

def yamlize(datatable_dict=None,configfile=None,snakedir=None):
        """ DOCSTRING: reads datatables and updates your config file as necessary, or prompts you for downstream options. """
        all_data_dict = {x:get_sample_info(datatable_dict[x],x) for x in datatable_dict if datatable_dict[x]}
        assays = all_data_dict.keys()
        all_samples = []
        for a in assays:
                for library in all_data_dict[a].keys():
                        if 'input' not in library:
                                all_samples.append(library)
        all_config_dict = {'assays':all_data_dict, 'all_samples':all_samples}

        if not configfile:
                configfile = 'config/config.yaml'
                #http://stackoverflow.com/questions/38987/how-to-merge-two-python-dictionaries-in-a-single-expression
                all_config_dict = {**all_config_dict,**get_run_options(assays)}
                update_message = "config file {a} created".format(a=configfile)

        elif configfile:
                try:
                        with open(configfile,'r') as f:
                                old_options = yaml.safe_load(f)
                                all_config_dict = {**all_config_dict,**old_options}
                                update_message = "config file {a} updated".format(a=configfile)
                except FileNotFoundError:
                        print("looks like your config file doesn't exist!")
                        sys.exit()

        ## TODO: user input, ask if you'd like to add run options
        
        with open(configfile,'w') as f:
                yaml.dump(all_config_dict,f,default_flow_style=False)

        print(update_message)
        
        ## TODO: add user input query for assay specific run params here

        
        #http://stackoverflow.com/questions/6656819/filepath-autocompletion-using-users-input
        #readline.set_completer


## TODO: add way to update with rx genome info
def get_run_options(assays):
        """ get all user options for all possible analyses """
        pipelines = {'macs14':None,
                             'macs2':None,
                             'rose':None,
                             'homer':None,
                             'crc':None,
                             'drose':None
                             }
        
        options = {a:pipelines for a in assays}

        return {}
