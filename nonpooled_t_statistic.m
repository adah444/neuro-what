function [p,answr] = nonpooled_t_statistic(raw1,raw2,al)

n1 = length(raw1);
n2 = length(raw2);
x1 = mean(raw1);
x2 = mean(raw2);
s1 = std(raw1);
s2 = std(raw2);

df = (s1^2/n1+s2^2/n2)^2/((s1^2/n1)^2/(n1-1)+(s2^2/n2)^2/(n2-1));

t = (x1-x2)/(s1^2/n1+s2^2/n2)^(1/2);

p = 1-tcdf(-t,df);

if al > p
    answr = 'Reject null!';
else
    answr = 'Cannot reject null!';
end