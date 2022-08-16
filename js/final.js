$( function() {
    var availableTagsResidue = [
        "ALA",
        "ARG",
	"ASN",
	"ASP",
	"CYS",
	"GLN",
	"GLU",
	"GLY",
	"GOL",
	"HIS",
	"HOH",
	"ILE",
	"LEU",
	"LYS",
	"MET",
	"PRO",
	"PHE",
	"SER",
	"THR",
	"TYR",
	"VAL",
        "TRP"
    ];
    $( "#residue" ).autocomplete({
      source: availableTagsResidue
    });
});


$( function() {
    var availableTagsProtein = [
        "1USU",
        "1USV"
    ];
    $( "#protein_id" ).autocomplete({
      source: availableTagsProtein
    });
});
