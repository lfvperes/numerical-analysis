function y = fw_sub(L, Pb)
    N = size(L)(1);
    % garantee Pb is vertical
    if (size(Pb)(1) == 1)
        Pb = Pb';
    endif

    % backward subtitution
    y = zeros(N, 1);
    for i = 1:N
        y(i) = (Pb(i) - L(i,1:i)*y(1:i)) / L(i, i);
    endfor
end