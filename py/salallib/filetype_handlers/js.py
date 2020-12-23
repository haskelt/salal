from salallib.utilities import utilities

class ProcessJS:
    
    #---------------------------------------------------------------------------

    name = '.js'
    
    #---------------------------------------------------------------------------

    @classmethod
    def process (cls, source_dir, target_dir, file_stem):
        utilities.substitute_variables(source_dir, target_dir, file_stem + '.js')
    
    #---------------------------------------------------------------------------

handler = ProcessJS
