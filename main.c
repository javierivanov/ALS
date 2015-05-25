#include "tools.h"
#include <stdio.h>
int main(int argc, char* argv[])
{
    FILE* fp;
    char* line=NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen(argv[1], "r");
    int i=0;
    int j;
    results dr;
    while((read = getline(&line, &len, fp)) != -1){
        if (i++ == 0)
            dr = LSH(line);
            for (j=0; j < dr.s; j++){
                printf("%d %d\n", j, dr.data[i]);
            }
    }
    fclose(fp);
    free(line);

    return 0;
}
