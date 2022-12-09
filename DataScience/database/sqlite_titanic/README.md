# Titanic Data


## Cleaning the data
. Delete all rows where `Embarked` is empty, as we'll assume these individuals did not get on the ship.
. Fill all empty cabins with **EMPTY**

Note: `NULL` is synonymous in SQL to `NaN` in Pandas.

## Feature extraction
1.  There are two columns that pertain to how many family members are on the boat for a given person. Create a new column called `FamilyCount` which will be the sum of those two columns.
2. Create new dummy variables:
  - 2-1. Reverends have a special title in their name, "Rev." Create a column called `IsReverend`: 1 if they're a reverend, 0 if they're not.
  - 2-2. Create 3 columns: `Embarked_C`, `Embarked_Q` and `Embarked_S`. These columns will have 1's and 0's that correspond to the `C`, `Q` and `S` values in the `Embarked` column.
  - 2-3. Create 2 columns: `M` and `F`. Create dummy variables for `Sex`.

## Exploratory analysis

For this section, I have provided some assistance with 1 and 2 to help you create a survival rate in SQL:

. What is the total number of individuals on the ship?

```sql
SELECT COUNT(*) FROM titanic;
```

. What was the survival rate overall?

```sql
SELECT SUM(Survived) / 889 FROM titanic;
```


. Run this command and compare your results to those you got from last part.
```sql
SELECT AVG(Survived) FROM titanic;
```

. What was the survival rate of men?

. What was the survival rate of women?

. What was the survival rate for each `Pclass`?

. Did any reverends survive? How many?

. How many unique fares are there?

. What is the range of fares?

. What is the survival rate for cabins marked **EMPTY**?

. What is the survival rate for people whose `Age` is missing?

. What is the survival rate for each port of embarkation? Answer using a GROUP BY statement.

. What is the survival rate for children (under 12) in each `Pclass`?

. Did the captain of the ship survive? Is he on the list?

. Of all the people that died, who had the most expensive ticket? How much did it cost?
  - Hint: You may want to look into the `ORDER BY` or `MAX()`

. Does having family on the boat help or hurt your chances of survival?
  - Hint: You could create a dummy variable here.
