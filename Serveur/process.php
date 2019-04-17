<? php
$ mon_fichier  =  ' messagefeed.txt ' ;
$ handle  =  fopen ( $ mon_fichier , ' a ' ) ou  die ( ' Impossible d'ouvrir le fichier:   ' . $ mon_fichier );
$ data  =  $ _GET [ ' u ' ] . " \ n " ;
? >
