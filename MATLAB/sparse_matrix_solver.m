clear all;
clc;

% Carico lista delle matrici da risolvere
list = dir('Matrix_List');

for i = 3:3 %length(list) 
    
    % Carico matrice dei coefficienti A
    mat = load(fullfile('Matrix_List', list(i).name));
    A = mat.Problem.A;
    
    % Inizializzo il profiler per l'utilizzo di memoria
    profile clear
    profile -memory on;
    
    %  Visualizzo informazioni base della matrice
    disp(['Name: ', mat.Problem.name]);
    disp(['Dimensions: ', num2str(size(mat.Problem.A, 1)), ' x ', ...
        num2str(size(mat.Problem.A, 2))]);
    disp(['Number of elements: ', num2str(nnz(mat.Problem.A)), ...
        ' (', num2str(100*(nnz(mat.Problem.A)/ ...
        (size(mat.Problem.A, 1)*size(mat.Problem.A, 1)))), '%)']);
    
    % Calcolo il vettore dei termini noti b
    xe = ones(length(A),1);
    b = A*xe;
    
    % Risolvo il sistema (Matlab sceglie l'algoritmo migliore)
    tic;
    x = A\b;
    t = toc;

    % Salvo informazioni riguardo l'utilizzo di memoria
    p = profile('info');
    mem_usage = (p.FunctionTable(5).TotalMemAllocated);
    
    % Calcolo errore relativo
    relative_error = norm(x - xe)/norm(xe);
    
    % Visualizzo report analisi
    disp(['System solving time: ', num2str(t),' s']);
    disp(['Relative Error: ', num2str(relative_error)]);
    disp(['Allocated memory: ',num2str(mem_usage),' Byte']);
end
