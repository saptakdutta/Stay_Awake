@echo off
call activate base

@echo on
python clicker.py -tgp 3 -clktm 120 -x 1142 -y 1066

@echo off
call conda deactivate
goto :eof