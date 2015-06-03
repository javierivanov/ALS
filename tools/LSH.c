#include "tools.h"
#include <stdio.h>

void plot(const char* str, int filter){
    int l = strlen(str);
    int i;
    for (i=0; i < l; i++)
    {
        int c=(int)(str[i]);
        if (filter){
          c = filter(str[i]);
        }
        printf("%d %d\n", i, c);
    }
}

void showAscii()
{
    int i;
    for (i=0; i < 155; i++)
    {
        printf("%d => %c\n", i, (char)i);
    }
}

int filter(const char cs)
{
    int c = cs;
    if (c <= 47) c = 1;
    if (c > 47 && c <= 57) c=2;
    if (c >= 58 && c <= 64) c=1;
    if (c > 64 && c <= 90) c=3;
    if (c >= 91 && c <= 96) c=1;
    if (c >= 97 && c <= 122) c=3;
    if (c > 122) c=1;
    return c;
}

int filter2(const char cs)
{

}

results LSH(const char* str)
{
    int l=strlen(str);
    int i;
    results r;
    r.data = (int*)(malloc(sizeof(int)*l));
    r.s=1;
    r.data[0] = filter(str[0]);
    for (i=1; i < l; i++)
    {
        int c=filter(str[i]);
        if (r.data[r.s-1] != c)
        {
            r.data[r.s++] = c;
        }
    }
    return r;
}

int LSH_gen(const results r)
{
    int out = 0;
    int i;
    for (i=r.s-1; i >= 0; i--)
    {
        out += (int)pow(r.data[i], i);
    }
    return out;
}
