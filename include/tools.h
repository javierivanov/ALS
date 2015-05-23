#ifndef TOOLS_H
#define TOOLS_H

#include<string.h>
#include<stdlib.h>
#include<omp.h>

int Levenshtein(char* str1, char* str2);
int min(int a, int b);
int LSH(char* str);
char* number_removal(const char* str);


#endif //TOOLS_H
