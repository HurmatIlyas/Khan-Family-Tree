mianBiwi('ChoteKhan','ChotiRani').
mianBiwi('BarreKhan','BarriRani').
mianBiwi('Salim','Kauser').
mianBiwi('Nadir','Nahid').
mianBiwi('Asad','Sumra').
mianBiwi('Rizwan','Sanam').



parent('ChoteKhan','Kauser').
parent('ChotiRani','Kauser').
parent('ChoteKhan','Nadir').
parent('ChotiRani','Nadir').
parent('ChoteKhan','Asad').
parent('ChotiRani','Asad').
parent('BarreKhan','Nahid').
parent('BarriRani','Nahid').
parent('BarreKhan','Sumra').
parent('BarriRani','Sumra').
parent('Salim','Rizwan').
parent('Kauser','Rizwan').
parent('Nadir','Burhan').
parent('Nahid','Burhan').
parent('Nadir','Rashid').
parent('Nahid','Rashid').
parent('Nadir','Akram').
parent('Nahid','Akram').
parent('Asad','Salima').
parent('Sumra','Salima').
parent('Asad','Sanam').
parent('Sumra','Sanam').
parent('Rizwan','Rabia').
parent('Sanam','Rabia').

gins('Male','ChoteKhan').
gins('Male','BarreKhan').
gins('Male','Salim').
gins('Male','Nadir').
gins('Male','Asad').
gins('Male','Rizwan').
gins('Male','Burhan').
gins('Male','Rashid').
gins('Male','Akram').
gins('Female','ChotiRani').
gins('Female','BarriRani').
gins('Female','Kauser').
gins('Female','Nahid').
gins('Female','Sumra').
gins('Female','Salima').
gins('Female','Sanam').
gins('Female','Rabia').

beti(X,Y) :- parent(Y,X) , gins('Female',X).
beta(X,Y) :- parent(Y,X), gins('Male',X).
dada(X,Y) :- parent(X,Z) , parent(Z,Y) , gins('Male',X),gins('Male',Z).
nana(X,Y) :- parent(X,Z), parent(Z,Y) , gins('Male',X) , gins('Female',Z).
dadi(X,Y) :- parent(X,Z),parent(Z,Y) , gins('Female',X), gins('Male',Z).
nani(X,Y) :- parent(X,Z),parent(Z,Y) , gins('Female',X), gins('Female',Z).
sala(X,Y) :- mianBiwi(Y,Z) , parent(A,Z) , gins('Female',Z), parent(A,X) , gins('Male',A), gins('Male',X).
bahu(X,Y) :- parent(Y,Z) , gins('Female',X) , gins('Male',Z) , mianBiwi(Z,X).
pota(X,Y) :- parent(Y,Z), parent(Z,X) , gins('Male',X),gins('Male',Z).
nawasa(X,Y) :- parent(Y,Z), parent(Z,X) , gins('Male',X), gins('Female',Z).

sussar(X,Y) :- mianBiwi(Y,Z) , parent(X,Z) , gins('Male',X), gins('Female',Z), gins('Male',Y).
sussar(X,Y) :- mianBiwi(Z,Y) , parent(X,Z) , gins('Male',X), gins('Male',Z), gins('Female',Y).

baapDada(X,Y) :- parent(X,Y), gins(male,X).
baapDada(X,Y) :- parent(X,Z) ,baapDada(Z,Y),gins('Male',Z),gins('Male',X).

khala(X,Y) :- parent(Z,Y), gins('Female',Z),parent(V,Y),gins('Male',V),parent(A,Z), gins('Male',A), parent(A,X), gins('Female',X),not(mianBiwi(V,X)).
chachataya(X,Y) :- parent(Z,Y), gins('Male',Z), parent(M,Y), gins('Female',M), parent(A,Z), gins('Male',A), parent(A,X), gins('Male',X), not(mianBiwi(X,M)).












