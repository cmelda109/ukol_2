import csv

# Ošetření nulových a záporných dat ve sloupci průtoků
with open("vstup.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    for row in reader:
        try:
            if float(row[-1]) == 0:
                print((f"Vstupní data ze dne {row[2]}.{row[3]}.{row[4]} obsahují nulový průtok"))
            elif float(row[-1]) < 0:
                print((f"Vstupní data ze dne {row[2]}.{row[3]}.{row[4]} obsahují záporný průtok"))
        except:
            pass 
   
# definovani proměnných    
prutoky_tyden = 0               
radky_tyden = 0 
rok = 0
prutoky_rok = 0
radky_rok = 0

try:
    # Sedmidenní průměry
    with open("vstup.csv", encoding="utf-8") as f,\
        open("vystup_7dni.csv", "w", newline='', encoding="utf-8") as fout:
        reader = csv.reader(f, delimiter = ",")
        writer = csv.writer(fout)                     
        
        # procházeni jednotlivých řádku, kumulace řádků a průtoků
        for row in reader:      
            radky_tyden += 1
            prutoky_tyden += float(row[-1]) 

            # prvni radek ze sedmi se ulozi do promenne vytiskni                                  
            if radky_tyden % 7 == 1:                                    
                vytiskni = row[0:-1]

            # pokud narazi na sedmy radek, vypise sedmidenni prumer, na konci se vynulují řádky a průtoky 
            if radky_tyden  == 7:                                        
                prumer_tyden = (f'{(prutoky_tyden/7):.4f}')   
                vytiskni.append(prumer_tyden)            
                writer.writerow(vytiskni)           
                prutoky_tyden = 0
                radky_tyden = 0

        # pokud se na konci nachází méně, jak 7 řádků, vypočítá se průměr pouze z nich
        if (radky_tyden-1) % 7 != 6:                                           
            prumer_prutok_tyden_zbytek = prutoky_tyden / radky_tyden
            zbytek = (f"{prumer_prutok_tyden_zbytek:.4f}")
            vytiskni.append(zbytek) 
            writer.writerow(vytiskni)

    # Roční průměry
    with open("vstup.csv", encoding="utf-8") as f,\
        open("vystup_rok.csv", "w", newline='', encoding="utf-8") as fout:
        reader = csv.reader(f, delimiter = ",")
        writer = csv.writer(fout)

        # procházeni jednotlivých řádku, kumulace řádků a průtoků    
        for row in reader:                                              
            
            # Uložení prvního řádku do proměnné vytiskni2, určení min a max podle prvního řádku, definování současného průtoku
            if rok == 0:                                            
                vytiskni2 = row[0:-1]                               
                prutok_max_radek = row                              
                prutok_min_radek = row 
                prutok_max = float(row[-1]) 
                prutok_min = float(row[-1]) 
            soucasny_prutok = float(row[-1])

            # Definování dalšího roku
            if rok != int(row[4]) and rok !=0:                      
                prumer_rok = (f'{(prutoky_rok/radky_rok):.4f}')
                vytiskni2.append(prumer_rok)
                writer.writerow(vytiskni2)
                prutoky_rok = 0
                radky_rok = 0 
                vytiskni2 = row[0:-1]

            # Porovnávání současného průtoku s max a min průtokem
            if soucasny_prutok > prutok_max:
                prutok_max_radek = row
                prutok_max = soucasny_prutok
            if soucasny_prutok < prutok_min:
                prutok_min_radek = row
                prutok_min = soucasny_prutok
            
            radky_rok += 1
            prutoky_rok +=  float(row[5])
            rok = int(row[4]) 

        # Dopočítání zbylých dní
        zbyle_dny_prumer = (f'{(prutoky_rok/radky_rok):.4f}')
        vytiskni2.append((zbyle_dny_prumer)) 
        writer.writerow(vytiskni2)

        print(f"Nejvyšší průtok byl dne {prutok_max_radek[4]}.{prutok_max_radek[3]}.{prutok_max_radek[2]}: {prutok_max}")
        print(f"Nejnižší průtok byl dne {prutok_min_radek[4]}.{prutok_min_radek[3]}.{prutok_min_radek[2]}: {prutok_min}")

# Ošetření dalších chyb vstupního souboru
except FileNotFoundError:
    print("Vstupní soubor nenalezen")
    exit()
except PermissionError:
    print("Neoprávněný přístup")
    exit()
except IndexError:
    print ("Index seznamu je mimo rozsah")
    exit()
except ValueError:
    print(f"Vstupní data ze dne {row[2]}.{row[3]}.{row[4]} nejsou v číselném formátu")
    pass 

print("Úspěch!")


    
