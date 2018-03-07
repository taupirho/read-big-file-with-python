/*
 * The original C file I used to process the big data file
 * run-time was approx 54 minutes to process a 21 GB text file
 * containing approx 335 Million records
 * 
 *
 */
 
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <fcntl.h>
#include <unistd.h>
main(int argc,char **argv)
{
    static const  BUFFER_SIZE = 1024*1024;
    int fd = open(argv[2], O_RDONLY);
    FILE *fdi = fdopen(fd,"r");
    char *ptr;
    char buf[BUFFER_SIZE + 101];
    char buf2[100];
    long recs = 0;
    int t = 0;
    int maxfiles = 0;
    int i = 0;
    int f2num = 0;
    char f1[15];
    char *lines;
    char tmp[100];
    char outname[2];
    maxfiles=56;
    FILE *files[100];

    if(fd == -1)
    {
        printf("input file open error\n");
        exit(0);
    }

    /* pre-open all our ouput files */
    for(i=1;i<=maxfiles;i++)
    {
       sprintf(outname,"issue%d.txt",i);
       files[i] = fopen(outname,"w");
    }

    buf[0] = 0;

    while(size_t bytes_read = read(fd, buf, BUFFER_SIZE))
    {
        /* No line in the file is > 100 bytes so the following */
        /* fgets ensures we reach an EOL boundary */
        fgets(buf2,100,fdi);
        buf[bytes_read] = 0;
        strcat(buf,buf2);

        lines=buf;  /* A bunch of lines */
        ptr=0;

        if(!bytes_read || bytes_read == (size_t)-1)
        {
            printf("read failed\n");
            break;
        }
        /* read our bunch of lines 1 at a time */
        while((ptr = strtok_r(lines,"\n",&lines)))
        {
              ptr[strlen(ptr)-1]=0;

              /* isolate the second field */
              if(sscanf(ptr,"%[^|]|%d|",f1,&f2num) != 2)
              {
                 printf("issue with sscanf at line %d %s\n",recs,ptr);
                 break;
              }

              if(f2num > 0 && f2num <= maxfiles)
                 fprintf(files[f2num],"%s\n",ptr);
              else
                 printf("issue with f2num = %d %s\n",f2num,ptr);

              recs++;

        }
    }

    for(i=1;i<=maxfiles;i++)
    {
      fclose(files[i]);
    }

    close(fd);

    printf("\nnr lines = %ld\n",recs);
}
