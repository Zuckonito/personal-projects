#Author: Sebastian Medina
#I added a new feature, if the user inputs a known compound, the program will show the name, if not, it will show "Unknown compound (not in the known compounds list)"
#In the return at get_known_compound_name theres a .get, this checks to see if there is a value for the key, if not it will return the second argument,
# which is the string "Unknown compound (not in the known compounds list)"
from formula import parse_formula


def main():

    formula = input("Enter the molecular formula of the sample: ")

    sample_mass = float(input("Enter the mass in grams of the sample: "))

    periodic_table = make_periodic_table()

    symbol_quantity_list = parse_formula(formula, periodic_table)

    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

    moles = sample_mass / molar_mass

    compound_name = get_known_compound_name(formula)
    
    print(f"{molar_mass:.5f} grams/mole")
    print(f"{moles:.5f} moles")
    print(f"Compound: {compound_name}")

def make_periodic_table():

    periodic_table_dict = {
        "Ac": ["Actinium", 227],
        "Ag": ["Silver", 107.8682],
        "Al": ["Aluminum", 26.9815386],
        "Ar": ["Argon", 39.948],
        "As": ["Arsenic", 74.9216],
        "At": ["Astatine", 210],
        "Au": ["Gold", 196.966569],
        "B": ["Boron", 10.811],
        "Ba": ["Barium", 137.327],
        "Be": ["Beryllium", 9.012182],
        "Bi": ["Bismuth", 208.9804],
        "Br": ["Bromine", 79.904],
        "C": ["Carbon", 12.0107],
        "Ca": ["Calcium", 40.078],
        "Cd": ["Cadmium", 112.411],
        "Ce": ["Cerium", 140.116],
        "Cl": ["Chlorine", 35.453],
        "Co": ["Cobalt", 58.933195],
        "Cr": ["Chromium", 51.9961],
        "Cs": ["Cesium", 132.9054519],
        "Cu": ["Copper", 63.546],
        "Dy": ["Dysprosium", 162.5],
        "Er": ["Erbium", 167.259],
        "Eu": ["Europium", 151.964],
        "F": ["Fluorine", 18.9984032],
        "Fe": ["Iron", 55.845],
        "Fr": ["Francium", 223],
        "Ga": ["Gallium", 69.723],
        "Gd": ["Gadolinium", 157.25],
        "Ge": ["Germanium", 72.64],
        "H": ["Hydrogen", 1.00794],
        "He": ["Helium", 4.002602],
        "Hf": ["Hafnium", 178.49],
        "Hg": ["Mercury", 200.59],
        "Ho": ["Holmium", 164.93032],
        "I": ["Iodine", 126.90447],
        "In": ["Indium", 114.818],
        "Ir": ["Iridium", 192.217],
        "K": ["Potassium", 39.0983],
        "Kr": ["Krypton", 83.798],
        "La": ["Lanthanum", 138.90547],
        "Li": ["Lithium", 6.941],
        "Lu": ["Lutetium", 174.9668],
        "Mg": ["Magnesium", 24.305],
        "Mn": ["Manganese", 54.938045],
        "Mo": ["Molybdenum", 95.96],
        "N": ["Nitrogen", 14.0067],
        "Na": ["Sodium", 22.98976928],
        "Nb": ["Niobium", 92.90638],
        "Nd": ["Neodymium", 144.242],
        "Ne": ["Neon", 20.1797],
        "Ni": ["Nickel", 58.6934],
        "Np": ["Neptunium", 237],
        "O": ["Oxygen", 15.9994],
        "Os": ["Osmium", 190.23],
        "P": ["Phosphorus", 30.973762],
        "Pa": ["Protactinium", 231.03588],
        "Pb": ["Lead", 207.2],
        "Pd": ["Palladium", 106.42],
        "Pm": ["Promethium", 145],
        "Po": ["Polonium", 209],
        "Pr": ["Praseodymium", 140.90765],
        "Pt": ["Platinum", 195.084],
        "Pu": ["Plutonium", 244],
        "Ra": ["Radium", 226],
        "Rb": ["Rubidium", 85.4678],
        "Re": ["Rhenium", 186.207],
        "Rh": ["Rhodium", 102.9055],
        "Rn": ["Radon", 222],
        "Ru": ["Ruthenium", 101.07],
        "S": ["Sulfur", 32.065],
        "Sb": ["Antimony", 121.76],
        "Sc": ["Scandium", 44.955912],
        "Se": ["Selenium", 78.96],
        "Si": ["Silicon", 28.0855],
        "Sm": ["Samarium", 150.36],
        "Sn": ["Tin", 118.71],
        "Sr": ["Strontium", 87.62],
        "Ta": ["Tantalum", 180.94788],
        "Tb": ["Terbium", 158.92535],
        "Tc": ["Technetium", 98],
        "Te": ["Tellurium", 127.6],
        "Th": ["Thorium", 232.03806],
        "Ti": ["Titanium", 47.867],
        "Tl": ["Thallium", 204.3833],
        "Tm": ["Thulium", 168.93421],
        "U": ["Uranium", 238.02891],
        "V": ["Vanadium", 50.9415],
        "W": ["Tungsten", 183.84],
        "Xe": ["Xenon", 131.293],
        "Y": ["Yttrium", 88.90585],
        "Yb": ["Ytterbium", 173.054],
        "Zn": ["Zinc", 65.38],
        "Zr": ["Zirconium", 91.224],
    }
    return periodic_table_dict


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):

    symbol_index = 0
    quantity_index = 1
    atomic_mass_index = 1

    total_molar_mass = 0.0

    for element in symbol_quantity_list:
        symbol = element[symbol_index]
        quantity = element[quantity_index]

        element_info = periodic_table_dict[symbol]
        atomic_mass = element_info[atomic_mass_index]

        total_molar_mass += atomic_mass * quantity

    return total_molar_mass

def get_known_compound_name(formula):

    known_compounds = {
        "H2O": "Water",
        "C6H12O6": "Glucose",
        "C6H6": "Benzene",
        "NaCl": "Sodium Chloride (Table Salt)",
        "CO2": "Carbon Dioxide",
        "NH3": "Ammonia",
        "CH4": "Methane",
        "C12H22O11": "Sucrose (Sugar)",
        "C2H5OH": "Ethanol",
        "HCl": "Hydrochloric Acid"
    }
    
    return known_compounds.get(formula, "Unknown compound (not in the known compounds list)")


if __name__ == "__main__":
    main()