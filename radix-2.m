%%%%%%%%%%%%%%%%%%%Bit Reverse%%%%%%%%%%%%%%
%%
%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%X=[0 1 2 3 4 5 6 7];
 X=[1 1 1 1 0 0 0 0 ];
N=length(X);
int j;
int t1;
int y;
int n1;
int n2;
j =1; %* bit-reverse */
a=N-1;
n2 = N/2;
i=1;
while i<a;i=i+1;n1 = n2;
          while j>=n1 
                  j = j - n1;
                  n1 = n1/2;
          end
      j = j + n1;
           if (i < j)              
               t1 = X(i);
               X(i) = X(j);
               X(j) = t1;
           end
end

%%%%%%%%%%%%%%%%%%%%%%%%%DITFFT%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
L=log2(N);
k1=2; k2=N/2; k3=1;
for i1=1:L  %Iteration stage 
        L1=1;
    for i2=1:k2
        k=1;
        for i3=1:k3
            i=i3+L1-1; j=i+k3;
            W=complex(cos(2*pi*(k-1)/N),sin(2*pi*(k-1)/N));
            T=X(j)*W;
            X(j)=X(i)-T; X(i)=X(i)+T;
            k=k+k2;
        end
            L1=L1+k1;
    end
        k1 = k1*2;  k2 = k2/2;  k3 = k3*2;
end