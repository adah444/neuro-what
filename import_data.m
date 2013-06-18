clc
clear all

k = 0;

[type, sheets] = xlsfinfo('aggregate_mechanical_test_data_without_E3.xlsx');


ndata = cell(1,length(sheets));

for i = 1:length(sheets)
    
    if length(sheets{i}) == 2
        
        ndata{i-k} = xlsread('aggregate_mechanical_test_data_without_E3.xlsx', i,'C5:D1500');
        
    else
        
        k = k + 1;
        
    end
    
end

ndata = ndata(~cellfun('isempty',ndata));