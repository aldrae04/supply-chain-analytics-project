from pathlib import Path
import duckdb

def main() -> None:
        script_dir = Path(__file__).resolve().parent
        db_path = (script_dir /".."/ "1_data_source" / "supply_chain_analytics.duckdb").resolve()
        con = duckdb.connect(str(db_path))

        con.execute("""
            CREATE OR REPLACE TABLE silver__location_master__lite AS
            SELECT
                UPPER(TRIM(location_id)) AS location_id,
                TRIM(location_name) AS location_name,
                UPPER(TRIM(location_type)) AS location_type,
                TRIM(region) AS region
            FROM bronze__location_master__lite;
            
        """)

        con.close()
        print("DONE: Created silver__location_master__lite")

if __name__ == "__main__":
    main()