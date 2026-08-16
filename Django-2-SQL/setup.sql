-- Run this once, as the postgres superuser
--   sudo -u postgres psql -f setup.sql
--
-- Creates the djangouser role and the djangotraining database it owns,
-- per the subject's requirements ("all the rights for it").

DROP DATABASE IF EXISTS djangotraining;
DROP ROLE IF EXISTS djangouser;

CREATE ROLE djangouser WITH LOGIN PASSWORD 'secret' CREATEDB;
CREATE DATABASE djangotraining OWNER djangouser;
GRANT ALL PRIVILEGES ON DATABASE djangotraining TO djangouser;
