/*
* Visual studio version using fscanf to process the file
*/

#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <fcntl.h>
#include <io.h>
#include <iostream>
#include <string>

int main ()
{
	FILE *fp = fopen("d:\\tmp\\iholding\\issueholding.txt", "r");
	if (!fp)
		exit(-1);

	long lines = 0;
	char buf[100];
	char therest[100];

	int f2num = 0;

	char outname[40];
	char f1[15];
	FILE *files[100];

	/* pre-open all our ouput files */
	for (int i = 1; i <= 56; i++)
	{
		sprintf(outname, "d:\\tmp\\iholding\\myfiles\\issue%d.txt", i);
		files[i] = fopen(outname, "w");
	}

	while (fscanf(fp, "%[^|]|%d|%s\n", f1, &f2num,therest) == 3)
	{
		if (f2num > 0 && f2num <= 56)
		{
			fprintf(files[f2num], "%s|%d|%s\n", f1,f2num,therest);
		}
		else
			printf("fscanf Issue %s|%d|%s",f1,f2num,therest);
	}
	

	for (int i = 1; i <= 56; i++)
	{
		fclose(files[i]);
	}

	return lines;
}
