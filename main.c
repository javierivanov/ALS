
#include "common.h"
#include <stdio.h>


int main(int argc, char* argv[])
{
    char* t1 = "Test1";
    char* t2 = "Test2";

    printf("%d\n", Levenshtein(t1, t2));

    return 0;
}
