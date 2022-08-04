-- upgrade --
CREATE TABLE IF NOT EXISTS "usertortoise" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "username" VARCHAR(200) NOT NULL UNIQUE,
    "password" TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS "idx_usertortois_usernam_bb5a57" ON "usertortoise" ("username");
CREATE TABLE IF NOT EXISTS "todotortoise" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "title" TEXT NOT NULL,
    "text" TEXT NOT NULL,
    "done" BOOL NOT NULL  DEFAULT False,
    "owner_uuid" UUID NOT NULL REFERENCES "usertortoise" ("uuid") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
