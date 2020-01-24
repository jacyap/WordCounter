# WordCounter
.bat executable to sum up your total word count in a latex document

Written by Jacinta Yap, 2020

In (probably) my second year I realised that TeXstudio didn't have an easy way of displaying my word count. I thought this feature would be useful for when I was writing up my Thesis using LaTeX, so using a combination of perl & python, I wrote this script to:

1. Count words in the main text body (skips all the LaTeX commands) for each chapter
2. Sum up up chapter totals 
3. Append the time, date, year and the total word count to a .txt document
4. Do this by just double clicking on a single file

Might be a bit convoluted but I didn't want to commit more time on this, it does the job!

Use this for however you see fit.


Required software:

TeXcount
https://app.uio.no/ifi/texcount/

Perl
Python
