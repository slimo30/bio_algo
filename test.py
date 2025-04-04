import time
import random
import pandas as pd
from tabulate import tabulate
from mp import morris_pratt
from bm import boyer_moore



def generer_sequence_adn(taille):
    # Génère une séquence ADN aléatoire (texte de recherche)
    # Utilisée pour simuler une séquence réaliste avec les bases A, G, C, T
    return ''.join(random.choice("AGCT") for _ in range(taille))

def generer_motif_meilleur_cas_mp(taille):
    # Meilleur cas pour l'algorithme Morris-Pratt (MP)
    # Motif sans structure répétitive → table des bords avec uniquement des zéros
    # Cela signifie qu'aucun préfixe n'est aussi un suffixe → pas de retour en arrière
    # Résultat : comparaisons rapides et décalages immédiats
    bases = list("AGCT")
    result = ""
    while len(result) < taille:
        random.shuffle(bases)
        result += ''.join(bases)
    return result[:taille]

def generer_motif_pire_cas_mp(taille):
    # Pire cas pour l'algorithme MP
    # Motif avec une seule lettre répétée (ex: "AAAAA") → forte redondance
    # Cela entraîne de nombreux sous-calculs sur la table des préfixes
    return 'A' * taille

def generer_motif_meilleur_cas_bm(taille):
    # Meilleur cas pour l'algorithme Boyer-Moore (BM)
    # Caractère final différent (ex: "AAAAAG") → décalage maximal après chaque échec
    # Comparaison de droite à gauche échoue tôt, donc grands sauts
    if taille > 1:
        return 'A' * (taille - 1) + 'G'
    else:
        return 'G'

def generer_motif_pire_cas_bm(taille):
    # Pire cas pour l'algorithme BM
    # Motif très répétitif (ex: "AAAAA") → faibles possibilités de décalage
    # BM ne peut pas faire de grands sauts, donc ralentissement
    return 'A' * taille


def tester_algorithmes():
    tailles_texte = [1000, 10000, 100000, 500000, 1000000]
    tailles_motif = [5, 10, 20, 50, 100, 200]
    
    resultats = []
    
    for n in tailles_texte:
        for m in tailles_motif:
            texte = generer_sequence_adn(n)
            motif = generer_motif_meilleur_cas_mp(m)
            
            debut = time.time()
            positions, mp_comparaisons = morris_pratt(texte, motif)
            mp_temps = time.time() - debut
            
            debut = time.time()
            positions, bm_comparaisons = boyer_moore(texte, motif)
            bm_temps = time.time() - debut
            
            resultats.append({
                'Cas': 'Meilleur cas MP',
                'Taille texte': n,
                'Taille motif': m,
                'MP comparaisons': mp_comparaisons,
                'MP temps (s)': mp_temps,
                'BM comparaisons': bm_comparaisons,
                'BM temps (s)': bm_temps
            })
    
    
    print("Test du pire cas pour Morris-Pratt...")
    for n in tailles_texte:
        for m in tailles_motif:
            texte = 'A' * n  
            motif = generer_motif_pire_cas_mp(m)
            
            
            debut = time.time()
            positions, mp_comparaisons = morris_pratt(texte, motif)
            mp_temps = time.time() - debut
            
            
            debut = time.time()
            positions, bm_comparaisons = boyer_moore(texte, motif)
            bm_temps = time.time() - debut
            
            resultats.append({
                'Cas': 'Pire cas MP',
                'Taille texte': n,
                'Taille motif': m,
                'MP comparaisons': mp_comparaisons,
                'MP temps (s)': mp_temps,
                'BM comparaisons': bm_comparaisons,
                'BM temps (s)': bm_temps
            })
    
    
    print("Test du meilleur cas pour Boyer-Moore...")
    for n in tailles_texte:
        for m in tailles_motif:
            
            texte = 'A' * n
            motif = generer_motif_meilleur_cas_bm(m)
            
            
            debut = time.time()
            positions, mp_comparaisons = morris_pratt(texte, motif)
            mp_temps = time.time() - debut
            
            
            debut = time.time()
            positions, bm_comparaisons = boyer_moore(texte, motif)
            bm_temps = time.time() - debut
            
            resultats.append({
                'Cas': 'Meilleur cas BM',
                'Taille texte': n,
                'Taille motif': m,
                'MP comparaisons': mp_comparaisons,
                'MP temps (s)': mp_temps,
                'BM comparaisons': bm_comparaisons,
                'BM temps (s)': bm_temps
            })
    
    
    print("Test du pire cas pour Boyer-Moore...")
    for n in tailles_texte:
        for m in tailles_motif:
            texte = 'A' * n
            motif = generer_motif_pire_cas_bm(m)
            
            
            debut = time.time()
            positions, mp_comparaisons = morris_pratt(texte, motif)
            mp_temps = time.time() - debut
            
            
            debut = time.time()
            positions, bm_comparaisons = boyer_moore(texte, motif)
            bm_temps = time.time() - debut
            
            resultats.append({
                'Cas': 'Pire cas BM',
                'Taille texte': n,
                'Taille motif': m,
                'MP comparaisons': mp_comparaisons,
                'MP temps (s)': mp_temps,
                'BM comparaisons': bm_comparaisons,
                'BM temps (s)': bm_temps
            })
    
    
    print("Test avec des séquences ADN aléatoires...")
    for n in tailles_texte:
        for m in tailles_motif:
            
            texte = generer_sequence_adn(n)
            motif = generer_sequence_adn(m)
            
            
            debut = time.time()
            positions, mp_comparaisons = morris_pratt(texte, motif)
            mp_temps = time.time() - debut
            
            
            debut = time.time()
            positions, bm_comparaisons = boyer_moore(texte, motif)
            bm_temps = time.time() - debut
            
            resultats.append({
                'Cas': 'Séquences ADN aléatoires',
                'Taille texte': n,
                'Taille motif': m,
                'MP comparaisons': mp_comparaisons,
                'MP temps (s)': mp_temps,
                'BM comparaisons': bm_comparaisons,
                'BM temps (s)': bm_temps
            })
    
    
    df = pd.DataFrame(resultats)
    
    
    df['Ratio comparaisons (BM/MP)'] = df['BM comparaisons'] / df['MP comparaisons']
    df['Ratio temps (BM/MP)'] = df['BM temps (s)'] / df['MP temps (s)']
    
    
    print("\nRésultats des tests :")
    tableau = tabulate(df, headers='keys', tablefmt='grid', showindex=False)
    print(tableau)
    
    
    print("\nAnalyse des résultats :")
    
    print("\nMeilleur cas pour Morris-Pratt :")
    meilleur_mp = df[df['Cas'] == 'Meilleur cas MP'].sort_values(by='MP comparaisons')
    print(tabulate(meilleur_mp[['Taille texte', 'Taille motif', 'MP comparaisons', 'BM comparaisons', 'Ratio comparaisons (BM/MP)']], 
                   headers='keys', tablefmt='grid', showindex=False))
    
    print("\nMeilleur cas pour Boyer-Moore :")
    meilleur_bm = df[df['Cas'] == 'Meilleur cas BM'].sort_values(by='BM comparaisons')
    print(tabulate(meilleur_bm[['Taille texte', 'Taille motif', 'MP comparaisons', 'BM comparaisons', 'Ratio comparaisons (BM/MP)']], 
                   headers='keys', tablefmt='grid', showindex=False))
    
    print("\nPire cas pour Morris-Pratt :")
    pire_mp = df[df['Cas'] == 'Pire cas MP'].sort_values(by='MP comparaisons', ascending=False)
    print(tabulate(pire_mp[['Taille texte', 'Taille motif', 'MP comparaisons', 'BM comparaisons', 'Ratio comparaisons (BM/MP)']], 
                   headers='keys', tablefmt='grid', showindex=False))
    
    print("\nPire cas pour Boyer-Moore :")
    pire_bm = df[df['Cas'] == 'Pire cas BM'].sort_values(by='BM comparaisons', ascending=False)
    print(tabulate(pire_bm[['Taille texte', 'Taille motif', 'MP comparaisons', 'BM comparaisons', 'Ratio comparaisons (BM/MP)']], 
                   headers='keys', tablefmt='grid', showindex=False))
    
    print("\nCas avec résultats semblables (séquences ADN aléatoires) :")
    
    cas_semblables = df[(df['Ratio comparaisons (BM/MP)'] > 0.9) & (df['Ratio comparaisons (BM/MP)'] < 1.1)]
    if len(cas_semblables) > 0:
        print(tabulate(cas_semblables[['Cas', 'Taille texte', 'Taille motif', 'MP comparaisons', 'BM comparaisons', 'Ratio comparaisons (BM/MP)']], 
                    headers='keys', tablefmt='grid', showindex=False))
    else:
        print("Aucun cas avec des performances vraiment similaires n'a été trouvé.")
        
        alea = df[df['Cas'] == 'Séquences ADN aléatoires']
        print(tabulate(alea[['Taille texte', 'Taille motif', 'MP comparaisons', 'BM comparaisons', 'Ratio comparaisons (BM/MP)']], 
                    headers='keys', tablefmt='grid', showindex=False))
    
    return df

if __name__ == "__main__":
    print("Analyse comparative des algorithmes de Morris-Pratt et de Boyer-Moore sur des séquences ADN")
    df = tester_algorithmes()
    
    
    df.to_csv('resultats_comparaison_mp_bm.csv', index=False)
    print("\nLes résultats ont été sauvegardés dans le fichier 'resultats_comparaison_mp_bm.csv'")