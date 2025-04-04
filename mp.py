def calculer_tableau_bords(motif):
  
    m = len(motif)
    bords = [0] * m
    
    
    bords[0] = 0
    longueur = 0
    i = 1
    
    while i < m:
        if motif[i] == motif[longueur]:
            
            longueur += 1
            bords[i] = longueur
            i += 1
        elif longueur > 0:
            
            longueur = bords[longueur - 1]
        else:
            
            bords[i] = 0
            i += 1


    return bords

def morris_pratt(texte, motif):

    n = len(texte)
    m = len(motif)
    
    if m <= 0:
        return [], 0  

  
    
    bords = calculer_tableau_bords(motif)
    # print("Tableau des bords:", " ".join(map(str, bords)))

    positions = []
    nb_comparaisons = 0

    i = 0  
    j = 0  
    
    while i < n:
        nb_comparaisons += 1
        
        if motif[j] == texte[i]:
            i += 1
            j += 1
            
            if j == m:
                positions.append(i - m)
                j = bords[j - 1]
        elif j > 0:
            
            j = bords[j - 1]
        else:
            i += 1
    # if positions:
    #     print(f"positions: {positions}")
    # else:
    #     print("Aucune occurrence")
    
    # print(f"comparaisons: {nb_comparaisons}")
    
    return positions, nb_comparaisons



def main():
    texte = "CTTGAGCTTCGAAATCGATTGAGCTT"
    motif = "AGCTT"
    
    calculer_tableau_bords(motif)
    positions, nb_comparaisons = morris_pratt(texte, motif)

if __name__ == "__main__":
    main()