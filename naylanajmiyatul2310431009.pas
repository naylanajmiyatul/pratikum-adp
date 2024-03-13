Program menghitung_kerucut;
Uses crt;
Var
   r,t,s,vol,ls,lp:real;
begin
     clrscr;
     writeln(‘menghitung kerucut’);
     write(‘masukan jari jari’);
     readln(r);
     write(‘masukan tinggi’);
     readln(t);
     write(‘masukan sisi miring’);
     readln(s);
     ls:=(22/7)*r*s;
     lp:=((22/7)*r*s)+((22/7)*r*r);
     vol:=(1/3)*(22/7)*r*r*t;
     writeln(‘luas selimut kerucut:’,ls:1:1);
     writeln(‘luas permukaan kerucut:’,lp:1:1);
     write(‘volume kerucut:’,vol:6:2);
     readln;

end.

