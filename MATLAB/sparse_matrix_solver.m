clear all;
clc;

% MAT_DIR = 'Matrices/positive_definite/';
% % Carico lista delle matrici da risolvere
% list = dir(MAT_DIR);
% list = arrayfun(@(item) item.name, list, 'UniformOutput', false);


% for i = 1:length(list)
%     curr_file = list{i};
%     if ~endsWith(curr_file, '.mat')
%         continue
%     end
%     
%     % Carico matrice dei coefficienti A
%     mat = load(fullfile(MAT_DIR, curr_file));
%     solve_matrix(mat);
%     
% end

pathName = input('');
mat = load(pathName);
input('Matrice caricata. Premi invio per continuare');
solve_matrix(mat);

function solve_matrix(mat)
    
    % Inizializzo il profiler per l'utilizzo di memoria
    profile clear
    profile -memory on;

    % Calcolo il vettore dei termini noti b
    A = mat.Problem.A;
    xe = ones(length(A),1);
    b = A*xe;

    % Risolvo il sistema (Matlab sceglie l'algoritmo migliore)
    tic;
    x = A\b;
    t = toc;
    input('Sistema risolto. Premi invio per continuare');

    % Salvo informazioni riguardo l'utilizzo di memoria
    p = profile('info');
    mem_usage = (p.FunctionTable(2).TotalMemAllocated);

    % Calcolo errore relativo
    relative_error = norm(x - xe)/norm(xe);

    [fileID, errormsg] = fopen('../logs/res.log', 'at+');
%     fprintf(fileID, 'name,dim,nnz,re,time,memory,positive,lang,os\n');
    fprintf(fileID, '%s', mat.Problem.name, ', ');
    fprintf(fileID, '%s', num2str(size(mat.Problem.A, 1)), ', ');
    fprintf(fileID, '%s', num2str(nnz(mat.Problem.A)), ', ');
    fprintf(fileID, '%s', num2str(relative_error), ', ');
    fprintf(fileID, '%s', num2str(t), ', ');
    fprintf(fileID, '%s', num2str(mem_usage), ', ');
%     fprintf(fileID,); Positive/Negative
    fprintf(fileID, 'matlab, ');
%     fprintf(fileID,); OS
    fprintf(fileID, '\n');

    fclose(fileID);

    %  Visualizzo informazioni matrice e report
%     disp(['Name: ', mat.Problem.name]);
%     disp(['Allocated memory: ',num2str(mem_usage),' Byte']);
%     disp(['Dimensions: ', num2str(size(mat.Problem.A, 1)), ' x ', ...
%         num2str(size(mat.Problem.A, 2))]);
%     disp(['Number of elements: ', num2str(nnz(mat.Problem.A)), ...
%         ' (', num2str(100*(nnz(mat.Problem.A)/ ...
%         (size(mat.Problem.A, 1)*size(mat.Problem.A, 1)))), '%)']);
%     disp(['Relative Error: ', num2str(relative_error)]);
%     disp(['System solving time: ', num2str(t),' s']);
%     fprintf('\n\n');
   
end