
function populateLoci(s1, s2) {
    // inserisce i valori dei loci appartenenti al tipo scelto
    s1 = document.getElementById(s1);
    s2 = document.getElementById(s2);
    var optionArray;

    s2.innerHTML = "--All Loci--";
    
    if (s1.value == "A") {
        optionArray = ["A|--All Loci--", 
        "MT-ATP6|MT-ATP6", 
        "MT-ATP8|MT-ATP8", 
        "MT-CO1|MT-CO1", 
        "MT-CO2|MT-CO2", 
        "MT-CO3|MT-CO3", 
        "MT-CYB|MT-CYB", 
        "MT-DLOOP|MT-DLOOP", 
        "MT-NC10|MT-NC10", 
        "MT-NC2|MT-NC2", 
        "MT-NC3|MT-NC3", 
        "MT-NC5|MT-NC5", 
        "MT-NC7|MT-NC7", 
        "MT-NC9|MT-NC9", 
        "MT-ND1|MT-ND1", 
        "MT-ND2|MT-ND2", 
        "MT-ND3|MT-ND3", 
        "MT-ND4|MT-ND4", 
        "MT-ND4L|MT-ND4L", 
        "MT-ND5|MT-ND5", 
        "MT-ND6|MT-ND6", 
        "MT-ORIL|MT-ORIL", 
        "MT-RNR1|MT-RNR1", 
        "MT-RNR2|MT-RNR2", 
        "MT-TA|MT-TA", 
        "MT-TC|MT-TC", 
        "MT-TD|MT-TD", 
        "MT-TE|MT-TE", 
        "MT-TF|MT-TF", 
        "MT-TG|MT-TG", 
        "MT-TH|MT-TH", 
        "MT-TI|MT-TI", 
        "MT-TK|MT-TK", 
        "MT-TL1|MT-TL1", 
        "MT-TL2|MT-TL2", 
        "MT-TM|MT-TM", 
        "MT-TN|MT-TN", 
        "MT-TP|MT-TP", 
        "MT-TQ|MT-TQ", 
        "MT-TR|MT-TR", 
        "MT-TS1|MT-TS1", 
        "MT-TS2|MT-TS2", 
        "MT-TT|MT-TT", 
        "MT-TV|MT-TV", 
        "MT-TW|MT-TW", 
        "MT-TY|MT-TY", ]; 
    } else if (s1.value == "CDS") {
        optionArray = ["A|--All Loci--", 
        "MT-ATP6|MT-ATP6", 
        "MT-ATP8|MT-ATP8", 
        "MT-CO1|MT-CO1", 
        "MT-CO2|MT-CO2", 
        "MT-CO3|MT-CO3", 
        "MT-CYB|MT-CYB", 
        "MT-ND1|MT-ND1", 
        "MT-ND2|MT-ND2", 
        "MT-ND3|MT-ND3", 
        "MT-ND4|MT-ND4", 
        "MT-ND4L|MT-ND4L", 
        "MT-ND5|MT-ND5", 
        "MT-ND6|MT-ND6", ]; 
    } else if (s1.value == "reg") {
        optionArray = ["A|--All Loci--", 
        "MT-DLOOP|MT-DLOOP", 
        "MT-NC10|MT-NC10", 
        "MT-NC2|MT-NC2", 
        "MT-NC3|MT-NC3", 
        "MT-NC5|MT-NC5", 
        "MT-NC7|MT-NC7", 
        "MT-NC9|MT-NC9", 
        "MT-ORIL|MT-ORIL", ]; 
    } else if (s1.value == "rRNA") {
        optionArray = ["A|--All Loci--", 
        "MT-RNR1|MT-RNR1", 
        "MT-RNR2|MT-RNR2", ]; 
    } else if (s1.value == "tRNA") {
        optionArray = ["A|--All Loci--", 
        "MT-TA|MT-TA", 
        "MT-TC|MT-TC", 
        "MT-TD|MT-TD", 
        "MT-TE|MT-TE", 
        "MT-TF|MT-TF", 
        "MT-TG|MT-TG", 
        "MT-TH|MT-TH", 
        "MT-TI|MT-TI", 
        "MT-TK|MT-TK", 
        "MT-TL1|MT-TL1", 
        "MT-TL2|MT-TL2", 
        "MT-TM|MT-TM", 
        "MT-TN|MT-TN", 
        "MT-TP|MT-TP", 
        "MT-TQ|MT-TQ", 
        "MT-TR|MT-TR", 
        "MT-TS1|MT-TS1", 
        "MT-TS2|MT-TS2", 
        "MT-TT|MT-TT", 
        "MT-TV|MT-TV", 
        "MT-TW|MT-TW", 
        "MT-TY|MT-TY", ]; 
    }

    for (var option in optionArray) {
        var pair = optionArray[option].split("|");
        var newOption = document.createElement("option");

        newOption.value = pair[0];
        newOption.innerHTML = pair[1];
        s2.options.add(newOption);
    }
}

