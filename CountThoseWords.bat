# Executable .bat file
# Put this into your /Chapters/ directory
# J Yap, 2020

texcount -1 -sum chapter1.tex -out=count1.txt
texcount -1 -sum chapter2.tex -out=count2.txt
texcount -1 -sum chapter3.tex -out=count3.txt
texcount -1 -sum chapter4.tex -out=count4.txt
texcount -1 -sum chapter5.tex -out=count5.txt
texcount -1 -sum chapter6.tex -out=count6.txt
texcount -1 -sum chapter7.tex -out=count7.txt
:: texcount -1 -sum abstract.tex -out=count8.txt
python sum.py
