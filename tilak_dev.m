clear all;
close all;
clc;

a=textread('raw_values.txt', '%c', 'whitespace', '');

inc = 1;
l=5000;
psi(l)=0;psic(l)=0;
i1=1;
i2=2;
i3=3;
for i=1:l
    b=strcat(a(i1),a(i2),a(i3));
    psi(i)= hex2dec(sscanf(b,'%c',3));
    if psi(i) >= 2^(12-1)              %%--Nathan
        psi(i) = psi(i) - 2^12;        %%--Nathan
    end
  % psi(i)=psi(i)*0.25-512;
    inc=inc+3; i1=i1+3;i2=i2+3;i3=i3+3;
    if inc >= size(a) inc = size(a);end
    if i1  >= size(a)   i1= size(a);end
    if i2  >= size(a)   i2= size(a);end
    if i3  >= size(a)   i3= size(a);end
end

%%%%%%%%%%%%%%%%%%%%
%  clear all;
%  close all;
%  clc;
%  psi=textread('3.txt', '%n', 'whitespace', '');
%%%%%%%%%%%%%%%%%%%%

% subplot(2,2,1);
 plot(psi);
 title('PSI Signal', 'FontSize', 12);
 xlabel('Symbol index', 'FontSize', 12);
 ylabel('Integer value', 'FontSize', 12);
 
 
 [maxtab, mintab] = peakdet(psi, 0.5);

 
 subplot(2,2,2);
 plot(psi); hold on;
 plot(maxtab(:,1), maxtab(:,2), 'r*');hold on;
  title('Max-peaks', 'FontSize', 12);
 xlabel('Symbol index', 'FontSize', 12);
 ylabel('Integer value', 'FontSize', 12);
 
 figure  
% subplot(2,2,3);
 plot(maxtab(:,2));
 title('Max-peaks Discretized', 'FontSize', 12);
 xlabel('Symbol index', 'FontSize', 12);
 ylabel('Integer value', 'FontSize', 12);
 
 
 
 for i=1:length(maxtab)
     %%%%%%%%%%%%%%%%%
     % if maxtab(i,2)>5 psic(maxtab(i))=1; else psic(maxtab(i))=0; end
     %%%%%%%%%%%%%%%%%
     
 if maxtab(i,2)>250 psic(maxtab(i))=1; else psic(maxtab(i))=0; end
 end
 subplot(2,2,4);
 stem(psic);
 title('Binary Symbols', 'FontSize', 12);
 xlabel('Symbol index', 'FontSize', 12);
 ylabel('Integer value', 'FontSize', 12);
 
 
 dt(l)=0;
 dt1(l)=0;
 c=1;
for i=1:length(psic)
    if psic(i)==1; dt(c)=i; c=c+1;end
 end

for i=1:length(dt)-1
     dt1(i)= dt(i+1)-dt(i);
end


    





















    
    

M = 32;k = log2(M);n = 3e4;
nSamp = 8;
xsym = bi2de(reshape(psic, k, length(psic)/k).', 'left-msb');
figure 
stem(xsym);
title('PSI symbols', 'FontSize', 18);
xlabel('Symbol index', 'FontSize', 18);
ylabel('Integer value', 'FontSize', 18);




% 
% figure 
% title('PSI-Signal')
% subplot(2,2,1);
% plot(psi);

[maxtab, mintab] = peakdet(psi, 0.5);
%title('Peaks')
% subplot(2,2,2);
% plot(psi); hold on;
% plot(maxtab(:,1), maxtab(:,2), 'r*');hold on;
% plot(mintab(:,1), mintab(:,2), 'b*');
% 
% %title('Max-Peaks')
% subplot(2,2,3);
% plot(maxtab(:,1), maxtab(:,2), 'r*');
% 
% %title('Min-Peaks')
% subplot(2,2,4);
% plot(mintab(:,1), mintab(:,2), 'b*');
 

for j= 1:size(maxtab,2)
   for i= 1:size(maxtab,2)
       if maxtab(i,j)> 0.5
           maxtab(i,j)=1;
       else maxtab(i,j)=0;
       end
   end
end

subplot(1,2,1)
plot(maxtab(:,2));


for j= 1:size(mintab,2)
   for i= 1:size(mintab,2)
       if mintab(i,j)> 0.5
           mintab(i,j)=1;
       else mintab(i,j)=0;
       end
   end
end

subplot(1,2,2)
plot(mintab(:,2));

%%%-------------------Calculating the Frequency of the Signal ----%
Fs = 1000;                   
T = 1/Fs;                    
L = 5000;                   
t = (0:L-1)*T;              
x=psi; 
y = x;     
plot(Fs*t(1:500),y(1:500))
title('Signal Corrupted with Zero-Mean Random Noise','FontSize', 18);
xlabel('time (milliseconds)','FontSize', 18);
NFFT = 2^nextpow2(L); 
Y = fft(y,NFFT)/L;
f = Fs/2*linspace(0,1,NFFT/2+1);
plot(f,2*abs(Y(1:NFFT/2+1))) 
title('Single-Sided Amplitude Spectrum of PSI(t)','FontSize', 18);
xlabel('Frequency (Hz)','FontSize', 18);
ylabel('|Y(f)|')













data = load('gv0_0-5.csv');
%data = load('gv0-4min-0-11.csv');
t = [1:length(data(:,1))];



figure;
plot(t,data);
grid on;
hold on;

% descritize the data
for j = 1:size(data,2)
    for i = 1:size(data,1)
        if data(i,j) > 2.5
            data(i,j) = 1;
        else
            data(i,j) = 0;
        end
    end
end



% convert the data to pulses (derrive and take only positive edges)
for j = 1:size(data,2)
    for i = 1:(size(data,1)-1)
        data(i,j) = data(i+1,j) - data(i,j);
        % remove negative edges
        if data(i,j) < 0
            data(i,j) = 0;
        end
    end
end

% calculate delay between peaks
delays = zeros(1,size(data,2));
for j = 1:size(data,2)
    current_row = 1;
    for i = 1:(size(data,1)-1)
        if data(i,j) < 1
            delays(current_row,j) = delays(current_row,j) + 1;
        else
            delays(current_row + 1, j) = 0;
            current_row = current_row + 1;
        end
    end
end

% remove trailing delay counts
for j = 1:size(delays,2)
    if length(find(delays(:,5) == 0, 1)) > 0
        delays(find(delays(:,j) == 0, 1) - 1, j) = 0;
    end
end

figure;
plot(t,data);
grid on;
hold on;

figure;
bar([1:length(delays)], delays);
grid on;
hold on;
