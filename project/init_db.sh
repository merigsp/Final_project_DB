echo "creating mydb..."
docker exec -i $(docker ps -qf "name=db") psql -U user -c "DROP DATABASE IF EXISTS mydb;"
docker exec -i $(docker ps -qf "name=db") psql -U user -c "CREATE DATABASE mydb OWNER user;"
docker exec -i $(docker ps -qf "name=db") psql -U user -d mydb -f /app/dump.sql
echo "Base is ready"


ALTER TABLE tournear ADD COLUMN IF NOT EXISTS additional_info JSONB;

CREATE INDEX IF NOT EXISTS idx_tournear_country ON tournear(country);
CREATE INDEX IF NOT EXISTS idx_tournear_qualification ON tournear(qualification_level);
CREATE INDEX IF NOT EXISTS idx_player_rating ON player(rating);

CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX IF NOT EXISTS idx_tournear_name_search ON tournear USING gin(t_name gin_trgm_ops);
