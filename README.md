# read-big-file-with-python
The first of a three part case study in reading a big (21GB) text file using C, Python, PYSPARK and Spark-Scala.
This part deals with a comparison between using a C and python program.

A lot of the work I do is dealing with large'ish data files from external data providers and 
trying to shoehorn their data into our system. One such file comprises company ownership data that
we download from Standard & Poors CapitalIQ data service. We use the file to calculate free floats for stocks 
and this in turn feeds in to whether or not the stock can become a member of various equity indexes 
that we calculate.

The data file is about 21 Gigabtyes big and holds approximately 335 Million pipe separated records. The first 
10 records are shown below:

```
18511|1|2587198|2004-03-31|0|100000|0|1.97|0.49988|100000||||
18511|2|2587198|2004-06-30|0|160000|0|3.2|0.79669|60000|60|||
18511|3|2587198|2004-09-30|0|160000|0|2.17|0.79279|0|0|||
18511|4|2587198|2004-09-30|0|160000|0|1.72|0.79118|0|0|||
18511|5|2587198|2005-03-31|0|0|0|0|0|-160000|-100|||19
18511|6|2587940|2004-03-31|0|240000|0|0.78|0.27327|240000||||
18511|7|2587940|2004-06-30|0|560000|0|1.59|0.63576|320000|133.33||24|
18511|8|2587940|2004-09-30|0|560000|0|1.13|0.50704|0|0|||
18511|9|2587940|2004-09-30|0|560000|0|0.96|0.50704|0|0|||
18511|10|2587940|2005-03-31|0|0|0|0|0|-560000|-100|||14

```
The second field in the above file can range between 1 and 56 and the goal was to split up the 
original file so that all the records with the same value for the second field would be 
grouped together in the same file. i.e we would end up with 56 separate files period1.txt, 
period2.txt ... period56.txt each containing approximately 6 million records.
Performance is quite critical to us so, I wrote a C program to run on our HP OpenVMS Alpha. I'm not a 
C expert but was a bit shocked to discover the program was taking about 54 minutes to run on a quiet system. 
Anyhow some time later I started to get into Python and as we all know Python is slow isn't it, so there wasn't 
much point in trying to rewrite my C code in Python and run it on my desktop PC was there? Well, at a loose end one day I 
decided to try and give it a go, more as a learning excercise for me rather that any expectation of producing
something that would be fasetr than my C code - allbeit on a different platform. Needless to say I was amazed 
when my python run came in at 1033 seconds elapsed time -that's just over 17 minutes or fully two thirds quicker
than my C program. I know we're not quite comparing like with like but make of it what you want. 
