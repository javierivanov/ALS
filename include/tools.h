#ifndef TOOLS_H
#define TOOLS_H

#include<string.h>
#include<stdlib.h>
#include<omp.h>

int Levenshtein(char* str1, char* str2);
int min(int a, int b);
char* number_removal(const char* str);
void plot(const char* str, int);
void showAscii();
int filter(const char c);
typedef struct _results
{
    int* data;
    size_t s;
} results;

results LSH(const char* str);
#endif //TOOLS_H
