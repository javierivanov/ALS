#include "tools.h"

int min(int a, int b)
{
    if (a > b) return b;
    return a;
}

int Levenshtein(char *s1,char *s2)
{   int t1,t2,i,j,*m,costo,res,ancho;

    t1=strlen(s1); t2=strlen(s2);

    if (t1==0) return(t2);
    if (t2==0) return(t1);
    ancho=t1+1;

    m=(int*)malloc(sizeof(int)*(t1+1)*(t2+1));
    if (m==NULL) return(-1); // ERROR!!

    #pragma omp parallel for
    for (i=0;i<=t1;i++) m[i]=i;
    #pragma omp parallel for
    for (j=0;j<=t2;j++) m[j*ancho]=j;

    for (i=1;i<=t1;i++) for (j=1;j<=t2;j++)
    { if (s1[i-1]==s2[j-1]) costo=0; else costo=1;
        m[j*ancho+i]=min(min(m[j*ancho+i-1]+1,     // Eliminacion
                             m[(j-1)*ancho+i]+1),              // Insercion
                         m[(j-1)*ancho+i-1]+costo); }      // Sustitucion

    res=m[t2*ancho+t1];
    free(m);
    return(res);
}
