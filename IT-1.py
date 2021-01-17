import csv
date=[]
time=[]
price=[]
with open ("new.csv", newline = '') as csvfile:       
    c = csv.DictReader(csvfile)
    for d in c:
        date.append(d['date'])
        time.append(d['time'])
        price.append(float(d['price']))
max=max(price)
nmax=price.index(max)
min=min(price)
nmin=price.index(min)
r=str(int(float(max)-float(min)))
datemin=date[nmin]
datemin=(datemin[:4]+'.'+datemin[4:6]+'.'+datemin[6:])
timemin=time[nmin]
timemin=(timemin[:2]+':'+timemin[2:4])
timemax=time[nmax]
timemax=(timemax[:2]+':'+timemax[2:4])
datemax=date[nmax]
datemax=(datemax[:4]+'.'+datemax[4:6]+'.'+datemax[6:])
print('Покупаем акции '+datemin+' в '+timemin+', продаём '+datemax+' в '+timemax+', акции подорожают на '+r)