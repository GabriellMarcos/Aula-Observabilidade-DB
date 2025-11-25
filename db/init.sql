CREATE TABLE IF NOT EXISTS logs (
  id serial PRIMARY KEY,
  valor integer NOT NULL,
  created_at timestamptz DEFAULT now()
);

-- optional seed
INSERT INTO logs (valor) VALUES (1),(2),(3);
