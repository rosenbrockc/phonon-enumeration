#!/usr/bin/env python

def _make_structures(args):
    """Makes a VASP POSCAR file for the desired structures."""
    from phenum.io_utils import read_enum_out, write_POSCAR
    from phenum.vector_utils import map_enumStr_to_real_space, cartesian2direct

    (system, structure_data) = read_enum_out(args)

    # for each structure write the vasp POSCAR
    for structure in structure_data:
        
        # space_data is a dictionary containing the spacial data for
        # the structure
        space_data = map_enumStr_to_real_space(system,structure,args["mink"])

        space_data["aBas"] = cartesian2direct(space_data["sLV"],space_data["aBas"],
                                              system["eps"])
        
        write_POSCAR(system,space_data,structure)
        

def _examples():
    """Print some examples on how to use this python version of the code."""
    helptext = ("For all the examples below, it is assumed that you have already "
                "compiled the modified enumlib code as described in the "
                "README or in some other manner obtained the HNFs (supercells) and "
                "their symmetry groups. You will then need to specify if you are "
                "obtaining the number of unique arrangements for each supercell and "
                "concentration allowed for your system or enumerating (finding) the "
                "desired number of configurations for each HNF and concentration. "
                "Additionally you way change the default input file names to ones of "
                "your own creation.")
    egs = [("Find the Polya distribution",
            "The code below finds the number of unique arrangements for each "
            "supercell (HNF) for a binary system on an fcc lattice which can have "
            "1 to 11 atoms in the supercell as described in the lattice.in found in "
            "input/fcc sample directory. The files labeled cell.n contain the HNFs "
            "and symmetry group for the supercells of size n and were generated by "
            "the modified enum.x code. For more information on the contents of this "
            "folder please see the README. To a different input file to use rather "
            "than lattice.in use the -lattice option or if you have the HNF and "
            "symmetry group data in a different file then cells.n then use "
            "-dataformat.","enumeration.py -polya"),
           ("Construct an enum.in file before running the -enum mode",
            "This code assumes that the -polya mode has arleady been run. It takes two"
            " arguments; the first is the disered distribution type ('size', 'conc',"
            " 'shape', 'all'), the second is the desired number of structures, if all"
            " the structures are wanted then the second argument should be 'all'.",
            "enumeration.py -distribution all all \n  enumeration.py -distribution "
            " size 200")]
    print("MAKES A VASP POSCAR FOR THE DESIRED STRUCTUR\n")
    for eg in egs:
        title, desc, code = eg
        print("--" + title + '--\n')
        print(desc + '\n')
        print('  ' + code + '\n')

def _parser_options(phelp=False):
    """Parses the options and arguments from the command line."""
    import argparse
    parser = argparse.ArgumentParser(description="Partial Superstructure Enumeration Code")
    parser.add_argument("structures", type=int, nargs ="+",
                        help="The desired structure numbers from the enum.out file")
    parser.add_argument("-debug", action="store_true",
                        help="Print verbose calculation information for debugging.")
    parser.add_argument("-examples", action="store_true",
                        help="Print some examples for how to use the enumeration code.")
    parser.add_argument("-displacement", type=float,
                        help=("The displacement amount for the arrows. Default is 0."))
    parser.add_argument("-input",
                        help=("Override the default 'enum.out' file name."))
    parser.add_argument("-mink", 
                        help=("Sets flag to perform minkowski reduction of the basis (T/F)."
                              " Default is True."))
    parser.add_argument("-verbose", type=int,
                        help="Specify the verbosity level (1-3) for additional computation info.")
    parser.add_argument("-outfile",
                        help=("Override the default output file names: 'vasp.{structure#}'" 
                              "for the structures."))
    vardict = vars(parser.parse_args())
    if phelp or vardict["examples"]:
        _examples()
        exit(0)

    if vardict["verbose"]:
        from phenum.msg import set_verbosity
        set_verbosity(vardict["verbose"])

    if vardict["mink"]:
        if vardict["mink"].lower() == "t":
            vardict["mink"] = True
        elif vardict["mink"].lower() == "f":
            vardict["mink"] = False
        else:
            from msg import err
            err("The -mink parameter only takes arguments of T or F")
    else:
        vardict["mink"] = True
            
    if not vardict["input"]:
        vardict["input"] = "enum.out"
    if not vardict["outfile"]:
        vardict["outfile"] = "vasp.{}"
    return vardict

def _script_enum(args):
    """Generates the vasp output file for the desired structure.
    """
    from os import path, system
            
    _make_structures(args)
        
if __name__ == '__main__':
    _script_enum(_parser_options())
