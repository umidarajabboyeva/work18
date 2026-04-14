 1-misol
float PowerA3(float a){ return a*a*a; }
int main(){
    printf("%.0f\n", PowerA3(2));
    return 0;
}
2-misol
void
 PowerA234(float a,float *a2,float *a3,float *a4){
    *a2=a*a; *a3=a*a*a; *a4=a*a*a*a;
}
int main(){
    float a2,a3,a4;
    PowerA234(2,&a2,&a3,&a4);
    printf("%.0f %.0f %.0f\n",a2,a3,a4);
    return 0;
}
3-misol
void MEAN(float x,float y,float *a,float *g)
{
    *a=(x+y)/2; *g=sqrt(x*y);
}
int main(){
    float ar,ge;
    MEAN(2,8,&ar,&ge);
    printf("%.0f %.2f\n",ar,ge);
    return 0;
}

4-misol
void Triangle(float a,float *P,float *S){
    *P=3*a; *S=sqrt(3)/4*a*a;
}
int main(){
    float P,S;
    Triangle(5,&P,&S);
    printf("%.0f %.2f\n",P,S);
    return 0;
}

5-misol
void RectPS(int x1,int y1,int x2,int y2,int *P,int *S){
    int a=abs(x2-x1), b=abs(y2-y1);
    *P=2*(a+b); *S=a*b;
}
int main(){
    int p,s;
    RectPS(1,1,5,4,&p,&s);
    printf("%d %d\n",p,s);
    return 0;
}

6-misol
void DigitCountSum(int k,int *c,int *s){
    *c=*s=0;
    while(k){ *s+=k%10; (*c)++; k/=10; }
}
int main(){
   int c,sum;
    DigitCountSum(12345,&c,&sum);
        printf("%d %d\n",c,sum);
    return 0;
}

7-misol
int AddRightDigit(int k,int r){
    return k*10+r;
}
int main(){
    printf("%d\n",AddRightDigit(123,5));
    return 0;
}

9-misol
void AddLeftDigit(int *k,int r){
    int m=1,t=*k;
        while(t){ m*=10; t/=10; }
    *k=r*m+*k;
}
int main(){
    int k=123;
    AddLeftDigit(&k,9);
    printf("%d\n",k);
    return 0;
}

10-misol
void Swap(int *a,int *b){
    int t=*a; *a=*b; *b=t;
}
int main(){
    int A=1,B=2;
    Swap(&A,&B);
    printf("%d %d\n",A,B);
    return 0;
}

11-misol
def Minmax(x, y):
    if x > y:
        x, y = y, x
     return x, y
 Kiritish
a, b, c, d = map(int, input().split())
 4 marta chaqirish
a, b = Minmax(a, b)
c, d = Minmax(c, d)
a, c = Minmax(a, c)
b, d = Minmax(b, d)
print("Eng kichik:", a)
print("Eng katta:", d)

12-misol
def SortInc3(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a, b, c
 Kiritish
A1, B1, C1 = map(int, input().split())
A2, B2, C2 = map(int, input().split())
 Tartiblash
A1, B1, C1 = SortInc3(A1, B1, C1)
A2, B2, C2 = SortInc3(A2, B2, C2)
print(A1, B1, C1)
print(A2, B2, C2)

14-misol
def ShiftRight3(a, b, c):
   return c, a, b
A1, B1, C1 = map(int, input().split())
A2, B2, C2 = map(int, input().split())
A1, B1, C1 = ShiftRight3(A1, B1, C1)
A2, B2, C2 = ShiftRight3(A2, B2, C2)
print(A1, B1, C1)
print(A2, B2, C2)

15-misol
def ShiftLeft3(a, b, c):
   return b, c, a
A1, B1, C1 = map(int, input().split())
A2, B2, C2 = map(int, input().split())
A1, B1, C1 = ShiftLeft3(A1, B1, C1)
A2, B2, C2 = ShiftLeft3(A2, B2, C2)
print(A1, B1, C1)

16-misol
def ishora(x):
    if x < 0:
   return -1
  elif x > 0:
        return 1
    return 0
print(ishora(-5) + ishora(10))

17-misol
def ildizlar_soni(A, B, C):
    D = B*B - 4*A*C
    if D > 0:
        return 2
    elif D == 0:
      return 1
  return 0
print(ildizlar_soni(1, -3, 2))

18-misol
PI = 3.1415
def doira_yuzi(R):
    return PI * R * R
print(doira_yuzi(1))
print(doira_yuzi(2))
print(doira_yuzi(3))

19-misol
PI = 3.1415
R1 = 5
R2 = 3
print(PI * (R1*R1 - R2*R2))

20-misol
import math
A = 3
B = 4
C = math.sqrt(A*A + B*B)
print(A + B + C)

21-misol
def SumRange(A, B):
    if A > B:
        return 0
    s = 0
    for i in range(A, B+1):
        s += i
    return s
print(SumRange(1, 5))

22-misol
def Calc(A, B, Op):
    if Op == 1:
        return A - B
    elif Op == 2:
        return A * B
    elif Op == 3:
        return A / B
   else:
        return A + B
print(Calc(6, 3, 2))

23-misol
def Quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4
print(Quarter(3, -4))
24-misol
def Even(K):
    return K % 2 == 0
print(Even(4))
print(Even(7))
print(Even(10))
25-misol
def IsSquare(K):
    i = 1
    while i*i <= K:
        if i*i == K:
            return True
        i += 1
    return False
print(IsSquare(9))
print(IsSquare(10))
print(IsSquare(16))

26-misol
def IsPower5(K):
    while K > 1:
0        if K % 5 != 0:
          return False
       K //= 5
  return True
print(IsPower5(25))
print(IsPower5(30))
27-misol
def IsPowerN(K, N):
    while K > 1:
        if K % N != 0:
            return False
        K //= N
    return True
print(IsPowerN(8, 2))
print(IsPowerN(9, 3))
28-misol
def IsPrime(N):
    return False
    return True
print(IsPrime(7))
print(IsPrime(10))

29-misol
def DigitCount(K):
    return len(str(K))
print(DigitCount(123))
print(DigitCount(98765))

30-misol
def DigitN(K, N):
    s = str(K)
    if N > len(s):
        return -1
    return int(s[-N])
print(DigitN(12345, 1))
print(DigitN(12345, 3))
print(DigitN(12345, 6))

31-misol
def IsPalindrome(N):
     return str(N) == str(N)[::-1]
print(IsPalindrome(121))
print(IsPalindrome(123))

 32-misol
import math
def DegToRad(D):
    return D * math.pi / 180
print(DegToRad(180))
print(DegToRad(90))
print(DegToRad(45))

 33-misol
import math
def RadToDeg(R):
    return R * 180 / math.pi
print(RadToDeg(math.pi))
rint(RadToDeg(math.pi/2))
print(RadToDeg(1))

 34-misol
def Fact(N):
    res = 1
    for i in range(1, N+1):
        res *= i
   return res
print(Fact(3))
print(Fact(5))
print(Fact(6))

 35-misol
def Fact2(N):
   res = 1
    while N > 0:
        res *= N
        N -= 2
    return res
print(Fact2(5))
print(Fact2(6))
print(Fact2(7))

36-misol
def Fib(N):
    a, b = 0, 1
    for i in range(N):
        a, b = b, a + b
    return a
print(Fib(5))
print(Fib(7))
print(Fib(10))

 37-misol
def Power1(A, B):
    return A ** B
print(Power1(2, 3))
print(Power1(3, 2))
print(Power1(4, 0.5))

 38-misol
def Power2(A, N):
    res = 1
    for i in range(abs(N)):
        res *= A
    if N < 0:
        return 1 / res
    return res
print(Power2(2, 3))
print(Power2(2, -2))

39-misol
def Power3(A, N):
    if int(N) == N:
        return A ** int(N)
    else:
       return A ** N
print(Power3(2, 3))
print(Power3(2, 2.5))

 40-misol
def Exp1(x, e):
    s = 1
    term = 1
   n = 1
    while abs(term) > e:
        term *= x / n

        s += term
        n += 1
    return s
print(Exp1(1, 0.001))
print(Exp1(2, 0.001))










