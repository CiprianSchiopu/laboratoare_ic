% Test CPA
% Author: Marios Choudary

%% Reset environment
close all;
% clear; % Only when need to clear variables
set(0, 'DefaulttextInterpreter', 'none'); % Remove TeX interpretation
tic

%% Setup the necessary paths and parameters
addpath('AES/');
data_title = 'Scores SIM DATA';
path_lab = 'lab6/';
name_data = sprintf('simdata.mat'); % Use for N=50000
% name_data = sprintf('simdata_small.mat'); % Use for N=1000
% rng('default'); % use same randomisation to get consistent results

%% Set possible candidate values
target_values = 0:255;
nr_values = length(target_values);

%% Set Hamming Weight as leakage model for each value in simulated data
lmodel = hamming_weight(target_values);

%% Load previously generated data
% 'M': vector of plaintexts
% 'X' vector of leakage traces
% 'K': key used for all traces
load(name_data);

%% Generate sbox
[s_box, ~] = s_box_gen;

%% Get number of leakage points/plaintexts
N = length(X);

%% Plot leakage data for first 1000 values
figure
idx = 1:1000;
X1 = X(idx);
plot(idx, X1);
xlabel('Sample index');
ylabel('Leakage');

%% Compute hamming weight value of S-box output for one key value
% Need (+1) in the 2 lines below due to Matlab indexing from 1
k = 1;
V = s_box(bitxor(target_values(k), M) + 1);
L = lmodel(V + 1);

%% Plot hamming weight leakage for S-box output of given key hypothesis
figure
idx = 1:1000;
L1 = L(idx);
plot(idx, L1);
xlabel('Sample index');
ylabel(sprintf('Hamming weight leakage for k=%d', k));

%% Compute correlation coefficient for this key hypothesis
c = corrcoef(X, L);
c = c(1,2);
fprintf('Correlation coefficient is: %f\n', c);

%% TODO: compute the correlation for each possible candidate
% You can initialize a vector like this:
% cv = zeros(N, 1); % column vector with N rows
C = zeros(1, 256);
for k = 1:nr_values
    V = s_box(bitxor(target_values(k), M) + 1);
    L = lmodel(V + 1);
    coef = corrcoef(X, L);
    C(k) = coef(1,2);
end

[~, i] = max(C);
fprintf('Highest correlation coefficient is: %f\n', i);


%%

%% TODO: plot correlation coefficient for each candidate
figure;
plot(1:256, C)
%% TODO: Compute success rate for different nuber of traces used in attack
% Success rate is computed as the frequency of times the correct
% key is classified first.
% For this, use variable amounts of traces (e.g. 100, 200, ..., 1000),
% and for each iteration (say 50 iterations) select that number of
% traces at random from the whole dataset
n_iter = 50;
success = 0;

ntraces = 100;
num_of_traces = [10, 20, 50, 100, 200, 500, 1000];
SR = zeros(7, 1);
R=50;
for q=1:7
    success = 0;
    for ii=1:n_iter
        sel_idx = randperm(N, num_of_traces(q));
        Mi = M(sel_idx);
        Xi = X(sel_idx);
        C = zeros(256, 1);
        for k = 1:nr_values
            V = s_box(bitxor(target_values(k), Mi) + 1);
            L = lmodel(V + 1);
            coef = corrcoef(Xi, L);
            C(k) = coef(1,2);

        end
        [~, i_res] = max(C);
        if i_res==i
            success = success + 1;
        end

        % TODO: obtain correlation vector for each selection of traces,
        % then compute success rate
    end
    SR(q) = success/R;
    
end
%% TODO: plot success rate as a function of number of traces used in attack

figure;
plot(traces_no, SR)