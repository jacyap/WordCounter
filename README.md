# WordCounter
A simple .bat executable to sum up your total word count in a LaTeX document (for TeXstudio in Windows)

Written by Jacinta Yap, 2020

In (probably) my second year I realised that TeXstudio didn't have an easy way of displaying my word count (without counting commands, headings, captions etc.). I thought this feature would be useful for when I was writing up my PhD Thesis in LaTeX using TeXstudio. Using a combination of perl & python, I wrote this script to:

1. Count words in the main text body (skips all the LaTeX commands) for each chapter
2. Sum up chapter totals 
3. Append the time, date, year and the total word count to a .txt document
4. Do this by just double clicking on a single file

Might be a bit convoluted but I didn't want to commit more time to this, it does the job!

You may need to change some things for your purposes (i.e. numbers of chapters) but use this for whatever your purpose.

Required software:
- TeXcount (have included the texcount.pl file here for ease):
https://app.uio.no/ifi/texcount/
- Perl: https://www.perl.org/get.html
- Python: https://www.python.org/downloads/

Note:
- Run all files from your Chapters directory (make sure the chapterX.tex files are defined correctly in the .bat file)
- You might need to create empty blank countX.txt files for each chapter
- You might need to mention the .pl extension in the .bat file to run TeXcount
- The '-1' option for TeXcount sums the total words in the main body of text, check the user guide if you want to see what it classifies as a word. If you want it to count other things (headers, floats, captions etc.) change this, all options are listed in here: https://app.uio.no/ifi/texcount/howto.html

TotalWordCount.txt example:\
1118 22/01/2020 1234\
1827 23/01/2020 2345

**Bonus: Python script to plot progress over time**

Run PlotWordCount.py with your TotalWordCount.txt to plot your progress, as shown below -

![WordCountPlot](https://github.com/jacyap/WordCounter/blob/master/TotalWordCount_JYAP.png)
