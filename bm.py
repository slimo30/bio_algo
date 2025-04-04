def creer_bad_char_tableau(motif):
    m = len(motif)
    bad_char = {}
    
    for i in range(m - 1):  
        bad_char[motif[i]] = m - 1 - i

    # print("Tableau Dictionnaire (Bad Character) :")
    # print(bad_char)
    
    return bad_char

def boyer_moore(texte, motif):
 
    n = len(texte)
    m = len(motif)
    
    
        
    if m <= 0:
        return [], 0  

    
    bad_char = creer_bad_char_tableau(motif)

    
    
    positions = []
    nb_comparaisons = 0
    i = m - 1  
    
    while i < n:
        j = 0
        while j < m and motif[m - 1 - j] == texte[i - j]:
            nb_comparaisons += 1
            j += 1
        
        if j == m:
            
            positions.append(i - m + 1)
            i += 1  
        else:
            
            nb_comparaisons += 1
            
            char = texte[i - j]
            
            
            shift = bad_char.get(char, m)
            
            
            i += max(1, shift - j)
    
    
    return positions, nb_comparaisons


def main():
    texte = "CTTGAGCTTCGAAATCGATTGAGCTT"
    motif = "AGCTT"
    
    positions, nb_comparaisons = boyer_moore(texte, motif)
    
    
    if positions:
        print(f"\nPositions des occurrences trouvées : {positions}")
    else:
        print("\nAucune occurrence trouvée.")
    
    print(f"Nombre de comparaisons effectuées : {nb_comparaisons}")

if __name__ == "__main__":
    main()