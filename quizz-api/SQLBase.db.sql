BEGIN TRANSACTION;
DROP TABLE IF EXISTS "Questions";
CREATE TABLE IF NOT EXISTS "Questions" (
	"Position"	INTEGER,
	"Title"	TEXT,
	"Content" TEXT,
	"Image"	TEXT,
	"Id"	INTEGER UNIQUE,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Anwsers";
CREATE TABLE IF NOT EXISTS "Anwsers" (
	"QuestionId"	INTEGER,
	"Id"	INTEGER UNIQUE,
	"Content"	TEXT,
	"IsCorrect"	INTEGER,
	"Position"	INTEGER,
	FOREIGN KEY("QuestionId") REFERENCES "Questions"("Id") ON UPDATE CASCADE,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Score";
CREATE TABLE IF NOT EXISTS "Score" (
	"playerName"	TEXT,
	"Date"	TEXT,
	"score"	INTEGER,
	"Id"	INTEGER UNIQUE,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
COMMIT;
