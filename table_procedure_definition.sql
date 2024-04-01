CREATE SEQUENCE IF NOT EXISTS tbl_defination_id_seq;

CREATE TABLE IF NOT EXISTS public.tbl_defination
(
    id integer NOT NULL DEFAULT nextval('tbl_defination_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default",
    detail character varying(500) COLLATE pg_catalog."default",
    deftarget jsonb,

    CONSTRAINT tbl_defination_pkey PRIMARY KEY (id)
    
);

-- Stored procedure for insertion
CREATE OR REPLACE PROCEDURE insert_definition(name_val VARCHAR(50), detail_val VARCHAR(500), deftarget_val JSONB, OUT inserted_id INTEGER)
AS $$
BEGIN
    INSERT INTO tbl_defination(name, detail, deftarget)
    VALUES (name_val, detail_val, deftarget_val)
    RETURNING id INTO inserted_id;
END;
$$ LANGUAGE plpgsql;


-- Stored procedure for updating
CREATE OR REPLACE PROCEDURE update_definition(def_id INTEGER, name_val VARCHAR(50), detail_val VARCHAR(500), deftarget_val JSONB)
AS $$
BEGIN
    UPDATE tbl_defination
    SET name = name_val, detail = detail_val, deftarget = deftarget_val
    WHERE id = def_id;
END;
$$ LANGUAGE plpgsql;
