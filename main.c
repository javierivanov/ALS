#include "tools.h"
#include <stdio.h>
#include <openssl/md5.h>
int main(int argc, char* argv[])
{
    FILE* fp;
    char* line=NULL;
    size_t len = 0;
    ssize_t read;
    if (argc != 4) return 1;
    fp = fopen(argv[1], "r");
    int i=0;
    int j;
    int lin = atoi(argv[2]);
    int plotv = atoi(argv[3]);

    results dr;
    while((read = getline(&line, &len, fp)) != -1){
        if (i++ == lin){
            if (plotv == 0){
                dr = LSH(line);
                for (j=0; j < dr.s; j++)
                {
                    //printf("%d %d\n", j, dr.data[j]);
                    printf("%d\n", LSH_gen(dr));
                }
            }
            if (plotv == 1)
            {
                plot(line, 1);
            }
            if (plotv == 2)
            {
                plot(line, 0);
            }
        }
    }
    fclose(fp);
    free(line);
    return 0;
}
