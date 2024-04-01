CREATE SEQUENCE IF NOT EXISTS tbl_locker_id_seq;

CREATE TABLE IF NOT EXISTS public.tbl_locker
(
    id integer NOT NULL DEFAULT nextval('tbl_locker_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    description character varying(500) COLLATE pg_catalog."default",
    lockerdata jsonb NOT NULL,
    CONSTRAINT tbl_locker_pkey PRIMARY KEY (id)
);

-- Stored procedure for insertion
CREATE OR REPLACE PROCEDURE insert_locker(name_val VARCHAR(50), description_val VARCHAR(500), lockerdata_val JSONB, OUT inserted_id INTEGER)
AS $$
BEGIN
    INSERT INTO tbl_locker(name, description, lockerdata)
    VALUES (name_val, description_val, lockerdata_val)
    RETURNING id INTO inserted_id;
END;
$$ LANGUAGE plpgsql;

-- Stored procedure for updating
CREATE OR REPLACE PROCEDURE update_locker(locker_id INTEGER, name_val VARCHAR(50), description_val VARCHAR(500), lockerdata_val JSONB)
AS $$
BEGIN
    UPDATE tbl_locker
    SET name = name_val, description = description_val, lockerdata = lockerdata_val
    WHERE id = locker_id;
END;
$$ LANGUAGE plpgsql;
