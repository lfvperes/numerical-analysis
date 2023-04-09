% Calculo Numerico - SME0300
% Luis Filipe Vasconcelos Peres
% Exercicio 1 - questao 3
% 29/03/2023

% a) propriedade associativa da soma:
% (a + b) + c = a + (b + c)
a= 1.0e+308;
b = 1.1e+308;
c = -1.001e+308;
esquerda = (a + b) + c;
direita = a + (b + c);
disp(esquerda == direita);  % resulta false (0)
                            % entao propriedade violada

disp(esquerda);             % Inf (ocorreu overflow)
disp(direita);              % 1.099e+308


% b) (1 + x) - 1) / x = x / x = 1
x = 1e-15;
resultado = ((1 + x) - 1) / x;
disp(resultado != 1);       % resulta true (1)
disp(abs((resultado-1)/1)); % erro de 11%