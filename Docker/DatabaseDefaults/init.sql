IF NOT EXISTS (
    SELECT * FROM sys.databases WHERE name = '${DATABASE_NAME}'
    )
    BEGIN
        DECLARE @dbname NVARCHAR(128) = '${DATABASE_NAME}';
        EXEC('CREATE DATABASE ' + @dbname);
    END;
