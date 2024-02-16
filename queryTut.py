import sqlite3
con = sqlite3.connect("db/tutorial.db")
cur = con.cursor()


# The data is now in the database, so we can query it
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

# Fetch one example
res = cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')

# Fetch all examples
res = cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
for title, year in res.fetchall():
    print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
