### SQLite

SQLite is a database software package built on the Structured Query Language (SQL). It is similar to other SQL databases, such as PostgreSQL, MySQL, Oracle, and Microsoft SQL Server. It's easy to set up and use for small projects, but less suitable for production environments. Once you are familiar with SQLite, the same ideas and similar syntax can be applied to other SQL databases.

### Common SQL Command Patterns


```sql
CREATE TABLE ...
ALTER TABLE ... ADD COLUMN ...
INSERT INTO ... VALUES ...
UPDATE ... SET ... WHERE ...
SELECT ... FROM ... WHERE ...
SELECT ... FROM ... JOIN ... ON ...
DELETE FROM ... WHERE ...
```


```sql
SELECT * FROM titanic WHERE sex = 'male';
select * from titanic where sex = 'male';
```

### `CREATE: Creating tables


```sql
CREATE TABLE table1 (field1 INTEGER PRIMARY KEY);
```

### `ALTER TABLE`: Adding columns

Add a few more columns to `table1`:

```sql
ALTER TABLE table1 ADD COLUMN field2 VARCHAR(16);
ALTER TABLE table1 ADD COLUMN field3 REAL;
ALTER TABLE table1 ADD COLUMN field4 TEXT;
```

### `INSERT`: Adding rows

Let's add some data:

```sql
INSERT INTO table1 VALUES (1, 'Henry James', 42, '75 Mission Street, San Francisco, CA');
INSERT INTO table1 VALUES (2, 'Carol James', 45, '75 Mission Street, San Francisco, CA');
INSERT INTO table1 VALUES (3, 'Jesse James', 12, '75 Mission Street, San Francisco, CA');
```

```sql
INSERT INTO table1 VALUES (3, 'Julie James', 10, '75 Mission Street, San Francisco, CA');
```

```sql
INSERT INTO table1 VALUES (NULL, 'Julie James', 10, '75 Mission Street, San Francisco, CA');
```

### `SELECT`: Viewing records

`SELECT` is the keyword to access information in SQL. Here are some use cases:

```sql
SELECT * FROM table1;
```

`SELECT` requires:
- the columns that you wish to see (using `*` will select all columns in a given table), 
- followed `FROM` and the table containing those columns,
- then any restrictions on which rows we want to query, if applicable.

Question:
```sql
SELECT * FROM table1;
```

Question:
```sql
SELECT field1, field2 FROM table1;
```

To see specific columns from a table, include them after `SELECT`. It's usually helpful (from a performance perspective) to select only the columns that you actually need from a table.

#### `LIMIT`: Showing a specified number of observations

```sql
SELECT field1, field2 FROM table1 LIMIT 5;
```

To limit the number of rows that SQL returns, end your command with `LIMIT` and the number of rows you would like to see. This is equivalent to calling `.head()` in Pandas -- it will show the top N rows.

#### `WHERE`: Showing observations that meet a certain condition

```sql
SELECT field1, field2 FROM table1 WHERE field1 = 'Julie James';
SELECT field1, field2 FROM table1 WHERE field3 >= 10;
SELECT * from table1 WHERE field3 IS NULL;
```

To filter rows on some criteria, include the `WHERE` keyword after the table name. After `WHERE`, include the column name and a comparison, noting the following:

- In SQL, there is no `==` -- use `=` for equality only
- To filter by null / not null, use `IS NULL` or `IS NOT NULL`
- Make sure to check for other cases that are not coded as missing data but may still represent missing data, such as empty spaces or improbable values like `-999999`

#### `LIKE`: Expanding `=` to broader cases

```sql
SELECT * FROM table1 WHERE field2 LIKE 'Julie James';
```

We can use `LIKE` to also pull observations that take on a certain value. However, we can use `%` as wildcard characters, making `LIKE` more valuable than `=` in some cases.

```sql
SELECT * FROM table1 WHERE field2 LIKE '%James';
```

```sql
SELECT * FROM table1 WHERE field2 LIKE '%James%';
```

#### `ORDER BY`: Organizing observations by value

```sql
SELECT * FROM table1 ORDER BY field3;

```

We can use `ORDER BY` to pull observations in a particular order.

```sql
SELECT * FROM table1 ORDER BY field3 ASC;

```

```sql
SELECT * FROM table1 ORDER BY field3 DESC;

```

The terms `ASC` and `DESC` refer to "ascending" and "descending," respectively, and give us greater control over how we see these values.

Practice: What SQL query would I need to query `field1`, `field2`, and `field3`, showing the two observations with the greatest values of `field3`?

#### `COUNT`/`SUM`/`AVG`/`MAX`/`MIN`: Summarizing observations in a numerical summary

```sql
SELECT COUNT(*) FROM table1 WHERE field3 >= 30;

```

To count how many observations fit some criteria, we use `COUNT(*)`.

```sql
SELECT SUM(field3) FROM table1;
```

Summarizing observations with a number will be beneficial - we are data scientists, after all! Rather than reading an entire table into Pandas and then running summaries, we can just directly query this from our database.

Practice: What SQL query would I need to find both the average value of `field3` and the maximum value of `field3` among those individuals who are of legal voting age? (In the United States, one must be at least 18 years old to vote.)

#### `GROUP BY`: Grouping observations (similar to a PivotTable in Excel!)

Suppose we want to look at summaries among different groups.

```sql
ALTER TABLE table1 ADD COLUMN field5 VARCHAR(3);
UPDATE table1 SET field5 = 'M' WHERE field1 = 1;
UPDATE table1 SET field5 = 'M' WHERE field1 = 3;
UPDATE table1 SET field5 = 'F' WHERE field1 = 2;
UPDATE table1 SET field5 = 'F' WHERE field1 = 4;
```

Question: What does the previous set of commands do?

```sql
SELECT COUNT(*) FROM table1 GROUP BY field5;
```

```sql
SELECT COUNT(*),field5 FROM table1 GROUP BY field5;
```

Question: Suppose I wanted to look at the average age of men and women from this table. What SQL query would I need to pull this?

#### `DISTINCT`: Pulling observations that have unique values of a variable

```sql
SELECT COUNT(*) FROM table1;
```

```sql
SELECT COUNT(DISTINCT field1) FROM table1;
```

```sql
SELECT COUNT(DISTINCT field4) FROM table1;
```

It's often beneficial for us to count distinct values of a variable. Whether we're looking for duplicates (i.e. duplicate names in voting records) or interested in knowing the unique count (i.e. how many unique credit card numbers are in our dataset of transactions), this will be a helpful query to have in our back pocket.

### `UPDATE`: Updating records

Suppose we need to update an existing record with new data - e.g. maybe Julie James is only 9. For this we use the UPDATE command:

```sql
UPDATE table1 SET field3 = 9 WHERE field1 = 4;
```

### `DELETE`: Removing records

To remove records use the DELETE command:

```sql
DELETE FROM table1 WHERE field2 like '%Jesse%';
```

To drop columns or entire tables, you'll use `DROP`. However, we won't practice that here.

# Wrap-Up
Unless you have practical experience with SQL before today, you probably aren't a master - yet. Getting good at SQL and understanding the syntax takes more time and practice than ninety minutes. However, between today's lab, tomorrow's lesson, and the SQL practice you'll encounter throughout the course, you'll be able to confidently put SQL on your resume and tackle database queries with ease.
