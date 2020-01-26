# WordCounter
.bat executable to sum up your total word count in a latex document

Written by Jacinta Yap, 2020

In (probably) my second year I realised that TeXstudio didn't have an easy way of displaying my word count. I thought this feature would be useful for when I was writing up my PhD Thesis in LaTeX. Using a combination of perl & python, I wrote this script to:

1. Count words in the main text body (skips all the LaTeX commands) for each chapter
2. Sum up up chapter totals 
3. Append the time, date, year and the total word count to a .txt document
4. Do this by just double clicking on a single file

Might be a bit convoluted but I didn't want to commit more time on this, it does the job!

You might need to change some things for your purposes but use this for however you see fit.

Required software:
- TeXcount (have included the texcount.pl file here for ease)
https://app.uio.no/ifi/texcount/
- Perl
- Python

Note:
- Run all files from your Chapters directory
- Might need to create empty blank countX.txt files for each chapter
- You might need to mention the .pl file extension in the .bat to run TeXcount

TotalWordCount.txt example:\
1118 22/01/2020 1234\
1827 23/01/2020 2345
