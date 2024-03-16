# ORM stands for Object-Relational Mapping.

It is a programming technique used to convert data between incompatible systems in object-oriented programming languages and relational databases
In simpler terms, it bridges the gap between the object-oriented world of application code and the relational world of databases.

---

## Why ORM systems are useful?

- **Abstraction:** ORM abstracts away the complexities of SQL queries and database schema details. Developers can work with high-level objects and methods, rather than dealing directly with database tables and SQL statements.

- **Productivity:** ORM tools often provide utilities and features to speed up development, such as automatic schema generation, query building interfaces, and caching mechanisms. This can reduce the amount of boilerplate code developers need to write.

- **Portability:** ORM frameworks are often designed to work with multiple database management systems (DBMS). This means that developers can write database-agnostic code, making it easier to switch between different database backends without significant code changes.

- **Maintainability:** By encapsulating database interactions within ORM models and classes, the code becomes more modular and easier to maintain. Changes to the database schema can often be accommodated with minimal impact on application code.

- **Object-Oriented Approach:** ORM allows developers to work with data in a way that is more aligned with the object-oriented paradigm, which is often the natural way of thinking for developers. This can lead to cleaner, more intuitive code.

The ORM systems can streamline database interactions, reduce development time, and improve code quality and maintainability. However, it is essential to understand the underlying principles of ORM and the performance implications of using such tools to make informed decisions when incorporating them into a project.

---

## The cursor object cursor()

In Python's database programming, particularly when using modules like sqlite3 or MySQLdb, the cursor() method is used to create a cursor object.

---

## What is the use of a cursor object?

A cursor is a database object used to manage the context of a fetch operation, effectively allowing you to interact with the database by executing SQL queries and fetching results.

---

### Overview of how it is typically used:

- **Establish a Connection:** First, you establish a connection to the database using the appropriate method provided by the database module. For example, in sqlite3, you use sqlite3.connect().

- **Create a Cursor:** Once the connection is established, you create a cursor object by calling the:
	- cursor() method
on the connection object. This cursor object will be used to execute SQL queries and manage the results.

- **Execute SQL Queries:** With the cursor object, you can execute SQL queries using methods like:
	- execute(),
	- executemany(), or
	- executescript(),
depending on your specific needs.

- **Fetch Results (if applicable):** After executing a query that returns results (such as a SELECT query), you can fetch the results using methods like:
	- fetchone(),
	- fetchall(), or
	- fetchmany().

- **Commit Changes (if applicable):** If you have made any changes to the database (such as:
	- INSERT,
	- UPDATE, or
	- DELETE
operations), you typically commit those changes using the
	- commit() method on the connection object.

- **Close Cursor and Connection:** Finally, it is good practice to close the cursor and the database connection once you are done interacting with the database, using the
	- close() method on both objects.

---
