clc
%clear all
tic

n = 10; %How many samples from first population
a = 1:length(ndata); % Do all samples
% a = 1:10;
len_a = length(a);
zeros_a = zeros(len_a);
mb1 = cell(1,len_a);
mb2 = cell(1,len_a);
anchor1 = zeros_a;
anchor2 = zeros_a;
R1 = zeros_a;
R2 = zeros_a;
peak1 = ones(len_a);
peak2 = ones(len_a);

for z = a
    
    x = ndata{z}(1:find(ndata{z}(:,2) == max(ndata{z}(:,2))),1);
    y = ndata{z}(1:find(ndata{z}(:,2) == max(ndata{z}(:,2))),2);

    t = 1;
    v = zeros(length(x));
    h = zeros(length(x)+2);
    c = 1;
    oldsign = 1;
    
    while t < length(x) && length(x) - t > peak2(z-min(a)+1)

        i = length(x);
        j = 2;
        P = ones(1,2);
        r = zeros(1);

        while r(j-1) < 0.998 && i > t %&& length(x)-j-t >= peak1(z-min(a)+1)

            P(j,:) = polyfit(x(t:i),y(t:i),1);

            yfit = polyval(P(j,:),x(t:i));
            yresid = y(t:i) - yfit;

            SSresid = sum(yresid.^2);
            SStot = var(y(t:i))*(length(y(t:i)) - 1);

            r(j) = 1 - SSresid/SStot;

            i = i - 1;
            j = j + 1;

        end

         v(t) = (length(x)-j-t);
         h(t+1) = v(t);

        if v(t) > 0      % Determines where the start of a group of linear regions.
            isneg = 0;   % This parameter allows the following conditional to execute.
        end
        
        if h(t+1)-h(t)<0 && oldsign > 0 && h(t)> peak2(z-min(a)+1) && isneg == 0  %  Looks to first see if the point is a peak, then if there has been a change in sign of the slope
            
            peak1(z-min(a)+1) = peak2(z-min(a)+1);
            anchor1(z-min(a)+1) = anchor2(z-min(a)+1);
            mb1{z-min(a)+1} = mb2{z-min(a)+1};
            R1(z-min(a)+1) = R2(z-min(a)+1);
            
            peak2(z-min(a)+1) = h(t);
            anchor2(z-min(a)+1) = t;
            mb2{z-min(a)+1} = P(j-1,:);
            R2(z-min(a)+1) = r(j-1);
            
            oldsign = -1;
            made = 1;
            
        elseif h(t+1)-h(t)<0 && oldsign > 0 && h(t)> peak1(z-min(a)+1) && made == 0; 
            
            peak1(z-min(a)+1) = h(t+1);
            anchor1(z-min(a)+1) = t;
            mb1{z-min(a)+1} = P(j-1,:);
            R1(z-min(a)+1) = r(j-1);
            
            oldsign = -1;
            
        elseif h(t+1)-h(t) > 0 && oldsign < 0
            
            oldsign = 1;
            
        elseif v(t) < 0
            
            isneg = 1;
            made = 0;
        end

        t = t + 1;

    end


% figure
% 
% hold on
% 
% plot(x,y,'d')
% Y2 = mb2{z-min(a)+1}(1,1)*x + mb2{z-min(a)+1}(1,2);
% plot(x,Y2,'-r') 
% Y1 = mb1{z-min(a)+1}(1,1)*x + mb1{z-min(a)+1}(1,2);
% plot(x,Y1,'-g') 

% %plot(1:length(v),v)

% hold off

end

if length(a) > n
    
    earlySlopes1 = zeros(n,1);
    lateSlopes1 = zeros(n,1);
    earlySlopes2 = zeros(len_a-n,1);
    lateSlopes2 = zeros(len_a-n,1);

    for i = 1:n
        earlySlopes1(i) = mb1{i}(1);
        lateSlopes1(i) = mb2{i}(1);
    end

    for i = 1:(length(a)-n)
        earlySlopes2(i) = mb1{i+n}(1);
        lateSlopes2(i) = mb2{i+n}(1);
    end
    
end

[early_pvalue,early_answr] = nonpooled_t_statistic(earlySlopes1,earlySlopes2,0.05);
[late_pvalue,late_answr] = nonpooled_t_statistic(lateSlopes1,lateSlopes2,0.05);

disp(early_answr)
disp(late_answr)

toc