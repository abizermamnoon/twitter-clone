CREATE EXTENSION postgis;

\set ON_ERROR_STOP on
create extension RUM;
CREATE INDEX idx_rum_message ON messages USING rum(to_tsvector('english', message));
BEGIN;
CREATE TABLE tweet_urls (
    id_tweets BIGINT PRIMARY KEY,
    id_urls BIGINT
);

CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    age INTEGER
);

create table messages (
    id BIGSERIAL primary key,
    sender_id integer not null,
    message text not null,
    created_at timestamp not null default current_timestamp
);
CREATE EXTENSION IF NOT EXISTS RUM;
CREATE INDEX search_query ON messages USING RUM(to_tsvector('english', message), created_at, id);
create index on users(username, password, id);
