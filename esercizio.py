voto_alunni={
    "Mario":{"matematica":6, "italiano":6,"scienze":7,"inglese":4},
    "Giovanni":{"matematica":4,"italiano":6,"scienze":5,"inglese":7},
    "Paola":{"matematica":9,"italiano":6,"scienze":8,"inglese":8}
    }
alunno=input("Di chi si vuole visualizzare la media? (Mario, Giovanni e Paola)")
a=voto_alunni[alunno].values()
totale=sum(a)
media_voti=totale/4
print("La media voti di",alunno,"è",media_voti)
