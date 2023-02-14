![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | Tableau+SQL

## Introduction

In this lab, we will practice creating a connection between Tableau and MySQL. Please note, we will use the publusher database/schema, introduced in an earlier lesson, if you do not have this database you can find the .sql script to load it here:
https://drive.google.com/drive/folders/1HgxUyyDCNP2URfMXfD6paGlLyAIwcHfZ



## Getting Started

To complete this lab, follow each of the steps below:

1. In sql workbench create the following views:

```sql
create view v_author_sales as (
select pa.au_id
, sum(ps.qty) as sales_qty -- lets also bring through sales_qty
, sum(pt.price * ps.qty * (pt.royalty / 100) * (pta.royaltyper / 100)) as author_sale_amount -- title price * sales quantity * royalty per author * royalty per author : summed to create gain through sales
from publications.authors pa
left join publications.titleauthor pta on pa.au_id = pta.au_id
left join publications.titles pt on pta.title_id = pt.title_id
left join publications.sales ps on ps.title_id = pt.title_id
group by 1)
```
 
```sql
create view v_author_advance as (
select pa.au_id, concat(pa.au_fname, " ", pa.au_lname) as au_name
, sum((pta.royaltyper / 100) * pt.advance) as author_advance_amount  -- royaltyper(author) is a percentage in integer format so we divide by 100 and multiply by the advance to get that authors share of the advance, we sum to total these advances
from publications.authors pa
left join publications.titleauthor pta on pa.au_id = pta.au_id
left join publications.titles pt on pta.title_id = pt.title_id
group by 1, 2)
```

 
2. Using Tableau connect to a new server data source, select MySQL. (You will need your server details to connect)

__Hint:__
_Server: 127.0.0.1
Port: 3306
Database: Publications (optional, as can be changed after connecting)
Username: root
Password: <<your MySQL server root password>>_

3. Choose one approach from the following:
   - Drag the two views we created (v_author_sales & v_author_advance) into "Drag tables here" window area - as both views have "au_id" columns this will form a **tableau relationship** between them.
   - Drag one of the views we created (v_author_sales) into "Drag tables here" window area, double click the newly created box for this table, now drag the other view v_author_sales next to v_author_sales  - as both views have "au_id" columns this will form a **join** between them.
   - Drag "New **Custom SQL**" into "Drag tables here" window area, write an SQL query that selects the au_name, sales_qty, author_sale_amount and author_advance_amount from the two views - they will need to be joined on au_id

4. Move to a the first sheet
5. Create a calculated field for: "Total Author Amount"  _tip: sum(author_sale_amount) + sum(author_advance_amount)_
6. Create a horizontal bar chart showing off the the total amounts gained by each author, sorted in descending order
7. **(Optional)** Add some polish to the bar chart, consider:
  - Adding a label to the bars to show the amount
  - Colors (On other or total, which looks best?)
  - If we have the labels showing the amount, do we still need the axis? gridlines?
  - Text - font, size, format

## Deliverables
1. SQL script (if used)
2. Tableau worksheet
3. Link to the published dashboard

## Sources
SQL-CSV-Tableau https://www.youtube.com/watch?v=onbnHygx_s8
SQL-Tableau connection https://youtu.be/SG6wcfI4KFE
