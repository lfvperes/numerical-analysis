% Calculo Numerico - SME0300
% Luis Filipe Vasconcelos Peres
% Exercicio 1 - questao 2
% 29/03/2023

format long
x = 0;
for i = 1:30
  x = x + 1/5;
  if (x > 3.5 && x < 3.7)
    disp(x);
  endif
endfor
