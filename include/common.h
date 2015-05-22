#ifndef COMMON_H
#define COMMON_H

#include<string.h>
#include<stdlib.h>
#include<omp.h>

int Levenshtein(char* str1, char* str2);
int min(int a, int b);
int LSH(char* str);
void number_removal(char* str);


#endif
