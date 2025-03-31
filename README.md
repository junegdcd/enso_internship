# Enso Internship
Purpose : analyzing associated ocean dynamics, improving ENSO predictors, studying the impact of climate change on ENSO memory

# Ongoing tasks

## WEEK 3

Main goals : have clear view on the key topics of the interships, finish draft and fedorov, get in touch Jvay

### 250331

- read fedorov (:1) (6)
- aviso clt : finish correlation (code left in compare)
- maps aviso ctl
> The maps of the model / aviso comparisons will be useful, now! Another thing that may be interesting is to take a look at maps of the corr / regression coefficient of the thermocline depth (D20) to ssh interannual anomalies. Those are usually considered to give the same information, but we saw in our recent draft that they don't exactly, and examining a bit more where the comparison breaks down would be interresting...

## WEEK 2

###  0328

- ~~read paper science~~ (:8)
- ~~include jvay's remark on aviso-ctl~~ (finish plot w correlation, change and adopt functional architecture of code (left in compare), despecialize funcs)
- ~~read fedorov~~ (:1)

### 0327

- read article science (:6)
- compare aviso and ctl : ~~timmenoleap series~~, interpolation, ...?

### 0326

- read article science
- ~~download data from spirit~~
- Compare Aviso RSSH with CTL RSSH (time series : cor, rms-dif, std-of each) : either download data from spirit, either work with windows. Mean on boxes ?

### 0325 Tue

- ~~practice with hovmoeller plot~~ (finish colorbar)

- Work on Aviso maps : plot RSSH in N3
  -  cor, rms-dif, std-of each, skewness
  -  idem in N4
-  **Read** (Boulanger, science?)

### 0324 Mon

- ~~faire marcher les comits~~
- ~~Comparer : plot AVISO RSSH, plot ORA5 RSSH, compute correlation, rmse, std~~ (valider)
- get CTL SSH data on Spirit
  
Later :
- effectuer une validation du niveau de la mer dans la simulation de contrôle aux observations (=prise en main : **comparer sorties entre AVISO SSH et CTL SSH**
(explore memory experiment dataset in the following path on SPIRITX : /scratchx/fliu/data_to_June/)
), a validation of the CTL simulation sea level anomalies to AVISO observations (Maps: cor, rms-dif, std-of each; **time series in regions such as Niño3 and Niño4**). You can do similar things (just cor) for **comparisons between sea level and D20**
- Continuer explorer git Yyan (hovmoeller not pour pouvoir sélctionner N3 et N4)
- Read : 
  - read the Fedorov overview of linear equatorial wave theory,  
  - paper submitted to science 
  - later chap on model, types and climate change interactions, 
  - check chapters 6.13 (baroclinic modes), 11.5 and 11.6 (equatorial dynamics in the long wave approximation)

## Notes :

- diagnostiquer les vitesses de propagation en fonction de la latitude (dans le run de contrôle, les obs, mais aussi le run “mémoire” ou les propagations se voient mieux)
- effectuer des cartes de date d’arrivée dans Niño3.4, coloriées en fonction de la stabilité du système couplé
- chercher des indices optimaux de prédiction du prochain ENSO
- comparer les régions qui donnent une prévision optimale avec celles obtenues en calculant les signaux qui arrivent au bon moment dans N3.4
  
- I added Gill’s bible on the same dropbox, and I suggest that you check chapters 6.13 (baroclinic modes), 11.5 and 11.6 (equatorial dynamics in the long wave approximation). I am not expecting you to understand everything, but I will answer questions (find dropbox)
- I think that finding an optimal proxy for the OMI (see science paper) based on sea-level average remains a priority. The “h_R index” we use in the Science paper was initially built on D20, not sea level, and *we did not very accurately work out propagation times, so I’m sure it is possible to do better than that*. That should be one of the objectives of your training period
- Completing administrative formalities, opening all the accounts, and doing some **reading to familiarize yourself with the linear equatorial theory** should already take a lot of your first two weeks. You can get started by a validation of the CTL simulation sea level anomalies to AVISO observations (Maps: cor, rms-dif, std-of each; time series in regions such as Niño3 and Niño4). You can do similar things (just cor) for comparisons between sea level and D20

## WEEK 1

### 0321 Fri
- ~~ssh key on laptop~~ (no : use git)

### 0319 Wed:
- ~~Fill chartes, Make Espri work and answer Yann~~
- event extend storage
- Read enso book
  
~~Yann 1st call : 
editeur python : mon ordi,
créer un dépot git~~

### 0318 Tue:
~~Check convention, 
Prepare python env on linux, 
Plotter les données aviso~~

### 0317 Mon:
Read enso book ro chapters
~~Create an account on the IPSL computing centre (https://documentations.ipsl.fr/spirit/index.html) which you will be able to do here: https://mesocentre.ipsl.fr/account-opening/, Eric: il faudra voir Erika pour l’ouverture de compte labo, la clef kaba,~~

-**l’accès cantine **
- le remboursement transport


