#include "tools.h"
#include <stdio.h>
char* number_removal(const char* str)
{
    int i,c,l;
    c=i=0;
    l=strlen(str);
    for (;i<l;i++)
    {
        if ((int)(str[i]) < 47 || (int)(str[i]) > 58){
            c++;
        }
    }
    char* dst = (char*)(malloc(sizeof(char)*c));
    c=0;
    for (i=0; i < l; i++)
    {
        if ((int)(str[i]) < 47 || (int)(str[i]) > 58){
            dst[c++]=str[i];
        }
    }
    return dst;
}
