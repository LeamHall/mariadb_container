from sqlalchemy import create_engine, text

# Need to fix the hardcoded IP.
engine = create_engine("mariadb+mariadbconnector://dba:my_cool_secret@172.17.0.2:3306/crew", echo=True, future=True)


with engine.connect() as conn:
  conn.execute(text("DROP TABLE IF EXISTS crew"))
  conn.execute(text("CREATE TABLE crew ( id int NOT NULL AUTO_INCREMENT, first_name text, last_name text, rank text, position text, PRIMARY KEY(id))"))
  conn.execute(
    text("INSERT INTO crew (first_name, last_name, rank, position) VALUES(:first_name, :last_name, :rank, :position)"),
    [ 
      { "first_name" : "Wilbur", "last_name" : "Lefron", "rank": "LT", "position": "Captain" },
      { "first_name" : "Alba", "last_name" : "Lefron", "rank": "SLT", "position": "First Officer" },
      { "first_name" : "James", "last_name" : "Lauwers", "rank": "CPO", "position": "Chief Engineer" },
      { "first_name" : "Smiley", "last_name" : "McGavren", "rank": "ENS", "position": "Engineer" }
    ])
  conn.commit()


with engine.connect() as conn:
  result = conn.execute(text("SELECT first_name, last_name, rank, position FROM crew"))
  for first_name, last_name, rank, position in result:
    print("{} {} {}, {}".format(rank, first_name, last_name, position))


