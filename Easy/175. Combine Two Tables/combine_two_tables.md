# 175. Combine Two Tables

**Difficulty:** Easy  
🔗 [View on LeetCode](https://leetcode.com/problems/combine-two-tables/)
📄 [Solution File](./combine_two_tables.sql)

## 📝 Problem Statement

**Table: Person**

| Column Name | Type    |
|-------------|---------|
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |

personId is the primary key (column with unique values) for this table.
This table contains information about the ID of some persons and their first and last names.
 

**Table: Address**

| Column Name | Type    |
|-------------|---------|
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |

addressId is the primary key (column with unique values) for this table.
Each row of this table contains information about the city and state of one person with ID = PersonId.

Write a solution to report the first name, last name, city, and state of each person in the Person table.  
If the address of a `personId` is not present in the Address table, report `null` instead.

Return the result table in any order.

---

## ✅ Constraints

- The `personId` in `Person` table is the primary key.
- The `addressId` in `Address` table is the primary key.
- Each row in the `Address` table corresponds to a `personId`.

---

## 🧠 Intuition / Thought Process

To combine data from two tables based on a common field (`personId`) and include unmatched entries from the `Person` table (with `null` where address info is missing), we should use a **LEFT JOIN**.

This ensures:
- Every person appears in the output
- If the person has no address, `city` and `state` will show as `NULL`

---

## 🔄 Pseudocode
```sql
FOR each record in Person table:
FIND matching record in Address table using personId
IF matching record exists:
INCLUDE firstName, lastName, city, state
ELSE:
INCLUDE firstName, lastName, NULL, NULL
```

---

## ⏱️ Time & Space Complexity

- Time Complexity: O(N), where N is the number of rows in the Person table.

- Space Complexity: O(1), the query runs in constant space on the server side.

---

## ✅ Test Case Example

**Input**

**Person table:**

| personId | lastName | firstName |
|----------|----------|-----------|
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |

**Address table:**

| addressId | personId | city          | state      |
|-----------|----------|---------------|------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |

**Output:** 

| firstName | lastName | city          | state    |
|-----------|----------|---------------|----------|
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |

**Explanation:** 

There is no address in the address table for the personId = 1 so we return null in their city and state.
addressId = 1 contains information about the address of personId = 2.